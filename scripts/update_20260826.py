#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-26 (1-day gap from 8/25)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 26)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    {
        "rank": 1,
        "owner": "freestylefly",
        "name": "awesome-gpt-image-2",
        "fullName": "freestylefly / awesome-gpt-image-2",
        "org": "freestylefly",
        "url": "https://github.com/freestylefly/awesome-gpt-image-2",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "17,639",
        "forks": "1,420",
        "starsToday": "1,698",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +1,698★！17.6K★ 连续两天登榜！GPT-Image2 提示词引擎——两天累计 +4,100★，Prompt as Code 持续霸榜。",
        "problems": [
            "<strong>图片提示词玄学：</strong>GPT 图片生成效果不稳定，提示词靠猜。",
            "<strong>优秀案例难沉淀：</strong>社区好提示词分散，无法系统复用。",
            "<strong>工程化缺失：</strong>图片生成缺乏模板化、版本化管理。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/freestylefly/awesome-gpt-image-2.git</code></pre>",
            "浏览 530+ 逆向工程案例。",
            "套用 20+ 工业级模板生成图片。"
        ],
        "insights": [
            "<strong>连登两天累计 4,100★：</strong>+2,442★ → +1,698★——GPT-Image2 提示词工程热度不减。",
            "<strong>Prompt as Code 验证：</strong>中文开发者把提示词做成模板库——图片生成工程化被全球采纳。",
            "<strong>提示词经济成型：</strong>案例逆向 + 模板复用——提示词正在变成可交易的知识资产。"
        ],
        "tags": ["gpt-image", "prompt-engineering", "templates", "ai-image", "awesome-list"]
    },
    {
        "rank": 2,
        "owner": "openai",
        "name": "codex",
        "fullName": "openai / codex",
        "org": "OpenAI",
        "url": "https://github.com/openai/codex",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "118,088",
        "forks": "13,120",
        "starsToday": "1,181",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +1,181★！118.1K★ 连续三天登榜！OpenAI 官方终端编码 Agent——三天累计超 5,000★，稳如泰山。",
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
            "<strong>三连登累计 5,000+★：</strong>+1,978 → +1,990 → +1,181——OpenAI 编码 Agent 热度持续高位。",
            "<strong>118K★ 的官方地位：</strong>Codex 已是终端编码 Agent 的事实标杆。",
            "<strong>与免费版对撞：</strong>free-claude-code 刚登榜，Codex 官方热度不降——定价争议不影响口碑。"
        ],
        "tags": ["openai", "codex", "coding-agent", "cli", "rust"]
    },
    {
        "rank": 3,
        "owner": "basecamp",
        "name": "omarchy",
        "fullName": "basecamp / omarchy",
        "org": "Basecamp",
        "url": "https://github.com/basecamp/omarchy",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "31,235",
        "forks": "1,390",
        "starsToday": "1,083",
        "count": 4,
        "description": "🔥 亮点 —— 今日 +1,083★！31.2K★ 连续两天破千！DHH 的现代化 Linux——31K 星，破千成常态。",
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
            "<strong>连续两天破千：</strong>+1,055 → +1,083——omarchy 热度破千成常态，第四天登榜。",
            "<strong>31K★ 的极客情怀：</strong>DHH 自建 OS 的浪漫持续吸粉——「摆脱依赖」思潮不减。",
            "<strong>AI 时代的逆流：</strong>当 AI 让一切变重，omarchy 代表「回到简单」的长期主义。"
        ],
        "tags": ["linux", "basecamp", "dhh", "distro", "developer-tools"]
    },
    {
        "rank": 4,
        "owner": "multica-ai",
        "name": "andrej-karpathy-skills",
        "fullName": "multica-ai / andrej-karpathy-skills",
        "org": "multica-ai",
        "url": "https://github.com/multica-ai/andrej-karpathy-skills",
        "lang": "Markdown",
        "langClass": "md",
        "stars": "207,189",
        "forks": "18,640",
        "starsToday": "830",
        "count": 4,
        "description": "🔥 亮点 —— 今日 +830★！207.2K★ 连续四天登榜！Karpathy 编码观察驱动的 CLAUDE.md——20 万星单文件神话继续。",
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
            "<strong>四连登 207.2K★：</strong>单个 CLAUDE.md 持续霸榜——Karpathy 的影响力还在扩散。",
            "<strong>单文件即技能：</strong>一个配置文件就是一个技能包——Agent 技能分发的最小单元。",
            "<strong>知识蒸馏新形式：</strong>把顶级工程师经验蒸馏进配置文件——「人格配置」成为新品类。"
        ],
        "tags": ["claude-code", "karpathy", "claude-md", "coding-agent", "llm"]
    },
    {
        "rank": 5,
        "owner": "AgriciDaniel",
        "name": "claude-obsidian",
        "fullName": "AgriciDaniel / claude-obsidian",
        "org": "AgriciDaniel",
        "url": "https://github.com/AgriciDaniel/claude-obsidian",
        "lang": "Python",
        "langClass": "py",
        "stars": "12,699",
        "forks": "530",
        "starsToday": "813",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +813★！12.7K★ 连续两天登榜且热度三倍！Obsidian + Claude Code 自组织 AI 第二大脑。",
        "problems": [
            "<strong>知识管理靠手动：</strong>笔记链接、归档、整理全要人工。",
            "<strong>第二大脑不智能：</strong>Obsidian 笔记无法自动关联理解。",
            "<strong>AI 与笔记割裂：</strong>Claude 输出无法沉淀进知识库。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/AgriciDaniel/claude-obsidian.git</code></pre>",
            "配置 Obsidian vault 与 Claude Code。",
            "拖入资料，让 Claude 自动读取、链接、归档。"
        ],
        "insights": [
            "<strong>热度三倍爆发：</strong>+272★ → +813★——AI 第二大脑概念被快速验证。",
            "<strong>Markdown 数据主权：</strong>「纯 Markdown 你拥有」——本地优先知识管理对抗云笔记。",
            "<strong>笔记党与 Agent 党合流：</strong>Zettelkasten 方法论 + 编码 Agent——知识工作者的终极形态。"
        ],
        "tags": ["obsidian", "claude-code", "second-brain", "knowledge-graph", "markdown"]
    },
    {
        "rank": 6,
        "owner": "apache",
        "name": "maka",
        "fullName": "apache / maka",
        "org": "Apache",
        "url": "https://github.com/apache/maka",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "3,321",
        "forks": "160",
        "starsToday": "543",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +543★！3.3K★ 连续两天登榜！Apache Maka（孵化中）本地优先 AI Agent 工作区——append-only 审计日志。",
        "problems": [
            "<strong>Agent 行为不可审计：</strong>Agent 做了什么、怎么决策的无法追溯。",
            "<strong>权限决策不透明：</strong>Agent 调用工具时权限判断缺乏记录。",
            "<strong>企业合规需求：</strong>Agent 进企业需要完整审计链路。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/apache/maka.git</code></pre>",
            "启动本地优先的 Agent 工作区。",
            "查看 append-only 的 Agent 行为审计日志。"
        ],
        "insights": [
            "<strong>连登两天热度走高：</strong>+408★ → +543★——Apache 基金会的含金量持续兑现。",
            "<strong>审计日志是新刚需：</strong>append-only 记录 Agent 决策——企业采纳 Agent 的合规前提。",
            "<strong>本地优先成为主流：</strong>从 OpenViking 到 Maka——Agent 基础设施全部本地优先化。"
        ],
        "tags": ["apache", "agent", "workspace", "audit-log", "local-first"]
    },
    {
        "rank": 7,
        "owner": "tinyhumansai",
        "name": "openhuman",
        "fullName": "tinyhumansai / openhuman",
        "org": "Tiny Humans AI",
        "url": "https://github.com/tinyhumansai/openhuman",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "37,756",
        "forks": "2,220",
        "starsToday": "542",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +542★！37.8K★ 连续两天登榜！个人 AI 超级智能——本地优先生活记忆 + Agent 舰队编排 + 深度研究。",
        "problems": [
            "<strong>个人数据分散：</strong>生活记录散落各处，无法形成统一记忆。",
            "<strong>Agent 单打独斗：</strong>单个 Agent 能力有限，缺编排舰队。",
            "<strong>AI 记忆隐私：</strong>个人记忆上云有隐私风险，需本地优先。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/tinyhumansai/openhuman.git</code></pre>",
            "构建本地优先的个人记忆库。",
            "编排 Agent 舰队完成深度研究任务。"
        ],
        "insights": [
            "<strong>连登两天：</strong>+515★ → +542★——个人 AI 大脑需求稳定增长。",
            "<strong>Agent 舰队编排：</strong>从单 Agent 到舰队——多 Agent 协作成为个人 AI 的新形态。",
            "<strong>记忆即资产延续：</strong>OpenViking、ai-memory、openhuman——Agent 记忆赛道持续霸榜。"
        ],
        "tags": ["personal-ai", "memory", "rust", "agent-orchestration", "local-first"]
    },
    {
        "rank": 8,
        "owner": "anthropics",
        "name": "claude-plugins-community",
        "fullName": "anthropics / claude-plugins-community",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-community",
        "lang": "Python",
        "langClass": "py",
        "stars": "1,731",
        "forks": "104",
        "starsToday": "351",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +351★！1.7K★ 连续两天登榜！Anthropic 官方社区插件市场——Claude Cowork 和 Claude Code 的插件集市。",
        "problems": [
            "<strong>Claude 插件分散：</strong>社区插件散落各处，无统一市场。",
            "<strong>质量参差：</strong>插件无官方评审，良莠不齐。",
            "<strong>发现难：</strong>好插件靠口口相传，无法检索。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/anthropics/claude-plugins-community.git</code></pre>",
            "浏览 Claude Cowork / Claude Code 插件。",
            "按官方规范提交自己的插件。"
        ],
        "insights": [
            "<strong>连登两天：</strong>+490★ → +351★——Anthropic 插件生态持续吸星。",
            "<strong>官方 + 社区双仓库：</strong>community（1.7K★）+ official（34K★）同日同榜——插件生态正式分层。",
            "<strong>插件经济前夜：</strong>对标 Cursor 插件规范——编码 Agent 的插件市场大战开打。"
        ],
        "tags": ["anthropic", "claude", "plugins", "marketplace", "ecosystem"]
    },
    {
        "rank": 9,
        "owner": "marin-community",
        "name": "marin",
        "fullName": "marin-community / marin",
        "org": "Marin Community",
        "url": "https://github.com/marin-community/marin",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,094",
        "forks": "118",
        "starsToday": "231",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +231★！2.1K★ 首登！基础模型研发开源框架——Marin 社区驱动的 AI 基础设施新玩家。",
        "problems": [
            "<strong>基础模型门槛高：</strong>训练/微调基础模型需要庞大的私有工具链。",
            "<strong>框架碎片化：</strong>研究机构各自为政，缺乏统一框架。",
            "<strong>复现困难：</strong>论文成果难以在社区复现。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/marin-community/marin.git</code></pre>",
            "按文档搭建基础模型研发环境。",
            "参与社区模型训练与复现。"
        ],
        "insights": [
            "<strong>社区驱动的开源框架：</strong>marin 首登——基础模型研究工具链正在开源化。",
            "<strong>与研究机构互补：</strong>对标 EleutherAI 模式——社区科研是开源 AI 的重要力量。",
            "<strong>Agent 时代的基础层：</strong>当 Agent 应用卷到极致，基础模型研究回归价值。"
        ],
        "tags": ["foundation-models", "research", "framework", "open-source", "ai"]
    },
    {
        "rank": 10,
        "owner": "TauricResearch",
        "name": "TradingAgents",
        "fullName": "TauricResearch / TradingAgents",
        "org": "Tauric Research",
        "url": "https://github.com/TauricResearch/TradingAgents",
        "lang": "Python",
        "langClass": "py",
        "stars": "100,227",
        "forks": "18,420",
        "starsToday": "218",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +218★！100.2K★ 首登！多 Agent LLM 金融交易框架——分析师/研究员/交易员 Agent 协作。",
        "problems": [
            "<strong>量化交易门槛高：</strong>专业量化框架复杂，个人难以入门。",
            "<strong>LLM 金融应用缺标杆：</strong>多 Agent 交易框架缺乏成熟开源实现。",
            "<strong>研究到实盘断层：</strong>学术框架难以落地真实交易。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/TauricResearch/TradingAgents.git</code></pre>",
            "配置 LLM API 与市场数据。",
            "让分析师/研究员/交易员 Agent 协作决策。"
        ],
        "insights": [
            "<strong>100K★ 的金融 Agent：</strong>TradingAgents 首登——LLM 金融交易框架进入百万星俱乐部。",
            "<strong>多 Agent 协作范式：</strong>分析师-研究员-交易员的角色分工——Agent 团队模拟投行工作流。",
            "<strong>呼应 nautilus_trader：</strong>Rust 量化引擎 + LLM 交易 Agent——金融 AI 双线并进。"
        ],
        "tags": ["trading", "multi-agent", "llm", "finance", "quant"]
    },
    {
        "rank": 11,
        "owner": "Shubhamsaboo",
        "name": "awesome-llm-apps",
        "fullName": "Shubhamsaboo / awesome-llm-apps",
        "org": "Shubhamsaboo",
        "url": "https://github.com/Shubhamsaboo/awesome-llm-apps",
        "lang": "Python",
        "langClass": "py",
        "stars": "134,216",
        "forks": "14,840",
        "starsToday": "161",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +161★！134.2K★ 首登！100+ AI Agents、Agent Skills 和 RAG 应用——免费开源大合集。",
        "problems": [
            "<strong>AI 应用模板难找：</strong>高质量 Agent/RAG 应用示例分散。",
            "<strong>学习成本高：</strong>从零搭建 AI 应用需要大量踩坑。",
            "<strong>示例质量参差：</strong>网上的 AI 应用示例良莠不齐。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git</code></pre>",
            "按场景挑选 Agent/RAG 应用示例。",
            "复制代码快速搭建自己的 AI 应用。"
        ],
        "insights": [
            "<strong>134K★ 的 AI 应用大全：</strong>100+ 开源示例——AI 应用开发的「菜谱书」登榜。",
            "<strong>教育价值巨大：</strong>Agent Skills + RAG 全覆盖——新手到专家的最短路径。",
            "<strong>清单经济延续：</strong>free-for-dev、public-apis、awesome-llm-apps——清单类项目持续霸榜。"
        ],
        "tags": ["llm", "rag", "agents", "awesome-list", "tutorials"]
    },
    {
        "rank": 12,
        "owner": "anthropics",
        "name": "claude-plugins-official",
        "fullName": "anthropics / claude-plugins-official",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-official",
        "lang": "Python",
        "langClass": "py",
        "stars": "34,081",
        "forks": "1,240",
        "starsToday": "55",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +55★！34.1K★ 首登！Anthropic 官方管理的高质量 Claude Code 插件目录——插件生态的「官方认证」。",
        "problems": [
            "<strong>插件质量无保障：</strong>第三方插件良莠不齐，安全风险高。",
            "<strong>官方插件难发现：</strong>高质量插件缺少官方认证渠道。",
            "<strong>生态信任缺失：</strong>开发者不敢随意安装社区插件。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/anthropics/claude-plugins-official.git</code></pre>",
            "浏览 Anthropic 官方认证插件。",
            "安装高质量 Claude Code 插件。"
        ],
        "insights": [
            "<strong>34K★ 官方插件目录：</strong>Anthropic 官方认证插件首登——插件质量有了官方背书。",
            "<strong>官方 + 社区双轨：</strong>official（认证）+ community（投稿）——插件生态的标准分层。",
            "<strong>生态战争升级：</strong>Anthropic 建插件市场、Cursor 建插件规范、OpenAI 拼 CLI——编码 Agent 生态全面开打。"
        ],
        "tags": ["anthropic", "claude", "plugins", "official", "ecosystem"]
    }
]

# Shift labels for 1-day gap (accurate offset: +1)
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
        day['label'] = f'{num + 1}天前'

# Insert new day
new_day = {
    "date": "2026-08-26",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-26'
data['topic'] = '🔥 <strong>awesome-gpt-image-2 连登 + Codex 三连登 + omarchy/karpathy 四连登 + claude-obsidian 热度三倍 + Anthropic 插件官方社区双仓库 + TradingAgents 100K + Apache Maka 连登 + openhuman 连登</strong> —— freestylefly/awesome-gpt-image-2（+1,698★）17.6K★ 连登两天累计四千星。openai/codex（+1,181★）118.1K★ 三连登。basecamp/omarchy（+1,083★）31.2K★ 连续两天破千四连登。multica-ai/andrej-karpathy-skills（+830★）207.2K★ 四连登。AgriciDaniel/claude-obsidian（+813★）12.7K★ 连登热度三倍。apache/maka（+543★）3.3K★ 连登。tinyhumansai/openhuman（+542★）37.8K★ 连登。anthropics/claude-plugins-community（+351★）与 claude-plugins-official（+55★）官方社区双仓库同榜。TauricResearch/TradingAgents（+218★）100.2K★ 多 Agent 金融交易框架首登。Shubhamsaboo/awesome-llm-apps（+161★）134.2K★ 应用大全首登。marin-community/marin（+231★）基础模型框架首登。编码 Agent 生态全面爆发——连登潮、插件双轨、金融 Agent、应用大全，开源世界的军备竞赛进入白热化。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
