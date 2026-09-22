#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: google-ax-agent-runtime-2026 (markdown -> site HTML) into data.json + gen index.html + sitemap"""
import json, os, re, html

BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
MD   = '/Users/xuefei/obsidian_object/猿来AI知识库/AI写作/2026-09-21_Google-AX深度分析.md'
path = BASE + 'data.json'

SLUG  = 'google-ax-agent-runtime-2026'
TITLE = 'Google 把 Agent 当成第三种工作负载：AX 想给它们造一个 Kubernetes'
DATE  = '2026-09-21'
TAGS  = ['AI Agent', '开源生态']
DESC  = 'Google 开源的 AX 把 agent 当成第三种工作负载：四个原语、三个动词，底下是能在 500 毫秒内恢复的沙箱层。但它默认你已经有一台 Kubernetes 集群。'

P   = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2  = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;font-weight:700;'
BQ  = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'
PRE = 'background:#1e1e2e;color:#e6e6e6;padding:14px 16px;border-radius:6px;overflow-x:auto;font-size:13px;line-height:1.7;margin:16px 0;'
CODE = 'font-family:Menlo,Consolas,monospace;font-size:14px;background:#f4f4f6;color:#c0392b;padding:1px 5px;border-radius:3px;'
HR  = 'border:none;border-top:1px solid #eee;margin:28px 0;'


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', rf'<span style="{RED}">\1</span>', t)
    t = re.sub(r'`([^`]+)`', rf'<span style="{CODE}">\1</span>', t)
    return t


def md_to_html(md):
    lines = md.split('\n')
    out, code, in_code = [], [], False
    i = 0
    while i < len(lines):
        l = lines[i]
        s = l.strip()
        if s.startswith('```'):
            if in_code:
                out.append(f'<pre style="{PRE}">{html.escape(chr(10).join(code))}</pre>')
                code, in_code = [], False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code.append(l)
            i += 1
            continue
        if not s:
            i += 1
            continue
        if s.startswith('## '):
            out.append(f'<h2 style="{H2}">{inline(s[3:])}</h2>')
        elif s.startswith('# '):
            pass  # h1 handled separately
        elif s.startswith('>'):
            bq = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                bq.append(lines[i].strip().lstrip('>').strip())
                i += 1
            body = ' '.join(x for x in bq if x)
            out.append(f'<blockquote style="{BQ}"><p style="font-size:15px;line-height:1.8;margin:0;color:#555;">{inline(body)}</p></blockquote>')
            continue
        elif s and set(s) <= set('-'):
            out.append(f'<hr style="{HR}">')
        elif s.startswith('- '):
            out.append(f'<p style="{P}">· {inline(s[2:])}</p>')
        else:
            out.append(f'<p style="{P}">{inline(s)}</p>')
        i += 1
    if in_code:
        out.append(f'<pre style="{PRE}">{html.escape(chr(10).join(code))}</pre>')
    return '\n\n'.join(out)


md = open(MD, encoding='utf-8').read()
md_body = md.split('---', 2)[2]

content = (
    f'<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;'
    f'margin-bottom:20px;padding-top:10px;letter-spacing:1px;">{TITLE}</h1>\n\n'
    f'<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;'
    f'border-bottom:1px solid #eee;">{DATE} · 猿来AI</p>\n\n'
    + md_to_html(md_body)
)

# ---- safety self-checks before touching data.json ----
clean = re.sub(r'<[^>]+>', '', content)
clean = re.sub(r'https?://\S+', '', clean).replace(' ', '').replace('\n', '')
cn = len([c for c in clean if '\u4e00' <= c <= '\u9fff'])
rel = len(re.findall(r'href="/', content))
TAGS_OK = {'大模型', 'AI Agent', '行业趋势', '中国 AI', '商业资本', '开源生态', '安全监管', '算力芯片', '榜单日报', '实用教程'}
assert set(TAGS) <= TAGS_OK, set(TAGS) - TAGS_OK
assert cn >= 3000, f'正文汉字不足: {cn}'
assert len(DESC) <= 120, f'desc 超 120 字: {len(DESC)}'
assert '<ul' not in content and '<b>' not in content, '微信禁用标签'
assert rel == 0, f'含相对链接 {rel} 处'
print(f"[selfcheck] 汉字 {cn} | desc {len(DESC)} | <ul> {content.count('<ul')} | <b> {content.count('<b>')} | 相对链接 {rel}")

article = {
    "title": TITLE, "tags": TAGS, "date": DATE, "readTime": "9 分钟",
    "desc": DESC, "slug": SLUG, "content": content, "wechatUrl": ""
}

with open(path, encoding='utf-8') as f:
    data = json.load(f)

existing = [i for i, a in enumerate(data['articles']) if a['slug'] == SLUG]
if existing:
    article["id"] = data['articles'][existing[0]]["id"]
    data['articles'][existing[0]] = article
    print("Updated existing article at index", existing[0], "id", article["id"])
else:
    article["id"] = max(a["id"] for a in data['articles']) + 1
    data['articles'].insert(0, article)
    print("Inserted new article id=", article["id"], "at index 0")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ---- generate articles/{slug}/index.html from zuckerberg template ----
tpl_path = BASE + 'articles/zuckerberg-chinese-ai-ban-warning-2026/index.html'
tpl = open(tpl_path, encoding='utf-8').read()

repl = [
    ('Zuckerberg 对 CNN 说：不要封禁中国 AI——但这不只是一句表态', 'TITLE_PLACEHOLDER'),
    ('zuckerberg-chinese-ai-ban-warning-2026', 'SLUG_PLACEHOLDER'),
    ('Mark Zuckerberg今天对CNN说不要封禁中国AI模型。但这不是孤立表态——从Jensen第一条X到OpenAI被迫站队，从Open Secure AI Alliance到微软安全模型，这是一条七天事件链的终点。', 'DESC_PLACEHOLDER'),
    ('AI,Zuckerberg,Meta,中国AI,开放权重,CNN,深度分析', 'KW_PLACEHOLDER'),
    ('2026-07-29', 'DATE_PLACEHOLDER'),
]
for old, new in repl:
    assert old in tpl, f"template marker missing: {old[:30]}"
    tpl = tpl.replace(old, new)

tpl = (tpl.replace('TITLE_PLACEHOLDER', TITLE)
          .replace('SLUG_PLACEHOLDER', SLUG)
          .replace('DESC_PLACEHOLDER', DESC)
          .replace('KW_PLACEHOLDER', ','.join(TAGS))
          .replace('DATE_PLACEHOLDER', DATE))

assert 'Zuckerberg' not in tpl and 'zuckerberg-chinese' not in tpl
assert 'TITLE_PLACEHOLDER' not in tpl and 'SLUG_PLACEHOLDER' not in tpl
assert "var slug = '" + SLUG + "';" in tpl
assert 'window.siteData' in tpl or 'window.__YUANLAI_DATA__' in tpl

out_dir = BASE + f'articles/{SLUG}/'
os.makedirs(out_dir, exist_ok=True)
with open(out_dir + 'index.html', 'w', encoding='utf-8') as f:
    f.write(tpl)
print("index.html written:", out_dir + 'index.html')

# ---- rebuild sitemap.xml ----
static_urls = ['https://yuanlaiai.github.io/', 'https://yuanlaiai.github.io/articles.html', 'https://yuanlaiai.github.io/awesome-ai-tools/']
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in static_urls:
    lines.append(f'  <url><loc>{u}</loc></url>')
for a in data['articles']:
    lines.append(f'  <url><loc>https://yuanlaiai.github.io/articles/{a["slug"]}/</loc></url>')
lines.append('</urlset>')
with open(BASE + 'sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print("sitemap.xml rebuilt with", len(data['articles']), "articles")
print("Total articles:", len(data['articles']), "| slug:", SLUG)
