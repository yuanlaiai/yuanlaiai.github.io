#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish 2026-08-18 article to WeChat draft: cover gen + draft/add + fetch url"""
import json, os, sys, urllib.request, urllib.parse, uuid

APPID = 'wx1a4dec7ba7da8975'
SECRET = 'bed0d73029e00d2e569baa67295b3d07'
BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
COVER = '/tmp/cover-nvidia-hf.png'

def get_token():
    url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential"
           f"&appid={APPID}&secret={SECRET}")
    with urllib.request.urlopen(url, timeout=20) as r:
        d = json.load(r)
    if 'access_token' not in d:
        print("TOKEN ERROR:", d); sys.exit(1)
    return d['access_token']

def gen_cover():
    from PIL import Image, ImageDraw, ImageFont
    W, H = 900, 500
    img = Image.new('RGB', (W, H))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        blend = y / H
        r = int(26*(1-blend) + 20*blend)
        g = int(26*(1-blend) + 31*blend)
        b = int(46*(1-blend) + 60*blend)
        for x in range(W):
            img.putpixel((x, y), (r, g, b))
    def font(size, idx=0):
        for p in ['/System/Library/Fonts/PingFang.ttc',
                  '/System/Library/Fonts/STHeiti Light.ttc',
                  '/System/Library/Fonts/Supplemental/Arial Unicode.ttf']:
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size, index=idx)
                except Exception:
                    continue
        return ImageFont.load_default()
    tf = font(72); sf = font(40); lf = font(22)
    # accent lines
    draw.rectangle([60, 90, 160, 94], fill='#ff8c42')
    draw.rectangle([60, 105, 130, 108], fill='#ff8c42')
    draw.text((60, 150), "Nvidia × Hugging Face", fill='#ffffff', font=tf)
    draw.text((60, 250), "开源央行要易主了", fill='#ff8c42', font=sf)
    draw.rectangle([60, 340, 260, 343], fill='#ff8c42')
    draw.text((60, 370), "猿来AI · 2026-08-28 深度解读", fill='#8a8a9a', font=lf)
    img.save(COVER)
    print("cover saved:", COVER, os.path.getsize(COVER), "bytes")

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
        d = json.load(r)
    if 'media_id' not in d:
        print("UPLOAD ERROR:", d); sys.exit(1)
    print("thumb_media_id:", d['media_id'])
    return d['media_id']

def add_draft(token, thumb):
    data = json.load(open(BASE + 'data.json', encoding='utf-8'))
    art = data['articles'][0]  # newest
    content = art['content']
    payload = {
        "articles": [{
            "title": art['title'],
            "author": "猿来AI",
            "digest": art['desc'][:120],
            "content": content,
            "content_source_url": f"https://yuanlaiai.github.io/articles/{art['slug']}/",
            "thumb_media_id": thumb,
            "need_open_comment": 1,
            "only_fans_can_comment": 0
        }]
    }
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    req = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    if 'media_id' not in d:
        print("DRAFT ERROR:", d); sys.exit(1)
    print("draft media_id:", d['media_id'])
    return d['media_id']

def fetch_draft_url(token, media_id):
    payload = json.dumps({"offset": 0, "count": 5, "no_content": 0}).encode()
    url = f"https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token={token}"
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    for item in d.get('item', []):
        if item.get('media_id') == media_id:
            u = item.get('content', {}).get('url', '')
            print("draft url:", u)
            return u
    print("draft not found in batchget; items:", len(d.get('item', [])))
    return ''

def main():
    token = get_token()
    print("token OK")
    gen_cover()
    thumb = upload_material(token, COVER)
    media_id = add_draft(token, thumb)
    url = fetch_draft_url(token, media_id)
    if url:
        # 回填 wechatUrl
        dp = BASE + 'data.json'
        data = json.load(open(dp, encoding='utf-8'))
        data['articles'][0]['wechatUrl'] = url
        json.dump(data, open(dp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print("wechatUrl backfilled for", data['articles'][0]['slug'])
    else:
        print("WARNING: no url, wechatUrl NOT backfilled")

if __name__ == '__main__':
    main()
