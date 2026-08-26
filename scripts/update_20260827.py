#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-27 (1-day gap from 8/26)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 27)
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
        "stars": "21,228",
        "forks": "1,680",
        "starsToday": "4,044",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +4,044★ 单日王炸！21.2K★ 三连登！GPT-Image2 提示词引擎——单日四千星，三天累计 8,100★，史上最猛提示词项目。",
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
            "<strong>单日 +4,044★ 王炸：</strong>三天累计 8,100+★——提示词工程项目创造近期最大单日涨幅。",
            "<strong>Prompt as Code 全球验证：</strong>中文开发者把提示词做成模板库——图片生成工程化被全球疯抢。",
            "<strong>提示词经济成型：</strong>案例逆向 + 模板复用——提示词正在变成可交易的知识资产。"
        ],
        "tags": ["gpt-image", "prompt-engineering", "templates", "ai-image", "awesome-list"]
    },
    {
        "rank": 2,
        "owner": "basecamp",
        "name": "omarchy",
        "fullName": "basecamp / omarchy",
        "org": "Basecamp",
        "url": "https://github.com/basecamp/omarchy",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "31,969",
        "forks": "1,420",
        "starsToday": "1,021",
        "count": 5,
        "description": "🔥 亮点 —— 今日 +1,021★！32K★ 五连登连续三天破千！DHH 的现代化 Linux——32K 星里程碑。",
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
            "<strong>五连登连续三天破千：</strong>+1,055 → +1,083 → +1,021——omarchy 成为近期最稳定的破千常客。",
            "<strong>32K★ 的极客情怀：</strong>DHH 自建 OS 的浪漫持续吸粉——「摆脱依赖」思潮不减。",
            "<strong>AI 时代的逆流：</strong>当 AI 让一切变重，omarchy 代表「回到简单」的长期主义。"
        ],
        "tags": ["linux", "basecamp", "dhh", "distro", "developer-tools"]
    },
    {
        "rank": 3,
        "owner": "tt-a1i",
        "name": "archify",
        "fullName": "tt-a1i / archify",
        "org": "tt-a1i",
        "url": "https://github.com/tt-a1i/archify",
        "lang": "HTML",
        "langClass": "html",
        "stars": "17,815",
        "forks": "620",
        "starsToday": "1,002",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,002★！17.8K★ 首登即破千！Agent 技能——生成漂亮可验证的架构/工作流/时序/数据流图，自包含 HTML + 动效。",
        "problems": [
            "<strong>架构图绘制费时：</strong>手动画架构图/流程图耗时且难维护。",
            "<strong>图表工具割裂：</strong>不同图表类型要用不同工具。",
            "<strong>可验证性缺失：</strong>图与实际代码/架构脱节。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/tt-a1i/archify.git</code></pre>",
            "加载 SKILL.md 到 AI 助手。",
            "让 Agent 生成自包含 HTML 架构图。"
        ],
        "insights": [
            "<strong>首登即破千：</strong>17.8K★ 的架构图 Agent 技能——可视化工程资产需求旺盛。",
            "<strong>自包含 HTML：</strong>单文件图表 + 动效 + 可导出——Agent 技能正在工业化。",
            "<strong>技能生态大爆发：</strong>archify、garden-skills、scientific-agent-skills 同榜——Agent 技能进入品类化时代。"
        ],
        "tags": ["agent-skills", "architecture", "diagrams", "html", "visualization"]
    },
    {
        "rank": 4,
        "owner": "AgriciDaniel",
        "name": "claude-obsidian",
        "fullName": "AgriciDaniel / claude-obsidian",
        "org": "AgriciDaniel",
        "url": "https://github.com/AgriciDaniel/claude-obsidian",
        "lang": "Python",
        "langClass": "py",
        "stars": "13,396",
        "forks": "560",
        "starsToday": "812",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +812★！13.4K★ 三连登！Obsidian + Claude Code 自组织 AI 第二大脑——连续三天热度高位。",
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
            "<strong>三连登稳定高位：</strong>+272 → +813 → +812——AI 第二大脑需求持续旺盛。",
            "<strong>Markdown 数据主权：</strong>「纯 Markdown 你拥有」——本地优先知识管理对抗云笔记。",
            "<strong>笔记党与 Agent 党合流：</strong>Zettelkasten 方法论 + 编码 Agent——知识工作者的终极形态。"
        ],
        "tags": ["obsidian", "claude-code", "second-brain", "knowledge-graph", "markdown"]
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
        "stars": "50,349",
        "forks": "6,480",
        "starsToday": "566",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +566★！50.4K★ 隔日回归！免费白嫖 Claude Code/Codex/Pi/OpenCode——突破 50K 星大关。",
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
            "<strong>50K★ 里程碑：</strong>免费白嫖编码 Agent 突破五万星——开发者对订阅价格的抵抗持续。",
            "<strong>隔日回归：</strong>8/25 首登后今天再回——免费浪潮不是一日热度。",
            "<strong>官方与社区的对撞：</strong>Codex 官方 vs 免费版——定价权之争继续。"
        ],
        "tags": ["claude-code", "free", "codex", "tokens", "developer-tools"]
    },
    {
        "rank": 6,
        "owner": "anthropics",
        "name": "claude-plugins-community",
        "fullName": "anthropics / claude-plugins-community",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-community",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,174",
        "forks": "130",
        "starsToday": "537",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +537★！2.2K★ 三连登！Anthropic 官方社区插件市场——Claude Cowork 和 Claude Code 的插件集市。",
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
            "<strong>三连登：</strong>+490 → +351 → +537——Anthropic 社区插件市场持续升温。",
            "<strong>官方 + 社区双轨：</strong>community 与 official 连续两天同榜——插件生态标准分层成型。",
            "<strong>插件经济前夜：</strong>编码 Agent 的插件市场大战——生态位之争白热化。"
        ],
        "tags": ["anthropic", "claude", "plugins", "marketplace", "ecosystem"]
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
        "stars": "38,187",
        "forks": "2,260",
        "starsToday": "522",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +522★！38.2K★ 三连登！个人 AI 超级智能——本地优先生活记忆 + Agent 舰队编排 + 深度研究。",
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
            "<strong>三连登：</strong>+515 → +542 → +522——个人 AI 大脑需求稳定。",
            "<strong>Agent 舰队编排：</strong>从单 Agent 到舰队——多 Agent 协作成为个人 AI 的新形态。",
            "<strong>记忆即资产延续：</strong>OpenViking、ai-memory、openhuman——Agent 记忆赛道持续霸榜。"
        ],
        "tags": ["personal-ai", "memory", "rust", "agent-orchestration", "local-first"]
    },
    {
        "rank": 8,
        "owner": "marin-community",
        "name": "marin",
        "fullName": "marin-community / marin",
        "org": "Marin Community",
        "url": "https://github.com/marin-community/marin",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,445",
        "forks": "136",
        "starsToday": "443",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +443★！2.4K★ 连续两天登榜！基础模型研发开源框架——Marin 社区驱动，热度翻倍。",
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
            "<strong>连登两天热度翻倍：</strong>+231 → +443——基础模型研究工具链需求持续。",
            "<strong>社区驱动的开源框架：</strong>对标 EleutherAI 模式——社区科研是开源 AI 的重要力量。",
            "<strong>Agent 时代的基础层：</strong>当 Agent 应用卷到极致，基础模型研究回归价值。"
        ],
        "tags": ["foundation-models", "research", "framework", "open-source", "ai"]
    },
    {
        "rank": 9,
        "owner": "anthropics",
        "name": "claude-plugins-official",
        "fullName": "anthropics / claude-plugins-official",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-official",
        "lang": "Python",
        "langClass": "py",
        "stars": "34,350",
        "forks": "1,260",
        "starsToday": "307",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +307★！34.4K★ 连续两天登榜！Anthropic 官方管理的高质量 Claude Code 插件目录——插件生态的「官方认证」。",
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
            "<strong>连登两天：</strong>+55 → +307——官方插件目录热度上升。",
            "<strong>官方 + 社区双轨：</strong>official（认证）+ community（投稿）——插件生态标准分层。",
            "<strong>生态战争升级：</strong>Anthropic 建插件市场、Cursor 建插件规范、OpenAI 拼 CLI——编码 Agent 生态全面开打。"
        ],
        "tags": ["anthropic", "claude", "plugins", "official", "ecosystem"]
    },
    {
        "rank": 10,
        "owner": "ConardLi",
        "name": "garden-skills",
        "fullName": "ConardLi / garden-skills",
        "org": "ConardLi",
        "url": "https://github.com/ConardLi/garden-skills",
        "lang": "CSS",
        "langClass": "css",
        "stars": "10,899",
        "forks": "420",
        "starsToday": "136",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +136★！10.9K★ 首登！ConardLi 的开源 Skills 合集——web 设计、知识检索、图像生成全覆盖。",
        "problems": [
            "<strong>技能分散难找：</strong>高质量 Agent 技能分散各处。",
            "<strong>web 设计技能稀缺：</strong>前端设计类 Agent 技能尤其匮乏。",
            "<strong>中文社区缺标杆：</strong>中文开发者的优质技能合集少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/ConardLi/garden-skills.git</code></pre>",
            "按分类加载 Skills 到 AI 助手。",
            "使用 web 设计/知识检索/图像生成技能。"
        ],
        "insights": [
            "<strong>中文开发者技能标杆：</strong>ConardLi（前端圈知名开发者）开源技能合集首登——中文 Agent 技能走向全球。",
            "<strong>技能品类化：</strong>web 设计、知识检索、图像生成——Agent 技能按场景分类成库。",
            "<strong>与 archify 同日登榜：</strong>技能生态大爆发——Agent 技能正在变成「可安装的插件」。"
        ],
        "tags": ["agent-skills", "web-design", "knowledge", "image-generation", "chinese-dev"]
    },
    {
        "rank": 11,
        "owner": "browser-use",
        "name": "browser-use",
        "fullName": "browser-use / browser-use",
        "org": "browser-use",
        "url": "https://github.com/browser-use/browser-use",
        "lang": "Python",
        "langClass": "py",
        "stars": "110,945",
        "forks": "11,240",
        "starsToday": "135",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +135★！110.9K★ 首登！让网站对 AI Agent 可访问——浏览器 Agent 的开源标杆 110K 星。",
        "problems": [
            "<strong>Agent 无法上网：</strong>AI Agent 难以操作真实网站完成在线任务。",
            "<strong>浏览器自动化难：</strong>传统爬虫/自动化工具门槛高。",
            "<strong>网页交互复杂：</strong>登录、表单、动态内容处理繁琐。"
        ],
        "usage": [
            "安装：<pre><code>pip install browser-use</code></pre>",
            "配置 LLM 与浏览器。",
            "让 Agent 自动完成网页任务。"
        ],
        "insights": [
            "<strong>110.9K★ 的浏览器 Agent：</strong>browser-use 首登——「让 AI 上网」成为 Agent 标配能力。",
            "<strong>Agent 与互联网的接口：</strong>浏览器是 Agent 感知世界的窗口——这个基础设施项目价值巨大。",
            "<strong>与编码 Agent 互补：</strong>写代码的 Agent（Codex/Claude Code）+ 上网的 Agent（browser-use）——Agent 能力拼图完善。"
        ],
        "tags": ["browser", "agent", "automation", "web", "llm"]
    },
    {
        "rank": 12,
        "owner": "K-Dense-AI",
        "name": "scientific-agent-skills",
        "fullName": "K-Dense-AI / scientific-agent-skills",
        "org": "K-Dense AI",
        "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "34,709",
        "forks": "2,040",
        "starsToday": "130",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +130★！34.7K★ 隔日回归！把任何 AI Agent 变成 AI 科学家——163 个技能 + 100+ 科学数据库，17.5 万科学家使用。",
        "problems": [
            "<strong>科研工具链复杂：</strong>科学家做数据分析需要大量编程技能。",
            "<strong>领域知识门槛：</strong>生物学/化学等领域的专业分析需要领域技能。",
            "<strong>Agent 不懂科学：</strong>通用 Agent 缺乏科研工作流支持。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/K-Dense-AI/scientific-agent-skills.git</code></pre>",
            "加载科研技能到 AI Agent。",
            "让 Agent 辅助生物学/化学等科研工作。"
        ],
        "insights": [
            "<strong>17.5 万科学家的选择：</strong>163 个验证技能 + 100+ 科学数据库——科研 Agent 技能库登榜。",
            "<strong>AI 科学家加速：</strong>从实验室到论文——Agent 正在进入严肃科研。",
            "<strong>技能库纵向深耕：</strong>横向技能库（garden/archify）+ 纵向科学库——Agent 技能生态立体化。"
        ],
        "tags": ["scientific", "agent-skills", "research", "biology", "science"]
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
    "date": "2026-08-27",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-27'
data['topic'] = '🔥 <strong>awesome-gpt-image-2 单日 4044 星王炸 + omarchy 五连登 + 技能生态大爆发 + Anthropic 插件双轨三连 + 个人 AI 三连 + 浏览器 Agent 回归</strong> —— freestylefly/awesome-gpt-image-2（+4,044★）21.2K★ 单日四千星三连登，提示词工程史上最猛。basecamp/omarchy（+1,021★）32K★ 五连登连续三天破千。tt-a1i/archify（+1,002★）17.8K★ 架构图 Agent 技能首登即破千。AgriciDaniel/claude-obsidian（+812★）13.4K★ 三连登。Alishahryar1/free-claude-code（+566★）50.4K★ 免费浪潮回归破五万。anthropics/claude-plugins-community（+537★）与 claude-plugins-official（+307★）双轨三连。tinyhumansai/openhuman（+522★）38.2K★ 三连登。marin-community/marin（+443★）连登。ConardLi/garden-skills（+136★）中文开发者技能库首登。browser-use/browser-use（+135★）110.9K★ 浏览器 Agent 回归。K-Dense-AI/scientific-agent-skills（+130★）科研技能库回归。提示词工程 × Agent 技能 × 插件生态——「技能经济」全面爆发，编码 Agent 生态进入品类化时代。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
