#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-25 (2-day gap from 8/23)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 25)
gap_days = (today - last).days  # 2
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
        "stars": "15,454",
        "forks": "1,208",
        "starsToday": "2,442",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +2,442★！15.5K★ 首登即王炸！GPT-Image2 工业级提示词引擎——530+ 案例逆向工程、20+ 工业级模板，Prompt as Code。",
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
            "<strong>单日 +2,442★ 王炸：</strong>GPT-Image2 提示词库首登即霸榜——图片生成进入「提示词工程化」时代。",
            "<strong>Prompt as Code：</strong>把提示词当代码管理——模板、版本、复用，中文开发者贡献的工程化范式。",
            "<strong>案例逆向工程：</strong>530+ 案例反向拆解——社区在给 GPT 图片模型做「提示词考古」。"
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
        "stars": "117,009",
        "forks": "12,980",
        "starsToday": "1,990",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +1,990★！117K★ 连续两天登榜！OpenAI 官方终端编码 Agent——单日近两千星，连续两天破千。",
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
            "<strong>连登两天都破千：</strong>+1,978★ → +1,990★——OpenAI 官方编码 Agent 热度持续高位。",
            "<strong>终端即战场：</strong>Codex 用 Rust 打磨启动速度——终端编码 Agent 的性能竞赛白热化。",
            "<strong>与免费化浪潮相遇：</strong>free-claude-code 同榜——官方收费 vs 社区免费的分水岭正在形成。"
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
        "stars": "30,082",
        "forks": "1,340",
        "starsToday": "1,055",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +1,055★！30.1K★ 单日破千回归！DHH 的现代化 Linux——30K 星里程碑 + 单日千星双buff。",
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
            "<strong>单日 +1,055★ 破千：</strong>omarchy 达到 30K 星里程碑——DHH 的极客浪漫持续吸粉。",
            "<strong>隔两日回归：</strong>8/19 后今天再次登榜且热度翻倍——Linux 极简化思潮还在扩散。",
            "<strong>AI 时代的反叛：</strong>当 AI 让一切变重，omarchy 代表「回到简单」的逆流。"
        ],
        "tags": ["linux", "basecamp", "dhh", "distro", "developer-tools"]
    },
    {
        "rank": 4,
        "owner": "NousResearch",
        "name": "hermes-agent",
        "fullName": "NousResearch / hermes-agent",
        "org": "Nous Research",
        "url": "https://github.com/NousResearch/hermes-agent",
        "lang": "Python",
        "langClass": "py",
        "stars": "235,775",
        "forks": "18,420",
        "starsToday": "899",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +899★！235.8K★ 首登！Nous Research 的「与你一起成长的 Agent」——Hermes 系列模型的 Agent 化身。",
        "problems": [
            "<strong>Agent 一次性使用：</strong>用完即弃，无法随用户成长。",
            "<strong>个性化缺失：</strong>通用 Agent 不了解用户偏好和历史。",
            "<strong>开源 Agent 缺标杆：</strong>头部开源 Agent 框架缺乏高质量实现。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/NousResearch/hermes-agent.git</code></pre>",
            "安装依赖并启动 Agent。",
            "让 Agent 在学习你的过程中不断进化。"
        ],
        "insights": [
            "<strong>235.8K★ 首登：</strong>Nous Research 的 Hermes 品牌效应——开源社区的信任积累变现。",
            "<strong>「与你一起成长」：</strong>Agent 从工具变成伙伴——成长型 Agent 是下一波叙事。",
            "<strong>开源 Agent 军备竞赛：</strong>Hermes Agent + Claude Code + Codex——开源 vs 闭源 Agent 全面对撞。"
        ],
        "tags": ["hermes", "nous-research", "agent", "open-source", "llm"]
    },
    {
        "rank": 5,
        "owner": "Alishahryar1",
        "name": "free-claude-code",
        "fullName": "Alishahryar1 / free-claude-code",
        "org": "Alishahryar1",
        "url": "https://github.com/Alishahryar1/free-claude-code",
        "lang": "Python",
        "langClass": "py",
        "stars": "48,925",
        "forks": "6,120",
        "starsToday": "889",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +889★！48.9K★ 首登！免费白嫖 Claude Code/Codex/Pi/OpenCode——1.3B+ 免费 tokens，终端/App/IDE/手机全端支持。",
        "problems": [
            "<strong>编码 Agent 订阅贵：</strong>Claude Code/Codex 官方订阅成本高。",
            "<strong>多端切换麻烦：</strong>终端、App、IDE、手机各用各的。",
            "<strong>免费额度分散：</strong>各家免费 tokens 无法统一管理。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Alishahryar1/free-claude-code.git</code></pre>",
            "配置免费 tokens 渠道。",
            "在终端/App/IDE/手机统一使用编码 Agent。"
        ],
        "insights": [
            "<strong>48.9K★ 的免费浪潮：</strong>「免费白嫖 Claude Code」48K 星——开发者对订阅价格的抵抗全面爆发。",
            "<strong>与 sub2api 同源：</strong>订阅拼车、免费 tokens——AI 价格战的灰色侧翼正在壮大。",
            "<strong>官方与社区的对撞：</strong>Codex 官方 117K 星 vs 免费版 48.9K 星——定价权之争开打。"
        ],
        "tags": ["claude-code", "free", "codex", "tokens", "developer-tools"]
    },
    {
        "rank": 6,
        "owner": "tinyhumansai",
        "name": "openhuman",
        "fullName": "tinyhumansai / openhuman",
        "org": "Tiny Humans AI",
        "url": "https://github.com/tinyhumansai/openhuman",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "37,246",
        "forks": "2,180",
        "starsToday": "515",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +515★！37.2K★ 首登！个人 AI 超级智能——本地优先的生活记忆 + Agent 舰队编排 + 深度研究，你的数字大脑。",
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
            "<strong>37.2K★ 的个人 AI 大脑：</strong>Rust 写的本地优先记忆系统——「第二大脑」赛道进入超级智能阶段。",
            "<strong>Agent 舰队编排：</strong>从单 Agent 到舰队——多 Agent 协作成为个人 AI 的新形态。",
            "<strong>记忆即资产延续：</strong>OpenViking、ai-memory、openhuman——Agent 记忆赛道持续霸榜。"
        ],
        "tags": ["personal-ai", "memory", "rust", "agent-orchestration", "local-first"]
    },
    {
        "rank": 7,
        "owner": "multica-ai",
        "name": "andrej-karpathy-skills",
        "fullName": "multica-ai / andrej-karpathy-skills",
        "org": "multica-ai",
        "url": "https://github.com/multica-ai/andrej-karpathy-skills",
        "lang": "Markdown",
        "langClass": "md",
        "stars": "206,479",
        "forks": "18,560",
        "starsToday": "491",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +491★！206.5K★ 连续三天登榜！Karpathy 编码观察驱动的 CLAUDE.md——单个文件 20 万星的现象级项目。",
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
            "<strong>三连登 206.5K★：</strong>单个 CLAUDE.md 三天吸星 1,300+——Karpathy 名字的含金量还在涨。",
            "<strong>单文件即技能：</strong>一个配置文件就是一个技能包——Agent 技能分发的最小单元。",
            "<strong>知识蒸馏新形式：</strong>把顶级工程师经验蒸馏进配置文件——「人格配置」成为新品类。"
        ],
        "tags": ["claude-code", "karpathy", "claude-md", "coding-agent", "llm"]
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
        "stars": "1,339",
        "forks": "86",
        "starsToday": "490",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +490★！1.3K★ 首登！Anthropic 官方社区插件市场——Claude Cowork 和 Claude Code 的插件集市。",
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
            "<strong>Anthropic 建插件市场：</strong>官方下场做社区插件集市——Claude 生态标准化的信号。",
            "<strong>插件经济前夜：</strong>对标 Cursor 插件规范——编码 Agent 的插件市场大战开打。",
            "<strong>Claude Cowork 新物种：</strong>从单 Agent 到协作工作区——Anthropic 在布局下一代形态。"
        ],
        "tags": ["anthropic", "claude", "plugins", "marketplace", "ecosystem"]
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
        "stars": "57,906",
        "forks": "5,560",
        "starsToday": "268",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +268★！57.9K★ 连续两天登榜！开源 Jira/Linear 替代——任务、Sprint、文档、Triage 一体化项目管理。",
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
            "<strong>连续两天登榜：</strong>8/23 → 8/25——开源项目管理需求持续。",
            "<strong>AI 团队最爱：</strong>自托管 + 数据主权——AI 团队对数据敏感，倾向自托管工具。",
            "<strong>团队基础设施开源化：</strong>工作流、项目管理、知识库——AI 时代的团队栈全面开源。"
        ],
        "tags": ["project-management", "jira-alternative", "self-hosted", "typescript", "team"]
    },
    {
        "rank": 10,
        "owner": "AgriciDaniel",
        "name": "claude-obsidian",
        "fullName": "AgriciDaniel / claude-obsidian",
        "org": "AgriciDaniel",
        "url": "https://github.com/AgriciDaniel/claude-obsidian",
        "lang": "Python",
        "langClass": "py",
        "stars": "11,868",
        "forks": "480",
        "starsToday": "272",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +272★！11.9K★ 首登！Obsidian + Claude Code 的自组织 AI 第二大脑——拖入任何资料，自动链接归档成知识图谱。",
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
            "<strong>11.9K★ 的第二大脑：</strong>Obsidian + Claude 自组织知识图谱——知识管理进入 AI 自动档。",
            "<strong>Markdown 数据主权：</strong>「纯 Markdown 你拥有」——本地优先知识管理正对抗云笔记。",
            "<strong>笔记党与 Agent 党合流：</strong>Zettelkasten 方法论 + 编码 Agent——知识工作者的终极形态。"
        ],
        "tags": ["obsidian", "claude-code", "second-brain", "knowledge-graph", "markdown"]
    },
    {
        "rank": 11,
        "owner": "apache",
        "name": "maka",
        "fullName": "apache / maka",
        "org": "Apache",
        "url": "https://github.com/apache/maka",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "2,886",
        "forks": "142",
        "starsToday": "408",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +408★！2.9K★ 首登！Apache Maka（孵化中）本地优先 AI Agent 工作区——消息/工具调用/权限决策全记录，append-only 审计日志。",
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
            "<strong>Apache 基金会入局：</strong>Maka 孵化——顶级开源基金会下场做 Agent 工作区，含金量背书。",
            "<strong>审计日志是新刚需：</strong>append-only 记录 Agent 决策——企业采纳 Agent 的合规前提。",
            "<strong>本地优先成为主流：</strong>从 OpenViking 到 Maka——Agent 基础设施全部本地优先化。"
        ],
        "tags": ["apache", "agent", "workspace", "audit-log", "local-first"]
    }
]

# Shift labels for 2-day gap (accurate offset: +2)
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '2天前'
    elif label == '昨天':
        day['label'] = '3天前'
    elif label == '前天':
        day['label'] = '4天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + 2}天前'

# Insert new day
new_day = {
    "date": "2026-08-25",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-25'
data['topic'] = '🔥 <strong>GPT-Image2 提示词库单日 2442 星王炸 + Codex 连登破千 + 免费编码 Agent 浪潮 + Hermes Agent 235K + omarchy 破千回归 + Apache 入局 Agent 工作区 + 个人 AI 大脑三连</strong> —— freestylefly/awesome-gpt-image-2（+2,442★）15.5K★ 中文开发者提示词工程首登即霸榜。openai/codex（+1,990★）117K★ 连续两天破千。basecamp/omarchy（+1,055★）30.1K★ 单日破千回归。NousResearch/hermes-agent（+899★）235.8K★ 成长型 Agent 首登。Alishahryar1/free-claude-code（+889★）48.9K★ 免费白嫖浪潮首登。tinyhumansai/openhuman（+515★）37.2K★ 个人 AI 超级智能首登。multica-ai/andrej-karpathy-skills（+491★）206.5K★ 三连登。anthropics/claude-plugins-community（+490★）Anthropic 官方插件市场首登。makeplane/plane（+268★）连登。AgriciDaniel/claude-obsidian（+272★）第二大脑首登。apache/maka（+408★）Apache 孵化 Agent 工作区。提示词工程 × 免费浪潮 × 个人 AI × 审计合规——编码 Agent 生态全面开花，官方与社区正面交锋。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
