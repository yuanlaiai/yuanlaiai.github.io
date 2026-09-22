#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish 2026-09-21 Google AX article to WeChat draft: cover gen + draft/add + fetch url + backfill"""
import json, os, sys, urllib.request, uuid

APPID = 'wx1a4dec7ba7da8975'
SECRET = 'bed0d73029e00d2e569baa67295b3d07'
BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
COVER = '/tmp/cover-ax.png'
SLUG = 'google-ax-agent-runtime-2026'

L1 = "Google 开源 AX"
L2 = "给 Agent 造一个 Kubernetes"
L3 = "628 分热帖背后的运行时之争"
FOOT = "猿来AI · 2026-09-21 深度解读"


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
        t = y / H
        r = int(26 * (1 - t) + 20 * t)
        g = int(26 * (1 - t) + 31 * t)
        b = int(26 * (1 - t) + 60 * t)
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

    def fit(text, start, limit=780):
        size = start
        while size > 20:
            f = font(size)
            if draw.textlength(text, font=f) <= limit:
                return f
            size -= 2
        return font(20)

    tf1 = fit(L1, 54)
    tf2 = fit(L2, 54)
    sf = fit(L3, 30)
    lf = font(22)
    draw.rectangle([60, 74, 160, 78], fill='#ff8c42')
    draw.rectangle([60, 89, 130, 92], fill='#ff8c42')
    draw.text((60, 122), L1, fill='#ffffff', font=tf1)
    draw.text((60, 204), L2, fill='#ff8c42', font=tf2)
    draw.text((60, 302), L3, fill='#ffffff', font=sf)
    draw.rectangle([60, 388, 260, 391], fill='#ff8c42')
    draw.text((60, 412), FOOT, fill='#8a8a9a', font=lf)
    img.save(COVER)
    print("cover saved:", COVER, os.path.getsize(COVER), "bytes")


def upload_material(token, path):
    boundary = '----HermesBoundary' + uuid.uuid4().hex
    filedata = open(path, 'rb').read()
    body = (f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="media"; filename="{os.path.basename(path)}"\r\n'
            f'Content-Type: image/png\r\n\r\n').encode() + filedata + f'\r\n--{boundary}--\r\n'.encode()
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image"
    req = urllib.request.Request(url, data=body, headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})
    with urllib.request.urlopen(req, timeout=40) as r:
        d = json.load(r)
    if 'media_id' not in d:
        print("UPLOAD ERROR:", d); sys.exit(1)
    print("thumb_media_id:", d['media_id'])
    return d['media_id']


def add_draft(token, thumb):
    data = json.load(open(BASE + 'data.json', encoding='utf-8'))
    art = next(a for a in data['articles'] if a['slug'] == SLUG)
    payload = {"articles": [{
        "title": art['title'],
        "author": "猿来AI",
        "digest": art['desc'][:120],
        "content": art['content'],
        "content_source_url": f"https://yuanlaiai.github.io/articles/{art['slug']}/",
        "thumb_media_id": thumb,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }]}
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    req = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=40) as r:
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
            u = item['content']['news_item'][0].get('url', '')
            if u.startswith('http://'):
                u = 'https://' + u[len('http://'):]
            print("draft url:", u)
            return u
    print("WARN: draft not found;", [i.get('media_id') for i in d.get('item', [])])
    return None


def backfill(url):
    data = json.load(open(BASE + 'data.json', encoding='utf-8'))
    for a in data['articles']:
        if a['slug'] == SLUG:
            a['wechatUrl'] = url
    with open(BASE + 'data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("backfilled wechatUrl in data.json")


if __name__ == '__main__':
    gen_cover()
    token = get_token()
    thumb = upload_material(token, COVER)
    media_id = add_draft(token, thumb)
    url = fetch_draft_url(token, media_id)
    if url:
        backfill(url)
        print("ALL DONE")
    else:
        print("PARTIAL: draft created but url not fetched")
