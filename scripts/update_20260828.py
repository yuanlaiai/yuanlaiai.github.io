#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-28 (1-day gap, 双栏结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 28)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 🆕 新面孔 ──
    {
        "rank": 1,
        "owner": "bilawalsidhu",
        "name": "gods-eye-view",
        "fullName": "bilawalsidhu / gods-eye-view",
        "org": "bilawalsidhu",
        "url": "https://github.com/bilawalsidhu/gods-eye-view",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "7,961",
        "forks": "480",
        "starsToday": "1,984",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,984★！8K★ 首登即破千！浏览器里的间谍卫星模拟器——真实数据的 3D 地球空间情报，开源版「上帝视角」。",
        "problems": [
            "<strong>空间情报门槛高：</strong>卫星数据可视化需要专业 GIS 工具。",
            "<strong>3D 地球渲染复杂：</strong>真实感地球可视化开发成本极高。",
            "<strong>数据封闭：</strong>卫星数据被商业公司垄断，普通人接触不到。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/bilawalsidhu/gods-eye-view.git</code></pre>",
            "本地启动浏览器 3D 地球。",
            "接入真实卫星数据源浏览空间情报。"
        ],
        "insights": [
            "<strong>首登即破千：</strong>8K★ 的浏览器卫星模拟器——「上帝视角」概念自带传播力。",
            "<strong>开源空间情报：</strong>真实卫星数据 + 浏览器渲染——空间情报民主化的开端。",
            "<strong>个人开发者杰作：</strong>bilawal 是知名开发者（曾任 Vercel/Resend）——个人项目也能引爆。"
        ],
        "tags": ["spatial-intelligence", "satellite", "3d-globe", "visualization", "open-source"]
    },
    {
        "rank": 2,
        "owner": "TauricResearch",
        "name": "TradingAgents",
        "fullName": "TauricResearch / TradingAgents",
        "org": "Tauric Research",
        "url": "https://github.com/TauricResearch/TradingAgents",
        "lang": "Python",
        "langClass": "py",
        "stars": "101,206",
        "forks": "18,580",
        "starsToday": "229",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +229★！101.2K★ 隔日回归！多 Agent LLM 金融交易框架——分析师/研究员/交易员 Agent 协作。",
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
            "<strong>隔日回归破 101K：</strong>百万星俱乐部成员——金融 Agent 需求稳定。",
            "<strong>多 Agent 协作范式：</strong>分析师-研究员-交易员的角色分工——Agent 团队模拟投行工作流。",
            "<strong>金融 AI 双线：</strong>Rust 量化引擎 + LLM 交易 Agent——金融 AI 持续吸星。"
        ],
        "tags": ["trading", "multi-agent", "llm", "finance", "quant"]
    },
    {
        "rank": 3,
        "owner": "JetBrains",
        "name": "go-modern-guidelines",
        "fullName": "JetBrains / go-modern-guidelines",
        "org": "JetBrains",
        "url": "https://github.com/JetBrains/go-modern-guidelines",
        "lang": "Go",
        "langClass": "go",
        "stars": "2,071",
        "forks": "96",
        "starsToday": "300",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +300★！2.1K★ 首登！JetBrains 官方 Go 指南——专门帮 AI 编码 Agent 写现代 Go。",
        "problems": [
            "<strong>AI 写 Go 不规范：</strong>LLM 生成的 Go 代码常过时、不符合现代实践。",
            "<strong>官方指南分散：</strong>Go 最佳实践散落各处，无权威汇总。",
            "<strong>Agent 需要喂养：</strong>编码 Agent 需要高质量的领域指南作为上下文。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/JetBrains/go-modern-guidelines.git</code></pre>",
            "把指南喂给 AI 编码 Agent。",
            "让 Agent 按现代 Go 实践写代码。"
        ],
        "insights": [
            "<strong>JetBrains 下场喂 Agent：</strong>官方出「给 AI 看的指南」——IDE 厂商拥抱 Agent 时代。",
            "<strong>指南即训练数据：</strong>高质量领域指南成为 Agent 上下文的关键资产。",
            "<strong>与 karpathy-skills 同赛道：</strong>给 Agent 的「食谱书」正在成为新品类。"
        ],
        "tags": ["jetbrains", "go", "guidelines", "ai-coding", "agent"]
    },
    {
        "rank": 4,
        "owner": "ComposioHQ",
        "name": "awesome-claude-skills",
        "fullName": "ComposioHQ / awesome-claude-skills",
        "org": "Composio",
        "url": "https://github.com/ComposioHQ/awesome-claude-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "73,603",
        "forks": "4,120",
        "starsToday": "130",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +130★！73.6K★ 首登！Claude Skills 精选大全——73K 星的技能资源库，Claude 工作流定制中心。",
        "problems": [
            "<strong>Skills 发现难：</strong>优质 Claude Skills 分散各处。",
            "<strong>工作流定制缺参考：</strong>不知道有哪些现成技能可用。",
            "<strong>生态资源聚合缺位：</strong>缺一个权威的 Claude 技能导航。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/ComposioHQ/awesome-claude-skills.git</code></pre>",
            "按分类浏览 Claude Skills。",
            "复制技能到自己的 Claude 工作流。"
        ],
        "insights": [
            "<strong>73.6K★ 的技能大全：</strong>Composio 的 Claude 技能导航——技能生态的「黄页」。",
            "<strong>与 Anthropic 插件双仓库呼应：</strong>官方建市场、社区建导航——Claude 生态双层结构成型。",
            "<strong>技能经济爆发：</strong>archify/garden/scientific/awesome-claude-skills——技能库连续四天霸榜。"
        ],
        "tags": ["claude", "skills", "awesome-list", "workflow", "ecosystem"]
    },
    # ── 🔥 连登追踪 ──
    {
        "rank": 5,
        "owner": "tt-a1i",
        "name": "archify",
        "fullName": "tt-a1i / archify",
        "org": "tt-a1i",
        "url": "https://github.com/tt-a1i/archify",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "23,121",
        "forks": "780",
        "starsToday": "4,239",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +4,239★ 单日王炸！23.1K★ 连登！架构图 Agent 技能——两天累计 5,200★，技能经济最猛选手。",
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
            "<strong>单日 +4,239★ 王炸：</strong>+1,002 → +4,239——架构图技能两天翻 4 倍，技能经济的现象级选手。",
            "<strong>自包含 HTML：</strong>单文件图表 + 动效 + 可导出——Agent 技能正在工业化。",
            "<strong>技能生态大爆发：</strong>archify/garden/scientific/awesome-claude-skills 同榜——Agent 技能进入品类化时代。"
        ],
        "tags": ["agent-skills", "architecture", "diagrams", "html", "visualization"]
    },
    {
        "rank": 6,
        "owner": "freestylefly",
        "name": "awesome-gpt-image-2",
        "fullName": "freestylefly / awesome-gpt-image-2",
        "org": "freestylefly",
        "url": "https://github.com/freestylefly/awesome-gpt-image-2",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "22,980",
        "forks": "1,820",
        "starsToday": "2,096",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +2,096★！23K★ 四连登！GPT-Image2 提示词引擎——四天累计 10,000+★，提示词工程的神话。",
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
            "<strong>四连登累计 10,000+★：</strong>+2,442 → +1,698 → +4,044 → +2,096——提示词工程持续霸榜。",
            "<strong>Prompt as Code 全球验证：</strong>中文开发者把提示词做成模板库——图片生成工程化被全球采纳。",
            "<strong>提示词经济成型：</strong>案例逆向 + 模板复用——提示词正在变成可交易的知识资产。"
        ],
        "tags": ["gpt-image", "prompt-engineering", "templates", "ai-image", "awesome-list"]
    },
    {
        "rank": 7,
        "owner": "AgriciDaniel",
        "name": "claude-obsidian",
        "fullName": "AgriciDaniel / claude-obsidian",
        "org": "AgriciDaniel",
        "url": "https://github.com/AgriciDaniel/claude-obsidian",
        "lang": "Python",
        "langClass": "py",
        "stars": "13,988",
        "forks": "580",
        "starsToday": "634",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +634★！14K★ 四连登！Obsidian + Claude Code 自组织 AI 第二大脑——连续四天高位稳定。",
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
            "<strong>四连登稳定高位：</strong>+272 → +813 → +812 → +634——AI 第二大脑需求持续。",
            "<strong>Markdown 数据主权：</strong>「纯 Markdown 你拥有」——本地优先知识管理对抗云笔记。",
            "<strong>笔记党与 Agent 党合流：</strong>Zettelkasten 方法论 + 编码 Agent——知识工作者的终极形态。"
        ],
        "tags": ["obsidian", "claude-code", "second-brain", "knowledge-graph", "markdown"]
    },
    {
        "rank": 8,
        "owner": "K-Dense-AI",
        "name": "scientific-agent-skills",
        "fullName": "K-Dense-AI / scientific-agent-skills",
        "org": "K-Dense AI",
        "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "35,300",
        "forks": "2,060",
        "starsToday": "498",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +498★！35.3K★ 连登！把任何 AI Agent 变成 AI 科学家——163 个技能 + 100+ 科学数据库，17.5 万科学家使用。",
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
            "<strong>连登：</strong>科研 Agent 技能库持续吸星——AI 科学家进入主流视野。",
            "<strong>17.5 万科学家的选择：</strong>163 个验证技能 + 100+ 科学数据库——纵向深耕的样板。",
            "<strong>技能库立体化：</strong>横向通用库 + 纵向科学库——Agent 技能生态完整成型。"
        ],
        "tags": ["scientific", "agent-skills", "research", "biology", "science"]
    },
    {
        "rank": 9,
        "owner": "ConardLi",
        "name": "garden-skills",
        "fullName": "ConardLi / garden-skills",
        "org": "ConardLi",
        "url": "https://github.com/ConardLi/garden-skills",
        "lang": "CSS",
        "langClass": "css",
        "stars": "11,318",
        "forks": "440",
        "starsToday": "415",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +415★！11.3K★ 连登！ConardLi 的开源 Skills 合集——web 设计、知识检索、图像生成全覆盖。",
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
            "<strong>连登：</strong>中文开发者技能标杆持续吸星——garden-skills 成为中文 Agent 技能出海代表。",
            "<strong>技能品类化：</strong>web 设计、知识检索、图像生成——Agent 技能按场景分类成库。",
            "<strong>技能生态大爆发：</strong>archify/garden/scientific 同榜——Agent 技能成为榜单主角。"
        ],
        "tags": ["agent-skills", "web-design", "knowledge", "image-generation", "chinese-dev"]
    },
    {
        "rank": 10,
        "owner": "anthropics",
        "name": "claude-plugins-official",
        "fullName": "anthropics / claude-plugins-official",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-official",
        "lang": "Python",
        "langClass": "py",
        "stars": "34,678",
        "forks": "1,280",
        "starsToday": "292",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +292★！34.7K★ 三连登！Anthropic 官方管理的高质量 Claude Code 插件目录——插件生态的「官方认证」。",
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
            "<strong>三连登：</strong>官方插件目录持续吸星——Anthropic 生态话语权巩固。",
            "<strong>官方 + 社区双轨：</strong>official（认证）+ community（投稿）——插件生态标准分层。",
            "<strong>生态战争升级：</strong>Anthropic 插件市场、Cursor 插件规范、OpenAI 拼 CLI——编码 Agent 生态全面开打。"
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
    "date": "2026-08-28",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-28'
data['topic'] = '🔥 <strong>archify 单日 4239 星王炸 + awesome-gpt-image-2 四连登破万 + 上帝视角卫星模拟器 + 技能生态四库同榜 + JetBrains 喂 Agent 指南</strong> —— tt-a1i/archify（+4,239★）23.1K★ 架构图技能单日王炸两天翻四倍。freestylefly/awesome-gpt-image-2（+2,096★）23K★ 四连登累计破万。bilawalsidhu/gods-eye-view（+1,984★）8K★ 浏览器卫星模拟器首登即破千。AgriciDaniel/claude-obsidian（+634★）14K★ 四连登。K-Dense-AI/scientific-agent-skills（+498★）连登。ConardLi/garden-skills（+415★）连登。JetBrains/go-modern-guidelines（+300★）官方喂 Agent 指南首登。anthropics/claude-plugins-official（+292★）三连登。TauricResearch/TradingAgents（+229★）隔日回归。ComposioHQ/awesome-claude-skills（+130★）73.6K★ 技能大全首登。技能经济全面爆发——archify/awesome-gpt-image-2 双王炸，Agent 技能连续第五天霸榜，技能库成为开源世界的新主角。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
