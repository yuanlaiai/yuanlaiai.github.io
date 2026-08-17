#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-18 (1-day gap from 8/17)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 18)
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
        "stars": "105,949",
        "forks": "16,105",
        "starsToday": "1,275",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +1,275★！105.9K★ 时隔两个多月回归登榜！AI 一键生成短视频的祖师爷级项目——输入主题，自动出片。",
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
            "<strong>时隔两个多月回归：</strong>从 6/9 到现在——AI 视频生成赛道老将依然能打，105.9K★ 持续增长。",
            "<strong>「一键出片」仍是刚需：</strong>短视频带货、口播、教程——自动化出片的需求从未消失，只是门槛被卷高了。",
            "<strong>与 Agent 时代的结合：</strong>接入 LLM 后，MoneyPrinterTurbo 从「工具」变成「内容生产线」——主题到成片全自动。"
        ],
        "tags": ["ai-video", "short-video", "automation", "content-creation", "text-to-video"]
    },
    {
        "rank": 2,
        "owner": "usestrix",
        "name": "strix",
        "fullName": "usestrix / strix",
        "org": "usestrix",
        "url": "https://github.com/usestrix/strix",
        "lang": "Python",
        "langClass": "py",
        "stars": "54,121",
        "forks": "5,794",
        "starsToday": "656",
        "count": 4,
        "description": "🔥 亮点 —— 今日 +656★！54.1K★ 第四次登榜！开源 AI 渗透测试工具——从 6/30 首登到现在 6 周涨了 2.2 万星。",
        "problems": [
            "<strong>安全测试门槛高：</strong>传统渗透测试需要专业技能和大量手动操作。",
            "<strong>漏洞发现周期长：</strong>从扫描到验证到修复流程缓慢。",
            "<strong>安全工具碎片化：</strong>不同扫描器各有专长，需要多种工具组合。"
        ],
        "usage": [
            "安装：<pre><code>pip install strix</code></pre>",
            "扫描：<pre><code>strix scan https://your-app.com</code></pre>",
            "CI 集成：<pre><code>strix ci --fail-on critical</code></pre>阻断高危漏洞。"
        ],
        "insights": [
            "<strong>第四次登榜：</strong>6/30 → 7/2 → 7/3 → 8/18——AI 安全工具从爆发走向常态。",
            "<strong>54K★ 的 6 周翻倍：</strong>32K → 54K——AI 安全是当下最确定的赛道之一。",
            "<strong>安全左移的实践：</strong>CI/CD 集成让 strix 不只是扫描器，而是开发流程中的安全检查点。"
        ],
        "tags": ["security", "penetration-testing", "ai-agent", "devsecops", "vulnerability"]
    },
    {
        "rank": 3,
        "owner": "nautechsystems",
        "name": "nautilus_trader",
        "fullName": "nautechsystems / nautilus_trader",
        "org": "nautechsystems",
        "url": "https://github.com/nautechsystems/nautilus_trader",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "25,898",
        "forks": "3,372",
        "starsToday": "115",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +115★！25.9K★ 首次登榜！Rust 原生的生产级量化交易引擎——事件驱动架构、回测实盘一体化。",
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
            "<strong>Rust 杀进量化赛道：</strong>生产级交易引擎用 Rust 重写——性能敏感领域正在全面 Rust 化。",
            "<strong>回测实盘一体化：</strong>同一套策略代码从回测到实盘零转换——解决量化最大痛点。",
            "<strong>25.9K★ 的慢热型项目：</strong>没有爆发式增长，但持续稳定吸星——基础设施类项目的典型曲线。"
        ],
        "tags": ["trading", "quant", "rust", "backtesting", "fintech"]
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
        "stars": "2,020",
        "forks": "192",
        "starsToday": "207",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +207★！2.0K★ 新项目首登！给编码 Agent 装上长期记忆——跨厂商（Claude/Codex/Cursor）交接不掉线。",
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
            "<strong>Fabio Akita 出手：</strong>巴西知名 Ruby 开发者/YouTuber——个人开发者做 Agent 基础设施的新样本。",
            "<strong>跨厂商记忆是刚需：</strong>多 Agent 工作流已成常态，「记忆接力棒」是下一个必争之地。",
            "<strong>记忆即资产：</strong>谁掌握了 Agent 的记忆层，谁就掌握了用户切换工具的迁移成本。"
        ],
        "tags": ["agent-memory", "llm", "developer-tools", "claude-code", "codex"]
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
        "stars": "18,975",
        "forks": "1,644",
        "starsToday": "96",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +96★！19.0K★ 首次登榜！Apple Silicon 上的 LLM 推理服务器——连续批处理 + SSD 缓存，菜单栏一键管理。",
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
            "<strong>Apple Silicon 推理生态成熟：</strong>连续批处理 + SSD 缓存——Mac 本地 LLM 从「能跑」走向「好用」。",
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
        "stars": "111,136",
        "forks": "6,574",
        "starsToday": "337",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +337★！111.1K★ 首次登榜！自托管照片/视频管理——Google Photos 的开源替代，本地 AI 智能检索内建。",
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
            "<strong>111K★ 的自托管之王：</strong>Google Photos 替代品——隐私意识的觉醒让自托管赛道持续升温。",
            "<strong>AI 是核心卖点：</strong>人脸识别、物体检索、OCR——immich 的搜索能力全靠本地 AI 模型。",
            "<strong>数据主权运动：</strong>从照片到视频到 AI 相册——个人数据的「私有化」正成为潮流。"
        ],
        "tags": ["self-hosted", "photos", "privacy", "google-photos-alternative", "ai-search"]
    },
    {
        "rank": 7,
        "owner": "cordiverse",
        "name": "cordis",
        "fullName": "cordiverse / cordis",
        "org": "Cordiverse",
        "url": "https://github.com/cordiverse/cordis",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "5,563",
        "forks": "296",
        "starsToday": "959",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +959★！5.6K★ 连续三天登榜且创单日新高！时空可组合性的元框架——机器人/Agent 插件的下一代基础设施。",
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
            "<strong>三天连登热度飙升：</strong>+599★ → +719★ → +959★——元框架概念持续走热且加速。",
            "<strong>插件生态基础设施：</strong>Agent 插件市场爆发前夜——需要统一的框架标准。",
            "<strong>TypeScript 生态延续：</strong>跨平台机器人框架继续由 TS 主导。"
        ],
        "tags": ["bot-framework", "typescript", "plugins", "composable", "meta-framework"]
    },
    {
        "rank": 8,
        "owner": "agalwood",
        "name": "Motrix",
        "fullName": "agalwood / Motrix",
        "org": "agalwood",
        "url": "https://github.com/agalwood/Motrix",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "53,051",
        "forks": "4,927",
        "starsToday": "295",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +295★！53.1K★ 首次登榜！全能下载管理器——HTTP/FTP/BT/磁力通吃，开源界老牌下载神器。",
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
            "<strong>老牌项目突然登榜：</strong>2018 年的项目 53K★——「去广告、去捆绑」的情绪又一次发酵。",
            "<strong>下载工具的去商业化：</strong>从 Motrix 到 aria2——开源下载工具是「反流氓软件」运动的受益者。",
            "<strong>AI 时代的下载需求：</strong>下载大模型权重、数据集——AI 时代下载管理反而是基础设施需求。"
        ],
        "tags": ["download-manager", "bt", "open-source", "cross-platform", "productivity"]
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
    "date": "2026-08-18",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-18'
data['topic'] = '🔥 <strong>短视频自动生成回归 + AI 安全四连登 + Agent 记忆新赛道 + 本地推理 Mac 化 + 自托管相册 111K + Cordis 三天连登新高 + 量化 Rust 化 + 下载神器回归</strong> —— harry0703/MoneyPrinterTurbo（+1,275★）105.9K★ 时隔两个多月回归，一键出片老将依然能打。usestrix/strix（+656★）54.1K★ 第四次登榜，AI 安全 6 周翻倍。akitaonrails/ai-memory（+207★）2.0K★ 新秀——跨厂商 Agent 长期记忆，记忆即资产。jundot/omlx（+96★）19.0K★ Apple Silicon 本地推理菜单栏化。immich-app/immich（+337★）111.1K★ 自托管相册之王，数据主权运动。cordiverse/cordis（+959★）5.6K★ 三天连登创单日新高。nautechsystems/nautilus_trader（+115★）25.9K★ Rust 量化引擎。agalwood/Motrix（+295★）53.1K★ 下载神器回归。内容生产 × 安全 × 记忆 × 本地推理 × 隐私 × 元框架 × 量化 × 下载——Agent 时代的基础设施大战全面铺开。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
