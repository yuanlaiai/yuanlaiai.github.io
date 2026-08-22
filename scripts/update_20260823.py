#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-23 (3-day gap from 8/20)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 23)
gap_days = (today - last).days  # 3
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    {
        "rank": 1,
        "owner": "openai",
        "name": "codex",
        "fullName": "openai / codex",
        "org": "OpenAI",
        "url": "https://github.com/openai/codex",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "113,289",
        "forks": "12,480",
        "starsToday": "1,978",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,978★！113.3K★ 首登即王炸！OpenAI 官方终端编码 Agent——Rust 写的轻量编码代理，单日近两千星。",
        "problems": [
            "<strong>编码 Agent 重体验：</strong>IDE 插件式 Agent 资源占用高、启动慢。",
            "<strong>终端工作流割裂：</strong>开发者习惯终端操作，Agent 却要开 GUI。",
            "<strong>上下文管理差：</strong>编码 Agent 容易丢失项目上下文。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @openai/codex</code></pre>",
            "启动：<pre><code>codex</code></pre>直接在终端对话。",
            "让 Codex 理解代码库、执行常规任务、解释复杂代码。"
        ],
        "insights": [
            "<strong>单日 +1,978★ 王炸：</strong>OpenAI 官方编码 Agent 首登即爆——终端编码 Agent 赛道迎来官方重量级玩家。",
            "<strong>Rust 的宣言：</strong>用 Rust 写编码 Agent——性能和启动速度是终端工具的生命线。",
            "<strong>编码 Agent 军备竞赛：</strong>Codex + Claude Code + Cursor 同榜——三巨头官方下场，独立开发者空间被压缩。"
        ],
        "tags": ["openai", "codex", "coding-agent", "cli", "rust"]
    },
    {
        "rank": 2,
        "owner": "multica-ai",
        "name": "andrej-karpathy-skills",
        "fullName": "multica-ai / andrej-karpathy-skills",
        "org": "multica-ai",
        "url": "https://github.com/multica-ai/andrej-karpathy-skills",
        "lang": "Markdown",
        "langClass": "md",
        "stars": "205,289",
        "forks": "18,240",
        "starsToday": "379",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +379★！205.3K★ 二次登榜！单个 CLAUDE.md 改善 Claude Code 行为——源自 Karpathy 对 LLM 编码陷阱的观察。",
        "problems": [
            "<strong>编码 Agent 踩坑多：</strong>LLM 写代码有固定陷阱模式，反复犯同样的错。",
            "<strong>提示词经验难沉淀：</strong>Karpathy 级别的编码经验无法固化到工具里。",
            "<strong>CLAUDE.md 无最佳实践：</strong>项目配置文件怎么写才有效缺乏权威参考。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/multica-ai/andrej-karpathy-skills.git</code></pre>",
            "复制 CLAUDE.md 到项目根目录。",
            "让 Claude Code 按 Karpathy 的编码观察优化行为。"
        ],
        "insights": [
            "<strong>205K★ 的号召力：</strong>Karpathy 的名字就是开源世界的流量密码——他的编码观察被固化成工程资产。",
            "<strong>单文件即技能：</strong>一个 CLAUDE.md 就是一个技能包——Agent 技能分发的最小单元正在形成。",
            "<strong>知识蒸馏的新形式：</strong>把顶级工程师的经验蒸馏进配置文件——「人肉 RAG」变成「人格配置」。"
        ],
        "tags": ["claude-code", "karpathy", "claude-md", "coding-agent", "llm"]
    },
    {
        "rank": 3,
        "owner": "anthropics",
        "name": "claude-code",
        "fullName": "anthropics / claude-code",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-code",
        "lang": "Python",
        "langClass": "py",
        "stars": "142,521",
        "forks": "12,640",
        "starsToday": "141",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +141★！142.5K★ 首登！Anthropic 官方编码 Agent——终端里的代理式编码工具，理解代码库、执行常规任务。",
        "problems": [
            "<strong>代码库理解难：</strong>大型项目结构复杂，开发者需要 Agent 快速上手。",
            "<strong>常规任务重复：</strong>重构、测试、文档等例行工作占据大量时间。",
            "<strong>Agent 上下文受限：</strong>编码 Agent 容易在长会话中丢失上下文。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @anthropic-ai/claude-code</code></pre>",
            "启动：<pre><code>claude</code></pre>在项目目录对话。",
            "让 Claude Code 执行日常编码任务、解释复杂代码。"
        ],
        "insights": [
            "<strong>142.5K★ 官方仓库首登：</strong>Claude Code 早已是事实标准，官方仓库登榜是水到渠成。",
            "<strong>与 Codex 同日同榜：</strong>Anthropic 和 OpenAI 的编码 Agent 正面相遇——终端是 AI 编程的主战场。",
            "<strong>生态位分化：</strong>Codex 重审查/委派，Claude Code 重长上下文推理——各有拥趸。"
        ],
        "tags": ["anthropic", "claude-code", "coding-agent", "cli", "agentic"]
    },
    {
        "rank": 4,
        "owner": "ripienaar",
        "name": "free-for-dev",
        "fullName": "ripienaar / free-for-dev",
        "org": "ripienaar",
        "url": "https://github.com/ripienaar/free-for-dev",
        "lang": "HTML",
        "langClass": "html",
        "stars": "133,887",
        "forks": "14,620",
        "starsToday": "915",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +915★！133.9K★ 首登！免费开发者资源大全——SaaS/PaaS/IaaS 免费套餐清单，开发者省钱必备。",
        "problems": [
            "<strong>免费资源难找：</strong>各家云服务的免费套餐分散，信息不透明。",
            "<strong>开发者预算有限：</strong>个人开发者和小团队需要控制成本。",
            "<strong>资源信息过期：</strong>免费套餐政策经常变动，需要持续维护的清单。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/ripienaar/free-for-dev.git</code></pre>",
            "按分类浏览免费资源。",
            "部署到自有环境前先查免费套餐。"
        ],
        "insights": [
            "<strong>+915★ 的经典回归：</strong>free-for-dev 是开源世界最老的清单之一——开发者省钱需求永远存在。",
            "<strong>Agent 时代的资源库：</strong>AI 工具调用也需要免费 API——清单类项目价值再次凸显。",
            "<strong>清单即基础设施：</strong>和 public-apis 一样——社区维护的「信息基础设施」有持久生命力。"
        ],
        "tags": ["free", "developer-tools", "resources", "list", "saas"]
    },
    {
        "rank": 5,
        "owner": "Tencent",
        "name": "AI-Infra-Guard",
        "fullName": "Tencent / AI-Infra-Guard",
        "org": "腾讯",
        "url": "https://github.com/Tencent/AI-Infra-Guard",
        "lang": "Python",
        "langClass": "py",
        "stars": "5,486",
        "forks": "612",
        "starsToday": "161",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +161★！5.5K★ 首登！腾讯全栈 AI 红队平台——Agent Scan、Skills Scan、MCP Scan、LLM 越狱评估一站式。",
        "problems": [
            "<strong>AI 安全碎片化：</strong>Agent、技能、MCP 各环节的安全风险分散，缺乏统一检测。",
            "<strong>越狱攻击防不胜防：</strong>LLM 越狱手段不断翻新，需要持续评估。",
            "<strong>红队工具门槛高：</strong>企业自建 AI 红队成本高，缺平台化工具。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Tencent/AI-Infra-Guard.git</code></pre>",
            "运行 Agent Scan / Skills Scan / MCP Scan。",
            "用 LLM 越狱评估测试自有模型防线。"
        ],
        "insights": [
            "<strong>腾讯开源 AI 红队平台：</strong>中国大厂在 AI 安全基建上加速——Agent 时代的安全检测成为刚需。",
            "<strong>MCP Scan 是亮点：</strong>给 Agent 工具协议做安全扫描——新协议催生新安全品类。",
            "<strong>呼应 strix 热潮：</strong>AI 安全从应用层渗透到 Agent 基础设施层。"
        ],
        "tags": ["ai-security", "red-team", "agent", "mcp", "tencent"]
    },
    {
        "rank": 6,
        "owner": "Wei-Shaw",
        "name": "sub2api",
        "fullName": "Wei-Shaw / sub2api",
        "org": "Wei-Shaw",
        "url": "https://github.com/Wei-Shaw/sub2api",
        "lang": "Go",
        "langClass": "go",
        "stars": "38,779",
        "forks": "5,120",
        "starsToday": "264",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +264★！38.8K★ 首登！一站式开源中转——Claude/OpenAI/Gemini/Grok 订阅统一转 API，支持拼车共享分摊成本。",
        "problems": [
            "<strong>订阅费用高：</strong>各家 AI 订阅叠加成本高，个人开发者难承受。",
            "<strong>API 按量贵：</strong>订阅制便宜但无 API，API 制灵活但贵。",
            "<strong>多模型切换麻烦：</strong>多家平台账号管理分散。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Wei-Shaw/sub2api.git</code></pre>",
            "配置你的订阅账号。",
            "用 OpenAI 兼容 API 接入任意工具，支持拼车共享。"
        ],
        "insights": [
            "<strong>38.8K★ 的中转生意：</strong>订阅转 API 开源项目大火——开发者对 API 价格的敏感度极高。",
            "<strong>拼车经济学：</strong>多人共享订阅摊薄成本——AI 时代的「合租」模式走红。",
            "<strong>合规灰色地带：</strong>中转服务涉及条款风险——热度与争议并存。"
        ],
        "tags": ["api", "proxy", "subscription", "openai", "go"]
    },
    {
        "rank": 7,
        "owner": "n8n-io",
        "name": "n8n",
        "fullName": "n8n-io / n8n",
        "org": "n8n",
        "url": "https://github.com/n8n-io/n8n",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "201,805",
        "forks": "18,240",
        "starsToday": "202",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +202★！201.8K★ 首登！工作流自动化平台——原生 AI 能力 + 400+ 集成，可视化搭建 + 自定义代码。",
        "problems": [
            "<strong>工作流自动化门槛：</strong>业务流程自动化需要写代码或复杂配置。",
            "<strong>AI 集成繁琐：</strong>把 LLM 接入业务流需要大量胶水代码。",
            "<strong>工具链割裂：</strong>400+ 应用之间的数据流难以打通。"
        ],
        "usage": [
            "自托管：<pre><code>docker run -it --rm -p 5678:5678 n8nio/n8n</code></pre>",
            "可视化拖拽搭建工作流。",
            "接入 AI 节点与 400+ 应用集成。"
        ],
        "insights": [
            "<strong>201.8K★ 的自动化之王：</strong>n8n 是自托管工作流的事实标准——Agent 时代它的价值被重新发现。",
            "<strong>AI 原生转型成功：</strong>从 RPA 工具变成 AI 编排平台——400+ 集成成为 Agent 的「手脚」。",
            "<strong>低代码与 Agent 合流：</strong>可视化工作流 + LLM 节点——业务自动化的终局形态。"
        ],
        "tags": ["workflow", "automation", "ai", "low-code", "self-hosted"]
    },
    {
        "rank": 8,
        "owner": "modular",
        "name": "modular",
        "fullName": "modular / modular",
        "org": "Modular",
        "url": "https://github.com/modular/modular",
        "lang": "Mojo",
        "langClass": "mojo",
        "stars": "28,838",
        "forks": "2,240",
        "starsToday": "395",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +395★！28.8K★ 首登！Modular 平台——MAX + Mojo 语言，AI 性能的 Python 超集。",
        "problems": [
            "<strong>Python 性能瓶颈：</strong>AI 计算密集场景 Python 太慢。",
            "<strong>多语言切换成本：</strong>Python 写逻辑、C++ 写性能，两套代码难维护。",
            "<strong>AI 部署复杂：</strong>模型推理优化需要专门工具链。"
        ],
        "usage": [
            "安装 Mojo：<pre><code>curl -sSf https://get.modular.com | sh</code></pre>",
            "用 Mojo 编写高性能 AI 代码。",
            "用 MAX 平台部署和优化模型推理。"
        ],
        "insights": [
            "<strong>Mojo 的坚持：</strong>Chris Lattner（Swift 之父）的 AI 语言梦——Python 语法 + C 性能。",
            "<strong>AI 原生语言赛道：</strong>Mojo 与 Rust 竞争 AI 基础设施语言生态位。",
            "<strong>性能焦虑的出口：</strong>AI 开发者既要 Python 生产力又要高性能——Mojo 赌的就是这个。"
        ],
        "tags": ["mojo", "ai", "language", "performance", "lattner"]
    },
    {
        "rank": 9,
        "owner": "makeplane",
        "name": "plane",
        "fullName": "makeplane / plane",
        "org": "Plane",
        "url": "https://github.com/makeplane/plane",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "57,211",
        "forks": "5,480",
        "starsToday": "263",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +263★！57.2K★ 首登！开源 Jira/Linear/Monday/ClickUp 替代——任务、Sprint、文档、Triage 一体化项目管理。",
        "problems": [
            "<strong>项目管理工具贵：</strong>Jira/Linear 等商业工具订阅成本高。",
            "<strong>工具割裂：</strong>任务、文档、路线图分散在不同系统。",
            "<strong>数据主权：</strong>团队数据存在 SaaS 平台上，缺乏自托管选项。"
        ],
        "usage": [
            "Docker 部署：<pre><code>docker compose up</code></pre>",
            "创建项目、任务、Sprint。",
            "用 Plane 替代 Jira/Linear 管理团队工作。"
        ],
        "insights": [
            "<strong>57.2K★ 的开源项目管理：</strong>Jira 贵、Linear 闭源——Plane 抓住的空档越来越多人认同。",
            "<strong>AI 团队最爱：</strong>自托管 + 数据主权——AI 团队对数据敏感，倾向自托管工具。",
            "<strong>与 n8n 同日登榜：</strong>工作流 + 项目管理——AI 时代的「团队基础设施」正在开源化。"
        ],
        "tags": ["project-management", "jira-alternative", "self-hosted", "typescript", "team"]
    },
    {
        "rank": 10,
        "owner": "cursor",
        "name": "plugins",
        "fullName": "cursor / plugins",
        "org": "Cursor",
        "url": "https://github.com/cursor/plugins",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "4,656",
        "forks": "240",
        "starsToday": "286",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +286★！4.7K★ 二次登榜！Cursor 插件规范 + 官方插件库——编码 Agent 生态开始标准化。",
        "problems": [
            "<strong>插件生态混乱：</strong>Cursor 插件缺少统一规范。",
            "<strong>官方插件分散：</strong>功能插件各自独立，体验割裂。",
            "<strong>生态标准缺位：</strong>第三方插件质量参差。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cursor/plugins.git</code></pre>",
            "查看插件规范与官方插件。",
            "按规范开发或安装 Cursor 插件。"
        ],
        "insights": [
            "<strong>插件规范即话语权：</strong>Cursor 定义插件标准——生态主导权之争从 IDE 延伸到插件层。",
            "<strong>编码 Agent 生态化：</strong>Codex/Claude Code 拼 CLI 能力，Cursor 拼生态——路线分化。",
            "<strong>5/28 登榜后回归：</strong>插件市场从 4.7K 星起步——生态早期，先发者占位。"
        ],
        "tags": ["cursor", "plugins", "ide", "ecosystem", "typescript"]
    }
]

# Shift labels for 3-day gap (accurate offset: each old entry shifts +3 days)
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '3天前'
    elif label == '昨天':
        day['label'] = '4天前'
    elif label == '前天':
        day['label'] = '5天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + 3}天前'

# Insert new day
new_day = {
    "date": "2026-08-23",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-23'
data['topic'] = '🔥 <strong>OpenAI Codex 单日 1978 星王炸 + 编码 Agent 三巨头同榜 + Karpathy 技能集 205K + 中国项目双响 + free-for-dev/n8n 回归</strong> —— openai/codex（+1,978★）113.3K★ OpenAI 官方终端编码 Agent 首登即王炸。multica-ai/andrej-karpathy-skills（+379★）205.3K★ Karpathy 编码陷阱观察驱动的 CLAUDE.md 二次登榜。anthropics/claude-code（+141★）142.5K★ Anthropic 官方编码 Agent 首登。cursor/plugins（+286★）4.7K★ Cursor 插件规范回归。ripienaar/free-for-dev（+915★）133.9K★ 免费资源大全首登。Tencent/AI-Infra-Guard（+161★）5.5K★ 腾讯全栈 AI 红队平台首登。Wei-Shaw/sub2api（+264★）38.8K★ 订阅拼车中转首登。n8n-io/n8n（+202★）201.8K★ 工作流自动化之王首登。modular/modular（+395★）28.8K★ Mojo 平台首登。makeplane/plane（+263★）57.2K★ 开源 Jira 替代首登。编码 Agent 军备竞赛全面开打——OpenAI/Anthropic/Cursor 官方下场，中国开发者基建双线并进，工作流与项目管理同步开源化。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
