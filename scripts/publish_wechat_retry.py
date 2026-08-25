#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retry WeChat publish for ai-homework-exam-study-2026 — polls token until whitelist kicks in"""
import json, os, sys, time, uuid, urllib.request

APPID = 'wx1a4dec7ba7da8975'
SECRET = 'bed0d73029e00d2e569baa67295b3d07'
BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
COVER = '/tmp/cover-ai-homework.png'

def get_token():
    url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential"
           f"&appid={APPID}&secret={SECRET}")
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r)

def upload_material(token, path):
    boundary = '----HermesBoundary' + uuid.uuid4().hex
    with open(path, 'rb') as f:
        filedata = f.read()
    body = (f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="media"; filename="{os.path.basename(path)}"\r\n'
            f'Content-Type: image/png\r\n\r\n').encode() + filedata + f'\r\n--{boundary}--\r\n'.encode()
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image"
    req = urllib.request.Request(url, data=body, headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def add_draft(token, thumb):
    data = json.load(open(BASE + 'data.json', encoding='utf-8'))
    art = data['articles'][0]
    payload = {"articles": [{
        "title": art['title'], "author": "猿来AI", "digest": art['desc'][:120],
        "content": art['content'],
        "content_source_url": f"https://yuanlaiai.github.io/articles/{art['slug']}/",
        "thumb_media_id": thumb, "need_open_comment": 1, "only_fans_can_comment": 0
    }]}
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    req = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def fetch_draft_url(token, media_id):
    payload = json.dumps({"offset": 0, "count": 5, "no_content": 0}).encode()
    url = f"https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token={token}"
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    for item in d.get('item', []):
        if item.get('media_id') == media_id:
            return item['content']['news_item'][0].get('url', '')
    return ''

# Poll token (whitelist may take a few minutes to propagate)
MAX_ATTEMPTS = 12
last_ip = None
for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"[{time.strftime('%H:%M:%S')}] attempt {attempt}/{MAX_ATTEMPTS} ...", flush=True)
    try:
        d = get_token()
        if 'access_token' in d:
            token = d['access_token']
            print("TOKEN OK!")
            break
        err = d.get('errmsg', '')
        ip = err.split()[-1] if 'invalid ip' in err else ''
        if ip and ip != last_ip:
            print(f"  still blocked, IP={ip}")
            last_ip = ip
    except Exception as e:
        print(f"  error: {e}")
    if attempt < MAX_ATTEMPTS:
        time.sleep(20)
else:
    print("Gave up after 12 attempts — whitelist not active yet.")
    sys.exit(1)

# Proceed
print("uploading cover...")
du = upload_material(token, COVER)
if 'media_id' not in du:
    print("UPLOAD ERROR:", du); sys.exit(1)
thumb = du['media_id']
print("thumb_media_id:", thumb)

print("creating draft...")
dd = add_draft(token, thumb)
if 'media_id' not in dd:
    print("DRAFT ERROR:", dd); sys.exit(1)
media_id = dd['media_id']
print("draft media_id:", media_id)

print("fetching draft url...")
url = fetch_draft_url(token, media_id)
if url:
    if url.startswith('http://'):
        url = 'https://' + url[len('http://'):]
    dp = BASE + 'data.json'
    data = json.load(open(dp, encoding='utf-8'))
    data['articles'][0]['wechatUrl'] = url
    json.dump(data, open(dp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print("wechatUrl backfilled:", url[:80])
else:
    print("WARNING: no url found")
