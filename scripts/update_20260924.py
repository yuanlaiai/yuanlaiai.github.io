#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-24 (1-day gap, 双栏：新面孔 6 + 连登 5)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 24)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-23 榜上）══
    {
        "rank": 1,
        "owner": "vectorize-io",
        "name": "hindsight",
        "fullName": "vectorize-io / hindsight",
        "org": "Vectorize",
        "url": "https://github.com/vectorize-io/hindsight",
        "lang": "Python",
        "langClass": "py",
        "stars": "26,888",
        "forks": "2,525",
        "starsToday": "1,607",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,607★ 登顶！会学习的 Agent 记忆系统：官方说法是「大多数记忆系统只是回放对话历史，Hindsight 要做的是让 Agent 真的学会」，在 LongMemEval 长期记忆基准上拿到最准成绩，自带 arXiv 论文、Python / JS 客户端、MCP 服务器与嵌入模式（不跑服务端也能用），另有云托管版本。",
        "problems": [
            "<strong>长对话记不住重点：</strong>上下文一长，早期关键信息就被稀释，Agent 反复问已经说过的事。",
            "<strong>RAG 只解决「找得到」：</strong>向量检索能捞出片段，不会把经验沉淀成判断。",
            "<strong>记忆散落在各处：</strong>对话历史、工具结果、项目约定各存一份，换个 Agent 就全丢。"
        ],
        "usage": [
            "起服务：<pre><code>pip install hindsight-api</code></pre>，或在 Python 里直接用嵌入式模式。",
            "接客户端：<pre><code>pip install hindsight-client</code></pre> 或 npm 包，两行代码包住 LLM 调用即可接入。",
            "给 Agent 挂 MCP 服务器，或用官方的 coding agent 集成。"
        ],
        "insights": [
            "<strong>它把「记忆」从存储问题改成学习问题：</strong>retain / recall / reflect 三个操作加上「观察」与「心智模型」，本质是让 Agent 把经历压缩成结论，而不是把原文再喂一遍。",
            "<strong>基准、论文、多云客户端一次配齐：</strong>开源仓库 + 云托管 + 客户端 SDK 的组合，是这两年被验证过的分发打法——先占住开发者的默认选择，再卖托管。",
            "<strong>本质是上下文经济的拐点：</strong>上下文窗口再大也是按 token 计费的，而「学会」是压缩——谁能把经历压成更少 token 而不丢判断，谁就同时赢了能力和成本。"
        ],
        "tags": ["agent-memory", "ai-agents", "longmemEval", "mcp", "python"]
    },
    {
        "rank": 2,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra (Jesse Vincent)",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "290,968",
        "forks": "26,034",
        "starsToday": "474",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +474★！29.1 万星（2.6 万 fork）的巨兽：一套完整的软件开发方法论 + 可组合技能包，插进 coding agent 之后，它不会直接开始写代码——先追问你到底要做什么，把设计分块给你确认，再产出细到「热情但没品味的新人也能照做」的实施计划，然后启动子代理开发流程，逐任务执行、逐任务复查。",
        "problems": [
            "<strong>Agent 上来就写代码：</strong>需求还没讲清，它已经改了三个文件，回头看全是返工。",
            "<strong>计划太粗：</strong>「实现登录功能」这种任务丢给 Agent，等于让它自由发挥。",
            "<strong>没人验收：</strong>Agent 说做完了，你只能自己一行行看，或者干脆信了。"
        ],
        "usage": [
            "按 README 安装插件（Claude Code、Codex、Cursor、Gemini CLI、OpenCode、Hermes Agent 等近二十种 harness 都有入口）。",
            "正常提需求即可——brainstorming、writing-plans、TDD 等技能会按流程自动触发。",
            "设计确认后选择子代理逐任务开发（更严）或在当前会话内逐任务执行（更省），最后统一走代码复查。"
        ],
        "insights": [
            "<strong>29 万星说明「方法论」比「工具」更稀缺：</strong>它提供的东西没有一行是模型能力，全是流程纪律——测试先行、YAGNI、证据高于断言，却成了这个体量最大的项目之一。",
            "<strong>它把 Agent 的自主时间从分钟拉到小时级：</strong>官方说法是有时能按计划自主干上几个小时不跑偏——计划细度和强制复查是自主的前提，不是结果。",
            "<strong>本质是「把工程师的习惯写成机器能执行的规矩」：</strong>测试先行、计划先行、复查先行，过去靠团队文化维持，现在被写成技能——软件工程的纪律正在从人的自律变成 Agent 的默认配置。"
        ],
        "tags": ["agent-skills", "tdd", "subagents", "methodology", "claude-code"]
    },
    {
        "rank": 3,
        "owner": "rohitg00",
        "name": "ai-engineering-from-scratch",
        "fullName": "rohitg00 / ai-engineering-from-scratch",
        "org": "rohitg00",
        "url": "https://github.com/rohitg00/ai-engineering-from-scratch",
        "lang": "Python",
        "langClass": "py",
        "stars": "55,879",
        "forks": "9,865",
        "starsToday": "310",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +310★ 首登！5.6 万星的手写课程：523 节课、20 个阶段、约 342 小时，覆盖 Python / TypeScript / Rust / Julia，从零实现到部署；每节课都产出一个可复用产物（提示词、技能、Agent、MCP 服务器）。作者引用数据是「84% 的学生已经在用 AI 工具，只有 18% 觉得自己能专业地用」——这份课程就是补这个差。近 30 天 11.4 万读者、18.2 万次页面浏览。",
        "problems": [
            "<strong>会用工具不等于会做系统：</strong>会写提示词的人很多，能从零搭出检索、评测、部署链路的很少。",
            "<strong>教程只讲不敢动手：</strong>大部分课程停在概念和 API 调用，不碰底层实现。",
            "<strong>学完没有作品：</strong>刷完课手上空空，面试与项目都拿不出东西。"
        ],
        "usage": [
            "挑一个目标（从零打基础 / 直接做 Agent / 专攻某个方向）而不是从头刷 523 课。",
            "按阶段推进，每节课跟着实现并留下可复用产物。",
            "支持十二种语言的落地页与机器翻译课程页，中文读者可直接看简体中文入口。"
        ],
        "insights": [
            "<strong>它把教学做成了供应链：</strong>523 节课、20 阶段、四种语言、每节一个可交付物——这种规模不是个人写博客的量级，而是把「从零学 AI」当成产品在迭代。",
            "<strong>与前一位上榜者构成同一条线：</strong>一个教人怎么用 Agent 做工程（superpowers），一个教人怎么从零造 AI 系统（本课程）——技能缺口已经从「会用工具」转向「理解系统」。",
            "<strong>本质是知识产品的重组：</strong>当「AI 工程师」成为岗位，培训市场会先于教育体系反应——523 节课背后是招聘需求在倒逼课程结构，而不是反过来。"
        ],
        "tags": ["education", "ai-engineering", "course", "llm", "mcp"]
    },
    {
        "rank": 4,
        "owner": "FxEmbed",
        "name": "FxEmbed",
        "fullName": "FxEmbed / FxEmbed",
        "org": "FxEmbed",
        "url": "https://github.com/FxEmbed/FxEmbed",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "5,252",
        "forks": "242",
        "starsToday": "165",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +165★！今天榜上唯一的「非 AI」项目：把 X / Twitter 与 Bluesky 链接里的视频、投票、引用、翻译完整还原到 Discord、Telegram 等平台——只要在链接前加 fx 或 fixup（FxTwitter / FixupX / FxBluesky 三个服务同源），支持自托管与 Docker 部署、Crowdin 多语言本地化。",
        "problems": [
            "<strong>平台故意简化嵌入：</strong>视频看不了、投票点不动、翻译缺失，跨平台转发等于内容残缺。",
            "<strong>想转发得先截图：</strong>为了让人看见完整内容，只能手动截图重发一遍。",
            "<strong>商业替代品收钱：</strong>把嵌入修好这件事，长期被当成付费功能卖。"
        ],
        "usage": [
            "把 <pre><code>twitter.com</code></pre> 换成 <pre><code>fxtwitter.com</code></pre>，把 x.com 换成 fixupx.com，Bluesky 链接前加 fx。",
            "粘到 Discord / Telegram 里即自动展开完整内容。",
            "有 Docker 与自托管文档，团队可内部部署，也有人用它的 API 做二次开发。"
        ],
        "insights": [
            "<strong>2022 年建仓的老工具再次上榜：</strong>四年里平台改过多次嵌入规则，它就一次次补回来——「维护一个别人不肯维护的小事」本身能积累五万星。",
            "<strong>与 lap 组成今天的非 AI 一栏：</strong>一个修跨平台内容完整性，一个做离线相册——都在处理「内容在别人平台上会变形或丢失」这个共同问题。",
            "<strong>本质是平台化时代的下水道工程：</strong>大平台没有动力修好跨平台体验，于是自托管的小服务填补空白——这类项目不性感，但一旦停摆，无数社区的日常分享立刻退化。"
        ],
        "tags": ["embed", "discord", "telegram", "self-hosted", "bluesky"]
    },
    {
        "rank": 5,
        "owner": "strands-agents",
        "name": "harness-sdk",
        "fullName": "strands-agents / harness-sdk",
        "org": "strands-agents",
        "url": "https://github.com/strands-agents/harness-sdk",
        "lang": "Python",
        "langClass": "py",
        "stars": "8,057",
        "forks": "1,216",
        "starsToday": "115",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +115★！「harness」正式做成 SDK：官方定位是「当你本来要自己写 agent 循环时，改用这个」——跑在你自己的进程里，没有托管控制面，一个 SDK 覆盖回合上限、token 预算、取消、停止原因等生命周期控制，加上工具调用、结构化输出、MCP、多 Agent 模式、记忆与会话、模型可移植与流式输出、护栏。Python 与 TypeScript 双语，任何模型、任何云。",
        "problems": [
            "<strong>手写 agent 循环越写越乱：</strong>一开始只要调用工具，半年后长出重试、超时、预算控制、会话恢复。",
            "<strong>被托管平台绑死：</strong>用厂商的托管编排服务，模型和云都换不了，数据还要出境。",
            "<strong>看不见花了多少：</strong>没有 token 预算与停止原因，跑飞了才发现账单。"
        ],
        "usage": [
            "安装 SDK：<pre><code>pip install strands-agents</code></pre>（或用 TypeScript 包）。",
            "配置模型供应商，定义工具与结构化输出。",
            "接上 MCP 服务器、记忆与会话管理，用回合上限与 token 预算给 Agent 设边界。"
        ],
        "insights": [
            "<strong>「harness」这个词今天在榜上出现两次：</strong>univer 把自己叫做 Office Harness，strands 直接把 harness 做成 SDK——从「框架」「编排」到「harness」，Agent 的运行时抽象正在收敛成一个正式品类。",
            "<strong>「没有托管控制面」是被强调的卖点：</strong>官方把「跑在你自己的进程里」写在第一段——企业要的不是能力更强，而是模型可换、数据不出境、账单可控。",
            "<strong>本质是接力棒从云厂商手里被抢：</strong>上一代平台靠托管编排锁定客户，这一代把编排重新塞回用户进程——同样的功能，归属权换了一边。"
        ],
        "tags": ["agent-harness", "sdk", "mcp", "bedrock", "multi-agent"]
    },
    {
        "rank": 6,
        "owner": "julyx10",
        "name": "lap",
        "fullName": "julyx10 / lap",
        "org": "julyx10",
        "url": "https://github.com/julyx10/lap",
        "lang": "Vue",
        "langClass": "vue",
        "stars": "2,669",
        "forks": "165",
        "starsToday": "71",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +71★ 首登！本地优先的开源相册管理器：浏览家庭相册、快速找回老照片、离线管理大型个人媒体库——不强制上传、本地 AI 搜索、以文件夹为中心的流程，macOS（已公证）/ Windows / Linux 三端安装包齐全，装了十种语言的说明文档。",
        "problems": [
            "<strong>云相册强制上传：</strong>家人的照片存在别人的服务器上，隐私与费用都不由自己。",
            "<strong>图库一大就卡：</strong>几十万张照片的检索、去重、人脸分组，云端服务也会变慢或催你升级。",
            "<strong>换平台就搬家：</strong>照片锁在某家生态里，迁移一次要折腾好几天。"
        ],
        "usage": [
            "从 Releases 页面下载对应系统的安装包（macOS 有公证版，Linux 提供 deb 与 AppImage）。",
            "指向本地照片文件夹，让它建立索引。",
            "用本地 AI 搜索找人找物、用重复检测与人脸分组整理老库，全程离线。"
        ],
        "insights": [
            "<strong>它是「自持」这条线的又一票：</strong>与昨天的 univer、前几天的离线知识服务器、自持行情平台同一条脉络——数据从云上撤回本地，已经连续多日占据榜单。",
            "<strong>本地 AI 是关键变量：</strong>过去「离线」意味着功能残缺，现在人脸识别与语义搜索都能在本机跑，隐私与能力第一次不再互斥。",
            "<strong>本质是基础设施的隐形成本被看见：</strong>云相册的真正代价不是订阅费，而是「你的记忆存放在别人的商业模式里」——当本地算力足够，这笔账就没人愿意再付。"
        ],
        "tags": ["photo-manager", "local-first", "privacy", "offline", "tauri"]
    },
    # ══ 连登（09-23 已在榜）══
    {
        "rank": 7,
        "owner": "google",
        "name": "ax",
        "fullName": "google / ax",
        "org": "Google",
        "url": "https://github.com/google/ax",
        "lang": "Go",
        "langClass": "go",
        "stars": "9,653",
        "forks": "475",
        "starsToday": "1,543",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +1,543★（7,525★ → 9,653★）！Google 的声明式 Agent 编排器：Task / Workspace / Gateway / Model 四原语，kubectl 式 CLI（apply / watch / ssh / suspend / resume），把 Agent 当「第三种工作负载」——既不是无状态微服务，也不是跑完就退出的批处理。",
        "problems": [
            "<strong>Agent 断了只能重来：</strong>四十分钟的任务中途失败，既不知道做到哪一步也没法接着做。",
            "<strong>沙箱要自己拼：</strong>容器隔离、网络白名单、凭证轮换、闲置成本，全得自己写。",
            "<strong>规模上去就失控：</strong>几百个 Agent 同时在集群里跑，没有统一的调度与生命周期管理。"
        ],
        "usage": [
            "装 CLI：<pre><code>go install github.com/google/ax/cmd/ax@latest</code></pre>",
            "写一份 YAML（Workspace + Task）后 <pre><code>ax apply -f task.yaml</code></pre>",
            "用 <pre><code>ax watch</code></pre> 看状态、<pre><code>ax ssh</code></pre> 进沙箱、<pre><code>ax suspend / ax resume</code></pre> 挂起与续跑。需要自备 Kubernetes 集群与镜像仓库。"
        ],
        "insights": [
            "<strong>连登第二天，日增仍在 1,500★ 以上：</strong>7,525 → 9,653，说明热度的来源不是发布当天的曝光，而是「Agent 该住在哪」这个问题本身积压得够久。",
            "<strong>它与昨天的底座同台、今天与金融套件同台：</strong>两天里调度层、沙箱层、行业成品轮流被看见——这一层的基础设施正在被整体估值。",
            "<strong>本质是编排权的争夺：</strong>「Agent 跑在谁的调度器上」比「用谁的模型」更靠前——模型可换，调度器难换。"
        ],
        "tags": ["ai-agents", "orchestration", "kubernetes", "golang", "google"]
    },
    {
        "rank": 8,
        "owner": "dream-num",
        "name": "univer",
        "fullName": "dream-num / univer",
        "org": "dream-num",
        "url": "https://github.com/dream-num/univer",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "16,941",
        "forks": "1,489",
        "starsToday": "1,142",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +1,142★（15,352★ → 16,941★）！2022 年建仓的开源 Office SDK，简介改成了「The Office Harness for AI Agents」：表格、文档、幻灯片、画布、关系表、PDF 一套运行时，Canvas 渲染 + 公式引擎 + 插件架构 + 浏览器与 Node 同构的 Facade API。",
        "problems": [
            "<strong>Office 能力嵌不进产品：</strong>想在自己应用里放一张能算的表格，商业组件贵、开源组件弱。",
            "<strong>模型读不懂文件结构：</strong>Agent 能写代码，却常常读不出表格里的公式依赖与文档层级。",
            "<strong>两端渲染不一致：</strong>浏览器算一遍、服务端再算一遍，结果还对不上。"
        ],
        "usage": [
            "安装：<pre><code>npm install @univerjs/presets</code></pre>",
            "用 Facade API 在浏览器或 Node 端创建表格、文档、幻灯片实例。",
            "按需要挂插件扩展公式、协同或自定义渲染。"
        ],
        "insights": [
            "<strong>连登且日增从 202★ 跳到 1,142★：</strong>涨了五倍多，说明改简介这件事被看见了——「Agent 的办公桌」这个定位比「开源 Office」好卖得多。",
            "<strong>它与 harness-sdk 同一天在榜：</strong>一个把 Office 叫 harness，一个把 Agent 运行时做成 harness SDK——同一天两个项目抢同一个词，说明品类认知已经形成。",
            "<strong>本质是资产重定价：</strong>代码没怎么变，叙事换了就回榜——在技术周期切换时，最先受益的往往不是新项目，而是那些早就把事做好、只差一个说法的老项目。"
        ],
        "tags": ["office-sdk", "spreadsheet", "typescript", "ai-agents", "chinese"]
    },
    {
        "rank": 9,
        "owner": "anthropics",
        "name": "financial-services",
        "fullName": "anthropics / financial-services",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/financial-services",
        "lang": "Python",
        "langClass": "py",
        "stars": "37,187",
        "forks": "5,407",
        "starsToday": "664",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +664★（36,304★ → 37,187★）！模型公司卖行业成品：投行、股票研究、私募与财富管理的参考 Agent、技能与数据连接器——Pitch Agent（路演材料）、Market Researcher、GL Reconciler（总账对账），附 /comps、/dcf 等斜杠命令。一套源码两种交付：Cowork 插件，或走 Managed Agents API 部署在你自己的流程引擎后面。",
        "problems": [
            "<strong>行业 Agent 从零搭：</strong>模型会写代码，但不知道 pitch book 该怎么组织、估值模型该怎么摆。",
            "<strong>数据接口各接各的：</strong>行情、财报、内部总账三套接口，接一次换一次。",
            "<strong>合规没人担责：</strong>Agent 直接给结论，出错没有审计链条。"
        ],
        "usage": [
            "作为 Claude Cowork 插件安装，或按 managed-agent-cookbooks 走 <pre><code>/v1/agents</code></pre> 部署。",
            "按垂直行业挑选技能与斜杠命令（如 /comps 可比公司、/dcf 现金流折现）。",
            "接上数据连接器后让 Agent 起草备忘录、模型与对账表，每步停在人工签字前。"
        ],
        "insights": [
            "<strong>连登第二天仍在 600★ 以上：</strong>说明行业套件的需求不是好奇，而是排队——金融机构不缺模型，缺的是能进流程的成品。",
            "<strong>免责声明比功能介绍更有信息量：</strong>明确写「不做投资建议、不执行交易、不记总账、不批准开户」，所有产出停在待签核——合规边界被当成产品说明来写。",
            "<strong>本质是劳动分工重排：</strong>初级分析师做的活被拆成可安装的技能包，人的位置后移到复核与签字——这不是替代，是审计链条上谁先动笔的重新分配。"
        ],
        "tags": ["financial-services", "ai-agents", "claude", "enterprise", "skills"]
    },
    {
        "rank": 10,
        "owner": "mvt-project",
        "name": "mvt",
        "fullName": "mvt-project / mvt",
        "org": "mvt-project",
        "url": "https://github.com/mvt-project/mvt",
        "lang": "Python",
        "langClass": "py",
        "stars": "14,594",
        "forks": "1,390",
        "starsToday": "543",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +543★（14,067★ → 14,594★）！Amnesty International 安全实验室 2021 年随「Pegasus 计划」发布的移动取证工具：在 Android / iOS 上找出间谍软件痕迹；本轮热度的直接原因是 v3 分支合并带来破坏性变更，依赖它输出的脚本需要改造。",
        "problems": [
            "<strong>被入侵查不出来：</strong>商业间谍软件的痕迹藏在系统日志与配置文件里，普通人连入口都不知道在哪。",
            "<strong>取证门槛高：</strong>需要命令行与数字取证经验，当事人无法自证清白。",
            "<strong>证据稍纵即逝：</strong>设备一重启或一升级，关键日志就可能被清掉。"
        ],
        "usage": [
            "安装：<pre><code>pip install mvt</code></pre>",
            "备份设备后跑 <pre><code>mvt-ios check-backup --iocs STIX2_FILE ./backup</code></pre>",
            "对照 IOC 指标（如 Pegasus 的 STIX2 文件）定位可疑进程与配置。"
        ],
        "insights": [
            "<strong>连登说明「升级即事件」：</strong>一个维护五年的取证工具靠破坏性变更连续两天在榜——老基建的接口变更会波及整条下游，这个影响面本身就是热度来源。",
            "<strong>它和 superpowers 形成今天的两个极端：</strong>一个教 Agent 守规矩，一个查人是否被监控——都在回答「怎么证明发生了什么」，只是对象一个是机器，一个是权力机构。",
            "<strong>本质是证据能力的民主化：</strong>Amnesty 把最贵的取证方法开源，把「谁能证明自己被监控」从机构特权变成可复制流程——监控工具按目标收费，反制工具免费开放，这本身就是答案。"
        ],
        "tags": ["forensics", "security", "ios", "android", "amnesty"]
    },
    {
        "rank": 11,
        "owner": "superdesigndev",
        "name": "treg",
        "fullName": "superdesigndev / treg",
        "org": "Superdesign",
        "url": "https://github.com/superdesigndev/treg",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,928",
        "forks": "250",
        "starsToday": "506",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +506★（2,191★ → 2,928★）！自称「Agent 工具的 OpenRouter」：一个 base URL、一个 token 调用 3,000+ 端点、60+ 供应商（SEO 外链、社媒趋势、人物与公司信息、广告、抓取、图像与视频生成），按次计价低至一美分，无需逐个注册；团队密钥与 CL​I 存服务端，凭证不出服务器，可自托管。",
        "problems": [
            "<strong>好工具都锁在订阅墙后：</strong>Semrush $139/月、Moz $99/月、Crunchbase $99/月、Apollo $59/座——为跑一次任务买一个月不划算。",
            "<strong>有些工具没有公开 API：</strong>邀请制、合作方制、应用审核制，Agent 连门票都没有。",
            "<strong>密钥散落各处：</strong>团队的 key 分布在多台机器与多份 Agent 配置里，谁用了多少没人说得清。"
        ],
        "usage": [
            "自托管：<pre><code>git clone https://github.com/superdesigndev/treg.git</code></pre>",
            "把 Agent 的 base URL 指向 treg，配一个 token。",
            "按「任务」而非「工具」检索调用，费用按次从团队预付余额扣除。"
        ],
        "insights": [
            "<strong>连登第二天，日增从 197★ 涨到 506★：</strong>升温而不是衰减，说明「Agent 要去哪买工具」这个问题被越来越多团队认可为真需求。",
            "<strong>它和 Strands 的「没有托管控制面」是同一枚硬币：</strong>一个把编排收回自己进程，一个把供应商账号收回自己服务器——企业买的是控制权，不是能力。",
            "<strong>本质是订阅制的拆解：</strong>SaaS 靠包月把轻度用户变成稳定收入，Agent 一来调用方变成机器、用量不可预测——按次计价的中间层会越来越多。"
        ],
        "tags": ["ai-agents", "registry", "credentials", "mcp", "developer-tools"]
    }
]

# 规整顺序与编号：新面孔在前（按日增降序），连登在后 —— 与 app.js 双栏渲染顺序一致
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

new_faces = sorted([p for p in today_projects if p['badge'] == '新面孔'], key=lambda p: -_today(p))
streaks = sorted([p for p in today_projects if p['badge'] == '连登'], key=lambda p: -_today(p))
today_projects = new_faces + streaks
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels for 1-day gap
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
    "date": "2026-09-24",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-24'
data['topic'] = '🔥 <strong>Agent 记忆登顶 + 「harness」正式成为品类词 + 技能框架长成 29 万星巨兽</strong> —— vectorize-io/hindsight（+1,607★）榜首：会学习的 Agent 记忆系统，LongMemEval 长期记忆基准最准，自带论文与云托管。obra/superpowers（+474★）29.1 万星：从头脑风暴、写计划、TDD 到子代理开发的完整方法论，支持近二十种 coding agent。rohitg00/ai-engineering-from-scratch（+310★）5.6 万星：523 节课、20 阶段、约 342 小时，每节产出一个可复用产物。strands-agents/harness-sdk（+115★）把 agent harness 做成 SDK：跑在自己进程里、没有托管控制面、任何模型任何云。julyx10/lap（+71★）离线相册与 FxEmbed（+165★）修跨平台嵌入，是今天两个非 AI 项目。连登：google/ax（+1,543★）9,653★、dream-num/univer（+1,142★）16,941★、anthropics/financial-services（+664★）37,187★、mvt-project/mvt（+543★）、superdesigndev/treg（+506★）。今日三条主线：一、记忆成为 Agent 竞赛的新战场——不是更长的上下文，而是会沉淀的学习；二、「harness」一天内出现两次（univer 的 Office Harness、strands 的 harness-sdk），运行时抽象正在收敛成正式品类；三、纪律与知识在工业化——29 万星的技能方法论与 523 节手写课程，说明「教 Agent 怎么干活」已经变成基础设施。'

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
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
