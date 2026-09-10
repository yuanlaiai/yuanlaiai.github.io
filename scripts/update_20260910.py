#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-10 (2-day gap, 无昨日榜→平铺结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 10)
gap_days = (today - last).days  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（2天gap无昨日榜，含回归项目，触发平铺渲染）──
    {
        "rank": 1,
        "owner": "ayghri",
        "name": "i-have-adhd",
        "fullName": "ayghri / i-have-adhd",
        "org": "ayghri",
        "url": "https://github.com/ayghri/i-have-adhd",
        "lang": "Python",
        "langClass": "py",
        "stars": "36,835",
        "forks": "2,134",
        "starsToday": "3,854",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,854★！36.8K★ 第三次上榜，两天暴涨 8.3K★！让编码 Agent 别再「先铺垫后结论」的输出纪律技能——答案放第一行，废话全部删掉。",
        "problems": [
            "<strong>答案埋在废话里：</strong>Agent 习惯先复述需求、再讲思路、最后才给结论，翻三屏才看到关键信息。",
            "<strong>上下文被稀释：</strong>冗长输出既烧 token 又淹没真正的改动点，人还得二次提炼。",
            "<strong>注意力成本高：</strong>工程师每天读几十条 Agent 输出，格式松散直接吃掉专注力。"
        ],
        "usage": [
            "安装为技能：<pre><code>npx skills add ayghri/i-have-adhd</code></pre>",
            "放进 Claude Code / Codex / Pi 的 skills 目录自动生效。",
            "要求输出格式：结论先行、要点化、删掉过程性寒暄。"
        ],
        "insights": [
            "<strong>三天三级跳：</strong>7-22 首登 6.8K★ → 9-8 二登 28.5K★ → 今天 36.8K★ +3,854★ 冲上日榜第一，登榜日即加速日是典型的「社交裂变期」特征。",
            "<strong>卖的是纪律不是能力：</strong>它一行模型权重都没改，只是约束「输出格式」——Agent 时代的竞争力正在从模型能力转向使用规范。",
            "<strong>本质是信息密度生意：</strong>当生成成本趋零，稀缺的是人的注意力——所有围绕「让输出更短更准」的技能都在给注意力定价。"
        ],
        "tags": ["agent", "skills", "productivity", "claude-code", "python"]
    },
    {
        "rank": 2,
        "owner": "bilawalsidhu",
        "name": "gods-eye-view",
        "fullName": "bilawalsidhu / gods-eye-view",
        "org": "bilawalsidhu",
        "url": "https://github.com/bilawalsidhu/gods-eye-view",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "22,488",
        "forks": "4,765",
        "starsToday": "1,588",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,588★！22.5K★ 时隔 11 天回归，星数近乎翻倍！浏览器里的「间谍卫星模拟器」——真实航班、船舶、卫星、地震、公共摄像头，语音操控，数据全部是真开源数据。",
        "problems": [
            "<strong>情报数据散落各处：</strong>航班、船舶、地震、卫星轨道分散在不同网站，无法在同一个视图里关联。",
            "<strong>没有空间视角：</strong>表格和列表看不到「谁在谁旁边」，地理关系完全丢失。",
            "<strong>可视化门槛高：</strong>做三维地球需要 Cesium / GIS 专业知识，普通人根本搭不起来。"
        ],
        "usage": [
            "打开在线版即可体验：<pre><code>https://maptheworld.ai/</code></pre>",
            "克隆部署：<pre><code>git clone https://github.com/bilawalsidhu/gods-eye-view.git</code></pre>",
            "语音指令切换图层：\"show me ships in the South China Sea\"。"
        ],
        "insights": [
            "<strong>11 天翻倍：</strong>8-29 二登 11,953★ → 今天 22,488★，涨了 10.5K——爆款内容（YouTube 系列 500 万播放）反哺开源仓库的典型路径。",
            "<strong>「仿军用」是最强钩子：</strong>它自称间谍卫星模拟器，却把「数据其实是公开的」当反转——震撼体验 + 认知颠覆，是开源传播的完美双螺旋。",
            "<strong>本质是 OSINT 民主化：</strong>过去只有机构能做的空间情报融合，如今一个浏览器标签页就能做到——能力下沉必然带来监管与隐私的新一轮博弈。"
        ],
        "tags": ["osint", "geospatial", "3d-globe", "visualization", "javascript"]
    },
    {
        "rank": 3,
        "owner": "cathrynlavery",
        "name": "diagram-design",
        "fullName": "cathrynlavery / diagram-design",
        "org": "cathrynlavery",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "lang": "HTML",
        "langClass": "html",
        "stars": "37,341",
        "forks": "2,372",
        "starsToday": "1,287",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,287★！37.3K★ 第五次上榜，较二登时翻倍！给 Claude Code / Codex / Pi 的 38 种「编辑级」图表规范——自包含 HTML + SVG，无阴影、无 Mermaid 味。",
        "problems": [
            "<strong>AI 图表审美差：</strong>默认生成 Mermaid 图，样式统一、配色随意，放进报告立刻拉低质感。",
            "<strong>配图不可控：</strong>模型每次生成的图形风格漂移，整套文档视觉不统一。",
            "<strong>改图成本高：</strong>生成图片无法编辑，改一个字要重画一张。"
        ],
        "usage": [
            "安装技能：<pre><code>/plugin marketplace add cathrynlavery/diagram-design</code></pre>",
            "向 Agent 描述图形，例如「画一个请求链路图」。",
            "产出 HTML/SVG 可直接嵌网页，或用浏览器导图。"
        ],
        "insights": [
            "<strong>四次登榜持续放大：</strong>8-13 首登 10.3K★ → 8-16 三登 18.9K★ → 9-8 四登 34.0K★ → 今天 37.3K★，「设计规范即技能」被反复验证。",
            "<strong>卖的是审美标准：</strong>它把「编辑级排版」写成可执行约束（无阴影、统一描边），审美从主观判断变成可复用的工程规则。",
            "<strong>本质是人的判断力外包：</strong>Agent 能画图但不会判断好看——谁把资深设计师的品味固化成技能，谁就在收割这一层溢价。"
        ],
        "tags": ["diagrams", "agent-skills", "design", "svg", "claude-code"]
    },
    {
        "rank": 4,
        "owner": "freestylefly",
        "name": "awesome-gpt-image-2",
        "fullName": "freestylefly / awesome-gpt-image-2",
        "org": "freestylefly",
        "url": "https://github.com/freestylefly/awesome-gpt-image-2",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "30,639",
        "forks": "2,969",
        "starsToday": "957",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +957★！30.6K★ 第六次上榜！GPT Image 2/2.5 的 530+ 案例库、20+ 工业模板与可复用 Skills，还带新旧模型同提示词对比专区。",
        "problems": [
            "<strong>提示词全靠碰运气：</strong>同一个想法反复试错，产出全靠抽卡，效率极低。",
            "<strong>效果无法复现：</strong>生成时没留存提示词，好图再也做不出第二张。",
            "<strong>不知道上限在哪：</strong>不清楚模型能做什么风格，只能在自己熟悉的几条路上打转。"
        ],
        "usage": [
            "访问案例库：<pre><code>https://gpt-image2.canghe.ai</code></pre>",
            "挑模板 → 替换主体描述 → 保留风格参数。",
            "把模板存成 Skills，让 Agent 直接调用。"
        ],
        "insights": [
            "<strong>五登到六登的稳定曲线：</strong>8-26 二登 17.6K★ → 8-29 五登 24.8K★ → 今天 30.6K★，「提示词工程」已经从技巧沉淀为资产库。",
            "<strong>Prompt as Code：</strong>把提示词当代码管理（模板化、可复用、可 diff），本质是给生成式 AI 补上「版本控制」这一环。",
            "<strong>本质是经验的可交易化：</strong>模型人人可用，差距只在「谁知道怎么问」——案例库正在把这些经验变成可流通的商品。"
        ],
        "tags": ["gpt-image", "prompts", "image-generation", "templates", "agents"]
    },
    {
        "rank": 5,
        "owner": "liquidslr",
        "name": "system-design-notes",
        "fullName": "liquidslr / system-design-notes",
        "org": "liquidslr",
        "url": "https://github.com/liquidslr/system-design-notes",
        "lang": "Markdown",
        "langClass": "md",
        "stars": "18,475",
        "forks": "3,455",
        "starsToday": "891",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +891★！18.5K★ 首登！一份个人系统设计面试笔记，29 章从限流器写到股票交易所，配手绘架构图——面试备战圈的常年硬通货。",
        "problems": [
            "<strong>系统设计资料碎片化：</strong>知识点散落在博客、视频、付费课里，没有体系。",
            "<strong>只看理论不会画：</strong>懂概念但无法在白板上画出一套完整架构。",
            "<strong>付费课太贵：</strong>经典面试书与配套课程动辄几百上千元，学生党难以承受。"
        ],
        "usage": [
            "克隆阅读：<pre><code>git clone https://github.com/liquidslr/system-design-notes.git</code></pre>",
            "按目录顺序过一遍：限流器 → 一致性哈希 → KV 存储 → 消息队列 → 支付系统。",
            "对照目录自测：盖住正文，自己先画一遍架构图。"
        ],
        "insights": [
            "<strong>2024 年建立的老仓库突然上榜：</strong>不是新项目，是「个人笔记开源化」的又一次胜利——内容型仓库的爆发往往滞后于创作一年以上。",
            "<strong>章节顺序就是能力地图：</strong>从单机扩容到股票交易所，29 章正好覆盖大厂面试的完整火力范围——结构化本身就是价值。",
            "<strong>本质是知识平权：</strong>付费课的核心内容被个人笔记免费替代，教育溢价的护城河正在被持续磨平，剩下的只有「讲解质量」和「陪伴感」无法被替代。"
        ],
        "tags": ["system-design", "interview", "notes", "architecture", "markdown"]
    },
    {
        "rank": 6,
        "owner": "Tencent",
        "name": "teamai-cli",
        "fullName": "Tencent / teamai-cli",
        "org": "Tencent",
        "url": "https://github.com/Tencent/teamai-cli",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "3,543",
        "forks": "222",
        "starsToday": "837",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +837★！腾讯官方开源！团队级 AI 配置管理器——把 skills、rules、MCP、知识库统一同步到 Claude Code、Codex、CodeBuddy 等所有 Agent。",
        "problems": [
            "<strong>团队成员各配各的：</strong>每个人的 Agent 配置、规则、技能都不同，输出质量参差不齐。",
            "<strong>配置无法继承：</strong>老员工的调教经验无法分发给新人，团队能力无法沉淀。",
            "<strong>多工具重复配置：</strong>Claude Code、Codex、CodeBuddy 各自的配置要手工维护一遍。"
        ],
        "usage": [
            "初始化：<pre><code>npx teamai-cli init</code></pre>",
            "把团队 skills / rules / MCP 配置纳入仓库版本管理。",
            "新人一条命令同步：<pre><code>npx teamai-cli sync</code></pre>"
        ],
        "insights": [
            "<strong>首个登上日榜的国产大厂 Agent 基建：</strong>不是模型、不是聊天应用，而是「团队配置治理」——说明国内大厂的 Agent 落地已进入工程化协作阶段。",
            "<strong>从个人调教到团队标准：</strong>AI 使用正在经历「个人技巧 → 组织资产」的制度化过程，这与软件工程当年的 CI/CD 规范化是同一条路径。",
            "<strong>本质是组织记忆的争夺：</strong>当每个人的 Agent 都能被统一配置，「什么算好的输出」就由公司定义——工具治理权的集中，比模型选择重要得多。"
        ],
        "tags": ["agent", "cli", "team", "mcp", "tencent"]
    },
    {
        "rank": 7,
        "owner": "THU-MAIC",
        "name": "OpenMAIC",
        "fullName": "THU-MAIC / OpenMAIC",
        "org": "THU-MAIC",
        "url": "https://github.com/THU-MAIC/OpenMAIC",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "34,979",
        "forks": "5,600",
        "starsToday": "806",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +806★！35.0K★ 第三次上榜，较首登时涨 12K★！清华团队的多智能体互动课堂——一键生成沉浸式教学场景，AI 老师 + AI 同学同台。",
        "problems": [
            "<strong>优质师资稀缺：</strong>名师资源集中在一线城市，教育公平难以实现。",
            "<strong>课堂互动缺失：</strong>录播课无法提问、无法讨论，学习效果大打折扣。",
            "<strong>内容制作昂贵：</strong>一套互动课程动辄数月开发，人力成本极高。"
        ],
        "usage": [
            "克隆并部署：<pre><code>git clone https://github.com/THU-MAIC/OpenMAIC.git</code></pre>",
            "输入课程主题，自动生成多智能体课堂。",
            "学生端提问，AI 教师与 AI 同学实时互动解答。"
        ],
        "insights": [
            "<strong>两次登榜后星数继续爬升：</strong>8-30 首登 22.9K★ → 8-31 二登 25.9K★ → 今天 35.0K★，gap 期仍净增 9K★，热度不依赖榜单曝光。",
            "<strong>「AI 同学」是关键设计：</strong>让智能体扮演同学提问，绕开了单模型自问自答的尴尬——多智能体真正的价值在角色关系，而不是数量堆叠。",
            "<strong>本质是教育资源的生产关系重构：</strong>名师不可复制，但「名师的教学设计模式」可以被复制——这是教育公平第一次有了可工程化的抓手，也是它最大的伦理争议点。"
        ],
        "tags": ["multi-agent", "education", "classroom", "tsinghua", "llm"]
    },
    {
        "rank": 8,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "284,436",
        "forks": "25,438",
        "starsToday": "731",
        "count": 14,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +731★！284K★ 第十四次上榜！Agent 技能框架与软件开发方法论的元老级项目——三十多天没上榜，回来依旧日增七百星。",
        "problems": [
            "<strong>Agent 方法论碎片化：</strong>各种提示技巧零散传播，没有成体系的工程框架。",
            "<strong>技能无法复用：</strong>换个项目、换个模型，之前调教出来的能力就归零。",
            "<strong>流程缺失：</strong>Agent 会写代码但不会做需求分析、方案设计、评审的完整流程。"
        ],
        "usage": [
            "安装技能：<pre><code>/plugin marketplace add obra/superpowers</code></pre>",
            "按方法论走完整流程：头脑风暴 → 方案 → 实施 → 评审。",
            "把可复用流程固化成自定义技能。"
        ],
        "insights": [
            "<strong>第十四次上榜：</strong>从 7 月初 244K★ 到现在 284K★，两个多月涨 40K★——技能经济里最稳的长青标的，热度从未真正离开。",
            "<strong>老项目与新品同台：</strong>超级技能框架（284K★）和 ADHD 输出技能（36.8K★）同日登榜——技能生态正在从「框架层」长到「细节层」。",
            "<strong>本质是方法论比工具长寿：</strong>模型半年一换代，工作流可以跨代复用——押注方法论的仓库，生命力天然长于押注具体模型的仓库。"
        ],
        "tags": ["skills", "methodology", "agent", "framework", "sdlc"]
    },
    {
        "rank": 9,
        "owner": "vastsa",
        "name": "PI-Desktop",
        "fullName": "vastsa / PI-Desktop",
        "org": "vastsa",
        "url": "https://github.com/vastsa/PI-Desktop",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "2,104",
        "forks": "181",
        "starsToday": "636",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +636★！本地优先的 AI 编码 Agent 桌面端——Electron + Rust 内核，自带模型、打开本地项目、插件可自行安装，无需账号、不强制走中转。",
        "problems": [
            "<strong>云端编码 Agent 数据外泄：</strong>公司代码上传到第三方服务，合规与保密双重风险。",
            "<strong>强制登录与中转：</strong>主流桌面 Agent 必须注册账号、走平台服务器，无法真正私有化。",
            "<strong>供应商锁定：</strong>换了平台，历史会话、插件、配置全部作废。"
        ],
        "usage": [
            "下载安装包：<pre><code>https://github.com/vastsa/PI-Desktop/releases</code></pre>",
            "配置自己的模型 API Key（支持本地模型）。",
            "打开本地项目目录，用插件扩展 Agent 能力。"
        ],
        "insights": [
            "<strong>国产开发者拿下 600+ 星/天：</strong>不是大厂项目，靠「本地优先 + 自带模型 + 无账号」三个承诺切入——叙事精准命中了企业最真实的顾虑。",
            "<strong>桌面端回潮：</strong>Agent 从浏览器插件回到桌面应用，因为真正的瓶颈是本地文件系统权限和长任务稳定性，不是交互花样。",
            "<strong>本质是数据主权的争夺：</strong>云端 Agent 卖的是省事，本地 Agent 卖的是安全——当企业开始为「代码不出内网」付费，这条赛道就再也没有天花板。"
        ],
        "tags": ["coding-agent", "desktop", "electron", "local-first", "rust"]
    },
    {
        "rank": 10,
        "owner": "diegosouzapw",
        "name": "OmniRoute",
        "fullName": "diegosouzapw / OmniRoute",
        "org": "diegosouzapw",
        "url": "https://github.com/diegosouzapw/OmniRoute",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "63,866",
        "forks": "8,948",
        "starsToday": "591",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +591★！63.9K★ 第五次上榜，一个半月涨 40K★！免费 MIT 的 AI 网关：一个端点接入 352 家供应商（150+ 免费）、1200+ 模型，额度用完自动切换。",
        "problems": [
            "<strong>多供应商管理地狱：</strong>Claude、GPT、Gemini、Kimi 各一套 Key 与额度，切换全靠手工。",
            "<strong>额度突然耗尽：</strong>写代码正到一半被限流，工作流直接中断。",
            "<strong>工具各自为政：</strong>Claude Code、Cursor、Cline 需要分别配置，无法共享同一路由。"
        ],
        "usage": [
            "启动网关：<pre><code>npx omniroute</code></pre>",
            "把 Claude Code / Codex / Cursor 指向同一端点。",
            "开启自动降级与压缩：额度告急自动换供应商，token 省 15%-95%。"
        ],
        "insights": [
            "<strong>从 23.6K★ 到 63.9K★：</strong>7-22 四登时 23,570★，七周涨 40K★——「免费多供应商路由」的刚需程度远超预期。",
            "<strong>与 llmfit 同日登榜不是巧合：</strong>一个解决「用哪家模型」，一个解决「本地跑得动哪个」——模型供给侧爆炸后，选择成本成了新瓶颈。",
            "<strong>本质是中间层的价值套利：</strong>上游免费额度与下游付费意愿之间的差价，就是网关的生意——它不生产智能，只搬运额度，却卡住了所有人必经的关口。"
        ],
        "tags": ["ai-gateway", "llm", "proxy", "mcp", "fallback"]
    },
    {
        "rank": 11,
        "owner": "alsk1992",
        "name": "CloddsBot",
        "fullName": "alsk1992 / CloddsBot",
        "org": "alsk1992",
        "url": "https://github.com/alsk1992/CloddsBot",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "1,361",
        "forks": "240",
        "starsToday": "299",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +299★！首登！能自己睡觉赚钱的 AI 交易智能体——覆盖 Polymarket、Kalshi、币安、Hyperliquid 等 1000+ 市场，扫描价差、自动下单、自己管风险。",
        "problems": [
            "<strong>人工盯盘不可行：</strong>预测市场与加密市场 7×24 运转，人不可能全天候扫价差。",
            "<strong>机会稍纵即逝：</strong>跨市场套利窗口常以秒计，手动操作永远慢一步。",
            "<strong>情绪化交易：</strong>人类会在亏损时加仓、盈利时恐慌离场，纪律性天然不足。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g clodds</code></pre>",
            "配置交易所 API Key 与风控参数后自托管运行。",
            "Agent 自主扫描市场、执行交易、管理仓位风险。"
        ],
        "insights": [
            "<strong>「Agent + 金融」的小体量高声量：</strong>1,361★ 却拿到 299★/天，说明日榜不只看体量，还看叙事密度——「让 AI 替你睡觉时赚钱」天生自带传播力。",
            "<strong>全套 Agent 经济三件套：</strong>GitHub 仓库 + 自建网站 + 代币合约地址，代码只是入口，代币才是商业模型——开源在此已变成一种获客工具。",
            "<strong>本质是风险的转移而非消除：</strong>它把人的情绪风险换成了模型与合约的技术风险，亏损速度可以比人工更快——自主金融 Agent 真正的考题不是收益率，而是谁敢给它钱。"
        ],
        "tags": ["trading", "agent", "crypto", "prediction-markets", "claude"]
    },
    {
        "rank": 12,
        "owner": "AlexsJones",
        "name": "llmfit",
        "fullName": "AlexsJones / llmfit",
        "org": "AlexsJones",
        "url": "https://github.com/AlexsJones/llmfit",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "35,539",
        "forks": "2,258",
        "starsToday": "247",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +247★！35.5K★ 首登！一条命令告诉你「本机跑得动哪个模型」——扫遍数百模型与供应商，匹配你的显存、内存与推理后端。",
        "problems": [
            "<strong>硬件与模型匹配靠猜：</strong>下载 40GB 模型才发现显存不够，白等一整天。",
            "<strong>量化格式选择困难：</strong>GGUF、MLX、不同量化等级各有取舍，新手完全无从下手。",
            "<strong>供应商太多挑花眼：</strong>本地跑还是调 API、哪家更划算，缺少统一对比。"
        ],
        "usage": [
            "安装：<pre><code>cargo install llmfit</code></pre>",
            "检测本机：<pre><code>llmfit</code></pre>",
            "按推荐结果选择量化等级与推理后端。"
        ],
        "insights": [
            "<strong>35.5K★ 首登的「工具型爆款」：</strong>二月建仓、九月上榜——不是模型、不是应用，只是一条匹配命令，却解决了本地 AI 最痛的第一公里。",
            "<strong>与 OmniRoute 构成供给侧的左右手：</strong>云端选路由、本地选拟合——模型数量爆炸后，真正的瓶颈已从「有没有模型」变成「该用哪个」。",
            "<strong>本质是选择权的生意：</strong>当可选项超出人能评估的范围，帮人做选择本身就成了最值钱的环节——AI 时代最稳的生意，往往不在生成侧，而在决策侧。"
        ],
        "tags": ["local-llm", "hardware", "gguf", "rust", "mlx"]
    }
]

# Shift labels for 2-day gap (accurate offset: +2)
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
    "date": "2026-09-10",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-10'
data['topic'] = '🔥 <strong>ADHD 输出技能两天暴涨 8.3K★登顶 + 间谍卫星模拟器 11 天星数翻倍 + 腾讯官方 teamai-cli 首登 + 清华多智能体课堂三登 + superpowers 十四登</strong> —— ayghri/i-have-adhd（+3,854★）36.8K★ 冲上日榜第一，让 Agent 别再铺垫废话。bilawalsidhu/gods-eye-view（+1,588★）22.5K★ 时隔 11 天回归，真实开源数据的浏览器版「间谍卫星」。cathrynlavery/diagram-design（+1,287★）37.3K★ 五登，编辑级图表规范翻倍。freestylefly/awesome-gpt-image-2（+957★）30.6K★ 六登，530+ 案例库。liquidslr/system-design-notes（+891★）18.5K★ 首登，29 章系统设计面试笔记。Tencent/teamai-cli（+837★）腾讯官方团队 AI 配置管理器首登。THU-MAIC/OpenMAIC（+806★）35.0K★ 清华多智能体课堂三登。obra/superpowers（+731★）284K★ 十四登。vastsa/PI-Desktop（+636★）本地优先编码 Agent 桌面端首登。diegosouzapw/OmniRoute（+591★）63.9K★ 七周涨 40K★。alsk1992/CloddsBot（+299★）自主交易 Agent 首登。AlexsJones/llmfit（+247★）35.5K★ 本地模型匹配工具首登。两天 gap 后回归——今日榜单的共性极其清晰：Agent 生态的外围设施（技能规范、配置治理、模型路由、硬件匹配）全面压过模型本身，行业叙事已从「谁的模型更强」转向「谁的工程体系更完整」。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:5]]}")

# Verify badge present on every project
assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
