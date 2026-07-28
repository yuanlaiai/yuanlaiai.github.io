#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-07-28 (6-day gap since 7/22)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 7, 28)
gap_days = (today - last).days  # 6
shift = gap_days + 1  # 7
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

def find_latest_count(project_name):
    for day in data['days']:
        for proj in day['projects']:
            if proj['name'] == project_name:
                return proj['count']
    return 0

today_projects = [
    {
        "rank": 1,
        "owner": "alibaba",
        "name": "open-code-review",
        "fullName": "alibaba / open-code-review",
        "org": "Alibaba",
        "url": "https://github.com/alibaba/open-code-review",
        "lang": "Go",
        "langClass": "go",
        "stars": "14,772",
        "forks": "997",
        "starsToday": "979",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +979★！14.8K★ 阿里巴巴开源 AI 代码审查混构引擎！确定性管线 + LLM Agent 双引擎，精确行级评论，内置 NPE/线程安全/XSS/SQL 注入规则集。",
        "problems": [
            "<strong>代码审查效率低：</strong>人工审查费时且容易遗漏，大型 PR 审查周期长。",
            "<strong>AI 审查不精准：</strong>纯 AI 审查容易产生幻觉，缺少确定性规则兜底。",
            "<strong>大厂最佳实践难获取：</strong>阿里巴巴级的规则集闭源，社区无法直接使用。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/alibaba/open-code-review.git</code></pre>",
            "配置 API Key：<pre><code>export OPENAI_API_KEY=xxx</code></pre>",
            "审查代码：<pre><code>ocr review --path src/</code></pre>"
        ],
        "insights": [
            "<strong>阿里巴巴开源诚意之作：</strong>不是 Demo 而是真正的生产级代码审查工具——确定性规则 + LLM Agent 双引擎架构。",
            "<strong>混构架构是趋势：</strong>纯 AI 审查有幻觉，纯规则太死板——混构引擎才是代码审查的正确打开方式。",
            "<strong>内置大厂规则集：</strong>NPE、线程安全、XSS、SQL 注入——这些不是通用规则，是阿里踩过的坑总结出来的实战经验。"
        ],
        "tags": ["code-review", "alibaba", "llm-agent", "developer-tools", "static-analysis"]
    },
    {
        "rank": 2,
        "owner": "pbakaus",
        "name": "impeccable",
        "fullName": "pbakaus / impeccable",
        "org": "pbakaus",
        "url": "https://github.com/pbakaus/impeccable",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "51,519",
        "forks": "3,039",
        "starsToday": "847",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +847★！51.5K★ 回归登榜！给 AI 装上设计品味的设计语言系统——让 AI 生成的内容不再有「AI 味」。",
        "problems": [
            "<strong>AI 设计品味差：</strong>大模型生成的设计缺乏高级审美，满屏 AI 感。",
            "<strong>设计语言缺失：</strong>AI 知道怎么写代码但不知道「怎么设计好看」——缺少设计原则的约束。",
            "<strong>品牌一致性难保障：</strong>自动生成的设计与品牌调性脱节，需要大量人工微调。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/pbakaus/impeccable.git</code></pre>",
            "加载 SKILL.md 到编码 Agent，AI 自动获得设计品味提升。",
            "支持 Claude Code、Cursor、Codex 等主流编码 Agent。"
        ],
        "insights": [
            "<strong>51.5K★ 二次登榜：</strong>5/30 首登后热度不降，回归榜单——「反 AI 味」持续是社区刚需。",
            "<strong>设计品味 = 用户感知的最后一公里：</strong>功能再强 UI 丑就是不行——AI 生成内容也需要审美兜底。",
            "<strong>Agent 技能品类化再确认：</strong>从省钱（caveman）到审美（impeccable）到品味（taste-skill），技能经济正在垂直细分。"
        ],
        "tags": ["ai-quality", "design-language", "anti-slop", "agent-skill", "ui-design"]
    },
    {
        "rank": 3,
        "owner": "yorukot",
        "name": "superfile",
        "fullName": "yorukot / superfile",
        "org": "yorukot",
        "url": "https://github.com/yorukot/superfile",
        "lang": "Go",
        "langClass": "go",
        "stars": "20,866",
        "forks": "676",
        "starsToday": "600",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +600★！20.9K★ 漂亮现代的终端文件管理器——Go 语言编写，交互体验对标 GUI，轻量高效。",
        "problems": [
            "<strong>终端文件管理体验差：</strong>cd/ls/mv/cp 命令行操作繁琐，缺少可视化导航。",
            "<strong>GUI 文件管理器启动慢：</strong>Finder/Nautilus 在服务器或无桌面环境不可用。",
            "<strong>终端工具各司其职：</strong>没有统一的、现代化的文件管理体验。"
        ],
        "usage": [
            "安装：<pre><code>brew install superfile</code></pre> 或从 Releases 下载二进制。",
            "启动：<pre><code>spf</code></pre> 即可打开终端文件管理器。",
            "快捷键导航：<pre><code>hjkl</code></pre> 移动，<pre><code>Enter</code></pre> 进入目录，<pre><code>q</code></pre> 退出。"
        ],
        "insights": [
            "<strong>终端 GUI 化趋势：</strong>超 20K★ 说明开发者对终端体验的要求越来越高——美观和效率可以兼得。",
            "<strong>Go 语言的终端新星：</strong>单二进制分发零依赖，性能出色，Go 正在成为终端工具的首选语言。",
            "<strong>20.9K★ 的共识：</strong>CLI 工具也可以有设计感——superfile 证明了终端工具能做得像 GUI 一样友好。"
        ],
        "tags": ["terminal", "file-manager", "go", "cli", "productivity"]
    },
    {
        "rank": 4,
        "owner": "moeru-ai",
        "name": "airi",
        "fullName": "moeru-ai / airi",
        "org": "萌 AI",
        "url": "https://github.com/moeru-ai/airi",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "44,011",
        "forks": "4,394",
        "starsToday": "572",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +572★！44K★ 自托管 Grok 伴侣 AI——实时语音聊天、Minecraft/Factorio 陪玩，全平台支持。Nero-sama 级别的 AI 伴侣。",
        "problems": [
            "<strong>AI 伴侣都是云端的：</strong>Character.AI 等平台依赖云端，隐私不安全且需付费。",
            "<strong>AI 与游戏整合难：</strong>想让 AI 进入游戏世界一起玩，但缺乏自托管方案。",
            "<strong>跨平台 AI 集成碎片化：</strong>Web/macOS/Windows 各有一套方案，没有统一框架。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/moeru-ai/airi.git</code></pre>",
            "启动：<pre><code>docker compose up</code></pre>",
            "接入游戏：在 Minecraft/Factorio 中配置 mod 连接即可。"
        ],
        "insights": [
            "<strong>44K★ 自托管 AI 伴侣爆发：</strong>隐私意识觉醒 + Grok 开源驱动——用户可以拥有自己的 AI 伴侣，无需上传数据到云端。",
            "<strong>从实用到陪伴：</strong>最火的开源 AI 项目从纯生产力工具延伸到情感陪伴——AI 正进入日常生活。",
            "<strong>全平台 + 游戏集成的壁垒：</strong>Web/macOS/Windows + Minecraft/Factorio——不只是聊天，是跨平台的 AI 伙伴。"
        ],
        "tags": ["ai-companion", "self-hosted", "grok", "gaming", "realtime-voice"]
    },
    {
        "rank": 5,
        "owner": "shiyu-coder",
        "name": "Kronos",
        "fullName": "shiyu-coder / Kronos",
        "org": "shiyu-coder",
        "url": "https://github.com/shiyu-coder/Kronos",
        "lang": "Python",
        "langClass": "py",
        "stars": "34,557",
        "forks": "5,795",
        "starsToday": "441",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +441★！34.6K★ 金融市场语言基础模型——回归登榜！AI 量化金融的世界模型，理解市场语言的开源基石。",
        "problems": [
            "<strong>金融 AI 模型缺失：</strong>通用 LLM 不理解 K 线、订单簿、波动率等金融术语和逻辑。",
            "<strong>量化门槛太高：</strong>传统量化需要 PhD 级别的数学和编程能力，普通人无法参与。",
            "<strong>金融数据模型不开放：</strong>高频量化公司的模型闭源，散户和小机构难以获取。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/shiyu-coder/Kronos.git</code></pre>",
            "推理示例：<pre><code>python kronos/predict.py --ticker AAPL</code></pre>",
            "微调：<pre><code>python finetune.py --data your_data.csv</code></pre>"
        ],
        "insights": [
            "<strong>34.6K★ 二次登榜：</strong>6/12 首登后再次回归——金融 AI 的热度正在从概念走向产品。",
            "<strong>AI 量化金融赛道升温：</strong>从 Kronos 到 FinGPT 到 BloombergGPT——金融是 AI 最大的变现方向之一。",
            "<strong>开源金融模型的价值：</strong>让个人投资者也能用上机构级别的 AI 量化能力——金融民主化的关键一步。"
        ],
        "tags": ["finance", "ai-model", "quantitative-trading", "open-source", "deep-learning"]
    },
    {
        "rank": 6,
        "owner": "bradautomates",
        "name": "claude-video",
        "fullName": "bradautomates / claude-video",
        "org": "bradautomates",
        "url": "https://github.com/bradautomates/claude-video",
        "lang": "Python",
        "langClass": "py",
        "stars": "11,048",
        "forks": "1,142",
        "starsToday": "434",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +434★！11K★ 二次登榜！让 Claude 看视频——/watch 下载、抽帧、转录、全交给 Claude 分析。",
        "problems": [
            "<strong>Claude 不能看视频：</strong>Claude 理解图片文字很棒，但无法直接处理视频内容。",
            "<strong>视频分析流程割裂：</strong>下载→抽帧→转录→分析，每一步都需要手动切换工具。",
            "<strong>缺少一站式解决方案：</strong>没有简单命令就能让 Claude 完整分析视频的工具。"
        ],
        "usage": [
            "安装：<pre><code>pip install claude-video</code></pre>",
            "让 Claude 看视频：<pre><code>/watch https://youtube.com/watch?v=xxx</code></pre>",
            "或本地文件：<pre><code>/watch path/to/video.mp4</code></pre>"
        ],
        "insights": [
            "<strong>二次登榜：</strong>7/6 首登 +917★ 后今天再次 +434★——AI 视频分析需求持续增长。",
            "<strong>Claude 能力的「外挂」扩展：</strong>Claude 原生不支持视频，但通过抽帧+转录实现了——工具链创新比等模型升级更快。",
            "<strong>/watch 是刚需：</strong>开发者每天处理大量视频教程、会议记录——一键分析视频比手动看高效十倍。"
        ],
        "tags": ["claude", "video-analysis", "agent-tool", "ai-tool", "automation"]
    },
    {
        "rank": 7,
        "owner": "mvanhorn",
        "name": "last30days-skill",
        "fullName": "mvanhorn / last30days-skill",
        "org": "mvanhorn",
        "url": "https://github.com/mvanhorn/last30days-skill",
        "lang": "Python",
        "langClass": "py",
        "stars": "54,154",
        "forks": "4,699",
        "starsToday": "240",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +240★！54.2K★ 回归登榜！跨平台 AI 研究技能——Reddit/X/YouTube/HN/Polymarket 全网搜索，生成摘要。",
        "problems": [
            "<strong>AI Agent 信息获取碎片化：</strong>Agent 需要搜索信息但局限于单一平台。",
            "<strong>实时研究效率低：</strong>手动浏览 Reddit/X/HN 找信息太慢。",
            "<strong>缺少统一研究入口：</strong>没有「一句话研究某个话题」的一站式 Agent 方案。"
        ],
        "usage": [
            "安装到编码 Agent：<pre><code>claude add mvanhorn/last30days-skill</code></pre>",
            "一句话研究：<pre><code>/last30days AI agent funding trends</code></pre>",
            "跨平台搜索：自动搜 Reddit、X、YouTube、HN、Polymarket 并合成报告。"
        ],
        "insights": [
            "<strong>54.2K★ 回归榜单：</strong>从 6 月初连续登榜到回归——跨平台 AI 研究是 Agent 的基础能力。",
            "<strong>AI Agent 需要「上网能力」：</strong>联网搜索 + 跨平台聚合 = Agent 研究和决策的核心基础设施。",
            "<strong>技术写作与 AI 研究的交汇：</strong>last30days-skill 既是开发工具也是内容创作工具——AI 研究能力正在产品化。"
        ],
        "tags": ["research", "ai-agent", "skill", "web-search", "content-creation"]
    }
]

# Shift labels for 6-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = f'{shift-1}天前'  # 6天前
    elif label == '昨天':
        day['label'] = f'{shift}天前'  # 7天前
    elif label == '前天':
        day['label'] = f'{shift+1}天前'  # 8天前
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + shift}天前'

# Insert new day
new_day = {
    "date": "2026-07-28",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-07-28'
data['topic'] = '🔥 <strong>阿里巴巴开源 AI 代码审查引擎登顶 + Impeccable 设计品味回归 + Superfile 终端革新 + Airi 自托管 AI 伴侣 + Kronos 金融模型回归 + Claude 视频分析 + 研究技能回归</strong> —— alibaba/open-code-review（+979★）14.8K★ 阿里巴巴混构代码审查开源！确定性管线 + LLM Agent 双引擎杀入第一。pbakaus/impeccable（+847★）51.5K★ 设计品味技能二次登榜——「反 AI 味」持续刚需。yorukot/superfile（+600★）20.9K★ 终端文件管理器的 GUI 化革命。moeru-ai/airi（+572★）44K★ 自托管 Grok 伴侣 AI——从工具到陪伴。shiyu-coder/Kronos（+441★）34.6K★ 金融 AI 模型回归，AI 量化赛道升温。bradautomates/claude-video（+434★）11K★ 二次登榜，让 Claude 能看懂视频。mvanhorn/last30days-skill（+240★）54.2K★ 跨平台 AI 研究技能回归。混构代码审查 × 设计品味 × 终端革新 × AI 伴侣 × 金融模型 × 视频分析 × 研究技能——七个方向全面开花。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
