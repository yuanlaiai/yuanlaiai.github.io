#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-17 (1-day gap from 8/16)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 17)
gap_days = (today - last).days  # 1
shift = gap_days + 1  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

today_projects = [
    {
        "rank": 1,
        "owner": "public-apis",
        "name": "public-apis",
        "fullName": "public-apis / public-apis",
        "org": "public-apis",
        "url": "https://github.com/public-apis/public-apis",
        "lang": "Python",
        "langClass": "py",
        "stars": "461,674",
        "forks": "50,996",
        "starsToday": "1,583",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +1,583★！461.7K★ 连续两天登榜！免费 API 大全——Agent 时代的「数据弹药库」持续升温。",
        "problems": [
            "<strong>API 发现难：</strong>开发者需要找免费 API 但缺乏统一索引。",
            "<strong>信息过载：</strong>网上 API 目录质量参差，缺少人工筛选。",
            "<strong>Agent 需要数据源：</strong>AI Agent 工具调用需要大量可用的外部 API。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/public-apis/public-apis.git</code></pre>",
            "按分类浏览：<pre><code>ls categories/</code></pre>",
            "接入 Agent 工具：直接把 API 列表喂给编码 Agent。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+2,260★ → +1,583★——461.7K★ 免费 API 大全热度持续。",
            "<strong>Agent 时代的弹药库：</strong>AI Agent 工具调用需要数据源——public-apis 成了 Agent 开发者的首选资源。",
            "<strong>清单类项目的持久价值：</strong>社区持续维护的「信息基础设施」——46 万星的传奇还在增长。"
        ],
        "tags": ["api", "open-source", "developer-tools", "resources", "data"]
    },
    {
        "rank": 2,
        "owner": "cordiverse",
        "name": "cordis",
        "fullName": "cordiverse / cordis",
        "org": "Cordiverse",
        "url": "https://github.com/cordiverse/cordis",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "4,691",
        "forks": "244",
        "starsToday": "719",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +719★！4.7K★ 连续两天登榜！时空可组合性的元框架——机器人/Agent 插件的下一代基础设施。",
        "problems": [
            "<strong>机器人插件碎片化：</strong>不同平台的机器人框架互不兼容。",
            "<strong>可组合性差：</strong>插件之间难以复用和组合，开发效率低。",
            "<strong>跨平台部署困难：</strong>同一套逻辑难以在不同平台上运行。"
        ],
        "usage": [
            "安装：<pre><code>npm install cordis</code></pre>",
            "创建项目：<pre><code>cordis create</code></pre>",
            "构建跨平台机器人/Agent 应用。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+599★ → +719★——元框架概念持续走热。",
            "<strong>插件生态基础设施：</strong>Agent 插件市场爆发前夜——需要统一的框架标准。",
            "<strong>TypeScript 生态延续：</strong>跨平台机器人框架继续由 TS 主导。"
        ],
        "tags": ["bot-framework", "typescript", "plugins", "composable", "meta-framework"]
    },
    {
        "rank": 3,
        "owner": "unslothai",
        "name": "unsloth",
        "fullName": "unslothai / unsloth",
        "org": "Unsloth AI",
        "url": "https://github.com/unslothai/unsloth",
        "lang": "Python",
        "langClass": "py",
        "stars": "72,534",
        "forks": "6,542",
        "starsToday": "580",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +580★！72.5K★ 连续三天登榜！本地训练/运行 LLM 和扩散模型的 UI——Qwen3.8、Kimi K3、DeepSeek-V4 全家桶支持。",
        "problems": [
            "<strong>本地微调门槛高：</strong>LLM 训练需要复杂的命令行和配置。",
            "<strong>模型生态碎片化：</strong>不同模型需要不同的工具链。",
            "<strong>GPU 利用率低：</strong>本地训练缺少性能优化。"
        ],
        "usage": [
            "安装：<pre><code>pip install unsloth</code></pre>",
            "启动 UI：<pre><code>unsloth ui</code></pre>",
            "选择模型开始训练或运行。"
        ],
        "insights": [
            "<strong>连续三天登榜：</strong>+328★ → +434★ → +580★——本地 AI 主力工具持续升温。",
            "<strong>中国模型全家桶支持：</strong>Qwen3.8、Kimi K3、DeepSeek-V4——中国开源模型的传播基础设施。",
            "<strong>本地 AI 加速普及：</strong>GUI 化让微调从极客走向普通开发者。"
        ],
        "tags": ["fine-tuning", "local-llm", "ui", "training", "open-source"]
    },
    {
        "rank": 4,
        "owner": "cactus-compute",
        "name": "needle",
        "fullName": "cactus-compute / needle",
        "org": "Cactus Compute",
        "url": "https://github.com/cactus-compute/needle",
        "lang": "Python",
        "langClass": "py",
        "stars": "6,540",
        "forks": "431",
        "starsToday": "447",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +447★！6.5K★ 连续三天登榜！14MB 基础模型——手机、可穿戴、智能家居和机器人的端侧 AI 新宠。",
        "problems": [
            "<strong>边缘设备无法跑大模型：</strong>手机、手表、智能家居内存和算力有限。",
            "<strong>云端推理隐私风险：</strong>小型设备依赖云端 AI，敏感数据外传。",
            "<strong>端侧 AI 生态空白：</strong>缺少为微型设备优化的基础模型。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cactus-compute/needle.git</code></pre>",
            "安装：<pre><code>pip install needle</code></pre>",
            "部署到手机/手表/智能家居/机器人。"
        ],
        "insights": [
            "<strong>连续三天登榜：</strong>+769★ → +547★ → +447★——14MB 微型模型持续走热。",
            "<strong>端侧 AI 爆发前夜：</strong>手机、穿戴、智能家居都需要本地智能——needle 押注微型设备赛道。",
            "<strong>隐私是驱动力：</strong>数据不出设备——端侧推理是隐私保护的终极方案。"
        ],
        "tags": ["edge-ai", "tiny-model", "embedded", "privacy", "on-device"]
    },
    {
        "rank": 5,
        "owner": "ToolJet",
        "name": "ToolJet",
        "fullName": "ToolJet / ToolJet",
        "org": "ToolJet",
        "url": "https://github.com/ToolJet/ToolJet",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "39,997",
        "forks": "5,329",
        "starsToday": "446",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +446★！40K★ 开源企业应用生成平台——内部工具、仪表盘、业务流程、AI Agent 一站式搭建。",
        "problems": [
            "<strong>内部工具开发慢：</strong>企业需要大量内部工具但开发成本高。",
            "<strong>低代码平台能力弱：</strong>现有低代码工具难以支撑复杂业务应用。",
            "<strong>Agent 集成缺位：</strong>企业内部工具与 AI Agent 工作流脱节。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/ToolJet/ToolJet.git</code></pre>",
            "部署：<pre><code>docker compose up</code></pre>",
            "拖拽搭建内部工具与 AI Agent 工作流。"
        ],
        "insights": [
            "<strong>40K★ 的低代码平台：</strong>ToolJet AI——企业应用生成平台 + AI Agent——低代码与 Agent 融合的新方向。",
            "<strong>企业内部工具刚需：</strong>业务应用、仪表盘、工作流——开源低代码持续走强。",
            "<strong>Agent 时代的低代码：</strong>从拖拽 UI 到 AI 生成——企业应用开发正在被重新定义。"
        ],
        "tags": ["low-code", "internal-tools", "enterprise", "dashboard", "workflow"]
    },
    {
        "rank": 6,
        "owner": "basecamp",
        "name": "omarchy",
        "fullName": "basecamp / omarchy",
        "org": "Basecamp",
        "url": "https://github.com/basecamp/omarchy",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "25,347",
        "forks": "2,588",
        "starsToday": "225",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +225★！25.3K★ Basecamp/DHH 出品的现代化 Linux 发行版——「Beautiful, Modern & Opinionated」哲学。",
        "problems": [
            "<strong>Linux 发行版碎片化：</strong>现有发行版配置复杂、审美参差。",
            "<strong>开发环境搭建繁琐：</strong>新机器初始化需要大量手动配置。",
            "<strong>缺乏开箱即用体验：</strong>开发者需要开箱即用的现代化 Linux 环境。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/basecamp/omarchy.git</code></pre>",
            "阅读安装文档：<pre><code>cat README.md</code></pre>",
            "按指南安装配置。"
        ],
        "insights": [
            "<strong>DHH 的 Linux 哲学：</strong>Basecamp 出品——「美观、现代、有主见」的 Linux——DHH 继续用行动对抗大厂生态。",
            "<strong>25.3K★ 的极客情怀：</strong>开发者自建 OS 的浪漫——omarchy 承载了「摆脱依赖」的思潮。",
            "<strong>与 AI 的关系：</strong>DHH 之前聊过 AI 写内核——omarchy 是他 AI 工作流的一部分。"
        ],
        "tags": ["linux", "basecamp", "dhh", "distro", "developer-tools"]
    },
    {
        "rank": 7,
        "owner": "OpenCut-app",
        "name": "OpenCut",
        "fullName": "OpenCut-app / OpenCut",
        "org": "OpenCut",
        "url": "https://github.com/OpenCut-app/OpenCut",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "83,852",
        "forks": "8,280",
        "starsToday": "134",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +134★！83.9K★ 开源版 CapCut——剪映/CapCut 的开源替代品。",
        "problems": [
            "<strong>视频剪辑工具贵：</strong>专业剪辑软件订阅贵，CapCut 有版权顾虑。",
            "<strong>开源视频编辑缺位：</strong>缺少现代化、好用的开源视频剪辑工具。",
            "<strong>模板生态封闭：</strong>商业剪辑工具的模板资源封闭。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/OpenCut-app/OpenCut.git</code></pre>",
            "安装依赖：<pre><code>npm install</code></pre>",
            "启动本地视频剪辑工具。"
        ],
        "insights": [
            "<strong>83.9K★ 的开源剪辑替代：</strong>CapCut 开源替代品——视频创作工具的去大厂化趋势。",
            "<strong>创作工具生态开源化：</strong>从设计到剪辑——创作工具链正在全面开源。",
            "<strong>与 AI 视频的衔接：</strong>AI 生成视频后需要编辑——OpenCut 是 AI 内容工作流的编辑端。"
        ],
        "tags": ["video-editing", "capcut", "open-source", "creative-tools", "typescript"]
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
    "date": "2026-08-17",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-17'
data['topic'] = '🔥 <strong>Public APIs 连登 + Cordis 连登 + Unsloth 三天连登 + Needle 三天连登 + ToolJet 40K 星 + Omarchy DHH Linux + OpenCut 剪映开源替代</strong> —— public-apis/public-apis（+1,583★）461.7K★ 连续两天免费 API 大全。cordiverse/cordis（+719★）4.7K★ 连续两天时空可组合元框架。unslothai/unsloth（+580★）72.5K★ 连续三天本地训练 UI。cactus-compute/needle（+447★）6.5K★ 连续三天 14MB 微型模型。ToolJet/ToolJet（+446★）40K★ 企业应用生成平台 + AI Agent。basecamp/omarchy（+225★）25.3K★ DHH 的现代化 Linux。OpenCut-app/OpenCut（+134★）83.9K★ 开源版 CapCut。数据弹药 × 元框架 × 本地训练 × 微型模型 × 低代码 × Linux × 剪辑——开源基础设施生态全面开花。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
