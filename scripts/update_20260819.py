#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-19 (1-day gap from 8/18)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 19)
gap_days = (today - last).days  # 1
shift = gap_days + 1  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

today_projects = [
    {
        "rank": 1,
        "owner": "harry0703",
        "name": "MoneyPrinterTurbo",
        "fullName": "harry0703 / MoneyPrinterTurbo",
        "org": "harry0703",
        "url": "https://github.com/harry0703/MoneyPrinterTurbo",
        "lang": "Python",
        "langClass": "py",
        "stars": "108,511",
        "forks": "16,405",
        "starsToday": "2,304",
        "count": 4,
        "description": "🔥 亮点 —— 今日 +2,304★！108.5K★ 连续两天登榜且热度翻倍！AI 一键生成短视频祖师爷——+1,275★ → +2,304★，短视频自动化出片需求二次爆发。",
        "problems": [
            "<strong>短视频制作门槛高：</strong>写脚本、配音、剪辑、配乐——一个人做一条视频要几小时。",
            "<strong>内容创作重复劳动：</strong>批量做口播/带货视频需要大量重复操作。",
            "<strong>AI 工具碎片化：</strong>生成文案、语音、画面的工具分散，难以串成流水线。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/harry0703/MoneyPrinterTurbo.git</code></pre>",
            "启动：<pre><code>docker compose up</code></pre>打开 Web 界面。",
            "输入主题或关键词，一键生成完整短视频。"
        ],
        "insights": [
            "<strong>连续两天登榜热度翻倍：</strong>+1,275★ → +2,304★——AI 视频生成老将迎来第二春。",
            "<strong>「一键出片」仍是刚需：</strong>短视频带货、口播、教程——自动化出片的需求从未消失。",
            "<strong>与 Agent 时代的结合：</strong>接入 LLM 后从「工具」变成「内容生产线」——主题到成片全自动。"
        ],
        "tags": ["ai-video", "short-video", "automation", "content-creation", "text-to-video"]
    },
    {
        "rank": 2,
        "owner": "volcengine",
        "name": "OpenViking",
        "fullName": "volcengine / OpenViking",
        "org": "火山引擎",
        "url": "https://github.com/volcengine/OpenViking",
        "lang": "Python",
        "langClass": "py",
        "stars": "29,365",
        "forks": "1,842",
        "starsToday": "213",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +213★！29.4K★ 首登！字节火山引擎开源自进化 Context Database——统一 Agent 记忆、RAG 与技能。",
        "problems": [
            "<strong>Agent 记忆碎片化：</strong>对话记忆、知识库、技能各自为政，上下文无法统一管理。",
            "<strong>RAG 与记忆割裂：</strong>检索增强和长期记忆是两套系统，Agent 无法自学习。",
            "<strong>上下文无进化机制：</strong>Agent 用的知识不会随使用自动更新和沉淀。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/volcengine/OpenViking.git</code></pre>",
            "安装：<pre><code>pip install openviking</code></pre>",
            "接入 Agent 框架，统一记忆/知识/技能三合一。"
        ],
        "insights": [
            "<strong>字节开源 Agent 记忆层：</strong>火山引擎亲自下场——「自进化上下文数据库」是 Agent 基础设施的关键卡位。",
            "<strong>记忆即资产的延续：</strong>继 ai-memory 后字节也押注 Agent 记忆——这个赛道正在升温。",
            "<strong>中国大厂开源节奏加快：</strong>从 Qwen 30 亿下载到 OpenViking——中国开源从模型卷到基础设施。"
        ],
        "tags": ["agent-memory", "rag", "context-database", "bytedance", "agent-infra"]
    },
    {
        "rank": 3,
        "owner": "public-apis",
        "name": "public-apis",
        "fullName": "public-apis / public-apis",
        "org": "public-apis",
        "url": "https://github.com/public-apis/public-apis",
        "lang": "Python",
        "langClass": "py",
        "stars": "464,532",
        "forks": "51,206",
        "starsToday": "1,005",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +1,005★！464.5K★ 隔日回归！免费 API 大全——Agent 时代的「数据弹药库」三天两登榜。",
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
            "<strong>三天两登榜：</strong>8/16 → 8/17 → 8/19——46.4 万星的传奇清单持续吸星。",
            "<strong>Agent 时代的弹药库：</strong>AI Agent 工具调用需要数据源——public-apis 成了 Agent 开发者的首选资源。",
            "<strong>清单类项目的持久价值：</strong>社区持续维护的「信息基础设施」——长尾需求永不消退。"
        ],
        "tags": ["api", "open-source", "developer-tools", "resources", "data"]
    },
    {
        "rank": 4,
        "owner": "akitaonrails",
        "name": "ai-memory",
        "fullName": "akitaonrails / ai-memory",
        "org": "akitaonrails",
        "url": "https://github.com/akitaonrails/ai-memory",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "2,717",
        "forks": "248",
        "starsToday": "648",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +648★！2.7K★ 连续两天登榜且热度三倍！给编码 Agent 装上长期记忆——跨厂商交接不掉线。",
        "problems": [
            "<strong>Agent 没有长期记忆：</strong>每次会话都是「失忆」状态，项目上下文要反复重讲。",
            "<strong>跨 Agent 交接断裂：</strong>Claude Code 和 Codex 之间切换，上下文全部丢失。",
            "<strong>记忆格式不统一：</strong>各家 Agent 的记忆存储互不兼容，迁移成本高。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/akitaonrails/ai-memory.git</code></pre>",
            "初始化记忆库：<pre><code>ai-memory init</code></pre>",
            "在不同编码 Agent 间共享同一份项目记忆。"
        ],
        "insights": [
            "<strong>连续两天热度三倍：</strong>+207★ → +648★——Agent 记忆赛道加速升温。",
            "<strong>记忆即资产：</strong>谁掌握了 Agent 的记忆层，谁就掌握了用户切换工具的迁移成本。",
            "<strong>个人开发者样本：</strong>Fabio Akita 一个人做的项目两天 2.7K★——基础设施级需求不挑团队大小。"
        ],
        "tags": ["agent-memory", "llm", "developer-tools", "claude-code", "codex"]
    },
    {
        "rank": 5,
        "owner": "bojieli",
        "name": "ai-agent-book",
        "fullName": "bojieli / ai-agent-book",
        "org": "bojieli",
        "url": "https://github.com/bojieli/ai-agent-book",
        "lang": "Python",
        "langClass": "py",
        "stars": "39,100",
        "forks": "5,302",
        "starsToday": "543",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +543★！39.1K★ 首登！李博杰《深入理解 AI Agent：设计原理与工程实践》开源全书+配套代码。",
        "problems": [
            "<strong>Agent 知识碎片化：</strong>网上教程零散，缺少系统化的设计原理教材。",
            "<strong>理论与实践脱节：</strong>概念看懂了但不会动手实现。",
            "<strong>中文优质资料稀缺：</strong>AI Agent 深度中文教材严重不足。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/bojieli/ai-agent-book.git</code></pre>",
            "阅读全书正文与编译版 PDF。",
            "按章运行配套代码，边学边练。"
        ],
        "insights": [
            "<strong>39K★ 的中文技术书：</strong>李博杰（前华为诺亚方舟）的 Agent 专著——中文开发者对系统性知识的需求被验证。",
            "<strong>开源书成为新赛道：</strong>从《动手学深度学习》到 AI Agent 书——技术书开源是开发者教育的最高效分发。",
            "<strong>Agent 工程师的「圣经」候选：</strong>设计原理+工程实践+代码三合一，正赶上 Agent 岗位爆发期。"
        ],
        "tags": ["ai-agent", "book", "education", "llm", "coding-agent"]
    },
    {
        "rank": 6,
        "owner": "jundot",
        "name": "omlx",
        "fullName": "jundot / omlx",
        "org": "jundot",
        "url": "https://github.com/jundot/omlx",
        "lang": "Python",
        "langClass": "py",
        "stars": "19,390",
        "forks": "1,680",
        "starsToday": "370",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +370★！19.4K★ 连续两天登榜！Apple Silicon 上的 LLM 推理服务器——菜单栏一键管理本地模型。",
        "problems": [
            "<strong>Mac 本地跑大模型慢：</strong>显存不够、批处理低效，Mac 上本地推理体验差。",
            "<strong>内存瓶颈：</strong>大模型装不进统一内存，只能降级用小模型。",
            "<strong>命令行门槛高：</strong>本地推理部署复杂，普通用户难以使用。"
        ],
        "usage": [
            "安装：<pre><code>brew install omlx</code></pre>",
            "启动：菜单栏点击 omlx，选择模型即开即用。",
            "通过 OpenAI 兼容 API 接入任何客户端。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+96★ → +370★——Mac 本地推理热度翻近四倍。",
            "<strong>菜单栏 = 消费级体验：</strong>把推理服务器做成菜单栏应用——本地 AI 正在走向普通用户。",
            "<strong>边缘 AI 的 Mac 侧翼：</strong>本地推理不再只是 GPU 服务器的事——Mac 统一内存架构成为重要阵地。"
        ],
        "tags": ["llm", "apple-silicon", "inference", "local-ai", "macos"]
    },
    {
        "rank": 7,
        "owner": "agalwood",
        "name": "Motrix",
        "fullName": "agalwood / Motrix",
        "org": "agalwood",
        "url": "https://github.com/agalwood/Motrix",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "53,652",
        "forks": "4,971",
        "starsToday": "609",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +609★！53.7K★ 连续两天登榜且热度翻倍！全能下载管理器——HTTP/FTP/BT/磁力通吃。",
        "problems": [
            "<strong>下载工具碎片化：</strong>普通下载、BT、磁力各用不同软件。",
            "<strong>商业下载器广告多：</strong>国产下载器捆绑广告和流氓行为。",
            "<strong>跨平台需求：</strong>Windows/Mac/Linux 需要统一的下载体验。"
        ],
        "usage": [
            "安装：<pre><code>brew install --cask motrix</code></pre>",
            "启动 Motrix，浏览器插件一键接管下载。",
            "支持 HTTP/FTP/BT/磁力链接，任务列表全程可视化。"
        ],
        "insights": [
            "<strong>连续两天登榜热度翻倍：</strong>+295★ → +609★——「去广告、去捆绑」情绪持续发酵。",
            "<strong>下载工具的去商业化：</strong>从 Motrix 到 aria2——开源下载工具是「反流氓软件」运动的受益者。",
            "<strong>AI 时代的下载需求：</strong>下载大模型权重、数据集——AI 时代下载管理反而是基础设施需求。"
        ],
        "tags": ["download-manager", "bt", "open-source", "cross-platform", "productivity"]
    },
    {
        "rank": 8,
        "owner": "basecamp",
        "name": "omarchy",
        "fullName": "basecamp / omarchy",
        "org": "Basecamp",
        "url": "https://github.com/basecamp/omarchy",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "26,421",
        "forks": "1,206",
        "starsToday": "356",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +356★！26.4K★ 隔日回归！DHH 的现代化 Linux——Beautiful, Modern & Opinionated。",
        "problems": [
            "<strong>Linux 发行版臃肿：</strong>主流发行版系统负担重、配置繁琐。",
            "<strong>桌面体验割裂：</strong>Linux 桌面美观度和一致性长期被诟病。",
            "<strong>极简需求无人满足：</strong>想要「开箱即用且好看」的 Linux 选择太少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/basecamp/omarchy.git</code></pre>",
            "按文档构建自己的 omarchy 系统。",
            "体验 DHH 风格的现代化 Linux 桌面。"
        ],
        "insights": [
            "<strong>隔日回归：</strong>8/17 → 8/19——DHH 的 Linux 持续有话题性。",
            "<strong>25K★ 的极客情怀：</strong>开发者自建 OS 的浪漫——omarchy 承载了「摆脱依赖」的思潮。",
            "<strong>与 AI 的关系：</strong>DHH 的 AI 工作流中包含 AI 写内核——omarchy 是他的试验田。"
        ],
        "tags": ["linux", "basecamp", "dhh", "distro", "developer-tools"]
    },
    {
        "rank": 9,
        "owner": "chaitanyagiri",
        "name": "munder-difflin",
        "fullName": "chaitanyagiri / munder-difflin",
        "org": "chaitanyagiri",
        "url": "https://github.com/chaitanyagiri/munder-difflin",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "2,022",
        "forks": "112",
        "starsToday": "306",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +306★！2.0K★ 首登！本地多 Agent 编排工具（名字致敬《办公室》）——免费搞定 Claude Code 多 Agent 协作。",
        "problems": [
            "<strong>多 Agent 编排复杂：</strong>同时跑多个编码 Agent 需要复杂配置。",
            "<strong>协作成本高：</strong>Agent 之间缺乏统一的任务协调机制。",
            "<strong>免费方案稀缺：</strong>多 Agent 工具多收费，本地免费方案少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/chaitanyagiri/munder-difflin.git</code></pre>",
            "启动本地多 Agent harness。",
            "配置多个 Claude Code 实例协同工作。"
        ],
        "insights": [
            "<strong>免费多 Agent 编排：</strong>2K★ 首登——本地、免费、多 Agent 是开发者刚需。",
            "<strong>名字即营销：</strong>Dunder Mifflin（《办公室》）梗让项目自带传播力。",
            "<strong>Agent 基础设施细分：</strong>记忆、编排、harness——Agent 工具链正在快速填坑。"
        ],
        "tags": ["multi-agent", "claude-code", "harness", "free", "orchestration"]
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
    "date": "2026-08-19",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-19'
data['topic'] = '🔥 <strong>MoneyPrinterTurbo 连登翻倍 + 火山引擎 OpenViking 首登 + public-apis 回归 + ai-memory 连登三倍 + AI Agent 开源书 39K + omlx 连登 + Motrix 连登 + omarchy + 免费多 Agent 编排</strong> —— harry0703/MoneyPrinterTurbo（+2,304★）108.5K★ 连续两天登榜且热度翻倍。volcengine/OpenViking（+213★）29.4K★ 字节火山引擎自进化 Context Database 首登——Agent 记忆赛道大厂下场。public-apis/public-apis（+1,005★）464.5K★ 三天两登榜。akitaonrails/ai-memory（+648★）2.7K★ 连续两天热度三倍。bojieli/ai-agent-book（+543★）39.1K★ 李博杰《深入理解 AI Agent》开源书。jundot/omlx（+370★）19.4K★ Mac 本地推理连登。agalwood/Motrix（+609★）53.7K★ 连登翻倍。basecamp/omarchy（+356★）26.4K★ DHH Linux 回归。chaitanyagiri/munder-difflin（+306★）2.0K★ 免费多 Agent 编排。Agent 记忆、编排、教材、视频、数据——Agent 基础设施军备竞赛全面铺开，中国大厂下场抢位。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
