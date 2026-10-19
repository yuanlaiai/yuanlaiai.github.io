#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-19 (1-day gap, 双栏 5 新面孔 + 6 连登 = 11 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 19)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 10-18 榜上）══
    {
        "rank": 1,
        "owner": "Comfy-Org",
        "name": "ComfyUI",
        "fullName": "Comfy-Org / ComfyUI",
        "org": "Comfy Org",
        "url": "https://github.com/Comfy-Org/ComfyUI",
        "lang": "Python",
        "langClass": "py",
        "stars": "139,244",
        "forks": "16,543",
        "starsToday": "1,011",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,011★ 重新上榜！13.92万★（8 月中首登时 12.58万★，两个月涨了 1.3 万）。最有名的扩散模型图形界面：节点式工作流、API 与后端一体，官方自称「世界上最快的本地推理引擎」。在什么都往云上跑的这两年，它一直守着本地这一侧。",
        "problems": [
            "<strong>云端生图不可控：</strong>排队、限流、内容策略随时变，工作流跑到一半被掐断。",
            "<strong>模型与流程被平台绑定：</strong>换一个服务商，之前调好的参数和节点全废。",
            "<strong>批量生产缺少工程化：</strong>网页版点一张一张出，接不进自动化流水线。"
        ],
        "usage": [
            "按 README 安装（Python，本地运行，需配 GPU）。",
            "用节点图搭工作流：加载模型、加条件、接后处理，连成一条流水线。",
            "通过内置 API 把工作流接进自己的服务，批量出图或做视频。"
        ],
        "insights": [
            "<strong>两个月涨 1.3 万星再回榜：</strong>它不是新项目，是这个领域的基础设施。这类项目回榜通常不是自己做了什么，而是整个生态又热闹了——新的开源模型一发布，第一批跑它的人还是回到这里。",
            "<strong>今天榜单的对照组：</strong>一边是九个 Agent 工具，一边是一个本地扩散引擎。前者优化的是「怎么用模型」，后者守着「模型跑在谁的机器上」——两件事在同一个榜单上，说明用户对这两件事都有焦虑。",
            "<strong>本质是本地推理是最后一道保险：</strong>当模型、API、内容策略都由别人控制时，能自己跑一份完整管线，本身就是一种议价能力。"
        ],
        "tags": ["diffusion", "comfyui", "image-generation", "local-first", "python"]
    },
    {
        "rank": 2,
        "owner": "Kruk2",
        "name": "jasna",
        "fullName": "Kruk2 / jasna",
        "org": "Kruk2",
        "url": "https://github.com/Kruk2/jasna",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,739",
        "forks": "205",
        "starsToday": "502",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +502★ 首登！2,739★，全榜星数最少的一个。仓库说明只有四个字的后半句：视频修复工具。基数小、增速快，是典型的新面孔爆发——它能上榜靠的不是体量，是今天突然有一批人在找它。",
        "problems": [
            "<strong>老视频画质没法用：</strong>家庭录像、旧素材分辨率低、噪点多，直接放进新项目里很违和。",
            "<strong>专业修复软件门槛高：</strong>要懂降噪、超分、去隔行，还要会调参数。",
            "<strong>修复流程碎：</strong>抽帧、逐帧处理、再合成，工具换好几个。"
        ],
        "usage": [
            "按 README 安装（Python 项目，建议有 GPU）。",
            "输入待修复的视频文件。",
            "输出处理后的视频，按需调整修复强度。"
        ],
        "insights": [
            "<strong>2,739 星却能上榜：</strong>GitHub 的日榜看的是当日增量不是总量，一个小项目只要今天被集中讨论，就能挤掉一个 20 万星的大项目。这也解释了为什么榜单上总有小体量的意外。",
            "<strong>「视频修复」是个被低估的场景：</strong>它不性感，但存量视频的量级远大于新拍的视频——每个家庭、每个档案馆都有一堆放不出来的老素材。",
            "<strong>本质是 AI 最扎实的落地在修旧东西：</strong>不是生成不存在的内容，而是把已经存在但没法用的东西救回来。这类需求不会因为模型变强而消失，只会变便宜。"
        ],
        "tags": ["video-restoration", "upscaling", "python", "media", "local-first"]
    },
    {
        "rank": 3,
        "owner": "withmarbleapp",
        "name": "os-taxonomy",
        "fullName": "withmarbleapp / os-taxonomy",
        "org": "withmarbleapp",
        "url": "https://github.com/withmarbleapp/os-taxonomy",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "5,892",
        "forks": "986",
        "starsToday": "427",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +427★ 首登！5,892★。仓库描述是空的，从组织名（withmarbleapp）和仓库名看，是一套「操作系统级」的分类体系。空描述还能上榜，说明它是被某个圈子直接推上来的，不是靠搜索发现。",
        "problems": [
            "<strong>分类体系各搞一套：</strong>不同工具、不同团队对同一批东西的叫法不统一，数据没法对齐。",
            "<strong>知识散在目录里：</strong>文件、任务、笔记各有一套层级，跨工具就断。",
            "<strong>交给 Agent 就乱：</strong>模型看不懂你的目录结构，只能一个个文件翻。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/withmarbleapp/os-taxonomy.git</code></pre>",
            "按 README 的说明查看分类定义。",
            "把它接到自己的工具或 Agent 流程里，统一归类口径。"
        ],
        "insights": [
            "<strong>空描述 + 427 日增：</strong>这是今天最反常的一条。没有说明文档的项目通常靠内部推荐传播——它的用户大概已经知道它是什么，不需要介绍。",
            "<strong>「taxonomy」这个词值得注意：</strong>当 Agent 要处理的东西从几个文件变成整个工作环境，「怎么分类」就从整理癖变成了基础设施问题——分错了，模型就找不到。",
            "<strong>本质是给 Agent 用的世界要先被命名：</strong>模型没法理解一个没有结构的硬盘。分类体系是让机器接管工作前的第一步，也是最不被注意的一步。"
        ],
        "tags": ["taxonomy", "knowledge-management", "javascript", "agent", "structure"]
    },
    {
        "rank": 4,
        "owner": "shiyu-coder",
        "name": "Kronos",
        "fullName": "shiyu-coder / Kronos",
        "org": "shiyu-coder",
        "url": "https://github.com/shiyu-coder/Kronos",
        "lang": "Python",
        "langClass": "py",
        "stars": "41,355",
        "forks": "6,892",
        "starsToday": "355",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +355★ 第3次登榜（上次是 7 月底 3.46万★，三个月涨了 6,800★）。Kronos：面向金融市场的「语言」基础模型——把 K 线、成交量这些行情数据当成一种语言来建模，而不是套用通用大模型。",
        "problems": [
            "<strong>通用大模型不懂行情：</strong>把 K 线当文本喂进去，模型抓不到时间序列的局部结构。",
            "<strong>金融数据噪声极大：</strong>直接预测价格容易被随机波动带偏。",
            "<strong>研究者复现困难：</strong>论文多、可跑的基线少。"
        ],
        "usage": [
            "按 README 安装（Python 项目）。",
            "用内置的行情数据处理流程准备数据。",
            "加载预训练模型做微调或推理，接入自己的研究流程。"
        ],
        "insights": [
            "<strong>三个月涨 6,800 星：</strong>金融 AI 项目的热度通常跟着市场行情走，涨得稳说明它积累的是研究者而不是投机者。",
            "<strong>「把行情当语言」这个思路是它的关键：</strong>不是让通用模型硬套，而是先把 K 线离散成 token，再按语言模型的方式训练——领域模型的正确做法往往始于重新定义输入。",
            "<strong>本质是垂直基础模型在抢通用模型的活：</strong>通用模型什么都能聊，但在结构化、高噪声的领域里，一个只为这件事训练的模型往往更划算。"
        ],
        "tags": ["finance", "foundation-model", "time-series", "python", "quant"]
    },
    {
        "rank": 5,
        "owner": "headroomlabs-ai",
        "name": "headroom",
        "fullName": "headroomlabs-ai / headroom",
        "org": "headroomlabs-ai",
        "url": "https://github.com/headroomlabs-ai/headroom",
        "lang": "Python",
        "langClass": "py",
        "stars": "76,027",
        "forks": "5,911",
        "starsToday": "317",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +317★ 首登就 7.60万★！在工具输出、日志、文件和 RAG 分块进入 LLM 之前先压缩：官方称编码 Agent 省 20% token、JSON 省 60-95%，而答案不变。提供三种形态——库、代理、MCP 服务器。这是 token 优化那条线上第一个把压缩做成「前置层」的。",
        "problems": [
            "<strong>上下文被垃圾占满：</strong>日志、JSON、RAG 分块动辄几万 token，真正有用的信息被挤出去。",
            "<strong>现有压缩发生在模型侧：</strong>等 token 送到模型再优化，账单已经产生了。",
            "<strong>接法不统一：</strong>每家 Agent 的接入方式不同，压缩逻辑要重写。"
        ],
        "usage": [
            "按 README 安装（Python 项目）。",
            "选一种形态接入：作为库调用、作为代理转发，或作为 MCP 服务器挂给 Agent。",
            "让工具输出与 RAG 分块先过一遍压缩，再交给模型。"
        ],
        "insights": [
            "<strong>首登 7.6 万星：</strong>这个体量说明它在圈内已经跑了很久，只是今天才被推上日榜。工具类项目常见这种「先有用户、后有曝光」的路径。",
            "<strong>它和 xerj 是同一件事的两端：</strong>xerj 让模型少读文件，headroom 让读进来的内容先瘦身。一个减少输入量，一个提高输入密度——都比「让模型少说话」更接近根因。",
            "<strong>本质是上下文开始被当成带宽来管理：</strong>压缩、去重、分级、缓存，这些网络传输里的老概念正在搬到 LLM 的输入侧——窗口就是带宽，token 就是流量。"
        ],
        "tags": ["token-optimization", "compression", "mcp", "proxy", "python"]
    },
    # ══ 连登（出现在 10-18 榜上）══
    {
        "rank": 6,
        "owner": "MadsLorentzen",
        "name": "ai-job-search",
        "fullName": "MadsLorentzen / ai-job-search",
        "org": "MadsLorentzen",
        "url": "https://github.com/MadsLorentzen/ai-job-search",
        "lang": "Python",
        "langClass": "py",
        "stars": "55,583",
        "forks": "17,808",
        "starsToday": "3,860",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +3,860★ 直接冲到全榜第一，日增是昨天的近三倍！5.56万★ 第5次登榜（昨天 5.06万★）。一套跑在你自己机器上的求职工具，基于 Claude Code：评估招聘信息、改简历、写求职信、准备面试。作者的说明很短——fork 它，然后据为己有。",
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
            "<strong>一天从 1,365 跳到 3,860：</strong>这个加速度不正常。求职工具不会因为技术更新而突然爆量，更可能是一个外部事件——裁员新闻、招聘季、或者某个大 V 的一条帖子。星数曲线在这里测的是就业市场的温度。",
            "<strong>它连续三天的走势值得记：</strong>898 → 1,365 → 3,860，全榜都在降温，只有它在加速。当其他工具的热度退潮，唯一还在涨的是帮人找工作的那个——这个对比比任何宏观数据都直接。",
            "<strong>本质是 AI 的叙事从「替代人」转向「帮人竞争」：</strong>同样是模型能力，用在写代码上是提效，用在求职上是抢位置。需求最刚性的时候，工具会自己找到场景。"
        ],
        "tags": ["job-search", "career", "claude-code", "python", "local-first"]
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
        "stars": "97,649",
        "forks": "6,224",
        "starsToday": "1,591",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,591★，日增比昨天接近翻倍！9.76万★ 第4次登榜（昨天 9.56万★），离十万星只差 2,400。Orca 是「同时指挥一支 Agent 舰队」的地方：Grok Bot、Claude Code 之类的编码 Agent 都能跑，用你自己的订阅额度，桌面、手机、远程运行时三端可用。",
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
            "<strong>连续三天加速：</strong>1,102 → 830 → 1,591。中间回落一天又拉起来，这种走势一般出现在产品刚推了一个关键功能，或者开始有团队批量采购。",
            "<strong>离十万星只差 2,400：</strong>它会是今天榜单里最快撞线的项目。一个「调度界面」能长到这个体量，说明多 Agent 并行已经从玩法变成了工作方式。",
            "<strong>本质是 Agent 的入口从命令行挪到多端界面：</strong>CLI 服务愿意敲命令的人，多数人要的是一个能看进度、能随时接管的地方。"
        ],
        "tags": ["agent-orchestration", "multi-agent", "typescript", "desktop", "mobile"]
    },
    {
        "rank": 8,
        "owner": "anomalyco",
        "name": "opencode",
        "fullName": "anomalyco / opencode",
        "org": "anomalyco",
        "url": "https://github.com/anomalyco/opencode",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "217,271",
        "forks": "29,059",
        "starsToday": "1,310",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,310★，日增是昨天的三倍！21.73万★ 第3次登榜（昨天 21.55万★）。一句话说明：开源的编码 Agent。首登 21 万星已经很反常，现在连续三天加速，说明它不是一次曝光带来的虚火。",
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
            "<strong>三天走势 488 → 438 → 1,310：</strong>前两天在回落，今天突然拉三倍。这种形态常见于新版本发布或重要集成落地——不是自然增长，是有具体事件。",
            "<strong>它和 claude-code 连续三天同屏：</strong>今天一个 +1,310，一个 +167，差了近八倍。开源可换模型这一侧正在拿到更多注意力，至少在这个时间点上。",
            "<strong>本质是编码 Agent 的竞争回到了「谁更透明」：</strong>能力都够用之后，用户开始问能不能换模型、能不能看代码、能不能自己改。"
        ],
        "tags": ["coding-agent", "open-source", "typescript", "cli", "developer-tools"]
    },
    {
        "rank": 9,
        "owner": "akitaonrails",
        "name": "ai-memory",
        "fullName": "akitaonrails / ai-memory",
        "org": "akitaonrails",
        "url": "https://github.com/akitaonrails/ai-memory",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "10,925",
        "forks": "777",
        "starsToday": "666",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +666★，日增是昨天的近四倍，正式破一万星！1.09万★ 第5次登榜（昨天 9,994★）。给编码 Agent 的长期记忆方案，重点在「交接」：当你从一家的 Agent 换到另一家，之前积累的记忆能带过去。用 Rust 写，追求本地读写性能。",
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
            "<strong>昨天差 6 星到一万，今天直接冲到 10,925：</strong>突破整数关口本身就带传播效应——「破万」是个能被转发的数字。",
            "<strong>日增从 178 跳到 666：</strong>和 orca、opencode 同一天加速。今天的共同点是「换工具不丢东西」这类需求在集中爆发。",
            "<strong>本质是记忆正在从功能变成资产：</strong>当记忆能被导出、迁移、跨厂商带走，它就变成了用户自己的东西——谁掌握记忆的格式，谁就掌握用户换工具时的议价权。"
        ],
        "tags": ["memory", "agent-handoff", "rust", "local-first", "coding-agent"]
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
        "stars": "54,970",
        "forks": "4,967",
        "starsToday": "607",
        "count": 6,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +607★！5.50万★ 第6次登榜（昨天 5.41万★）。港大数据智能实验室的项目，口号是「让所有软件变成 Agent 原生」，配套一个 CLI-Hub 做入口。它想解决的是 Agent 会用聊天、但不会用你桌上那些专业软件的问题。",
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
            "<strong>连续三天日增上升：</strong>281 → 574 → 607。一个基础设施项目能有这种持续爬坡，说明接它的人在做具体的事，不是逛逛就走。",
            "<strong>它是今天榜单里唯一给别人铺路的项目：</strong>其他项目都在增强 Agent 自己，只有它在扩大 Agent 能触到的软件范围——前者的收益归自己，后者的收益归整个生态。",
            "<strong>本质是存量软件才是 Agent 的真正战场：</strong>新软件可以天生为 Agent 设计，但多数人每天用的还是那些老软件。"
        ],
        "tags": ["cli", "agent-native", "automation", "python", "integration"]
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
        "stars": "76,888",
        "forks": "9,078",
        "starsToday": "564",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +564★，日增比昨天回升三分之一！7.69万★ 第4次登榜（昨天 7.61万★）。作者 ruvnet 自称「最原始的 agent harness」：部署多智能体编队、协调自主工作流、搭对话式 AI 系统，带自适应记忆、自学习、联邦和向量 RAG，原生支持 Claude Code、Codex、Hermes 等。",
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
            "<strong>连续三天 672 → 420 → 564：</strong>它没有像 orca 那样爆发，但也没掉队。在一个每天换脸的榜单上稳定出现，本身就是一种位置。",
            "<strong>它和 orca 是同一个需求的两副面孔：</strong>orca 给你一个指挥舰队的地方，ruflo 给你一套编排舰队的框架——一个做界面，一个做引擎。",
            "<strong>本质是复杂度在往上走：</strong>单 Agent 好用了之后，人的胃口就变成「让一群一起干」。"
        ],
        "tags": ["multi-agent", "orchestration", "agent-harness", "typescript", "swarm"]
    }
]

# ── 规整顺序与编号：新面孔在前（按日增降序），连登在后 —— 与 app.js 双栏渲染顺序一致 ──
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

new_faces = sorted([p for p in today_projects if p['badge'] == '新面孔'], key=lambda p: -_today(p))
streaks = sorted([p for p in today_projects if p['badge'] == '连登'], key=lambda p: -_today(p))
today_projects = new_faces + streaks
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
    "date": "2026-10-19",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-19'
data['topic'] = '🔥 <strong>AI 求职工具单日爆量 + 本地图像引擎回归 + token 压缩层首次上榜</strong> —— MadsLorentzen/ai-job-search（+3,860★）一天涨 3,860 星，日增是昨天的近三倍，从 5.06万★ 冲到 5.56万★，在全榜降温的第三天上逆势加速；连续三天 898 → 1,365 → 3,860，这条曲线比任何宏观数据都直接地反映就业市场。stablyai/orca（+1,591★）第4次、离十万星只差 2,400，anomalyco/opencode（+1,310★）第3次日增翻三倍，Agent 客户端与编排层继续占位。新面孔里最值得看的是两个：Comfy-Org/ComfyUI（+1,011★）两个月后回归，13.9万★ 的本地扩散引擎，在一切往云上走的时候守着本地推理；headroomlabs-ai/headroom（+317★）首登 7.6万★，把压缩做在工具输出进入 LLM 之前，编码 Agent 省 20% token、JSON 省 60-95%，提供库、代理、MCP 三种形态——它和 xerj 正好是 token 优化的两端：一个让模型少读，一个让读进来的先瘦身。另外 akitaonrails/ai-memory（+666★）破一万星，日增翻近四倍；Kruk2/jasna（+502★）以 2,739 星挤进榜单，视频修复；shiyu-coder/Kronos（+355★）把 K 线当语言建模，三个月涨 6,800 星。今日主线：Agent 中间层继续固化，但真正在加速的是能直接换算成钱或时间的场景——求职、token 账单、修旧视频。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
assert nf <= 6 and st <= 6, f"栏位超限: 新面孔 {nf} / 连登 {st}"
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★ count={p['count']}")
