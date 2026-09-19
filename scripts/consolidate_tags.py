#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolidate article tags: 116 distinct tags -> 10 canonical categories (2026-09-20)"""
import json, collections

BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
PATH = BASE + 'data.json'

# 10 个规范分类
TAXONOMY = ['大模型', 'AI Agent', '行业趋势', '中国 AI', '商业资本',
            '开源生态', '安全监管', '算力芯片', '榜单日报', '实用教程']

MAP = {
    'agent-code-review-rework-tax-2026':            ['AI Agent', '行业趋势'],
    'jev-typesafe-system-one-no-strings-2026':      ['大模型', 'AI Agent'],
    'deepseek-v41-flash-kv-cache-cost-2026':        ['大模型', '中国 AI'],
    'mistral-e3b-sovereign-ai-2026':                ['商业资本', '行业趋势'],
    'openai-cuts-cursor-spacex-2026':               ['商业资本', 'AI Agent'],
    'nvidia-huggingface-acquisition-2026':          ['算力芯片', '开源生态', '商业资本'],
    'ox-alpha-glm-5-3-flash-zhipu-2026':            ['大模型', '中国 AI', '算力芯片'],
    'ai-homework-exam-study-2026':                  ['行业趋势'],
    'google-student-gemini-free-2026':              ['大模型', '行业趋势'],
    'agent-memory-arms-race-2026':                  ['AI Agent', '中国 AI', '榜单日报'],
    'apple-alibaba-china-ai-model-qwen-2026':       ['中国 AI', '大模型', '开源生态'],
    'nvidia-cuts-openai-guarantee-circular-financing-2026': ['算力芯片', '商业资本', '行业趋势'],
    'burry-covers-bis-imf-warning-ai-bubble-2026':  ['商业资本', '行业趋势'],
    'claude-watermark-24h-defeated-2026':           ['安全监管', '大模型'],
    'deepseek-v4-pro-0813-fable-5-price-2026':      ['大模型', '中国 AI'],
    'openai-astra-critical-cyber-pause-2026':       ['大模型', '安全监管'],
    'deepseek-price-increase-cheap-tokens-2026':    ['商业资本', '中国 AI'],
    'deepseek-v4-flash-0731-shock-v2-2026':         ['大模型', '中国 AI'],
    'sam-altman-cognitive-atrophy-irony-2026':      ['行业趋势', '安全监管'],
    'china-ai-open-weights-deep-analysis-2026':     ['行业趋势', '中国 AI', '开源生态'],
    'ai-fatigue-explosion-2026':                    ['行业趋势'],
    'china-ai-open-weights-winning-2026':           ['行业趋势', '中国 AI', '开源生态'],
    'edge-voice-ai-transcribe-moonshine-2026':      ['实用教程', '开源生态'],
    'china-ai-k3-moment-2026':                      ['中国 AI', '大模型'],
    'ai-bubble-debate-2026-07':                     ['行业趋势', '商业资本'],
    'xai-grok-build-open-source-2026':              ['大模型', 'AI Agent', '开源生态'],
    'github-ai-trending-2026-06-08':                ['榜单日报', '开源生态'],
    'github-ai-trending-2026-06-10':                ['榜单日报', '开源生态'],
    'github-ai-trending-2026-06-11':                ['榜单日报', '开源生态'],
    'github-trending-ai-daily-bot':                 ['实用教程'],
    'apple-gemini-wwdc2026':                        ['大模型', '商业资本'],
    'agent-skill-three-kingdoms':                   ['AI Agent'],
    'research-agent-next-blueprint':                ['AI Agent'],
    'ai-bottleneck-debate-2026':                    ['行业趋势', '商业资本'],
    'openai-sandbox-escape-huggingface-2026':       ['安全监管', 'AI Agent'],
    'ai-kill-switch-act-2026':                      ['安全监管'],
    'microsoft-ai-security-mai-cyber-2026':         ['安全监管', 'AI Agent'],
    'open-weights-silicon-valley-split-2026':       ['开源生态', '大模型', '行业趋势'],
    'zuckerberg-chinese-ai-ban-warning-2026':       ['中国 AI', '开源生态', '行业趋势'],
}

with open(PATH, encoding='utf-8') as f:
    data = json.load(f)

before = collections.Counter()
for a in data['articles']:
    for t in a.get('tags', []):
        before[t] += 1

unmapped = [a['slug'] for a in data['articles'] if a['slug'] not in MAP]
print("未映射的文章:", unmapped if unmapped else "无")

changed = 0
for a in data['articles']:
    new = MAP.get(a['slug'])
    if not new:
        continue
    assert all(t in TAXONOMY for t in new), f"非规范标签: {a['slug']} {new}"
    if a['tags'] != new:
        a['tags'] = new
        changed += 1

after = collections.Counter()
for a in data['articles']:
    for t in a.get('tags', []):
        after[t] += 1

assert all(len(a['tags']) >= 1 for a in data['articles']), "有文章没有任何标签"
assert set(after) <= set(TAXONOMY), set(after) - set(TAXONOMY)

with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n标签总数：{len(before)} 种 -> {len(after)} 种 | 改动文章：{changed}/{len(data['articles'])}")
print("\n新分类分布：")
for t, c in after.most_common():
    print(f"  {c:3d}  {t}")
