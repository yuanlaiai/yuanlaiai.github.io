#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-20 (1-day gap from 8/19)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 20)
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
        "stars": "110,562",
        "forks": "16,720",
        "starsToday": "2,221",
        "count": 5,
        "description": "🔥 亮点 —— 今日 +2,221★！110.6K★ 连续三天登榜！AI 一键生成短视频祖师爷——三天累计 +5,800★，短视频自动化出片热度持续爆发。",
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
            "<strong>三连登创纪录：</strong>+1,275★ → +2,304★ → +2,221★——三天累计近六千星，AI 视频老将迎来第二春。",
            "<strong>「一键出片」仍是刚需：</strong>短视频带货、口播、教程——自动化出片的需求从未消失。",
            "<strong>Agent 化的内容生产线：</strong>接 LLM 后从「工具」变成「内容生产线」——主题到成片全自动。"
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
        "stars": "30,147",
        "forks": "1,905",
        "starsToday": "803",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +803★！30.1K★ 连续两天登榜且热度近四倍！字节火山引擎自进化 Context Database——Agent 记忆底座持续吸星。",
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
            "<strong>连续两天热度近四倍：</strong>+213★ → +803★——字节下场后 Agent 记忆赛道加速。",
            "<strong>30K★ 破圈速度：</strong>首登 29.4K → 今天 30.1K——大厂开源 + 全矩阵运营的传播力。",
            "<strong>记忆即资产的延续：</strong>OpenViking + ai-memory 同赛道轮番登榜——记忆层正成为 Agent 基础设施的兵家必争之地。"
        ],
        "tags": ["agent-memory", "rag", "context-database", "bytedance", "agent-infra"]
    },
    {
        "rank": 3,
        "owner": "chaitanyagiri",
        "name": "munder-difflin",
        "fullName": "chaitanyagiri / munder-difflin",
        "org": "chaitanyagiri",
        "url": "https://github.com/chaitanyagiri/munder-difflin",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "2,666",
        "forks": "146",
        "starsToday": "797",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +797★！2.7K★ 连续两天登榜且热度 2.6 倍！本地免费多 Agent 编排——Dunder Mifflin 梗 + 免费双buff。",
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
            "<strong>连续两天热度 2.6 倍：</strong>+306★ → +797★——免费多 Agent 编排需求被验证。",
            "<strong>名字即营销：</strong>Dunder Mifflin（《办公室》）梗让项目自带传播力——命名是开源第一生产力。",
            "<strong>Agent 工具链填坑：</strong>记忆、编排、harness——Agent 基础设施各环节都在快速补位。"
        ],
        "tags": ["multi-agent", "claude-code", "harness", "free", "orchestration"]
    },
    {
        "rank": 4,
        "owner": "amadeusprotocol",
        "name": "node",
        "fullName": "amadeusprotocol / node",
        "org": "Amadeus Protocol",
        "url": "https://github.com/amadeusprotocol/node",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "4,512",
        "forks": "298",
        "starsToday": "1,415",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,415★！4.5K★ 首登即王炸！Amadeus 区块链节点——AssemblyScript 智能合约 + 本地 Testnet，单日千星级爆发。",
        "problems": [
            "<strong>区块链节点部署难：</strong>主流链节点配置复杂、资源占用高。",
            "<strong>合约开发门槛高：</strong>智能合约多用 Solidity，新语言栈学习成本大。",
            "<strong>测试环境搭建慢：</strong>本地测试网需要完整环境，开发迭代效率低。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/amadeusprotocol/node.git</code></pre>",
            "构建：<pre><code>./build.sh</code></pre>（docker/podman 环境）。",
            "启动本地 Testnet，用 RPC 部署 AssemblyScript 合约。"
        ],
        "insights": [
            "<strong>单日 +1,415★ 的爆发：</strong>4.5K 星一天涨三成——区块链节点类项目罕见的恐怖热度，大概率有事件驱动。",
            "<strong>AssemblyScript 合约路线：</strong>用 TypeScript 系写智能合约——降低开发者迁移门槛的差异化打法。",
            "<strong>AI × 区块链概念回暖：</strong>amadeus + GenLayer 同日登榜——AI 区块链叙事正在重新吸筹。"
        ],
        "tags": ["blockchain", "node", "smart-contract", "assemblyscript", "testnet"]
    },
    {
        "rank": 5,
        "owner": "jundot",
        "name": "omlx",
        "fullName": "jundot / omlx",
        "org": "jundot",
        "url": "https://github.com/jundot/omlx",
        "lang": "Python",
        "langClass": "py",
        "stars": "19,826",
        "forks": "1,716",
        "starsToday": "467",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +467★！19.8K★ 连续三天登榜！Apple Silicon 上的 LLM 推理服务器——菜单栏一键管理本地模型。",
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
            "<strong>三连登：</strong>+96★ → +370★ → +467★——Mac 本地推理持续升温。",
            "<strong>菜单栏 = 消费级体验：</strong>把推理服务器做成菜单栏应用——本地 AI 正在走向普通用户。",
            "<strong>边缘 AI 的 Mac 侧翼：</strong>本地推理不再只是 GPU 服务器的事——Mac 统一内存架构成为重要阵地。"
        ],
        "tags": ["llm", "apple-silicon", "inference", "local-ai", "macos"]
    },
    {
        "rank": 6,
        "owner": "immich-app",
        "name": "immich",
        "fullName": "immich-app / immich",
        "org": "Immich",
        "url": "https://github.com/immich-app/immich",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "111,852",
        "forks": "6,620",
        "starsToday": "137",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +137★！111.9K★ 隔日回归！自托管照片/视频管理——Google Photos 的开源替代，本地 AI 智能检索内建。",
        "problems": [
            "<strong>云相册隐私担忧：</strong>照片全传云端，隐私和数据主权成问题。",
            "<strong>Google Photos 收费：</strong>免费空间越来越小，订阅越来越贵。",
            "<strong>自托管门槛：</strong>NAS/服务器上管理照片需要复杂工具链。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/immich-app/immich.git</code></pre>",
            "Docker 部署：<pre><code>docker compose up -d</code></pre>",
            "手机 App 自动备份，Web 端按人脸/地点/物体智能检索。"
        ],
        "insights": [
            "<strong>111.9K★ 的自托管之王：</strong>Google Photos 替代品——隐私意识的觉醒让自托管赛道持续升温。",
            "<strong>AI 是核心卖点：</strong>人脸识别、物体检索、OCR——immich 的搜索能力全靠本地 AI 模型。",
            "<strong>数据主权运动：</strong>从照片到视频到 AI 相册——个人数据的「私有化」正成为潮流。"
        ],
        "tags": ["self-hosted", "photos", "privacy", "google-photos-alternative", "ai-search"]
    },
    {
        "rank": 7,
        "owner": "nautechsystems",
        "name": "nautilus_trader",
        "fullName": "nautechsystems / nautilus_trader",
        "org": "nautechsystems",
        "url": "https://github.com/nautechsystems/nautilus_trader",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "26,435",
        "forks": "3,438",
        "starsToday": "79",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +79★！26.4K★ 隔日回归！Rust 原生的生产级量化交易引擎——事件驱动架构、回测实盘一体化。",
        "problems": [
            "<strong>量化回测不可靠：</strong>回测和实盘不一致，策略上线就翻车。",
            "<strong>交易系统性能瓶颈：</strong>Python 回测慢，高频场景撑不住。",
            "<strong>框架碎片化：</strong>回测、实盘、风控各用一套系统，衔接困难。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/nautechsystems/nautilus_trader.git</code></pre>",
            "安装：<pre><code>pip install nautilus_trader</code></pre>",
            "回测：<pre><code>python backtest.py</code></pre>同一套代码直接上实盘。"
        ],
        "insights": [
            "<strong>隔日回归：</strong>8/18 首登后今天再次上榜——Rust 量化引擎持续稳定吸星。",
            "<strong>回测实盘一体化：</strong>同一套策略代码从回测到实盘零转换——解决量化最大痛点。",
            "<strong>性能敏感领域 Rust 化：</strong>生产级交易引擎用 Rust 重写——Rust 正在吃掉金融基建。"
        ],
        "tags": ["trading", "quant", "rust", "backtesting", "fintech"]
    },
    {
        "rank": 8,
        "owner": "genlayerlabs",
        "name": "genlayer-project-boilerplate",
        "fullName": "genlayerlabs / genlayer-project-boilerplate",
        "org": "GenLayer",
        "url": "https://github.com/genlayerlabs/genlayer-project-boilerplate",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "16,222",
        "forks": "1,410",
        "starsToday": "421",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +421★！16.2K★ 首登！GenLayer AI 区块链样板——智能合约接 LLM，足球博彩示例 + 全套测试/CI 管线。",
        "problems": [
            "<strong>合约接 LLM 难：</strong>传统智能合约无法访问互联网和模型，应用场景受限。",
            "<strong>AI 上链门槛高：</strong>在链上跑 AI 逻辑缺乏可复用的工程样板。",
            "<strong>开发体验差：</strong>合约测试、部署、CI 管线要自己搭。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/genlayerlabs/genlayer-project-boilerplate.git</code></pre>",
            "查看智能合约示例（Football Bets，含 web 访问 + LLM 集成）。",
            "跑 Direct mode 测试：<pre><code>npm test</code></pre>毫秒级完成。"
        ],
        "insights": [
            "<strong>AI × 区块链样板：</strong>智能合约带 LLM 集成 + 全套工程化管线——「AI 上链」从概念走向工程。",
            "<strong>与 amadeus 同日登榜：</strong>两个区块链 AI 项目同一天爆发——叙事板块在轮动。",
            "<strong>样板即标准：</strong>官方 boilerplate 定义开发范式——抢样板就是抢开发者心智。"
        ],
        "tags": ["blockchain", "ai", "smart-contract", "llm", "boilerplate"]
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
    "date": "2026-08-20",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-20'
data['topic'] = '🔥 <strong>MoneyPrinterTurbo 三连登 + OpenViking 连登四倍 + amadeusprotocol 单日千星 + munder-difflin 连登 2.6 倍 + omlx 三连登 + immich/nautilus 回归 + GenLayer AI 区块链</strong> —— harry0703/MoneyPrinterTurbo（+2,221★）110.6K★ 连续三天登榜，三天累计近六千星。volcengine/OpenViking（+803★）30.1K★ 连续两天热度近四倍，字节 Agent 记忆底座持续吸星。chaitanyagiri/munder-difflin（+797★）2.7K★ 连续两天 2.6 倍，免费多 Agent 编排需求被验证。amadeusprotocol/node（+1,415★）4.5K★ 首登即王炸，区块链节点单日千星爆发。jundot/omlx（+467★）19.8K★ 三连登 Mac 本地推理。immich-app/immich（+137★）111.9K★ 自托管之王回归。nautechsystems/nautilus_trader（+79★）26.4K★ Rust 量化引擎回归。genlayerlabs/genlayer-project-boilerplate（+421★）16.2K★ GenLayer AI 区块链样板首登。Agent 生态持续霸榜，AI × 区块链叙事同日异动——开源世界双线作战。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
