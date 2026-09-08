#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-08 (8-day gap, 无昨日榜→平铺结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 8)
gap_days = (today - last).days  # 8
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（8天gap无昨日榜，含回归项目，触发平铺渲染）──
    {
        "rank": 1,
        "owner": "heygen-com",
        "name": "hyperframes",
        "fullName": "heygen-com / hyperframes",
        "org": "HeyGen",
        "url": "https://github.com/heygen-com/hyperframes",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "47,423",
        "forks": "4,375",
        "starsToday": "2,628",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,628★！47.4K★ 首登！写 HTML、渲染视频、为 Agent 而生——HeyGen 出品的程序化视频渲染框架。",
        "problems": [
            "<strong>视频制作门槛高：</strong>传统剪辑工具复杂，非专业人士难上手。",
            "<strong>AI 视频不可控：</strong>生成式视频难以精确指定每一帧内容。",
            "<strong>重复劳动多：</strong>模板化视频无法批量程序化生产。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/heygen-com/hyperframes.git</code></pre>",
            "用 HTML 描述镜头与动效。",
            "让 Agent 渲染成最终视频。"
        ],
        "insights": [
            "<strong>47.4K★ 首登：</strong>HeyGen 官方开源——视频生成公司押注「代码即视频」。",
            "<strong>HTML→视频：</strong>把视频当网页写——浏览器渲染管线成为视频引擎，这是程序化视频的终极形态。",
            "<strong>Agent 原生：</strong>HTML 是 LLM 最擅长的输出格式——视频生成正在被 Agent 工作流接管。"
        ],
        "tags": ["video", "html", "rendering", "agent", "heyGen"]
    },
    {
        "rank": 2,
        "owner": "microsoft",
        "name": "markitdown",
        "fullName": "microsoft / markitdown",
        "org": "Microsoft",
        "url": "https://github.com/microsoft/markitdown",
        "lang": "Python",
        "langClass": "py",
        "stars": "181,354",
        "forks": "13,316",
        "starsToday": "2,045",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,045★！181K★ 重磅回归！微软官方文档转 Markdown 工具——所有文件格式统一喂给 LLM 的「格式翻译官」。",
        "problems": [
            "<strong>文档格式多样：</strong>PDF/Office/音视频格式混杂难处理。",
            "<strong>LLM 读不懂：</strong>喂给大模型前需要把二进制文档转文本。",
            "<strong>转换质量差：</strong>通用转换器常丢结构、乱排版。"
        ],
        "usage": [
            "安装：<pre><code>pip install markitdown</code></pre>",
            "转换：<pre><code>markitdown file.pdf</code></pre>",
            "接入 RAG 或 Agent 数据管线。"
        ],
        "insights": [
            "<strong>181K★ 重磅回归：</strong>6 月初 142K → 今天 181K——三个月涨 40K，AI 数据管线刚需持续。",
            "<strong>Markdown 是 AI 通用语：</strong>所有文档先转 Markdown 再进 LLM——格式归一化是 RAG 的第一公里。",
            "<strong>微软的 Agent 基建：</strong>微软持续押注 AI 工具链开源——markitdown 是其中最「不起眼却刚需」的一环。"
        ],
        "tags": ["markdown", "document-conversion", "microsoft", "rag", "python"]
    },
    {
        "rank": 3,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "253,809",
        "forks": "38,063",
        "starsToday": "1,426",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,426★！254K★ 第六次上榜！Agent Harness 性能优化系统——技能/直觉/记忆/安全，245K→254K 持续吸星。",
        "problems": [
            "<strong>Agent 性能瓶颈：</strong>Harness 层低效拖慢整个 Agent 工作流。",
            "<strong>记忆与技能管理乱：</strong>技能/直觉/记忆缺乏统一调度。",
            "<strong>安全缺失：</strong>Agent 自主执行缺少权限边界。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/affaan-m/ECC.git</code></pre>",
            "接入 Claude Code / Codex / Opencode。",
            "启用性能优化与安全策略。"
        ],
        "insights": [
            "<strong>第六次上榜：</strong>8-31 刚 +490，今天 +1,426 加速——Agent Harness 优化需求没有退潮。",
            "<strong>245K→254K：</strong>一周涨 9K★——技能经济的基础设施层被反复加仓。",
            "<strong>Harness 生意：</strong>所有技能库的火热最终都会传导到 Harness 层——ECC 是卖铲子的铲子。"
        ],
        "tags": ["agent", "harness", "performance", "optimization", "javascript"]
    },
    {
        "rank": 4,
        "owner": "cathrynlavery",
        "name": "diagram-design",
        "fullName": "cathrynlavery / diagram-design",
        "org": "cathrynlavery",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "lang": "HTML",
        "langClass": "html",
        "stars": "33,993",
        "forks": "2,167",
        "starsToday": "1,070",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,070★！34K★ 第四次上榜！38 种编辑级图表类型——自包含 HTML+SVG，「无阴影、无 Mermaid 俗套」的设计级图表技能。",
        "problems": [
            "<strong>Mermaid 图丑：</strong>自动生成图表千篇一律、审美堪忧。",
            "<strong>风格不统一：</strong>团队图表缺乏编辑级设计规范。",
            "<strong>图与内容脱节：</strong>通用图表工具不懂内容层级。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cathrynlavery/diagram-design.git</code></pre>",
            "加载 skill 到 Claude Code / Codex / Pi。",
            "生成自包含 HTML+SVG 编辑级图表。"
        ],
        "insights": [
            "<strong>第四次上榜：</strong>8-13 的 10K → 今天 34K——三周翻三倍，设计级图表是垂直技能爆款。",
            "<strong>审美反叛：</strong>「No Mermaid slop」——开发者苦自动图表丑久矣，设计品味正在成为技能卖点。",
            "<strong>与 archify 互补：</strong>架构图技能管结构、diagram-design 管审美——图表技能全面工业化。"
        ],
        "tags": ["diagrams", "design", "html", "svg", "agent-skills"]
    },
    {
        "rank": 5,
        "owner": "jo-inc",
        "name": "camofox-browser",
        "fullName": "jo-inc / camofox-browser",
        "org": "jo-inc",
        "url": "https://github.com/jo-inc/camofox-browser",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "10,246",
        "forks": "1,040",
        "starsToday": "872",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +872★！10.2K★ 首登！隐形无头浏览器——绕过 Cloudflare/机器人检测/反爬，Puppeteer/Playwright 的即插即用替代品。",
        "problems": [
            "<strong>反爬拦截：</strong>Cloudflare 等防护挡掉正常自动化。",
            "<strong>指纹暴露：</strong>无头浏览器特征明显，易被识别。",
            "<strong>Agent 上网难：</strong>AI Agent 抓网页经常被反爬系统拒之门外。"
        ],
        "usage": [
            "安装：<pre><code>npm install camofox-browser</code></pre>",
            "替换 Puppeteer/Playwright 调用。",
            "让 Agent 隐身浏览目标网站。"
        ],
        "insights": [
            "<strong>10.2K★ 首登：</strong>反反爬工具登榜——Agent 上网需求撞上网站防护墙。",
            "<strong>军备竞赛：</strong>网站反爬越强、隐形浏览器越火——这场攻防没有终点。",
            "<strong>Agent 的数字身份：</strong>当 Agent 要替人操作网页，它需要一套「不像机器人」的浏览器——隐身即生产力。"
        ],
        "tags": ["browser", "stealth", "scraping", "automation", "agent"]
    },
    {
        "rank": 6,
        "owner": "coreyhaines31",
        "name": "marketingskills",
        "fullName": "coreyhaines31 / marketingskills",
        "org": "Corey Haines",
        "url": "https://github.com/coreyhaines31/marketingskills",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "48,544",
        "forks": "7,476",
        "starsToday": "666",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +666★！48.5K★ 首登！Claude Code/AI Agent 营销技能包——CRO、文案、SEO、分析、增长工程，营销人的 Agent 工具箱。",
        "problems": [
            "<strong>营销工作流重复：</strong>CRO/SEO/文案任务琐碎且高度模板化。",
            "<strong>领域技能缺失：</strong>通用 Agent 不懂转化率优化与增长实验。",
            "<strong>工具割裂：</strong>营销分析散落多平台难整合。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/coreyhaines31/marketingskills.git</code></pre>",
            "加载营销技能到 Claude Code。",
            "执行 CRO/文案/SEO 自动化任务。"
        ],
        "insights": [
            "<strong>48.5K★ 首登：</strong>Corey Haines（知名开发者布道师）出手——营销技能库登榜。",
            "<strong>技能从开发到商业：</strong>继科研/专利/图表后，营销成为技能经济新赛道——Agent 正在进入每个职业。",
            "<strong>名人效应加持：</strong>48K★ 的起点——个人品牌 + Agent 技能是新的开源分发密码。"
        ],
        "tags": ["marketing", "agent-skills", "seo", "cro", "growth"]
    },
    {
        "rank": 7,
        "owner": "mksglu",
        "name": "context-mode",
        "fullName": "mksglu / context-mode",
        "org": "mksglu",
        "url": "https://github.com/mksglu/context-mode",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "21,232",
        "forks": "1,537",
        "starsToday": "652",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +652★！21.2K★ 首登！AI 编码 Agent 的上下文窗口优化器——工具输出沙箱化（压缩 98%）、会话记忆持久化、MCP+hooks 跨 17 平台路由。",
        "problems": [
            "<strong>上下文爆掉：</strong>工具输出刷屏，Agent 很快用完上下文窗口。",
            "<strong>状态丢失：</strong>每次会话记忆清零，Agent 像失忆症。",
            "<strong>平台孤岛：</strong>17 种编码工具各自为政，技能不互通。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/mksglu/context-mode.git</code></pre>",
            "安装 hooks 接入编码 Agent。",
            "工具输出自动压缩、记忆跨会话持久化。"
        ],
        "insights": [
            "<strong>21.2K★ 首登：</strong>上下文优化工具登榜——token 就是钱，省上下文就是省成本。",
            "<strong>98% 压缩：</strong>把工具输出先沙箱再压缩——「少喂垃圾」比「更大窗口」更聪明。",
            "<strong>记忆持久化：</strong>Agent 失忆是最大痛点——跨会话记忆正在成为标配基础设施。"
        ],
        "tags": ["context", "agent", "optimization", "mcp", "tokens"]
    },
    {
        "rank": 8,
        "owner": "The-Swarm-Corporation",
        "name": "AutoHedge",
        "fullName": "The-Swarm-Corporation / AutoHedge",
        "org": "The Swarm Corporation",
        "url": "https://github.com/The-Swarm-Corporation/AutoHedge",
        "lang": "Python",
        "langClass": "py",
        "stars": "5,526",
        "forks": "831",
        "starsToday": "494",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +494★！5.5K★ 首登！几分钟搭建你的自主对冲基金——群智 + AI Agent 自动完成市场分析、风险管理与交易执行。",
        "problems": [
            "<strong>量化门槛高：</strong>对冲基金级策略需要大量工程与金融知识。",
            "<strong>盯盘费人：</strong>24 小时市场无法人工持续监控。",
            "<strong>风控复杂：</strong>自动化交易最难的是风险边界控制。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/The-Swarm-Corporation/AutoHedge.git</code></pre>",
            "配置交易所 API 密钥。",
            "启动 swarm agents 自动分析执行。"
        ],
        "insights": [
            "<strong>5.5K★ 首登：</strong>「自主对冲基金」登榜——AI 交易从策略库升级为组织形态。",
            "<strong>Swarm 叙事：</strong>多 Agent 分工（分析/风控/执行）——金融是最早验证多智能体的商业场景。",
            "<strong>双刃剑：</strong>交易民主化的另一面是风险民主化——Agent 亏钱的速度同样快。"
        ],
        "tags": ["trading", "hedge-fund", "swarm", "finance", "agents"]
    },
    {
        "rank": 9,
        "owner": "openai",
        "name": "skills",
        "fullName": "openai / skills",
        "org": "OpenAI",
        "url": "https://github.com/openai/skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "26,331",
        "forks": "1,765",
        "starsToday": "490",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +490★！26.3K★ 首登！OpenAI 官方 Codex Skills 目录——巨头亲自下场定义 Agent 技能标准。",
        "problems": [
            "<strong>技能标准混乱：</strong>各平台技能格式不互通，迁移成本高。",
            "<strong>官方缺位：</strong>技能生态缺乏巨头级规范背书。",
            "<strong>发现难：</strong>好技能散落各处难以检索。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/openai/skills.git</code></pre>",
            "浏览官方技能目录。",
            "在 Codex 中安装使用。"
        ],
        "insights": [
            "<strong>26.3K★ 首登：</strong>OpenAI 官方技能目录登榜——技能经济从社区自发进入巨头军备。",
            "<strong>标准之争：</strong>Anthropic 技能生态 + OpenAI 官方目录 + 社区标准——谁能定义 Agent 技能格式谁就赢。",
            "<strong>平台锁定的新战场：</strong>技能市场是下一代应用商店——巨头必须亲自下场。"
        ],
        "tags": ["openai", "codex", "skills", "catalog", "agents"]
    },
    {
        "rank": 10,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "283,137",
        "forks": "25,373",
        "starsToday": "446",
        "count": 13,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +446★！283K★ 第十三次上榜！Agentic 技能框架与软件开发方法论——「真正可用的」Agent 工作流体系。",
        "problems": [
            "<strong>Agent 行为不可控：</strong>缺乏方法论约束的 Agent 像脱缰野马。",
            "<strong>技能无体系：</strong>零散技能无法形成完整开发工作流。",
            "<strong>复现困难：</strong>成功经验难以沉淀为可复用流程。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/obra/superpowers.git</code></pre>",
            "安装进 Claude Code。",
            "按方法论驱动完整开发流程。"
        ],
        "insights": [
            "<strong>第十三次上榜：</strong>283K★ 的常青树——从 8-08 回归，方法论型技能有最长尾。",
            "<strong>框架 vs 目录：</strong>OpenAI 给目录、superpowers 给方法论——技能经济分层：内容层与系统层。",
            "<strong>「真正可用」：</strong>口号直指痛点——大多数技能演示大于实用，方法论才是护城河。"
        ],
        "tags": ["agent", "skills", "framework", "methodology", "claude"]
    },
    {
        "rank": 11,
        "owner": "ayghri",
        "name": "i-have-adhd",
        "fullName": "ayghri / i-have-adhd",
        "org": "ayghri",
        "url": "https://github.com/ayghri/i-have-adhd",
        "lang": "Python",
        "langClass": "py",
        "stars": "28,555",
        "forks": "1,779",
        "starsToday": "422",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +422★！28.6K★ 回归！阻止编码 Agent 把答案埋起来——ADHD 友好输出的 Agent 技能，7 月 6.8K 至今涨 4 倍。",
        "problems": [
            "<strong>答案被淹没：</strong>Agent 回答冗长绕弯，关键结论藏在最后。",
            "<strong>注意力失焦：</strong>长输出让 ADHD 用户读不下去。",
            "<strong>信息密度低：</strong>大量寒暄挤占真正有用的内容。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/ayghri/i-have-adhd.git</code></pre>",
            "把技能加载进编码 Agent。",
            "让 Agent 直接给结论、少废话。"
        ],
        "insights": [
            "<strong>28.6K★ 回归：</strong>7-22 的 6.8K → 今天 28.5K——一个多月涨 4 倍，ADHD 话题出圈。",
            "<strong>「直接给答案」是普遍刚需：</strong>打着 ADHD 旗号，解决的是所有人对高效沟通的渴望。",
            "<strong>神经多样性 UX：</strong>Agent 交互设计开始考虑 ADHD/阅读障碍人群——包容性设计进入 AI 层。"
        ],
        "tags": ["adhd", "agent-skills", "ux", "communication", "clarity"]
    },
    {
        "rank": 12,
        "owner": "browser-use",
        "name": "browser-use",
        "fullName": "browser-use / browser-use",
        "org": "Browser Use",
        "url": "https://github.com/browser-use/browser-use",
        "lang": "Python",
        "langClass": "py",
        "stars": "113,156",
        "forks": "12,476",
        "starsToday": "330",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +330★！113K★ 回归！让网站对 AI Agent 可访问——网页自动化的事实标准，8-27 后再次上榜。",
        "problems": [
            "<strong>Agent 操作网页难：</strong>浏览器自动化涉及选择器、等待、状态管理。",
            "<strong>登录态复杂：</strong>需要鉴权的站点 Agent 无法直接访问。",
            "<strong>任务编排繁琐：</strong>多步网页任务难以稳定执行。"
        ],
        "usage": [
            "安装：<pre><code>pip install browser-use</code></pre>",
            "配置 LLM API。",
            "用自然语言让 Agent 执行网页任务。"
        ],
        "insights": [
            "<strong>113K★ 回归：</strong>8-27 后再次上榜——网页 Agent 基础设施的持续刚需。",
            "<strong>网站即 API：</strong>没有开放 API 的网站，Agent 也能用浏览器访问——浏览器是最后的通用接口。",
            "<strong>与 camofox 同台：</strong>一个做隐身一个做自动化——网页 Agent 的「能访问」与「不被封」是同一枚硬币。"
        ],
        "tags": ["browser", "agent", "automation", "web", "python"]
    }
]

# Shift labels for 8-day gap (accurate offset: +8)
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = f'{gap_days}天前'
    elif label == '昨天':
        day['label'] = f'{gap_days+1}天前'
    elif label == '前天':
        day['label'] = f'{gap_days+2}天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + gap_days}天前'

# Insert new day
new_day = {
    "date": "2026-09-08",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-08'
data['topic'] = '🔥 <strong>HeyGen hyperframes 程序化视频首登 + 微软 markitdown 重磅回归 + ECC 六次上榜 + OpenAI 官方 skills 目录 + diagram-design 设计级图表 + camofox 隐形浏览器</strong> —— heygen-com/hyperframes（+2,628★）47.4K★ 写 HTML 渲染视频首登。microsoft/markitdown（+2,045★）181K★ 文档转 Markdown 重磅回归。affaan-m/ECC（+1,426★）254K★ 第六次上榜。cathrynlavery/diagram-design（+1,070★）34K★ 设计级图表四登。jo-inc/camofox-browser（+872★）隐形浏览器首登。coreyhaines31/marketingskills（+666★）营销技能首登。mksglu/context-mode（+652★）上下文优化首登。The-Swarm-Corporation/AutoHedge（+494★）自主对冲基金首登。openai/skills（+490★）OpenAI 官方技能目录首登。obra/superpowers（+446★）283K★ 十三登。ayghri/i-have-adhd（+422★）ADHD 友好输出回归。browser-use/browser-use（+330★）113K★ 网页 Agent 回归。时隔 8 天回归更新——技能经济进入巨头军备（OpenAI 下场）+ 视频生成程序化 + 文档/上下文/浏览器全链路 Agent 基建——「Agent 的工具箱」正在成为开源最大叙事。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:5]]}")

# Verify badge present on every project
assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
