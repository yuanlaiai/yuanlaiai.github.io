#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-16 (2-day gap from 8/14)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 16)
gap_days = (today - last).days  # 2
shift = gap_days + 1  # 3
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
        "stars": "460,566",
        "forks": "50,884",
        "starsToday": "2,260",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +2,260★！460.6K★ 免费 API 大全回归登榜——Agent 时代的「数据弹药库」，46 万星的开源传奇。",
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
            "<strong>460.6K★ 开源传奇：</strong>GitHub 最知名项目之一——免费 API 大全在 Agent 时代焕发第二春。",
            "<strong>Agent 时代的弹药库：</strong>AI Agent 工具调用需要数据源——public-apis 成了 Agent 开发者的首选资源。",
            "<strong>2,260★ 单日回归：</strong>社区持续维护的「信息基础设施」——清单类项目的持久价值。"
        ],
        "tags": ["api", "open-source", "developer-tools", "resources", "data"]
    },
    {
        "rank": 2,
        "owner": "cathrynlavery",
        "name": "diagram-design",
        "fullName": "cathrynlavery / diagram-design",
        "org": "cathrynlavery",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "lang": "HTML",
        "langClass": "html",
        "stars": "18,944",
        "forks": "1,150",
        "starsToday": "1,607",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +1,607★！18.9K★ 连续三天登榜！29 种编辑级图表设计给 Claude Code——反 Mermaid-slop 三天涨 1.9 万星。",
        "problems": [
            "<strong>AI 图表千篇一律：</strong>Mermaid 生成的图表模板感强，缺乏设计感。",
            "<strong>图表设计门槛高：</strong>编辑级图表需要专业设计技能，普通开发者做不出来。",
            "<strong>缺少可直接用的图表库：</strong>想让 Claude 生成高质量图表，但没有设计规范可循。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cathrynlavery/diagram-design.git</code></pre>",
            "按类型加载图表设计到 Claude Code。",
            "生成自包含 HTML + SVG 图表，无需额外依赖。"
        ],
        "insights": [
            "<strong>连续三天登榜：</strong>+2,855★ → +4,475★ → +1,607★ 三天涨 1.9 万星——编辑级图表是现象级需求。",
            "<strong>设计类 Agent 技能持续走红：</strong>把专业设计标准注入 Agent 输出——审美革命延伸到图表领域。",
            "<strong>18.9K★ 的验证：</strong>「反 AI 味」不只停留在文本，图表设计成为新战场。"
        ],
        "tags": ["diagram", "claude-code", "design", "svg", "html"]
    },
    {
        "rank": 3,
        "owner": "github",
        "name": "spec-kit",
        "fullName": "github / spec-kit",
        "org": "GitHub",
        "url": "https://github.com/github/spec-kit",
        "lang": "Python",
        "langClass": "py",
        "stars": "129,315",
        "forks": "11,564",
        "starsToday": "892",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +892★！129.3K★ GitHub 官方出品！Spec-Driven Development 工具包——规范驱动的开发，让 Agent 按规格干活。",
        "problems": [
            "<strong>开发需求模糊：</strong>AI Agent 编码时缺乏明确的规格定义，容易跑偏。",
            "<strong>Spec 驱动开发门槛：</strong>规范驱动开发（SDD）概念好但缺少工具支撑。",
            "<strong>Agent 协作缺标准：</strong>多个 Agent 协作开发时没有统一的规格语言。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/github/spec-kit.git</code></pre>",
            "初始化：<pre><code>spec-kit init</code></pre>",
            "编写规范并用 Agent 实现。"
        ],
        "insights": [
            "<strong>GitHub 官方押注 SDD：</strong>规范驱动开发（Spec-Driven Development）——GitHub 认为 Agent 时代需要「先写规格再写代码」。",
            "<strong>129.3K★ 的高增速：</strong>官方背书 + 方法论创新——规范驱动开发正在成为 Agent 协作的新范式。",
            "<strong>从 TDD 到 SDD：</strong>测试驱动开发之后，规范驱动开发——Agent 时代的工程方法论演进。"
        ],
        "tags": ["spec-driven", "github", "development-methodology", "agent", "sdd"]
    },
    {
        "rank": 4,
        "owner": "citrolabs",
        "name": "ego-lite",
        "fullName": "citrolabs / ego-lite",
        "org": "Citro Labs",
        "url": "https://github.com/citrolabs/ego-lite",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "11,169",
        "forks": "569",
        "starsToday": "545",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +545★！11.2K★ 给 AI Agent 用的最快浏览器——把你的登录态共享给 Agent 跑自动化，零成本零配置。",
        "problems": [
            "<strong>Agent 浏览器自动化慢：</strong>通用浏览器给 Agent 用效率低，环境初始化慢。",
            "<strong>登录态共享难：</strong>Agent 需要访问你的已登录服务，但共享凭证麻烦。",
            "<strong>配置复杂：</strong>现有浏览器自动化工具需要大量配置。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g ego-lite</code></pre>",
            "启动：<pre><code>ego-lite</code></pre>",
            "共享浏览器登录态给 Codex/Claude Code 等 Agent。"
        ],
        "insights": [
            "<strong>11.2K★ 的 Agent 浏览器赛道：</strong>「给 Agent 用的浏览器」——登录态共享 + 零配置是核心卖点。",
            "<strong>浏览器即 Agent 的手：</strong>从 Cloudflare computer 到 ego-lite——Agent 操作 Web 的基础设施竞争白热化。",
            "<strong>登录态共享的隐私问题：</strong>把浏览器状态共享给 Agent——便利与风险并存的新领域。"
        ],
        "tags": ["browser-automation", "agent", "login-state", "automation", "browser"]
    },
    {
        "rank": 5,
        "owner": "cactus-compute",
        "name": "needle",
        "fullName": "cactus-compute / needle",
        "org": "Cactus Compute",
        "url": "https://github.com/cactus-compute/needle",
        "lang": "Python",
        "langClass": "py",
        "stars": "6,187",
        "forks": "411",
        "starsToday": "547",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +547★！6.2K★ 连续两天登榜！14MB 基础模型——手机、可穿戴、智能家居和机器人的端侧 AI 新宠。",
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
            "<strong>连续两天登榜：</strong>+769★ → +547★——14MB 微型模型需求稳定增长。",
            "<strong>端侧 AI 爆发前夜：</strong>手机、穿戴、智能家居都需要本地智能——needle 押注微型设备赛道。",
            "<strong>隐私是驱动力：</strong>数据不出设备——端侧推理是隐私保护的终极方案。"
        ],
        "tags": ["edge-ai", "tiny-model", "embedded", "privacy", "on-device"]
    },
    {
        "rank": 6,
        "owner": "unslothai",
        "name": "unsloth",
        "fullName": "unslothai / unsloth",
        "org": "Unsloth AI",
        "url": "https://github.com/unslothai/unsloth",
        "lang": "Python",
        "langClass": "py",
        "stars": "72,188",
        "forks": "6,504",
        "starsToday": "434",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +434★！72.2K★ 连续两天登榜！本地训练/运行 LLM 和扩散模型的 UI——支持 Qwen3.8、Kimi K3、DeepSeek-V4、FLUX 等。",
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
            "<strong>连续两天登榜：</strong>72.2K★ 本地 AI 主力工具——训练/推理一体 UI 是开源微调事实标准。",
            "<strong>中国模型全家桶支持：</strong>Qwen3.8、Kimi K3、DeepSeek-V4——中国开源模型的传播基础设施。",
            "<strong>本地 AI 加速普及：</strong>GUI 化让微调从极客走向普通开发者。"
        ],
        "tags": ["fine-tuning", "local-llm", "ui", "training", "open-source"]
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
        "stars": "4,297",
        "forks": "212",
        "starsToday": "599",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +599★！4.3K★ 时空可组合性的元框架——机器人/Agent 插件的下一代基础设施。",
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
            "<strong>599★ 的元框架概念：</strong>「时空可组合性」——把机器人/Agent 插件的组合能力提升到新高度。",
            "<strong>插件生态基础设施：</strong>Agent 插件市场爆发前夜——需要统一的框架标准。",
            "<strong>TypeScript 生态延续：</strong>跨平台机器人框架继续由 TS 主导。"
        ],
        "tags": ["bot-framework", "typescript", "plugins", "composable", "meta-framework"]
    }
]

# Shift labels for 2-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '前天'  # shift-1 = 2天前 = 前天
    elif label == '昨天':
        day['label'] = f'{shift}天前'  # 3天前
    elif label == '前天':
        day['label'] = f'{shift+1}天前'  # 4天前
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + shift}天前'

# Insert new day
new_day = {
    "date": "2026-08-16",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-16'
data['topic'] = '🔥 <strong>Public APIs 46 万星回归 + 图表设计三天 1.9 万星 + GitHub Spec Kit 官方 SDD + Ego Lite Agent 浏览器 + Needle 连登 + Unsloth 连登 + Cordis 元框架</strong> —— public-apis/public-apis（+2,260★）460.6K★ 免费 API 大全回归——Agent 时代的数据弹药库。cathrynlavery/diagram-design（+1,607★）18.9K★ 连续三天登榜三天涨 1.9 万星。github/spec-kit（+892★）129.3K★ GitHub 官方规范驱动开发工具包。citrolabs/ego-lite（+545★）11.2K★ 给 Agent 的最快浏览器。cactus-compute/needle（+547★）6.2K★ 连续两天 14MB 微型模型。unslothai/unsloth（+434★）72.2K★ 连续两天本地训练。cordiverse/cordis（+599★）4.3K★ 时空可组合元框架。数据弹药 × 设计技能 × 规范驱动 × Agent 浏览器 × 微型模型 × 本地训练——Agent 基础设施生态全面繁荣。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
