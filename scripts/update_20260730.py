#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-07-30 (1-day gap from 7/29)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 7, 30)
gap_days = (today - last).days  # 1
shift = gap_days + 1  # 2
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
        "owner": "different-ai",
        "name": "openwork",
        "fullName": "different-ai / openwork",
        "org": "Different AI",
        "url": "https://github.com/different-ai/openwork",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "18,373",
        "forks": "1,875",
        "starsToday": "916",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +916★！18.4K★ 开源版 Claude Cowork 替代品！基于 Opencode 的 AI 协作者，让 Agent 和你一起工作。",
        "problems": [
            "<strong>Claude Cowork 闭源：</strong>Anthropic 发布的 AI 协作者体验很好但不开源，无法自托管或定制。",
            "<strong>AI 协作工作流碎片化：</strong>不同 Agent 协作方案互不兼容，生态割裂。",
            "<strong>缺少透明 AI 协作者：</strong>开发者想要看得见、可修改的 AI 协作工具。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/different-ai/openwork.git</code></pre>",
            "启动：<pre><code>docker compose up</code></pre>",
            "在浏览器打开 <pre><code>http://localhost:3000</code></pre> 开始协作。"
        ],
        "insights": [
            "<strong>开源替代品爆发：</strong>Claude Cowork 发布后，社区迅速做出开源替代——这是 AI 工具开源化的典型路径。",
            "<strong>基于 Opencode：</strong>和 Claude Code 兼容的 Opencode 协议——生态兼容性是存活关键。",
            "<strong>18.4K★ 首日爆发：</strong>证明开发者想要的是一个开放、透明、可定制的 AI 协作者，不是黑盒。"
        ],
        "tags": ["ai-cowork", "open-source", "opencode", "claude-cowork", "developer-tools"]
    },
    {
        "rank": 2,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "236,008",
        "forks": "35,901",
        "starsToday": "810",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +810★！236K★ 连续两天登榜！Agent Harness 性能优化系统——技能/直觉/记忆/安全全栈调度，全编码 Agent 兼容。",
        "problems": [
            "<strong>Agent 运行效率低：</strong>编码 Agent 执行任务时缺乏系统化的性能优化机制。",
            "<strong>Agent 能力孤岛：</strong>技能、记忆、安全各管各的，缺少统一的性能调度层。",
            "<strong>跨平台兼容困难：</strong>Claude Code、Codex、Cursor 各有配置体系，无法复用。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g ecc</code></pre>",
            "初始化 Agent：<pre><code>ecc init</code></pre>",
            "优化当前项目：<pre><code>ecc optimize --harness</code></pre>"
        ],
        "insights": [
            "<strong>连续两天登榜巩固：</strong>+636★ → +810★，ECC 热度持续升温——Agent 性能优化是永恒刚需。",
            "<strong>236K★ 的 AI 基础设施：</strong>比昨天再涨 1.2K★，ECC 正在成为 AI 编码 Agent 的性能层标准。",
            "<strong>从工具到平台：</strong>技能管理→记忆优化→安全护栏→性能调度，ECC 覆盖了 Agent 运行的每一个环节。"
        ],
        "tags": ["agent-harness", "performance", "claude-code", "codex", "agent-framework"]
    },
    {
        "rank": 3,
        "owner": "paperswithbacktest",
        "name": "awesome-systematic-trading",
        "fullName": "paperswithbacktest / awesome-systematic-trading",
        "org": "PapersWithBacktest",
        "url": "https://github.com/paperswithbacktest/awesome-systematic-trading",
        "lang": "Python",
        "langClass": "py",
        "stars": "10,746",
        "forks": "1,375",
        "starsToday": "628",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +628★！10.7K★ 系统化交易资源大全——精选库、策略、书籍、博客、教程，量化交易者的一站式收藏。",
        "problems": [
            "<strong>量化交易信息碎片化：</strong>策略、库、教程散落在各处，新手不知道从哪入手。",
            "<strong>缺少高质量筛选：</strong>网上量化资源良莠不齐，需要专家精选。",
            "<strong>系统化交易学习路径不清晰：</strong>从入门到实战缺乏结构化指引。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/paperswithbacktest/awesome-systematic-trading.git</code></pre>",
            "浏览分类：各目录对应不同资源类型。",
            "官网：<pre><code>https://paperswithbacktest.com</code></pre>"
        ],
        "insights": [
            "<strong>10.7K★ 的爆发式增长：</strong>从前天 9.6K 到今天 10.7K，两天涨超 1K★——量化交易赛道正在升温。",
            "<strong>AI + 量化交易双轮驱动：</strong>昨天 Kronos 金融 AI 模型上榜，今天系统化交易资源上榜——金融科技正在全面 AI 化。",
            "<strong>awesome-list 的持久魅力：</strong>精选列表永远有市场——信息过载时代，人的筛选就是价值。"
        ],
        "tags": ["quantitative-trading", "finance", "awesome-list", "python", "algorithmic-trading"]
    },
    {
        "rank": 4,
        "owner": "huggingface",
        "name": "speech-to-speech",
        "fullName": "huggingface / speech-to-speech",
        "org": "Hugging Face",
        "url": "https://github.com/huggingface/speech-to-speech",
        "lang": "Python",
        "langClass": "py",
        "stars": "8,256",
        "forks": "1,027",
        "starsToday": "627",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +627★！8.3K★ Hugging Face 官方出品！用开源模型构建本地语音 Agent——语音到语音全链路开源方案。",
        "problems": [
            "<strong>语音 Agent 依赖云端 API：</strong>大多数语音助手（Siri/Alexa）数据上传云端，隐私无保障。",
            "<strong>语音到语音管线复杂：</strong>ASR→LLM→TTS 每一步都要选型、调参、集成。",
            "<strong>本地语音推理性能差：</strong>开源语音模型优化不足，实时交互延迟高。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/huggingface/speech-to-speech.git</code></pre>",
            "安装依赖：<pre><code>pip install -r requirements.txt</code></pre>",
            "启动语音 Agent：<pre><code>python run.py</code></pre>"
        ],
        "insights": [
            "<strong>HF 官方入局语音 Agent：</strong>Hugging Face 从模型库到框架官方出品——语音 Agent 是下一个标准能力。",
            "<strong>本地语音的隐私优势：</strong>所有处理在本地完成——对隐私敏感的场景（医疗、金融、会议）是刚需。",
            "<strong>8.3K★ 的 Launch 爆发：</strong>HF 的品牌号召力 + 语音 Agent 的广阔需求 = 爆发式增长。"
        ],
        "tags": ["speech-to-speech", "voice-agent", "huggingface", "open-source", "privacy"]
    },
    {
        "rank": 5,
        "owner": "pascalorg",
        "name": "editor",
        "fullName": "pascalorg / editor",
        "org": "Pascal",
        "url": "https://github.com/pascalorg/editor",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "19,893",
        "forks": "2,612",
        "starsToday": "617",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +617★！19.9K★ 连续两天登榜！Web 端 3D 建筑项目编辑器——TypeScript 全栈，零安装创建和分享 3D 建筑模型。",
        "problems": [
            "<strong>3D 建筑工具贵且复杂：</strong>Blender/SketchUp 学习曲线陡峭，AutoCAD 价格昂贵。",
            "<strong>3D 项目协作困难：</strong>传统 3D 文件格式大、版本管理难，分享不便。",
            "<strong>Web 端 3D 工具稀缺：</strong>浏览器中能做 3D 建模的工具少之又少。"
        ],
        "usage": [
            "直接访问：<pre><code>https://editor.pascal.app</code></pre>",
            "创建项目：选择模板开始建模。",
            "分享：一键生成链接，任何人可在线查看。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+341★ → +617★，Editor 热度翻倍——Web 3D 工具的需求被低估了。",
            "<strong>AI + 3D 建筑设计：</strong>结合 AI 生成 3D 模型的能力——editor 可能是建筑行业 AI 化的重要入口。",
            "<strong>浏览器 3D 已成熟：</strong>19.9K★ 证明纯 Web 3D 编辑器已能胜任严肃的 3D 建模工作。"
        ],
        "tags": ["3d", "architecture", "web-editor", "typescript", "design-tools"]
    },
    {
        "rank": 6,
        "owner": "mvanhorn",
        "name": "last30days-skill",
        "fullName": "mvanhorn / last30days-skill",
        "org": "mvanhorn",
        "url": "https://github.com/mvanhorn/last30days-skill",
        "lang": "Python",
        "langClass": "py",
        "stars": "55,258",
        "forks": "4,773",
        "starsToday": "377",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +377★！55.3K★ 回归登榜！跨平台 AI 研究技能——Reddit/X/YouTube/HN/Polymarket 全网搜索，一句话生成研究摘要。",
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
            "<strong>55.3K★ 回归榜单：</strong>从 7/28 上榜后再回归——跨平台 AI 研究是 Agent 的基础能力，持续有需求。",
            "<strong>AI Agent 需要「联网能力」：</strong>联网搜索 + 跨平台聚合 = Agent 研究和决策的核心基础设施。",
            "<strong>技术写作与 AI 研究的交汇：</strong>last30days-skill 既是开发工具也是内容创作工具——Agent 正在模糊工具和媒体的边界。"
        ],
        "tags": ["research", "ai-agent", "skill", "web-search", "content-creation"]
    },
    {
        "rank": 7,
        "owner": "agavra",
        "name": "tuicr",
        "fullName": "agavra / tuicr",
        "org": "agavra",
        "url": "https://github.com/agavra/tuicr",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "1,705",
        "forks": "152",
        "starsToday": "338",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +338★！1.7K★ 代码审查 TUI——用 Rust 编写，Vim 键位绑定，终端里的代码审查利器。",
        "problems": [
            "<strong>代码审查体验差：</strong>GitHub PR 审查的 Web 界面操作繁琐，键盘流用户效率低。",
            "<strong>缺少终端原生审查工具：</strong>开发者想要在终端里完成审查，不用切换到浏览器。",
            "<strong>Vim 用户缺乏适配：</strong>主流代码审查工具没有为 Vim 键位做优化。"
        ],
        "usage": [
            "安装：<pre><code>cargo install tuicr</code></pre>",
            "审查 PR：<pre><code>tuicr review https://github.com/user/repo/pull/123</code></pre>",
            "Vim 键位：<pre><code>hjkl</code></pre> 导航，<pre><code>c</code></pre> 评论，<pre><code>q</code></pre> 退出。"
        ],
        "insights": [
            "<strong>Rust 终端工具新秀：</strong>1.7K★ 体量虽小但增长迅猛——开发者对原生终端体验的追求从未停止。",
            "<strong>代码审查的终端化：</strong>从 GitHub Web UI 到 TUI——代码审查回归终端的趋势正在加速。",
            "<strong>Vim 键位是核心体验：</strong>专门为 Vim 用户设计的代码审查工具——小但忠诚的用户群。"
        ],
        "tags": ["code-review", "tui", "rust", "vim", "terminal"]
    }
]

# Shift labels for 1-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '昨天'
    elif label == '昨天':
        day['label'] = '前天'
    elif label == '前天':
        day['label'] = '3天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + 2}天前'

# Insert new day
new_day = {
    "date": "2026-07-30",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-07-30'
data['topic'] = '🔥 <strong>OpenWork 开源 Claude Cowork 首日爆发 + ECC 两天连涨 236K + 量化交易资源爆棚 + HF 语音 Agent + Editor 3D 翻倍 + Last30days 研究回归 + TUICR 终端审查</strong> —— different-ai/openwork（+916★）18.4K★ 开源版 Claude Cowork 替代品！基于 Opencode 的 AI 协作者，首日即爆。affaan-m/ECC（+810★）236K★ 连续两天登榜加速，Agent 性能标准层。paperswithbacktest/awesome-systematic-trading（+628★）10.7K★ 量化交易资源大全，AI+金融双轮驱动。huggingface/speech-to-speech（+627★）8.3K★ HF 官方语音 Agent 方案，本地语音赛道爆发。pascalorg/editor（+617★）19.9K★ Web 3D 编辑器两天翻倍。mvanhorn/last30days-skill（+377★）55.3K★ 跨平台 AI 研究回归。agavra/tuicr（+338★）1.7K★ Rust 终端代码审查新秀。开源协作者 × Agent 优化 × 量化交易 × 语音 Agent × 3D 建筑 × AI 研究 × 终端审查——七条赛道同日开花，AI 工具链向全场景渗透。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
