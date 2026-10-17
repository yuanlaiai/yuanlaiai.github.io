#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-17 (2-day gap, 无昨日榜→平铺结构, 13 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 17)
gap_days = (today - last).days  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（2天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "debpalash",
        "name": "VoiceStudio",
        "fullName": "debpalash / VoiceStudio",
        "org": "debpalash",
        "url": "https://github.com/debpalash/VoiceStudio",
        "lang": "Python",
        "langClass": "py",
        "stars": "72,064",
        "forks": "7,874",
        "starsToday": "2,301",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,301★ 连续第二天拿下日增第一！7.21万★ 第4次登榜（两天前 6.80万★）。完全本地跑的开源 ElevenLabs 替代：声音克隆、音色设计、视频配音、听写、转录、有声书制作，覆盖 646 种语言。",
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
            "<strong>连续两天日增第一：</strong>前两天它排第二，今天直接顶到榜首，两天又涨了 4,000 星。这种持续性说明它不是被谁转发带起来的，而是真有一批人在批量把配音工作搬到本地。",
            "<strong>本地替代云服务这件事，语音是最后一块硬骨头：</strong>文本、图像早就有了本地方案，语音因为模型大、推理重，一直留在云端。它跑通之后，内容生产的整条链路第一次可以完全不碰外部服务。",
            "<strong>本质是「能力自主」在往上游走：</strong>用户要的不只是省钱，是这条流水线什么时候停、给谁用、留不留记录，都由自己说了算。"
        ],
        "tags": ["voice", "tts", "local-first", "elevenlabs-alternative", "python"]
    },
    {
        "rank": 2,
        "owner": "xerj-org",
        "name": "xerj",
        "fullName": "xerj-org / xerj",
        "org": "xerj",
        "url": "https://github.com/xerj-org/xerj",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "7,311",
        "forks": "380",
        "starsToday": "1,648",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,648★，日增是两天前的两倍多！7,311★ 第2次登榜（两天前 4,834★）。给 AI 搜数据的新做法：autoindex 让 Agent 直接「知道」你的数据，而不是靠 grep 和 sed 一遍遍扫。一条命令索引代码、文档、日志和 PDF，官方称比 grep 省 40 倍 token，且兼容 Elasticsearch。",
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
            "<strong>两天从 4,834 涨到 7,311，日增还翻了倍：</strong>新项目最怕第二天就熄火，它反而加速，说明第一批用的人确实省到了钱，才会继续传。",
            "<strong>昨天的那批 token 工具今天只剩它还在榜上：</strong>context-mode、caveman 都退了，留下的这个是唯一一个真去动「数据结构」而不是「措辞」的——省 token 的可持续做法，是让模型少读，而不是让它少说。",
            "<strong>本质是 Agent 开始需要自己的数据层：</strong>模型能不能用上你的数据，取决于数据有没有被整理成它读得懂的样子——这层工作正在独立成一个品类。"
        ],
        "tags": ["search", "indexing", "rust", "rag", "token-optimization"]
    },
    {
        "rank": 3,
        "owner": "anthropics",
        "name": "claude-plugins-official",
        "fullName": "anthropics / claude-plugins-official",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-official",
        "lang": "Python",
        "langClass": "py",
        "stars": "41,091",
        "forks": "4,430",
        "starsToday": "1,552",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,552★，日增是两天前的 8.5 倍！4.11万★ 第6次登榜（两天前 3.84万★）。Anthropic 官方维护的 Claude Code 插件目录：由官方挑选和管理的「高质量插件清单」。它不生产插件，只负责盖章，但恰恰是这件事决定了插件生态的秩序。",
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
            "<strong>两天日增从 181 跳到 1,552，涨了 8.5 倍：</strong>一份「目录」突然被大量访问，通常意味着旁边的生态刚发生了什么事——要么新版本发布，要么有热门插件出圈，用户回头来找官方清单。",
            "<strong>它和 claude-code 今天同时上榜：</strong>Anthropic 在榜单上凑齐了「客户端 + 目录」两件套。一个负责让你天天打开，一个负责决定你打开后装什么，这是平台方最稳的组合。",
            "<strong>本质是生态的秩序由发目录的人掌握：</strong>不生产插件的人，靠一份清单决定了谁能被看见——这是把入口握在手里的经典做法。"
        ],
        "tags": ["plugins", "anthropic", "claude-code", "marketplace", "ecosystem"]
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
        "stars": "51,872",
        "forks": "4,596",
        "starsToday": "1,158",
        "count": 8,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,158★！5.19万★ 第8次登榜（两天前 5.00万★）。把任何 AI Agent 变成「AI 科学家」：177 个现成技能加 100 多个科研数据库，覆盖生物、化学、医学和药物发现。作者称全球已有 25 万以上科研人员在用，兼容 Cursor、Claude Code、Codex、Pi 以及开放的 Agent Skills 标准。",
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
            "<strong>第8次登榜，日增还稳在四位数：</strong>技能库能连着上榜这么多次，靠的不是新鲜感，是科研工作的周期长——一批人用上了就不会换，新的人还在陆续进来。",
            "<strong>它的壁垒不是代码，是那 25 万人的社群：</strong>技能条目谁都能抄，但一个专业圈子认不认你，抄不走。垂直技能库真正的门槛在背书。",
            "<strong>本质是科研门槛在换位置：</strong>过去卡在会不会用工具，现在卡在能不能提出对的问题——工具链越完备，提问能力的权重越高。"
        ],
        "tags": ["agent-skills", "science", "research", "bioinformatics", "python"]
    },
    {
        "rank": 5,
        "owner": "stablyai",
        "name": "orca",
        "fullName": "stablyai / orca",
        "org": "Stably AI",
        "url": "https://github.com/stablyai/orca",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "94,779",
        "forks": "6,062",
        "starsToday": "1,102",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,102★！9.48万★ 第2次登榜（8 月中 4.38万★，两个月翻了一倍多）。Orca 是「同时指挥一支 Agent 舰队」的地方：Grok Bot、Codex 之类的编码 Agent 都能跑，用你自己的订阅额度，桌面、手机、远程运行时三端可用。",
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
            "<strong>两个月从 4.38 万涨到 9.48 万：</strong>翻倍的速度比大多数新项目慢，但它一直在榜——这类产品的增长来自「用顺手了就不换」，而不是一次爆红。",
            "<strong>「用你自己的订阅」这句是它最聪明的地方：</strong>它不卖模型额度，只卖调度界面。这样一来它和所有模型厂商都不竞争，反而成了它们的入口。",
            "<strong>本质是 Agent 的入口从命令行挪到了多端界面：</strong>CLI 是给愿意敲命令的人用的，而多数人要的是一个能看进度、能随时接管的地方——谁做成那个界面，谁就拿到了日常入口。"
        ],
        "tags": ["agent-orchestration", "multi-agent", "typescript", "desktop", "mobile"]
    },
    {
        "rank": 6,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "281,883",
        "forks": "41,914",
        "starsToday": "1,057",
        "count": 12,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,057★！28.19万★ 第12次登榜（两天前 27.99万★）。一套 Agent 运行环境的性能优化系统，管技能、管本能（instincts）、管记忆、管安全，主张研究先行的开发方式，支持 Claude Code、Codex、Opencode、Cursor 等。",
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
            "<strong>第12次登榜，28 万星：</strong>它上榜的频率已经接近常驻。这类项目的意义不在「今天涨了多少」，而在于它成了多少人默认装的底座。",
            "<strong>它今天和 orca、opencode、claude-code 挤在一起：</strong>这四类东西拼起来正好是一套完整的运行环境——客户端、编排、调优、模型。榜单第一次像一张产品架构图。",
            "<strong>本质是模型之外的战场更拥挤：</strong>当底层模型能力越来越接近，拉开差距的不再是模型本身，而是谁把它调得更顺手、更可控、更省心。"
        ],
        "tags": ["agent-harness", "skills", "memory", "javascript", "developer-tools"]
    },
    {
        "rank": 7,
        "owner": "MadsLorentzen",
        "name": "ai-job-search",
        "fullName": "MadsLorentzen / ai-job-search",
        "org": "MadsLorentzen",
        "url": "https://github.com/MadsLorentzen/ai-job-search",
        "lang": "Python",
        "langClass": "py",
        "stars": "49,082",
        "forks": "16,725",
        "starsToday": "898",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +898★！4.91万★ 第3次登榜（7 月初 1.75万★，三个月涨了近两倍）。一套跑在你自己机器上的求职工具，基于 Claude Code：评估招聘信息、改简历、写求职信、准备面试。作者的说明很短——fork 它，然后据为己有。",
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
            "<strong>三个月从 1.75 万涨到 4.91 万：</strong>求职是强周期需求，这类项目的星数会跟着就业市场波动——它的增长本身就是一个经济指标。",
            "<strong>「fork it and own it」（克隆走，归你）是它真正的定位：</strong>不做一个网站收你的简历，而是给你一套代码放在自己机器上。这个选择直接回应了求职者对平台的信任问题。",
            "<strong>本质是垂直流程被打包：</strong>过去 AI 帮你写一段文字，现在它把「看岗位、改简历、写求职信、准备面试」整条链路接了下来——价值从单点能力转向流程编排。"
        ],
        "tags": ["job-search", "career", "claude-code", "python", "local-first"]
    },
    {
        "rank": 8,
        "owner": "ruvnet",
        "name": "ruflo",
        "fullName": "ruvnet / ruflo",
        "org": "ruvnet",
        "url": "https://github.com/ruvnet/ruflo",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "75,786",
        "forks": "8,979",
        "starsToday": "672",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +672★，日增是两天前的 4.6 倍！7.58万★ 第2次登榜（两天前 7.48万★）。作者 ruvnet 自称「最原始的 agent harness」：部署多智能体编队、协调自主工作流、搭对话式 AI 系统，带自适应记忆、自学习、联邦和向量 RAG，原生支持 Claude Code、Codex、Hermes 等。",
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
            "<strong>日增从 146 涨到 672，四倍多：</strong>它上一次上榜时几乎是个安静的回归，这次突然放量，多半是踩上了「多智能体」这个正在被讨论的话题。",
            "<strong>它和 orca 是同一个需求的两副面孔：</strong>orca 给你一个指挥舰队的地方，ruflo 给你一套编排舰队的框架——一个做界面，一个做引擎，说明「多 Agent 协作」已经从概念进入工具分化阶段。",
            "<strong>本质是复杂度在往上走：</strong>单 Agent 好用了之后，人的胃口就变成「让一群一起干」——工具的进化方向永远是把上一代的复杂度变成下一代的默认能力。"
        ],
        "tags": ["multi-agent", "orchestration", "agent-harness", "typescript", "swarm"]
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
        "stars": "214,513",
        "forks": "28,794",
        "starsToday": "488",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +488★ 首登就 21.45万★！一句话说明：开源的编码 Agent。能做到这个体量还没上过榜，本身说明它此前一直靠口碑在圈内扩散，今天才被推到大盘面前。",
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
            "<strong>21.45 万星却从未上榜：</strong>这种反差说明它的用户黏性极强但不依赖曝光——编码 Agent 是每天要打开的工具，用的人不会去 star 榜单，只会去写配置。",
            "<strong>它和 claude-code 同一天上榜：</strong>一个闭源官方、一个开源可换模型，正好是这条赛道上的两种路线选择。榜单把这场对比直接摆在了同一屏。",
            "<strong>本质是编码 Agent 的竞争回到了「谁更透明」：</strong>当各家能力都够用时，用户开始问的是能不能换模型、能不能看代码、能不能自己改——开源在这个阶段重新变成了卖点。"
        ],
        "tags": ["coding-agent", "open-source", "typescript", "cli", "developer-tools"]
    },
    {
        "rank": 10,
        "owner": "HKUDS",
        "name": "CLI-Anything",
        "fullName": "HKUDS / CLI-Anything",
        "org": "HKU DS",
        "url": "https://github.com/HKUDS/CLI-Anything",
        "lang": "Python",
        "langClass": "py",
        "stars": "53,730",
        "forks": "4,879",
        "starsToday": "281",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +281★！5.37万★ 第4次登榜（5 月中 3.91万★，五个月涨了 37%）。港大数据智能实验室的项目，口号是「让所有软件变成 Agent 原生」，配套一个 CLI-Hub 做入口。它想解决的是 Agent 会用聊天，但不会用你桌上那些专业软件的问题。",
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
            "<strong>第4次登榜，五个月涨了 37%：</strong>涨幅不算猛，但一直有人在用——这类「基础设施型」项目的节奏就是这样，它不制造话题，只解决一次性的接入问题。",
            "<strong>「让所有软件 Agent 原生」这个口号背后是一个很朴素的判断：</strong>Agent 要干活，只能通过接口。而现成的接口里，命令行是改造成本最低的那一种。",
            "<strong>本质是存量软件才是 Agent 的真正战场：</strong>新写的软件可以天生为 Agent 设计，但绝大多数人每天用的还是那些老软件——谁把老软件的接口铺好，谁就决定 Agent 能触到多远。"
        ],
        "tags": ["cli", "agent-native", "automation", "python", "integration"]
    },
    {
        "rank": 11,
        "owner": "anthropics",
        "name": "claude-code",
        "fullName": "anthropics / claude-code",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-code",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "151,325",
        "forks": "26,853",
        "starsToday": "168",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +168★！15.13万★ 第5次登榜（9 月中 14.69万★）。Claude Code 本体：一个住在终端里的编码 Agent，读得懂你的代码库，跑日常任务、解释复杂代码、处理 git 流程，全用自然语言下指令。",
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
            "<strong>官方客户端自己第5次登榜：</strong>它的星数增长和插件目录同步，说明今天这一波热度来自生态侧——用户不是来看客户端的，是回来找插件的。",
            "<strong>它和 opencode 同屏：</strong>闭源官方对开源可换模型，这是编码 Agent 赛道最直接的一次对照。两边都能上 15 万星以上，说明市场大到容得下两种路线。",
            "<strong>本质是终端变成了新的入口：</strong>过去 IDE 是写代码的地方，现在 Agent 住在终端里，人不写代码只下指令——入口换了，围绕它长出来的生态（插件、技能、目录）也跟着换。"
        ],
        "tags": ["claude-code", "coding-agent", "cli", "typescript", "anthropic"]
    },
    {
        "rank": 12,
        "owner": "akitaonrails",
        "name": "ai-memory",
        "fullName": "akitaonrails / ai-memory",
        "org": "akitaonrails",
        "url": "https://github.com/akitaonrails/ai-memory",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "9,654",
        "forks": "691",
        "starsToday": "159",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +159★！9,654★ 第3次登榜（8 月中 2,717★，两个月涨了 3.5 倍）。给编码 Agent 的长期记忆方案，重点在「交接」：当你从一家的 Agent 换到另一家，之前积累的记忆能带过去。用 Rust 写，追求本地读写性能。",
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
            "<strong>两个月从 2,717 涨到 9,654，3.5 倍：</strong>这个增速比大多数记忆类项目快，说明它踩中的不是「记忆」这个大词，而是「换工具」这个具体时刻。",
            "<strong>「handoff between different agent vendors」是它最锋利的一句定位：</strong>它承认用户会换 Agent，并且把「换的时候别失忆」做成产品。厂商不会做这件事，第三方做正好。",
            "<strong>本质是记忆正在从功能变成资产：</strong>当记忆能被导出、迁移、跨厂商带走，它就变成了用户自己的东西——谁掌握记忆的格式，谁就掌握了用户换工具时的议价权。"
        ],
        "tags": ["memory", "agent-handoff", "rust", "local-first", "coding-agent"]
    },
    {
        "rank": 13,
        "owner": "android",
        "name": "skills",
        "fullName": "android / skills",
        "org": "android",
        "url": "https://github.com/android/skills",
        "lang": "Kotlin",
        "langClass": "kotlin",
        "stars": "8,220",
        "forks": "540",
        "starsToday": "36",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +36★ 首登！8,220★。Google 的 android 组织下新开的 skills 仓库，描述是空的，从命名和语言看，是给 Agent 用的 Android 开发技能库。日增很低，但「平台方亲自下场做技能库」这件事本身比数字重要。",
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
            "<strong>日增只有 36，却是今天最值得记的一条：</strong>Android 官方开始把平台知识做成 Agent 能读的技能，这意味着「技能库」从社区自发的积累，变成了平台方主动维护的基础设施。",
            "<strong>它和 anthropics/claude-plugins-official、K-Dense-AI 的科研技能是同一个动作：</strong>平台方、厂商、垂直社群都在把自己的知识封装成技能——谁先把自己的领域做成技能，谁就定义了 Agent 在这个领域里的默认行为。",
            "<strong>本质是文档的形态在换代：</strong>过去平台写文档给人看，现在要写技能给模型执行——同一份知识，两种读者，而后者的话语权正在变大。"
        ],
        "tags": ["android", "agent-skills", "kotlin", "google", "mobile"]
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
    "date": "2026-10-17",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-17'
data['topic'] = '🔥 <strong>Agent 客户端与编排层占满榜单 + 记忆开始跨厂商迁移 + 垂直流程被打包</strong> —— 今天榜单第一次像一张产品架构图：anomalyco/opencode（+488★）21.45万★ 的开源编码 Agent、anthropics/claude-code（+168★）15.13万★、stablyai/orca（+1,102★）9.48万★ 用你自己的订阅指挥一支 Agent 舰队、ruvnet/ruflo（+672★，日增翻 4.6 倍）做多智能体编队、affaan-m/ECC（+1,057★）第12次调优 harness——客户端、编排、调优、模型四层同时在场。记忆层开始解决「换厂商」这个具体痛点：akitaonrails/ai-memory（+159★）两个月涨 3.5 倍，主打不同 Agent 之间的记忆交接，和昨天还在榜、今天退场的 claude-mem 是同一个方向。垂直流程被打包成整条链路：MadsLorentzen/ai-job-search（+898★）本地跑求职全流程、HKUDS/CLI-Anything（+281★）要把存量软件变成 Agent 原生的 CLI、android/skills（+36★）首登——Google 官方开始把平台知识做成技能。debpalash/VoiceStudio（+2,301★）连续第二天日增第一，本地语音替代云服务。anthropics/claude-plugins-official（+1,552★）日增暴涨 8.5 倍，官方用一份清单定义插件秩序。今天最值得记的不是哪条涨得猛，而是 token 那批工具只剩 xerj-org/xerj（+1,648★，日增翻倍）还在：省 token 的可持续做法是让模型少读，而不是让它少说。'

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
