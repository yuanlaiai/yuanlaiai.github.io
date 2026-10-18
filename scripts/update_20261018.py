#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-18 (1-day gap, 有昨日榜, 13 席全部连登→平铺渲染)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 18)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为连登：13 个席位全在昨日榜上，零新面孔 → app.js 平铺分支渲染 ──
    {
        "rank": 1,
        "owner": "debpalash",
        "name": "VoiceStudio",
        "fullName": "debpalash / VoiceStudio",
        "org": "debpalash",
        "url": "https://github.com/debpalash/VoiceStudio",
        "lang": "Python",
        "langClass": "py",
        "stars": "73,612",
        "forks": "8,050",
        "starsToday": "2,125",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +2,125★ 连续第三天日增第一！7.36万★ 第5次登榜（昨天 7.21万★）。完全本地跑的开源 ElevenLabs 替代：声音克隆、音色设计、视频配音、听写、转录、有声书，覆盖 646 种语言。",
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
            "<strong>连续三天日增第一：</strong>榜单换了一整天，第一名没换。这种稳定性比单日爆量更能说明问题——它已经进入「每天有人新装」的渠道期，而不是靠一条爆款帖子。",
            "<strong>它的日增在回落，但位置没动：</strong>从 +2,301 降到 +2,125，全榜都在降温，它依然第一。热度退潮的时候还站在前面，才看得出谁是真需求。",
            "<strong>本质是本地替代走到了语音这一层：</strong>文本和图像早就有成熟的本地方案，语音因为模型重一直留在云端。它跑通之后，内容生产的整条链路第一次可以完全不碰外部服务。"
        ],
        "tags": ["voice", "tts", "local-first", "elevenlabs-alternative", "python"]
    },
    {
        "rank": 2,
        "owner": "anthropics",
        "name": "claude-plugins-official",
        "fullName": "anthropics / claude-plugins-official",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-official",
        "lang": "Python",
        "langClass": "py",
        "stars": "41,892",
        "forks": "4,471",
        "starsToday": "1,397",
        "count": 7,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,397★！4.19万★ 第7次登榜（昨天 4.11万★），连续两天日增四位数。Anthropic 官方维护的 Claude Code 插件目录：官方挑选和管理的「高质量插件清单」。它不生产插件，只负责盖章，但恰恰是这件事决定了插件生态的秩序。",
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
            "<strong>连续两天日增四位数：</strong>昨天 +1,552、今天 +1,397，一份「目录」能连续两天拿到这个量级，说明访问它的人不是来看热闹的，是真的在找东西装。",
            "<strong>它比客户端本体涨得快：</strong>今天它 +1,397，claude-code 只有 +179。生态的注意力已经从「用哪个工具」转移到「装什么插件」——这是平台成熟的标志。",
            "<strong>本质是入口由发目录的人掌握：</strong>不生产插件的人，靠一份清单决定了谁能被看见。这种权力不需要写代码，只需要被默认信任。"
        ],
        "tags": ["plugins", "anthropic", "claude-code", "marketplace", "ecosystem"]
    },
    {
        "rank": 3,
        "owner": "MadsLorentzen",
        "name": "ai-job-search",
        "fullName": "MadsLorentzen / ai-job-search",
        "org": "MadsLorentzen",
        "url": "https://github.com/MadsLorentzen/ai-job-search",
        "lang": "Python",
        "langClass": "py",
        "stars": "50,647",
        "forks": "16,960",
        "starsToday": "1,365",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,365★，日增比昨天还高 50%！5.06万★ 第4次登榜（昨天 4.91万★），排名从第七升到第三。一套跑在你自己机器上的求职工具，基于 Claude Code：评估招聘信息、改简历、写求职信、准备面试。作者的说明很短——fork 它，然后据为己有。",
        "problems": [
            "<strong>投简历是体力活：</strong>一份 JD 改一版简历、写一封求职信，投十家就是十遍重复劳动。",
            "<strong>工具要交出自己的数据：</strong>在线求职平台要你的履历、联系方式和投递记录。",
            "<strong>通用 AI 不懂岗位：</strong>直接让模型改简历，容易写成一套漂亮但没有针对性的空话。"
        ],
        "usage": [
            "克隆仓库并在本地配置（Python，基于 Claude Code）。",
            "喂给它目标岗位的招聘信息，让它评估匹配度。",
            "按岗位定制简历与求职信，准备面试问题。"
        ],
        "insights": [
            "<strong>全榜都在降温，它反而加速：</strong>昨天 +898，今天 +1,365，排名从第七冲到第三。在一个整体降温的榜单里逆势上涨，通常意味着需求端刚发生了什么事。",
            "<strong>求职是少数几个能直接算回报的场景：</strong>省下的时间能换算成面试机会，投出去的成本几乎为零。这类工具的增长不依赖技术叙事，只看就业市场紧不紧。",
            "<strong>本质是「本地跑」成了这类工具的信任前提：</strong>把简历和职业经历交给一个网站，和把代码放在自己机器上跑一遍，用户的心理成本完全不同。"
        ],
        "tags": ["job-search", "career", "claude-code", "python", "local-first"]
    },
    {
        "rank": 4,
        "owner": "xerj-org",
        "name": "xerj",
        "fullName": "xerj-org / xerj",
        "org": "xerj",
        "url": "https://github.com/xerj-org/xerj",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "7,901",
        "forks": "422",
        "starsToday": "1,160",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,160★！7,901★ 第3次登榜（昨天 7,311★），连续三天日增四位数。给 AI 搜数据的新做法：autoindex 让 Agent 直接「知道」你的数据，而不是靠 grep 和 sed 一遍遍扫。一条命令索引代码、文档、日志和 PDF，官方称比 grep 省 40 倍 token，且兼容 Elasticsearch。",
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
            "<strong>连续三天日增四位数，是这批小项目里最稳的：</strong>4,834 → 7,311 → 7,901，基数小但每天都有新人进来，说明它是靠搜索和口口相传在滚，不是靠一次曝光。",
            "<strong>它是之前那批 token 工具里唯一活下来的：</strong>context-mode、caveman 都退了，只有它还在。差别在于它动的是数据结构，不是措辞。",
            "<strong>本质是「少读」比「少说」更可持续：</strong>让模型的输出变短只是省一层，让模型不去读无关文件才是从源头省——后者的收益随代码量增长，前者不会。"
        ],
        "tags": ["search", "indexing", "rust", "rag", "token-optimization"]
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
        "stars": "282,620",
        "forks": "41,992",
        "starsToday": "1,145",
        "count": 13,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,145★！28.26万★ 第13次登榜（昨天 28.19万★）。一套 Agent 运行环境的性能优化系统，管技能、管本能（instincts）、管记忆、管安全，主张研究先行的开发方式，支持 Claude Code、Codex、Opencode、Cursor 等。",
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
            "<strong>第13次登榜，日增还在四位数：</strong>一个项目能连着上榜十几次且不掉速，说明它已经进入「默认安装」的位置——用户不是在探索它，是在按习惯重装。",
            "<strong>它今天和 claude-plugins-official、orca、opencode、claude-code 同屏：</strong>调优层、目录、客户端、开源客户端，四件东西拼起来正是一套完整运行环境。榜单今天像一张架构图。",
            "<strong>本质是模型之外的战场更拥挤：</strong>当底层能力越来越接近，拉开差距的不再是模型，而是谁把它调得更顺手、更可控、更省心。"
        ],
        "tags": ["agent-harness", "skills", "memory", "javascript", "developer-tools"]
    },
    {
        "rank": 6,
        "owner": "K-Dense-AI",
        "name": "scientific-agent-skills",
        "fullName": "K-Dense-AI / scientific-agent-skills",
        "org": "K-Dense AI",
        "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "52,326",
        "forks": "4,636",
        "starsToday": "878",
        "count": 9,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +878★！5.23万★ 第9次登榜（昨天 5.19万★）。把任何 AI Agent 变成「AI 科学家」：177 个现成技能加 100 多个科研数据库，覆盖生物、化学、医学和药物发现。作者称全球已有 25 万以上科研人员在用，兼容 Cursor、Claude Code、Codex、Pi 以及开放的 Agent Skills 标准。",
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
            "<strong>第9次登榜：</strong>它上榜的频率比大多数通用技能库还高。科研用户的特点是进来就不走，这类项目的曲线因此长而不陡。",
            "<strong>它是今天榜单里唯一一个「有专业社群」的项目：</strong>25 万科研人员这个数字比星数更能说明它的位置——技能可以抄，圈子抄不走。",
            "<strong>本质是垂直知识在被编译成 Agent 能执行的形式：</strong>论文、数据库、实验流程，过去只给人看，现在要写成模型能调用的技能——这是科研基础设施的一次静默改造。"
        ],
        "tags": ["agent-skills", "science", "research", "bioinformatics", "python"]
    },
    {
        "rank": 7,
        "owner": "stablyai",
        "name": "orca",
        "fullName": "stablyai / orca",
        "org": "Stably AI",
        "url": "https://github.com/stablyai/orca",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "95,550",
        "forks": "6,118",
        "starsToday": "830",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +830★！9.56万★ 第3次登榜（昨天 9.48万★）。Orca 是「同时指挥一支 Agent 舰队」的地方：Grok Bot、Claude Code 之类的编码 Agent 都能跑，用你自己的订阅额度，桌面、手机、远程运行时三端可用。",
        "problems": [
            "<strong>Agent 被锁在终端里：</strong>一个会话只能干一件事，想并行得开一堆窗口，状态还容易乱。",
            "<strong>订阅额度浪费：</strong>买了多家的额度，用起来要来回切工具。",
            "<strong>离开电脑就断线：</strong>Agent 跑到一半要出门，任务只能停。"
        ],
        "usage": [
            "在桌面端或移动端登录，接上自己的模型订阅。",
            "把任务分给多个 Agent 并行执行，统一查看进度。",
            "长任务交给远程运行时，关掉客户端也会继续跑。"
        ],
        "insights": [
            "<strong>连续两天日增八百以上：</strong>它昨天的 +1,102 不是偶然，今天还有 +830。这类「界面型」产品的增长通常慢，能连着两天破八百，说明有多 Agent 并行需求的人在变多。",
            "<strong>它不卖额度，只卖调度：</strong>用你自己的订阅这条定位，让它和所有模型厂商都不冲突，反而成了它们的共同入口。",
            "<strong>本质是 Agent 的入口从命令行挪到多端界面：</strong>CLI 服务愿意敲命令的人，多数人要的是一个能看进度、能随时接管的地方。"
        ],
        "tags": ["agent-orchestration", "multi-agent", "typescript", "desktop", "mobile"]
    },
    {
        "rank": 8,
        "owner": "HKUDS",
        "name": "CLI-Anything",
        "fullName": "HKUDS / CLI-Anything",
        "org": "HKU DS",
        "url": "https://github.com/HKUDS/CLI-Anything",
        "lang": "Python",
        "langClass": "py",
        "stars": "54,129",
        "forks": "4,908",
        "starsToday": "574",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +574★，日增比昨天翻了一倍！5.41万★ 第5次登榜（昨天 5.37万★）。港大数据智能实验室的项目，口号是「让所有软件变成 Agent 原生」，配套一个 CLI-Hub 做入口。它想解决的是 Agent 会用聊天、但不会用你桌上那些专业软件的问题。",
        "problems": [
            "<strong>专业软件没有 Agent 接口：</strong>设计、仿真、科研软件都是给人点的，Agent 插不上手。",
            "<strong>每家都造一套 API：</strong>要接一个软件就得读一遍它的文档，成本高得没人愿意做。",
            "<strong>图形界面不可自动化：</strong>模拟点击又慢又脆，界面一改就全废。"
        ],
        "usage": [
            "按 README 安装（Python 项目）。",
            "为你需要的软件接入或生成对应的命令行封装。",
            "让 Agent 通过统一 CLI 操作这些软件，串进自动化流程。"
        ],
        "insights": [
            "<strong>日增从 281 翻到 574：</strong>昨天它还是全榜倒数第四，今天翻倍。这种变化通常来自一篇新文章或一次演示——基础设施型项目自己没有传播力，得靠别人讲。",
            "<strong>它的位置很关键：</strong>榜单上其他项目都在造新的 Agent 能力，只有它在给存量软件补接口。新能力可以慢慢长，旧软件的接口不补，Agent 就永远只能停在聊天框里。",
            "<strong>本质是存量软件才是 Agent 的真正战场：</strong>新软件可以天生为 Agent 设计，但多数人每天用的还是那些老软件——谁把老接口铺好，谁决定 Agent 能触到多远。"
        ],
        "tags": ["cli", "agent-native", "automation", "python", "integration"]
    },
    {
        "rank": 9,
        "owner": "anomalyco",
        "name": "opencode",
        "fullName": "anomalyco / opencode",
        "org": "anomalyco",
        "url": "https://github.com/anomalyco/opencode",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "215,511",
        "forks": "28,874",
        "starsToday": "438",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +438★！21.55万★ 第2次登榜（昨天 21.45万★）。一句话说明：开源的编码 Agent。它昨天首登就 21 万星，今天继续涨——说明那批用户不是来看热闹的。",
        "problems": [
            "<strong>编码 Agent 被厂商绑定：</strong>用谁家的模型就得用谁家的客户端，工作流跟着绑定。",
            "<strong>黑盒不可审计：</strong>闭源客户端读你的代码、改你的文件，但你看不到它怎么处理。",
            "<strong>成本不透明：</strong>订阅套餐说变就变，用量和价格对不上。"
        ],
        "usage": [
            "按 README 安装（TypeScript，终端里运行）。",
            "接上自己的模型提供方（可换）。",
            "在项目目录里用自然语言让它改代码、跑测试、处理 git 流程。"
        ],
        "insights": [
            "<strong>首登之后的第二天最考验人：</strong>很多项目首次上榜靠一次曝光，第二天就掉；它还有 +438，说明排名带来的新用户留下来了。",
            "<strong>它和 claude-code 连续两天同屏：</strong>开源可换模型对闭源官方，这场对照已经不是一次性话题，而是每天都在发生的选择。",
            "<strong>本质是编码 Agent 的竞争回到了「谁更透明」：</strong>能力都够用之后，用户开始问能不能换模型、能不能看代码、能不能自己改。"
        ],
        "tags": ["coding-agent", "open-source", "typescript", "cli", "developer-tools"]
    },
    {
        "rank": 10,
        "owner": "ruvnet",
        "name": "ruflo",
        "fullName": "ruvnet / ruflo",
        "org": "ruvnet",
        "url": "https://github.com/ruvnet/ruflo",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "76,127",
        "forks": "9,006",
        "starsToday": "420",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +420★！7.61万★ 第3次登榜（昨天 7.58万★）。作者 ruvnet 自称「最原始的 agent harness」：部署多智能体编队、协调自主工作流、搭对话式 AI 系统，带自适应记忆、自学习、联邦和向量 RAG，原生支持 Claude Code、Codex、Hermes 等。",
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
            "<strong>连续两天上榜，日增稳定在四百以上：</strong>它昨天从 146 跳到 672，今天回落到 420 但没有掉出榜单——这种「放量后不熄火」是回归项目最好的状态。",
            "<strong>它和 orca 是同一个需求的两副面孔：</strong>orca 给你一个指挥舰队的地方，ruflo 给你一套编排舰队的框架——一个做界面，一个做引擎。",
            "<strong>本质是复杂度在往上走：</strong>单 Agent 好用了之后，人的胃口就变成「让一群一起干」。"
        ],
        "tags": ["multi-agent", "orchestration", "agent-harness", "typescript", "swarm"]
    },
    {
        "rank": 11,
        "owner": "android",
        "name": "skills",
        "fullName": "android / skills",
        "org": "android",
        "url": "https://github.com/android/skills",
        "lang": "Kotlin",
        "langClass": "kotlin",
        "stars": "8,464",
        "forks": "556",
        "starsToday": "355",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +355★，日增是昨天的近十倍！8,464★ 第2次登榜（昨天 8,220★）。Google 的 android 组织下新开的 skills 仓库，描述是空的，从命名和语言看，是给 Agent 用的 Android 开发技能库。昨天只有 +36，今天突然放量。",
        "problems": [
            "<strong>平台知识散在文档里：</strong>Android 的版本兼容、构建配置、最佳实践，Agent 学不全。",
            "<strong>通用技能不懂平台细节：</strong>社区写的技能经常给出过时的 API 用法。",
            "<strong>官方没有可执行标准：</strong>文档是给人读的，不是给 Agent 执行的。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/android/skills.git</code></pre>",
            "把技能目录接入支持 Agent Skills 的编码工具。",
            "在 Android 项目里让 Agent 按官方技能执行开发任务。"
        ],
        "insights": [
            "<strong>日增从 36 涨到 355，接近十倍：</strong>昨天它是全榜最安静的一条，今天突然被大量访问。这类官方仓库自己没有传播动作，放量通常意味着某个大会、版本发布或官方文档开始引用它。",
            "<strong>它和 anthropics/claude-plugins-official、K-Dense-AI 的科研技能是同一个动作：</strong>平台方、厂商、垂直社群都在把自己的知识封装成技能——谁先把自己的领域做成技能，谁就定义了 Agent 在这个领域里的默认行为。",
            "<strong>本质是文档的形态在换代：</strong>过去平台写文档给人看，现在要写技能给模型执行。同一份知识，两种读者，后者的话语权正在变大。"
        ],
        "tags": ["android", "agent-skills", "kotlin", "google", "mobile"]
    },
    {
        "rank": 12,
        "owner": "anthropics",
        "name": "claude-code",
        "fullName": "anthropics / claude-code",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-code",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "151,845",
        "forks": "26,883",
        "starsToday": "179",
        "count": 6,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +179★！15.18万★ 第6次登榜（昨天 15.13万★）。Claude Code 本体：一个住在终端里的编码 Agent，读得懂你的代码库，跑日常任务、解释复杂代码、处理 git 流程，全用自然语言下指令。",
        "problems": [
            "<strong>上下文靠人喂：</strong>项目一大，Agent 就找不到该看哪几个文件。",
            "<strong>改错地方：</strong>模型容易顺手改无关代码，review 时才发现。",
            "<strong>流程不透明：</strong>它执行了什么命令、动了哪些文件，事后要自己拼。"
        ],
        "usage": [
            "在终端里安装并登录。",
            "进入项目目录直接描述任务，它自己找文件、改代码、跑命令。",
            "用 /review、git 相关指令把改动纳入正常流程。"
        ],
        "insights": [
            "<strong>它涨得远不如自己的插件目录：</strong>今天 +179，而 claude-plugins-official +1,397。这个反差很直白：客户端已经装好了，用户在找的是装什么。",
            "<strong>它和 opencode 连续两天同屏：</strong>闭源官方对开源可换模型。两边都能站在 15 万星以上，说明这个市场大到容得下两种路线。",
            "<strong>本质是终端变成了新的入口：</strong>过去 IDE 是写代码的地方，现在 Agent 住在终端里，人只下指令——入口换了，围绕它长出来的生态也跟着换。"
        ],
        "tags": ["claude-code", "coding-agent", "cli", "typescript", "anthropic"]
    },
    {
        "rank": 13,
        "owner": "akitaonrails",
        "name": "ai-memory",
        "fullName": "akitaonrails / ai-memory",
        "org": "akitaonrails",
        "url": "https://github.com/akitaonrails/ai-memory",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "9,994",
        "forks": "725",
        "starsToday": "178",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +178★！9,994★ 第4次登榜（昨天 9,654★），离一万星只差 6 个。给编码 Agent 的长期记忆方案，重点在「交接」：当你从一家的 Agent 换到另一家，之前积累的记忆能带过去。用 Rust 写，追求本地读写性能。",
        "problems": [
            "<strong>换个 Agent 就失忆：</strong>在一个工具里调教出的上下文，换到另一家全部作废。",
            "<strong>记忆绑在会话里：</strong>会话一关，之前的结论和偏好就找不回来了。",
            "<strong>厂商之间的格式不通：</strong>每家存的记忆结构不一样，没法直接迁移。"
        ],
        "usage": [
            "按 README 安装（Rust 实现，本地运行）。",
            "让它接管编码 Agent 的记忆读写。",
            "切换 Agent 厂商时，把已有记忆交接过去继续用。"
        ],
        "insights": [
            "<strong>差 6 个星到一万：</strong>这个位置有点象征意义——记忆这类「不起眼但每天都要用」的工具，正好该长在这个量级。",
            "<strong>「handoff between different agent vendors」还是它最锋利的一句定位：</strong>它承认用户会换 Agent，并把「换的时候别失忆」做成产品。厂商不会做这件事，第三方做正好。",
            "<strong>本质是记忆正在从功能变成资产：</strong>当记忆能被导出、迁移、跨厂商带走，它就变成了用户自己的东西——谁掌握记忆的格式，谁就掌握用户换工具时的议价权。"
        ],
        "tags": ["memory", "agent-handoff", "rust", "local-first", "coding-agent"]
    }
]

# 按日增降序规整编号（全部连登，app.js 走平铺分支）
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
    "date": "2026-10-18",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-18'
data['topic'] = '🔥 <strong>今天榜单一个新人没有：13 个席位全是昨日原班人马，热点高度固化</strong> —— 这是近期第一次出现零新面孔。debpalash/VoiceStudio（+2,125★）连续第三天日增第一；anthropics/claude-plugins-official（+1,397★）第7次、日增是自己客户端 claude-code（+179★）的八倍，注意力已经从「装哪个工具」转到「装什么插件」；MadsLorentzen/ai-job-search（+1,365★）第4次，在全榜降温时逆势从第七冲到第三；xerj-org/xerj（+1,160★）第3次，是之前那批 token 工具里唯一活下来的；affaan-m/ECC（+1,145★）第13次。整张榜单被 Agent 的中间层包场：技能（scientific-agent-skills 第9次）、客户端（opencode 第2次、claude-code 第6次、orca 第3次）、编排（ruflo 第3次）、记忆（ai-memory 第4次，差 6 星到一万）、插件目录（claude-plugins-official 第7次）。两个值得注意的加速：ai-job-search 日增比昨天还高 50%，android/skills 日增从 36 跳到 355、接近十倍。今天没有新闻，只有惯性——而惯性本身说明这层东西已经从「值得关注」变成了「日常在用」。'

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
