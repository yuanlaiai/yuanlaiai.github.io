#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-15 (4-day gap, 无昨日榜→平铺结构, 12 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 15)
gap_days = (today - last).days  # 4
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（4天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "morluto",
        "name": "rea",
        "fullName": "morluto / rea",
        "org": "morluto",
        "url": "https://github.com/morluto/rea",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "259,298",
        "forks": "65,209",
        "starsToday": "32,282",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +32,282★ 连续第三次登榜，4 天从 7.32万★ 一路飙到 25.93万★！用 Agent 做逆向工程：从应用行为一路下探到原生二进制。这是最近榜单上最不讲道理的一条曲线，单日再破三万。",
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
            "<strong>四天涨 18.6 万星：</strong>从 7.32万 到 25.93万，这个斜率已经超出了正常项目的传播曲线。当一个专业门槛被工具直接抹平，围观的人会远多于真正用它的人——热度里有多少是真需求，得等潮水退了才知道。",
            "<strong>它和 ghidra 同一天上榜：</strong>一个是刚出炉的 Agent 工具，一个是 NSA 沉淀了二十年的逆向框架。逆向这件事同时喂饱了新旧两种解法，说明需求不是被创造出来的，是一直在。",
            "<strong>本质是存量世界的焦虑：</strong>新代码越来越多，但真正跑在生产里的是旧代码——能看懂别人怎么写的人，正在变成最稀缺的那一类。"
        ],
        "tags": ["reverse-engineering", "ai-agent", "typescript", "binary-analysis", "developer-tools"]
    },
    {
        "rank": 2,
        "owner": "debpalash",
        "name": "VoiceStudio",
        "fullName": "debpalash / VoiceStudio",
        "org": "debpalash",
        "url": "https://github.com/debpalash/VoiceStudio",
        "lang": "Python",
        "langClass": "py",
        "stars": "67,971",
        "forks": "7,449",
        "starsToday": "3,027",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,027★ 冲到日增第二！6.80万★ 第3次登榜（9 月底 4.64万★）。完全本地跑的开源 ElevenLabs 替代：声音克隆、音色设计、视频配音、听写、转录、有声书制作，覆盖 646 种语言。",
        "problems": [
            "<strong>云端语音又贵又涉及隐私：</strong>按字计费的商业 API，把用户的音频传到别人的服务器上。",
            "<strong>多语言配音门槛高：</strong>小语种的专业配音员难找，价格也高。",
            "<strong>声音资产不受控：</strong>用云服务克隆出来的音色，什么时候下架由平台说了算。"
        ],
        "usage": [
            "按 README 安装（Python 项目，本地运行，建议有 GPU）。",
            "用一段样本做声音克隆或音色设计。",
            "用于视频配音、转录、听写与有声书制作，全部在自己机器上完成。"
        ],
        "insights": [
            "<strong>本地替代云服务的又一次胜利：</strong>ElevenLabs 是闭源云 API，VoiceStudio 把同样的能力搬回自己机器——隐私和成本这两个驱动力从来不会过时。",
            "<strong>646 种语言这个数字值得琢磨：</strong>语音是多语言世界里最后被 AI 攻下的模态之一，而一旦本地模型能覆盖几百种语言，小语种内容的生产成本第一次和大语种拉平。",
            "<strong>本质是能力自主成了默认诉求：</strong>从语音、索引到部署，同一批人反复为「东西跑在自己机器上」买单——他们要的不只是省钱，是拿回控制权。"
        ],
        "tags": ["voice", "tts", "local-first", "elevenlabs-alternative", "python"]
    },
    {
        "rank": 3,
        "owner": "NationalSecurityAgency",
        "name": "ghidra",
        "fullName": "NationalSecurityAgency / ghidra",
        "org": "NSA",
        "url": "https://github.com/NationalSecurityAgency/ghidra",
        "lang": "Java",
        "langClass": "java",
        "stars": "88,197",
        "forks": "9,839",
        "starsToday": "1,366",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,366★！8.82万★ 第5次登榜（9 月中 7.85万★）。美国国安局（NSA）开源的软件逆向工程框架，2019 年放出来之后一直是这个领域的免费标准，能反编译、能写脚本扩展，业内拿它替代昂贵的商业工具。",
        "problems": [
            "<strong>商业逆向工具太贵：</strong>专业反汇编器一套授权费不菲，个人和小团队用不起。",
            "<strong>大二进制分析吃力：</strong>现代程序动辄几百 MB，反编译后人和工具都容易迷路。",
            "<strong>扩展门槛高：</strong>想按自己的需求写插件，得先啃透一整套框架。"
        ],
        "usage": [
            "从 Releases 下载，或用 JDK 自行构建。",
            "导入目标二进制，让反编译器还原出接近源码的逻辑。",
            "用 Java 或 Python 脚本扩展分析流程，批量处理任务。"
        ],
        "insights": [
            "<strong>NSA 把工具开源，本身是逆向圈的一次结构性变化：</strong>2019 年之前，这个领域靠昂贵的商业软件把持；一个政府机构把同类工具免费放出，直接改写了定价权。",
            "<strong>它和 rea 同榜：</strong>一个沉淀二十年、要人亲自上手，一个刚出炉、让 Agent 代劳。需求同时喂饱两种解法，说明「看懂程序」这件事的缺口一直在扩大。",
            "<strong>本质是封装越厚，拆解越值钱：</strong>软件越抽象、越闭源，能穿透封装看清底层的能力就越稀缺——所以一款老工具到今天还能稳定涨星。"
        ],
        "tags": ["reverse-engineering", "ghidra", "java", "security", "nsa"]
    },
    {
        "rank": 4,
        "owner": "K-Dense-AI",
        "name": "scientific-agent-skills",
        "fullName": "K-Dense-AI / scientific-agent-skills",
        "org": "K-Dense AI",
        "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "50,005",
        "forks": "4,459",
        "starsToday": "1,091",
        "count": 7,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,091★！5.00万★ 第7次登榜（8 月底 4.04万★）。把任何 AI Agent 变成「AI 科学家」：177 个现成技能加 100 多个科研数据库，覆盖生物、化学、医学和药物发现。作者称全球已有 25 万以上的科研人员在用，兼容 Cursor、Claude Code、Codex、Pi 以及开放的 Agent Skills 标准。",
        "problems": [
            "<strong>科研工具链琐碎：</strong>查序列、算结构、跑对接，每一步都在不同的站点和脚本之间跳。",
            "<strong>通用 Agent 不懂科研：</strong>直接让大模型做科学任务，术语和流程经常出错。",
            "<strong>专业数据库难用：</strong>上百个数据库接口各异，非本行的人摸不到门。"
        ],
        "usage": [
            "把技能库接进你正在用的 Agent（Cursor / Claude Code / Codex / Pi 等）。",
            "按研究方向挑技能与数据库，覆盖生物、化学、医学等。",
            "让 Agent 用专业工具链完成检索、分析与数据整理。"
        ],
        "insights": [
            "<strong>垂直技能库开始起量：</strong>通用技能（比如 mattpocock/skills）跑通之后，科学这种高门槛领域长出了专门的技能包——技能这件事正在从「通用提示词」细分成「学科工具链」。",
            "<strong>「25 万科研人员」是它的真正资产：</strong>技能本身可以被抄，但一个专业社群的背书抄不走。垂直技能库的壁垒不在代码，在谁在用它。",
            "<strong>本质是科研的门槛在换位置：</strong>过去卡在会不会写代码、会不会用工具，现在卡在能不能提出对的问题——工具链越完备，提问能力的权重就越高。"
        ],
        "tags": ["agent-skills", "science", "research", "bioinformatics", "python"]
    },
    {
        "rank": 5,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "279,903",
        "forks": "41,637",
        "starsToday": "1,015",
        "count": 11,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,015★！27.99万★ 第11次登榜（9 月中 26.33万★）。一套 Agent 运行环境的性能优化系统，管技能、管本能（instincts）、管记忆、管安全，主张研究先行的开发方式，支持 Claude Code、Codex、Opencode、Cursor 等。",
        "problems": [
            "<strong>Agent 干活效率不稳定：</strong>同样的模型，配置不同，产出质量差好几倍。",
            "<strong>能力散落各处：</strong>技能、记忆、安全策略各管各的，没有统一的调优层。",
            "<strong>换平台就重来：</strong>在一套工具里调好的配置，换个 Agent 就作废。"
        ],
        "usage": [
            "克隆仓库，按 README 接入你正在用的 Agent。",
            "按它的分层结构配置技能、记忆与安全策略。",
            "用研究先行的流程组织开发，让 Agent 在约束下工作。"
        ],
        "insights": [
            "<strong>第11次登榜、逼近 28 万星：</strong>「harness 优化」这个词本身很新，但它已经有近 28 万人在关注——Agent 的运行环境正在从「随便配配」变成一门正经的工程。",
            "<strong>它和 superpowers、ruflo 挤在同一张榜上：</strong>今天的榜单有一半是技能框架和 harness。模型是别人的，围绕模型那一圈的工程——技能、记忆、路由、安全——正被第三方抢着占。",
            "<strong>本质是模型之外的战场更拥挤：</strong>当底层模型的能力越来越接近，拉开差距的就不再有模型本身，而是谁把它调得更顺手、更可控、更省心。"
        ],
        "tags": ["agent-harness", "skills", "memory", "javascript", "developer-tools"]
    },
    {
        "rank": 6,
        "owner": "mksglu",
        "name": "context-mode",
        "fullName": "mksglu / context-mode",
        "org": "mksglu",
        "url": "https://github.com/mksglu/context-mode",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "29,591",
        "forks": "2,064",
        "starsToday": "902",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +902★ 日增比上次翻了五倍！2.96万★ 第3次登榜（4 天前 2.63万★）。给 AI 编码 Agent 做上下文窗口优化：把工具的原始输出关进沙箱（官方说削减 98%），持久化会话记忆，再通过 MCP + hooks 在 17 个平台上做路由。",
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
            "<strong>日增从 178 涨到 902，四天翻了五倍：</strong>这种加速通常意味着有人开始大规模安利它——token 优化是硬需求，不是可有可无的优化项。",
            "<strong>它和 caveman、xerj 构成今天的 token 组：</strong>一个砍工具输出、一个砍对话措辞、一个砍检索开销。三个项目从三个方向围剿同一个成本，这说明 token 账单已经疼到用户愿意为省它专门装软件。",
            "<strong>本质是上下文窗口成了新的稀缺资源：</strong>窗口再大也是有限的，谁能让同样的窗口装下更多有效信息，谁就替用户省了钱——省 token 的生意会一直做下去。"
        ],
        "tags": ["context-window", "mcp", "ai-agent", "typescript", "token-optimization"]
    },
    {
        "rank": 7,
        "owner": "xerj-org",
        "name": "xerj",
        "fullName": "xerj-org / xerj",
        "org": "xerj",
        "url": "https://github.com/xerj-org/xerj",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "4,834",
        "forks": "296",
        "starsToday": "725",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +725★ 首登！4,834★。给 AI 搜数据的一套新做法：用 autoindex 让 Agent 直接「知道」你的数据，而不是靠 grep 和 sed 一遍遍扫。一条命令索引代码、文档、日志和 PDF，官方称比 grep 省 40 倍 token。兼容 Elasticsearch，现有客户端不用改就能连。",
        "problems": [
            "<strong>Agent 翻文件太费 token：</strong>让模型用 grep、sed 逐个文件找答案，上下文很快被搜索结果塞满。",
            "<strong>索引与检索是两套系统：</strong>数据要搜之前先得专门建索引，日常没人维护。",
            "<strong>换工具就要重接：</strong>现有检索生态不兼容，迁移成本高。"
        ],
        "usage": [
            "按 README 安装（Rust 实现，提供命令行入口）。",
            "一条命令为代码、文档、日志或 PDF 建好索引。",
            "Agent 通过它与数据交互；Elasticsearch 兼容，现有客户端可直接连接。"
        ],
        "insights": [
            "<strong>4,834 星、日增 725，典型的新面孔爆发：</strong>基数小、增速快，说明它踩中了某个刚被普遍意识到的痛点，而不是靠存量用户的惯性。",
            "<strong>「比 grep 省 40 倍 token」是在把成本摆到台面上算：</strong>过去没人会拿检索方式和 token 账单挂钩，现在这成了核心卖点——评价工具的标准变了。",
            "<strong>本质是 Agent 开始需要自己的数据层：</strong>模型能不能用上你的数据，取决于数据有没有被整理成它读得懂的样子——这层工作正在独立成一个品类。"
        ],
        "tags": ["search", "indexing", "rust", "rag", "token-optimization"]
    },
    {
        "rank": 8,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra (Jesse Vincent)",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "299,502",
        "forks": "26,753",
        "starsToday": "534",
        "count": 18,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +534★！逼近 30 万★（29.95万★），第18次登榜。一套 Agent 技能框架加软件开发方法论，作者是 Perl 圈的老面孔 Jesse Vincent。它把技能做成可以像软件包一样安装、卸载的东西，是榜单上最持久的项目之一。",
        "problems": [
            "<strong>Agent 技能没法管理：</strong>散落在各个文件夹和聊天记录里，装了什么、还剩什么都不清楚。",
            "<strong>方法论缺席：</strong>模型能力够强，却没人告诉它该按什么流程干活。",
            "<strong>平台不通用：</strong>在 A 工具里能用的技能，换到 B 工具就废。"
        ],
        "usage": [
            "安装 CLI：<pre><code>npm install -g superpowers</code></pre>",
            "搜索技能：<pre><code>superpowers search &quot;test generator&quot;</code></pre>",
            "安装技能：<pre><code>superpowers install writing-plans</code></pre>，自动配置到当前编辑器。"
        ],
        "insights": [
            "<strong>第18次登榜，逼近 30 万星：</strong>从 5 月到现在几乎每周都在榜上，它已经不是热点，是基础设施——这种项目衡量的是「多少人默认依赖它」，而不是「多少人第一次听说它」。",
            "<strong>把技能当软件包管：</strong>install / search / uninstall 这套动作是从包管理器借来的。它真正解决的，是技能多起来之后的混乱问题。",
            "<strong>本质是 Agent 生态在重演软件工程史：</strong>先是散装脚本，然后有人发明包管理器，再后来长出方法论——Agent 的技能体系只用了几个月就走完了这套路。"
        ],
        "tags": ["agent-framework", "skills", "shell", "cli", "methodology"]
    },
    {
        "rank": 9,
        "owner": "JuliusBrussee",
        "name": "caveman",
        "fullName": "JuliusBrussee / caveman",
        "org": "JuliusBrussee",
        "url": "https://github.com/JuliusBrussee/caveman",
        "lang": "Go",
        "langClass": "go",
        "stars": "112,117",
        "forks": "6,502",
        "starsToday": "398",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +398★！11.21万★ 第3次登榜（7 月初 8.35万★）。一个让编码 Agent 说「野人语」的技能加代理，用最少的词把意思说清楚，官方说能砍掉 65% 的 token。仓库说明就一句话：要很多 token 做什么，少 token 也能成事。",
        "problems": [
            "<strong>Agent 话太多：</strong>回复里大量客套和冗余描述，每一个字都在烧钱。",
            "<strong>成本与频率矛盾：</strong>想让 Agent 多干点活，账单就跟着涨。",
            "<strong>省钱的工具少：</strong>大家都在卷能力，没人管成本。"
        ],
        "usage": [
            "按 README 安装技能或代理。",
            "让编码 Agent 在「野人语」模式下工作，输出被压到最短。",
            "支持多种编码工具，安装后自动生效。"
        ],
        "insights": [
            "<strong>从 7 月的 8.35 万星到今天 11.21 万星：</strong>一个定位明显带着玩笑的项目活了下来，还一直在涨——因为「省 token」是真需求，包一层段子反而更容易传播。",
            "<strong>它是今天 token 组的第三个：</strong>context-mode 砍工具输出，xerj 砍检索开销，caveman 砍对话措辞。三个方向，一个结论——成本意识已经渗进 Agent 的每一层。",
            "<strong>本质是省钱需求会筛选出真正的常识：</strong>当工具卷到一定程度，最先被广泛接受的往往不是最花哨的功能，而是最朴素的降本——「少说点话」这种常识，反倒成了卖点。"
        ],
        "tags": ["token-saving", "claude-code", "skill", "cost-optimization", "go"]
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
        "stars": "38,371",
        "forks": "4,286",
        "starsToday": "181",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +181★！3.84万★ 第5次登榜（8 月底 3.52万★）。Anthropic 官方维护的 Claude Code 插件目录：由官方挑选和管理的「高质量插件清单」。它不生产插件，只负责盖章——但恰恰是这件事决定了插件生态的秩序。",
        "problems": [
            "<strong>插件市场鱼龙混杂：</strong>搜到的插件不知道能不能信，装了可能出安全问题。",
            "<strong>发现成本高：</strong>好插件藏在角落里，靠口口相传。",
            "<strong>没有质量标尺：</strong>谁都能发布，用户没有判断依据。"
        ],
        "usage": [
            "浏览官方目录，按类别找插件。",
            "按 README 的指引安装到 Claude Code。",
            "优先选官方维护的条目，避开来源不明的插件。"
        ],
        "insights": [
            "<strong>它和 knowledge-work-plugins 是姊妹：</strong>一个官方插件库、一个官方插件目录——Anthropic 同时在铺货和定标准，这是平台方下场最典型的两个动作。",
            "<strong>第5次登榜，日增不高但一直在：</strong>这种项目不需要爆红，它只需要成为「官方推荐」这四个字——一旦用户养成先去官方目录找插件，其他人做的插件市场就很难翻盘。",
            "<strong>本质是生态的秩序由发目录的人掌握：</strong>不生产插件的人，靠一份清单决定了谁能被看见——这是平台把入口握在手里的方式。"
        ],
        "tags": ["plugins", "anthropic", "claude-code", "marketplace", "ecosystem"]
    },
    {
        "rank": 11,
        "owner": "ruvnet",
        "name": "ruflo",
        "fullName": "ruvnet / ruflo",
        "org": "ruvnet",
        "url": "https://github.com/ruvnet/ruflo",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "74,804",
        "forks": "8,899",
        "starsToday": "146",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +146★ 首登即 7.48万★！作者 ruvnet 自称「最原始的 agent harness」。它能部署多智能体编队、协调自主工作流、搭对话式 AI 系统：自适应记忆、自学习、联邦、向量 RAG 集成，原生支持 Claude Code、Codex、Hermes 等一串工具。",
        "problems": [
            "<strong>多智能体难协调：</strong>让一群 Agent 并行干活，任务分配和结果汇总没人管。",
            "<strong>记忆与学习是散的：</strong>每个 Agent 记各的，经验无法沉淀到系统层面。",
            "<strong>集成成本高：</strong>换一个 Agent 平台，整套编排逻辑要重写。"
        ],
        "usage": [
            "按 README 安装（TypeScript 项目，CLI 形式）。",
            "定义参与工作的 Agent 编队与各自的职责。",
            "用内置的记忆、RAG 与联邦能力组织多智能体协作流程。"
        ],
        "insights": [
            "<strong>首登就是 7.48 万星：</strong>这个体量说明它积累了相当长时间，只是今天才被推上榜单——它不是新项目，是被重新发现的旧项目，这类上榜往往和某个外部事件有关。",
            "<strong>「多智能体编队」是这条线的下一个词：</strong>从单 Agent 调技能，到多 Agent 分工协作，编排层正在成为新的竞争点——谁定义编队协议，谁就掌握下一层入口。",
            "<strong>本质是复杂度在往上走：</strong>单个 Agent 好用了之后，人的胃口就变成「让一群一起干」——工具的进化方向永远是把上一代的复杂度变成下一代的默认能力。"
        ],
        "tags": ["multi-agent", "orchestration", "agent-harness", "typescript", "swarm"]
    },
    {
        "rank": 12,
        "owner": "lightseekorg",
        "name": "tokenspeed",
        "fullName": "lightseekorg / tokenspeed",
        "org": "lightseek",
        "url": "https://github.com/lightseekorg/tokenspeed",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,309",
        "forks": "331",
        "starsToday": "25",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +25★ 首登！2,309★。一个自称「光速」的 LLM 推理引擎。星数不高、日增也小，它挤进榜单靠的是名字里的野心——在所有项目都在抢着降低 token 成本的时候，它押的是更直接的一条路：让推理本身跑得更快。",
        "problems": [
            "<strong>推理慢就等于贵：</strong>同样的算力，速度上不去，单次请求的时间和成本都压不下来。",
            "<strong>现有引擎偏重：</strong>部署一套推理服务要拖一堆依赖，轻量场景不划算。",
            "<strong>延迟敏感场景吃亏：</strong>交互式应用对首字延迟要求高，通用引擎不够灵活。"
        ],
        "usage": [
            "按 README 安装（Python 项目）。",
            "加载目标模型并启动推理服务。",
            "在延迟敏感的场景里替换现有推理后端。"
        ],
        "insights": [
            "<strong>2,309 星却能上榜：</strong>它的出现本身是信号——推理引擎这个赛道一直没有停止过竞争，vLLM 之后仍有新玩家想从速度上切一刀。",
            "<strong>它是今天 token 主题的第四种解法：</strong>context-mode 砍输入、xerj 砍检索、caveman 砍输出、tokenspeed 提高吞吐——前三个省钱，最后一个省时间，而时间也是钱。",
            "<strong>本质是效率竞争换了几轮主角：</strong>先比谁模型强，再比谁推理快，现在比谁用更少的 token 办更多的事——每一轮的主角换了，被优化的那个变量没变：单位成本。"
        ],
        "tags": ["inference", "llm", "python", "performance", "engine"]
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
    "date": "2026-10-15",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-15'
data['topic'] = '🔥 <strong>逆向工具继续暴涨 + 本地语音回归 + Token 经济扎堆上榜</strong> —— morluto/rea（+32,282★）连续第三次登榜，四天从 7.32万★ 飙到 25.93万★，配上 NSA 的 ghidra（+1,366★）8.82万★，逆向工程这条线还在加速，一种需求同时喂饱了 Agent 新工具和二十年老框架。debpalash/VoiceStudio（+3,027★）冲到日增第二：完全本地跑的开源 ElevenLabs 替代，声音克隆、配音、转录、有声书，覆盖 646 种语言。今天最集中的是 token 这条线索：mksglu/context-mode（+902★，日增四天翻五倍）砍工具输出 98%、xerj-org/xerj（+725★）用索引替代 grep 省 40 倍 token、JuliusBrussee/caveman（+398★）用野人语砍对话措辞 65%、lightseekorg/tokenspeed（+25★）提高推理吞吐——三个省钱，一个省时间，围剿的是同一个单位成本。Agent 技能与 harness 层继续霸榜：obra/superpowers（+534★）逼近 30 万星第18次、affaan-m/ECC（+1,015★）第11次、K-Dense-AI/scientific-agent-skills（+1,091★）第7次把 25 万科研人员接进 Agent、anthropics/claude-plugins-official（+181★）第5次用一份清单定义插件秩序、ruvnet/ruflo（+146★）首登即 7.48 万星押注多智能体编队。今日三条主线：一、逆向与二进制工具的热度没有见顶，看懂存量代码仍是本季最贵的技能；二、模型之外的工程层（技能、记忆、编排、插件目录）在集体产品化，第三方抢着占位；三、token 成本成了公开的战场，省钱的手法从输入、检索、输出到吞吐被逐个拿出来单卖。'

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
