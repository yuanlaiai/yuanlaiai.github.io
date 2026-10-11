#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-11 (2-day gap, 无昨日榜→平铺结构, 13 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 11)
gap_days = (today - last).days  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（2天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "morluto",
        "name": "rea",
        "fullName": "morluto / rea",
        "org": "morluto",
        "url": "https://github.com/morluto/rea",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "73,222",
        "forks": "15,449",
        "starsToday": "25,793",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +25,793★ 继续碾压全场，两天从 2.49万★ 冲到 7.32万★！用 Agent 做逆向工程：从应用行为一路下探到原生二进制。它把「看懂一个黑盒程序」拆成 Agent 能一步步执行的流程。两天涨将近 5 万星，是最近榜单上最陡的一条曲线。",
        "problems": [
            "<strong>逆向工程门槛极高：</strong>拆一个二进制要懂反汇编、调试器、调用约定，能上手的人本来就少。",
            "<strong>工具链割裂：</strong>行为观察、网络抓包、二进制分析分散在不同工具里，各自的结论很难串成一条线。",
            "<strong>黑盒只会越来越多：</strong>闭源 App、混淆代码、逻辑后移到服务端，纯静态分析看不到全貌。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/morluto/rea.git</code></pre>",
            "指向目标应用或二进制，让 Agent 从行为层开始观察，再逐层下探到实现层。",
            "产出结构化的逆向结论，可交给后续的自动化流程使用。"
        ],
        "insights": [
            "<strong>两天 +48,347★ 不是噪声：</strong>从 2.49万 到 7.32万，一天多的时间翻近三倍。这种斜率通常只出现在「某个专业门槛被工具直接抹平」的时候，而不是又一次框架炒作。",
            "<strong>它和 AnyPS5、raddebugger 连成了一条线：</strong>连续几天榜单上都有二进制层的工具，指向同一件事——写新代码越来越便宜，读懂已有的机器码越来越贵。",
            "<strong>本质是逆向从手艺变成流程：</strong>过去靠一个人的经验和直觉，现在被拆成 Agent 能执行的步骤。手艺一旦能流程化，它的稀缺性就从「谁会」转移到「谁能定义问题」。"
        ],
        "tags": ["reverse-engineering", "ai-agent", "typescript", "binary-analysis", "developer-tools"]
    },
    {
        "rank": 2,
        "owner": "boykopovar",
        "name": "AnyPS5",
        "fullName": "boykopovar / AnyPS5",
        "org": "boykopovar",
        "url": "https://github.com/boykopovar/AnyPS5",
        "lang": "C++",
        "langClass": "cpp",
        "stars": "26,928",
        "forks": "2,265",
        "starsToday": "5,805",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +5,805★ 连续两天天增破五千！两天从 1.52万★ 涨到 2.69万★。把 PS5 的可执行文件自动移植到 Linux 和 Windows——主机二进制被锁在定制系统和专有运行时里，这个项目想把它「翻译」成通用平台能跑的代码。",
        "problems": [
            "<strong>主机程序被平台锁死：</strong>PS5 跑在定制 FreeBSD 加专有运行时上，换平台几乎等于从零重写。",
            "<strong>手动移植成本吓人：</strong>系统调用、图形 API、内存模型处处不一样，一个项目几个月起步。",
            "<strong>整机模拟太慢：</strong>模拟器能跑但性能损耗大，不如把二进制转换成目标平台的原生代码。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/boykopovar/AnyPS5.git</code></pre>",
            "准备目标平台的构建环境（Linux / Windows），按文档编译工具本身。",
            "输入 PS5 可执行文件，得到可在目标平台运行的程序；实际支持范围要看 README 的兼容清单。"
        ],
        "insights": [
            "<strong>它踩在最敏感的地带：</strong>主机二进制移植天然贴着版权与厂商政策的边线，热度能起来，能不能长期存在取决于法律而不是技术——追它的人得先把这一点看清楚。",
            "<strong>日增连续两天破五千：</strong>说明这不是一波流量的意外，而是有人真的在用它干活。移植工具的价值和「有多少现成资产想换平台跑」直接挂钩。",
            "<strong>本质是把封闭生态的价值重新释放：</strong>主机靠独占生态卖硬件，移植工具在拆这道墙——它服务的是「我买过的东西为什么不能在别的机器上跑」这个长期怨气。"
        ],
        "tags": ["ps5", "porting", "binary-translation", "cpp", "homebrew"]
    },
    {
        "rank": 3,
        "owner": "storytold",
        "name": "artcraft",
        "fullName": "storytold / artcraft",
        "org": "storytold",
        "url": "https://github.com/storytold/artcraft",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "14,552",
        "forks": "2,299",
        "starsToday": "3,222",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,222★ 连续两天日增过三千！两天从 7,648★ 涨到 1.46万★。一个用 Rust 写的创作引擎，作者给它的定位是 intentional crafting engine（刻意、有意图的创作引擎），面向艺术家、设计师和电影人。重点放在「创作过程可控」，而不是「一句话生成」。",
        "problems": [
            "<strong>生成式工具让人失控：</strong>输入提示词出一张图，构图、细节、风格都不可精确控制，改一处动全身。",
            "<strong>创作意图没有落点：</strong>从草图到成品之间缺一层工具，现有的要么太底层（三维软件），要么太黑箱（文生图）。",
            "<strong>多工种工具不通：</strong>艺术家、设计师、导演各自用一套软件，资产在图与模型之间来回丢。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/storytold/artcraft.git</code></pre>",
            "用 Rust 工具链构建：<pre><code>cargo build --release</code></pre>",
            "按文档导入资产、搭建场景，导出给后续制作流程使用。"
        ],
        "insights": [
            "<strong>连续两天日增三千：</strong>一个还没到两万星的 Rust 项目能有这种持续性，说明「可控创作」这批人不是围观者，是掏钱掏时间的一方。",
            "<strong>「intentional」是今天最值钱的一个词：</strong>生成式 AI 把出图成本压到接近零之后，一批工具开始反着做——不卖「一句话生成」，卖「每一步都可控」。生成越免费，可控越贵。",
            "<strong>本质是创意工具在分路线：</strong>效率派押 AI 生成，掌控派押精确工具，ArtCraft 选后者——它赌的是专业创作者不会把最终控制权交出去。"
        ],
        "tags": ["creative-tools", "rust", "art", "design", "rendering"]
    },
    {
        "rank": 4,
        "owner": "mattpocock",
        "name": "skills",
        "fullName": "mattpocock / skills",
        "org": "mattpocock",
        "url": "https://github.com/mattpocock/skills",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "284,526",
        "forks": "23,814",
        "starsToday": "1,736",
        "count": 10,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,736★！28.45万★ 第10次登榜，成了榜单上第一个上双位数的项目。Matt Pocock 把自己 .agents 目录里的技能直接开源出来，仓库说明只有一句：给真正的工程师用的技能。",
        "problems": [
            "<strong>Agent 技能全靠自己攒：</strong>每个人从零写自己的提示词和技能，重复造轮子，还造得不好。",
            "<strong>公开技能良莠不齐：</strong>大部分是演示品，看着漂亮，真干活时用不上。",
            "<strong>不知道信谁的：</strong>技能满天飞，缺一个能判断「这套靠不靠谱」的可信来源。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/mattpocock/skills.git</code></pre>",
            "把需要的技能目录拷进你自己的 .agents / skills 目录。",
            "在 Claude Code、Codex 等支持技能的工具里直接调用。"
        ],
        "insights": [
            "<strong>第10次登榜，第一个上双位数：</strong>从 5 月的 7.6 万星到今天 28.4 万星，半年涨了近四倍。技能库早已不是尝鲜品类，而是基础设施。",
            "<strong>卖点是署名，不是功能：</strong>描述里那句「straight from my .agents directory」（直接来自我的 .agents 目录）才是关键——技能不缺，缺的是「这个人写的」。",
            "<strong>本质是 Agent 生态在走开源的老路：</strong>从个人配置变成公开技能库，很像十几年前 dotfiles 流行的那一阵——工具越强，个人配置越会变成一种可分享、可 star 的资产。"
        ],
        "tags": ["agent-skills", "shell", "dotfiles", "developer-tools", "ai-agent"]
    },
    {
        "rank": 5,
        "owner": "cathrynlavery",
        "name": "diagram-design",
        "fullName": "cathrynlavery / diagram-design",
        "org": "cathrynlavery",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "lang": "HTML",
        "langClass": "html",
        "stars": "48,977",
        "forks": "3,095",
        "starsToday": "1,190",
        "count": 7,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,190★！4.90万★ 第7次登榜（两天前 4.62万★）。给编码 Agent 用的图表设计技能，这次有两处更新：图表类型从 42 种加到 44 种，兼容名单新增 Cursor。仓库说明还是那两句硬话——不要阴影，不要 Mermaid 那种糊弄。",
        "problems": [
            "<strong>Agent 默认产出的图见不得人：</strong>流程图千篇一律、配色难看，放进正式文档一眼就露怯。",
            "<strong>样式改不动：</strong>想调一个图表的配色或排版，只能改提示词碰运气，试十次不一定对一次。",
            "<strong>导出不自由：</strong>很多图表依赖渲染服务，想嵌进自己的文档或网页得绕一大圈。"
        ],
        "usage": [
            "把技能装进 Claude Code / Codex / GitHub Copilot / Cursor / Factory Droid / Pi。",
            "用自然语言说清图表需求，从 44 种类型里选一种。",
            "得到自包含的 HTML 加 SVG，可直接嵌进文档或网页，不依赖外部渲染。"
        ],
        "insights": [
            "<strong>连续三次更新都在扩品种和扩平台：</strong>42→44 种图表、兼容名单新增 Cursor——作者在做的不是加功能，是把这个技能焊进更多人的默认工作流。",
            "<strong>第7次登榜：</strong>它已经过了「被发现的阶段」，现在的每一次上榜更像老客户的续费。回榜是习惯，不是新闻。",
            "<strong>「No Mermaid slop」是一句定位宣言：</strong>在 Agent 什么都能生成的时代，「生成得好看且可控」本身成了生意——它卖的其实不是功能，是审美。"
        ],
        "tags": ["diagram", "svg", "agent-skill", "design", "documentation"]
    },
    {
        "rank": 6,
        "owner": "anthropics",
        "name": "knowledge-work-plugins",
        "fullName": "anthropics / knowledge-work-plugins",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/knowledge-work-plugins",
        "lang": "Python",
        "langClass": "py",
        "stars": "28,830",
        "forks": "3,277",
        "starsToday": "625",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +625★！2.88万★ 第5次登榜（两天前 2.75万★）。Anthropic 官方开源、面向知识工作者的插件库，主要装在 Claude Cowork 里用。方向很清楚：把 Claude 从「陪你聊天」变成「在你的日常工作里替你干活」。",
        "problems": [
            "<strong>知识工作散落在工具里：</strong>邮件、文档、表格、会议纪要，Agent 一样都够不着。",
            "<strong>插件格式没标准：</strong>各家 Agent 的插件互不兼容，写一个只能给一个平台用。",
            "<strong>企业想用又不敢用：</strong>缺官方背书的插件，安全与合规没有底，落地时推不动。"
        ],
        "usage": [
            "从仓库取出需要的插件，装进 Claude Cowork。",
            "按具体场景（文档处理、研究、协作）挑对应插件。",
            "官方维护，跟 Claude 的版本一起更新。"
        ],
        "insights": [
            "<strong>两天涨 1,355★，日增还翻了一倍多：</strong>官方插件库的走势比个人项目稳得多，这是生态在成熟的信号——厂商开始下场定义「插件长什么样」。",
            "<strong>关键词是 Cowork，不是 Code：</strong>Anthropic 的注意力正从「给开发者的编码」扩到「给知识工作者的日常」——后者人群大得多，也是和 OpenAI 正面撞上的战场。",
            "<strong>本质是 Agent 的入口之争：</strong>谁定了插件格式，谁就定了用户在哪儿调用 Agent。插件库是平台把触角伸进别人日常工作流的方式。"
        ],
        "tags": ["plugins", "anthropic", "knowledge-work", "claude", "productivity"]
    },
    {
        "rank": 7,
        "owner": "hugohe3",
        "name": "ppt-master",
        "fullName": "hugohe3 / ppt-master",
        "org": "hugohe3",
        "url": "https://github.com/hugohe3/ppt-master",
        "lang": "Python",
        "langClass": "py",
        "stars": "59,476",
        "forks": "4,687",
        "starsToday": "461",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +461★！5.95万★ 第2次登榜（8 月中首登时 4.55万★）。AI 把文档或题目变成真正的原生 PowerPoint：原生形状、转场与动画、按需生成的数据图表和表格、用讲者备注生成语音旁白，还支持套用你自己的 .pptx 模板。",
        "problems": [
            "<strong>AI 生成的 PPT 是图片：</strong>很多工具导出的幻灯片其实是截图，点进去一个字都改不了。",
            "<strong>公司模板套不进去：</strong>企业有自己的 pptx 模板和字号规范，通用工具生成的东西用不了。",
            "<strong>图表和旁白要另做：</strong>数据图和讲稿还得手工补，AI 只完成了封面和标题页。"
        ],
        "usage": [
            "按 README 安装（Python 项目）。",
            "给它一份文档或一个主题，指定你自己的 .pptx 模板。",
            "产出可以直接继续编辑的原生 pptx，图表与旁白按需生成。"
        ],
        "insights": [
            "<strong>关键两个字是「原生」：</strong>市面上多数 AI PPT 工具交出来的是不可编辑的图片，它交出来的是真实的 pptx 形状、转场和动画——能不能二次编辑，才是职场人真正的门槛。",
            "<strong>第2次上榜涨了 1.4 万星：</strong>PPT 看着是个小场景，但它是知识工作者每周都要碰的高频痛点，高频本身就值得一个专用工具。",
            "<strong>本质是 AI 办公的竞争换了赛点：</strong>从「能不能生成」进入「生成的东西能不能直接用」——输出格式的可用性，正在取代生成质量成为决定成败的那一环。"
        ],
        "tags": ["powerpoint", "pptx", "productivity", "python", "office"]
    },
    {
        "rank": 8,
        "owner": "multica-ai",
        "name": "andrej-karpathy-skills",
        "fullName": "multica-ai / andrej-karpathy-skills",
        "org": "multica-ai",
        "url": "https://github.com/multica-ai/andrej-karpathy-skills",
        "lang": "",
        "langClass": "",
        "stars": "218,289",
        "forks": "21,982",
        "starsToday": "278",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +278★！21.8万★ 第5次登榜（8 月底 20.7万★）。整个仓库的核心是一个 CLAUDE.md 文件，用来纠正 Claude Code 的行为，内容提炼自 Andrej Karpathy 对 LLM 编码常见毛病的观察——把一个人的判断力固化成了模型能直接读的规则。",
        "problems": [
            "<strong>Agent 编码有系统性坏习惯：</strong>过度自信、爱改无关代码、不验证就下结论。",
            "<strong>每次都要重新调教：</strong>没有一份可以复用的行为准则，换个项目从头来过。",
            "<strong>权威声音缺位：</strong>网上提示词满天飞，但没人背书，不知道听谁的。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/multica-ai/andrej-karpathy-skills.git</code></pre>",
            "把 CLAUDE.md 放进你的项目根目录。",
            "Claude Code 会自动读取它，行为随之改变，不用改任何代码。"
        ],
        "insights": [
            "<strong>一个文件 21.8 万星：</strong>价值不在代码行数，在于它把 Karpathy 对 LLM 编码毛病的判断固化成了可执行规则——人再厉害，也很难每次都在场，但一份文件可以。",
            "<strong>第5次登榜：</strong>从 8 月的 20.7 万到今天 21.8 万，涨得慢但一直在榜上——说明「权威人物的经验文件」是长期需求，不是一时的跟风。",
            "<strong>本质是最佳实践的载体换了：</strong>Agent 时代的「最佳实践」不再写成博客或书，而是写成模型能直接读的文件——知识的形态正在从「给人看」变成「给模型读」。"
        ],
        "tags": ["claude-code", "prompt-engineering", "best-practices", "ai-agent", "markdown"]
    },
    {
        "rank": 9,
        "owner": "mksglu",
        "name": "context-mode",
        "fullName": "mksglu / context-mode",
        "org": "mksglu",
        "url": "https://github.com/mksglu/context-mode",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "26,325",
        "forks": "1,894",
        "starsToday": "178",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +178★！2.63万★ 第2次登榜（9 月初首登时 2.12万★）。给 AI 编码 Agent 做上下文窗口优化：把工具的原始输出关进沙箱（官方说削减 98%），持久化会话记忆，再通过 MCP + hooks 在 17 个平台上做路由。",
        "problems": [
            "<strong>上下文窗口被工具输出撑爆：</strong>一条命令的原始输出几千 token，真正的任务信息反被挤出去。",
            "<strong>会话记忆留不住：</strong>新会话开始，上一轮的中间结果全丢。",
            "<strong>平台各搞一套：</strong>换个 Agent 工具，之前调好的上下文策略就作废。"
        ],
        "usage": [
            "按 README 安装（TypeScript 项目，走 MCP + hooks 接入）。",
            "让它接管工具输出，在沙箱里裁剪后再交给模型。",
            "在支持的 17 个平台上启用统一的路由与记忆策略。"
        ],
        "insights": [
            "<strong>98% 这个数字才是卖点：</strong>上下文窗口再大也是有限资源，把工具输出砍掉 98% 等于给每个会话多留出十几倍的有效空间——省的是 token，用的是注意力。",
            "<strong>它和昨天的 claude-mem 是一类：</strong>都在给 Agent 补「上下文管理」这一层。一个做记忆持久化，一个做窗口压缩，两条路都在绕开模型的硬限制。",
            "<strong>本质是上下文窗口成了新的稀缺资源：</strong>围绕它的压缩、裁剪、持久化正在长成一个独立品类——谁能让同样的窗口装下更多有效信息，谁就替用户省了钱。"
        ],
        "tags": ["context-window", "mcp", "ai-agent", "typescript", "token-optimization"]
    },
    {
        "rank": 10,
        "owner": "huggingface",
        "name": "transformers",
        "fullName": "huggingface / transformers",
        "org": "Hugging Face",
        "url": "https://github.com/huggingface/transformers",
        "lang": "Python",
        "langClass": "py",
        "stars": "167,270",
        "forks": "34,797",
        "starsToday": "96",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +96★ 首次登榜！16.7万★。🤗 Transformers：定义模型的开源框架，覆盖文本、视觉、音频和多模态，推理与训练都能用。它是过去几年几乎所有开源模型「被加载一次」的必经之路，今天和 pytorch、tensorflow、flutter 一起挤进榜单。",
        "problems": [
            "<strong>模型生态碎片化：</strong>每冒出一个新模型就带一套自己的加载代码，集成成本全压在用户身上。",
            "<strong>训练与推理接口不统一：</strong>同一个模型，跑推理一套写法，做微调又一套。",
            "<strong>前沿落地要等适配：</strong>论文放出来的模型，得等有人写好集成才能用上。"
        ],
        "usage": [
            "安装：<pre><code>pip install transformers</code></pre>",
            "用 AutoModel / AutoTokenizer 加载任意受支持的模型，不必关心底层实现。",
            "同一套接口既能做推理，也能接着训练或微调。"
        ],
        "insights": [
            "<strong>它今天上榜本身就是个信号：</strong>连着几周都是 Agent 工具在刷屏，四个基础框架同一天挤进来，往往是新一轮模型发布或算力事件的前兆——应用越热闹，越有人回头检查地基。",
            "<strong>全生态的公共接口：</strong>它的价值不在跑分，在于是绝大多数开源模型「被加载一次」的必经之路。谁定义了「怎么加载一个模型」，谁就拿走了所有模型的第一入口。",
            "<strong>本质是越热闹的应用层越依赖沉默的底座：</strong>它不生产新闻，但所有新闻都跑在它上面——这类项目的上榜，测的是整个行业的体温。"
        ],
        "tags": ["transformers", "huggingface", "nlp", "framework", "infrastructure"]
    },
    {
        "rank": 11,
        "owner": "flutter",
        "name": "flutter",
        "fullName": "flutter / flutter",
        "org": "Flutter",
        "url": "https://github.com/flutter/flutter",
        "lang": "Dart",
        "langClass": "dart",
        "stars": "179,529",
        "forks": "33,601",
        "starsToday": "88",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +88★ 首次登榜！17.95万★。Flutter：一套代码构建移动端与更多平台的界面框架，Google 出品。它今天出现在一张被 AI 工具占满的榜单上，本身就值得说一句——传统工程基础设施正在重新挤回视线。",
        "problems": [
            "<strong>跨平台要写多套界面：</strong>iOS、Android、Web、桌面各维护一份 UI，人力翻倍。",
            "<strong>体验与效率难两全：</strong>用 Web 技术省事但手感差，用原生手感好但成本高。",
            "<strong>新平台适配慢：</strong>设备形态一变，原有代码就要大改。"
        ],
        "usage": [
            "安装 Flutter SDK，配置对应平台工具链。",
            "新建项目：<pre><code>flutter create myapp</code></pre>",
            "一套代码编译到 iOS / Android / Web / 桌面，热重载边改边看。"
        ],
        "insights": [
            "<strong>它挤进一张 AI 榜单，是今天最反差的画面：</strong>前十里九个都是 Agent 工具，第十一个是十年前那套「一次编写，到处运行」——热点的轮换和地基的存在感，在同一天被摆到了一起。",
            "<strong>Flutter 这些年真正赢下的是工程效率：</strong>它没做 AI，也没做新概念，靠的就是把跨平台 UI 的开发成本压下来，成为很多人默认的选择。",
            "<strong>本质是基建从不出局，只是不时髦：</strong>今天它上榜不是因为发生了什么，而是因为 AI 的热闹需要有人提醒——所有炫目的上层，最后都要落在这样的框架上。"
        ],
        "tags": ["flutter", "dart", "cross-platform", "mobile", "ui"]
    },
    {
        "rank": 12,
        "owner": "pytorch",
        "name": "pytorch",
        "fullName": "pytorch / pytorch",
        "org": "PyTorch",
        "url": "https://github.com/pytorch/pytorch",
        "lang": "Python",
        "langClass": "py",
        "stars": "104,146",
        "forks": "31,956",
        "starsToday": "84",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +84★ 首次登榜！10.4万★。PyTorch：带强 GPU 加速的张量与动态神经网络框架。它是过去几年几乎每一个新模型出生时用的第一套工具，今天和 tensorflow、transformers 一起回到榜单上。",
        "problems": [
            "<strong>研究代码与生产代码脱节：</strong>论文里的实现跑得通，推到线上要重写一遍。",
            "<strong>框架迁移成本高：</strong>换一套训练框架，模型和流程都要跟着改。",
            "<strong>底层出错难定位：</strong>张量维度、显存、并行策略出问题，报错信息不友好。"
        ],
        "usage": [
            "安装：<pre><code>pip install torch</code></pre>",
            "用 Tensor 与自动求导搭网络，动态图写法和普通 Python 一样。",
            "单卡到多卡训练用同一套 API，可导出到部署格式。"
        ],
        "insights": [
            "<strong>研究界的事实标准：</strong>大多数公开模型的第一份实现都是 PyTorch 写的，这个习惯性选择本身就是它最难撼动的地方——不是功能领先，是路径依赖足够深。",
            "<strong>它和 tensorflow、transformers 同日上榜：</strong>三件套一起出现很少见，通常意味着行业在某个节点上集体回顾底座，而不是又出了个新玩具。",
            "<strong>本质是底座之争早已结束：</strong>前几年还在比框架优劣，现在没人讨论了——胜负已分，剩下的工作是让后来者沿着这条路继续走。"
        ],
        "tags": ["pytorch", "deep-learning", "python", "gpu", "framework"]
    },
    {
        "rank": 13,
        "owner": "tensorflow",
        "name": "tensorflow",
        "fullName": "tensorflow / tensorflow",
        "org": "TensorFlow",
        "url": "https://github.com/tensorflow/tensorflow",
        "lang": "C++",
        "langClass": "cpp",
        "stars": "200,729",
        "forks": "78,965",
        "starsToday": "26",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +26★ 首次登榜！20.07万★，全榜星数最高的项目。TensorFlow：面向所有人的开源机器学习框架，Google 出品。日增只有两位数，它上榜靠的不是热度，而是这个量级的项目一出现，就说明有人在重新翻地基。",
        "problems": [
            "<strong>从研究到生产的断层：</strong>训练出来容易，部署到端侧、服务端要另起一套工程。",
            "<strong>门槛偏高：</strong>图执行、分布式、服务化，概念多，新人上手慢。",
            "<strong>生态分流：</strong>新模型大多首发在别的框架上，迁移过来总有落差。"
        ],
        "usage": [
            "安装：<pre><code>pip install tensorflow</code></pre>",
            "用 Keras 高层接口快速搭模型，也能下沉到自定义算子。",
            "训练完可导出到端侧、服务端的多条部署链路。"
        ],
        "insights": [
            "<strong>日增 26★ 却排进榜单：</strong>这说明它的上榜和热度无关，和体量有关——一个 20 万星的项目哪怕只涨几十星，也足够在趋势里冒头。",
            "<strong>它是这一波「底座回归」里最沉默的一个：</strong>当年和 PyTorch 打得难解难分，如今讨论度让位，但生产环境的存量依旧巨大——这就是它还没消失的原因。",
            "<strong>本质是技术口碑和实际存量是两回事：</strong>舆论场上的输赢很快，企业里跑着的代码很慢——谁在场更久，谁就活得更久。"
        ],
        "tags": ["tensorflow", "machine-learning", "cpp", "google", "framework"]
    }
]

# 按日增降序规整编号（平铺渲染，全部新面孔）
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

today_projects = sorted(today_projects, key=lambda p: -_today(p))
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels for the real gap
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

new_day = {
    "date": "2026-10-11",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-11'
data['topic'] = '🔥 <strong>逆向工程 Agent 两天翻三倍 + Agent 上下文中间层集体霸榜 + 四大基础框架同日回归</strong> —— morluto/rea（+25,793★）第二天继续碾压全场，两天从 2.49万★ 冲到 7.32万★，Agent 驱动的逆向工程把「看懂黑盒程序」变成了可执行流程；boykopovar/AnyPS5（+5,805★）涨到 2.69万★、storytold/artcraft（+3,222★）涨到 1.46万★，二进制工具与可控创作这条线继续放大。Agent 的中间层在同一天集体登榜：mattpocock/skills（+1,736★）第10次成为首个上双位数的项目、cathrynlavery/diagram-design（+1,190★）第7次（图表类型 42→44 并新增 Cursor）、anthropics/knowledge-work-plugins（+625★）第5次、multica-ai/andrej-karpathy-skills（+278★）第5次、mksglu/context-mode（+178★）把工具输出砍掉 98% 并跨 17 个平台路由——技能、记忆、上下文三条线都在被单独产品化。hugohe3/ppt-master（+461★）输出可直接编辑的原生 pptx。最意外的是四个几乎从不露面的底座同日上榜：huggingface/transformers（+96★）、flutter/flutter（+88★）、pytorch/pytorch（+84★）、tensorflow/tensorflow（+26★）。今日三条主线：一、逆向与二进制工具继续爆发，看懂存量代码是本季最贵的技能；二、Agent 的技能、记忆、上下文被拆成独立品类，谁压低 token 谁得利；三、基础框架集体回归，热点换了一轮，地基没换。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★ count={p['count']}")
