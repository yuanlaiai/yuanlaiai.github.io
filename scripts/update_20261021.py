#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-21 (2-day gap, 无昨日榜→平铺结构, 13 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 21)
gap_days = (today - last).days  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（2天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "MadsLorentzen",
        "name": "ai-job-search",
        "fullName": "MadsLorentzen / ai-job-search",
        "org": "MadsLorentzen",
        "url": "https://github.com/MadsLorentzen/ai-job-search",
        "lang": "Python",
        "langClass": "py",
        "stars": "62,264",
        "forks": "19,238",
        "starsToday": "3,131",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,131★ 连续第五天日增破千，两天又涨 6,681★！6.23万★ 第6次登榜。一套跑在自己机器上的求职工具，基于 Claude Code：评估招聘信息、改简历、写求职信、准备面试。作者的说明很短——fork 它，然后据为己有。",
        "problems": [
            "<strong>投简历是体力活：</strong>一份 JD 改一版简历、写一封求职信，投十家就是十遍重复劳动。",
            "<strong>工具要交出你的数据：</strong>在线求职平台要你的履历、联系方式和投递记录。",
            "<strong>通用 AI 不懂岗位：</strong>直接让模型改简历，容易写成一套漂亮但没有针对性的空话。"
        ],
        "usage": [
            "克隆仓库并在本地配置（Python，基于 Claude Code）。",
            "喂给它目标岗位的招聘信息，让它评估匹配度。",
            "按岗位定制简历与求职信，准备面试问题。"
        ],
        "insights": [
            "<strong>五天走势 898 → 1,365 → 3,860 → 3,131 → 现在这个位置：</strong>中间回落过一次，又立刻拉回来。这种曲线不像一次性曝光，更像需求在持续释放，有人用完又推荐给同一批处境相似的人。",
            "<strong>今天它有了同伴：</strong>同榜还出现一个开源求职搜索引擎 freehire。两个求职工具同时上榜，说明这不是单个项目的运气，是一个正在扩大的需求面。",
            "<strong>本质是 AI 叙事从「替代人」转到「帮人抢位置」：</strong>同样的模型能力，用在写代码上是提效，用在求职上是竞争。需求最刚性的时候，工具会自己找到场景。"
        ],
        "tags": ["job-search", "career", "claude-code", "python", "local-first"]
    },
    {
        "rank": 2,
        "owner": "DietrichGebert",
        "name": "ponytail",
        "fullName": "DietrichGebert / ponytail",
        "org": "DietrichGebert",
        "url": "https://github.com/DietrichGebert/ponytail",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "170,775",
        "forks": "9,287",
        "starsToday": "2,051",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,051★ 首登就 17.08万★！让 AI agent 像屋里最懒的那个资深开发一样思考。仓库说明只有一句主张：最好的代码，是你从来没写过的代码。在一个所有人都在比谁能生成更多代码的年份，它反着来。",
        "problems": [
            "<strong>生成太多用不完：</strong>agent 一开口就是几百行，接进来之后没人看得完，也删不掉。",
            "<strong>代码量被当成产出：</strong>评审、测试、维护的成本全跟着行数走，写得越多欠得越多。",
            "<strong>年轻工程师的直觉被压掉：</strong>模型倾向于「先写点什么」，而不是先判断这件事该不该做。"
        ],
        "usage": [
            "把技能接入支持 Agent Skills 的编码工具。",
            "在开工前让 agent 先判断需求是否必要、能否用现有代码解决。",
            "让它优先给出删除、复用、配置化的方案，最后才考虑新写一个模块。"
        ],
        "insights": [
            "<strong>17 万星的项目，核心主张是「少写」：</strong>这个体量说明它已经不只是个玩笑。「最懒的资深开发」在现实里就是那个会问你「这功能非做不可吗」的人，而模型恰恰不会问。",
            "<strong>它和同榜的 cloudflare 安全审计、求职工具构成一组：</strong>三个日增最高的项目，一个帮你挑机会，一个帮你少写，一个帮你验证。生成过剩之后，这三种需求同时浮上来。",
            "<strong>本质是评价标准在往回摆：</strong>这一年比的是谁能生成更多，下一段可能比谁能删掉更多。写得快是能力，判断该不该写是判断力，后者目前还没法外包。"
        ],
        "tags": ["agent-skill", "code-quality", "javascript", "minimalism", "developer-tools"]
    },
    {
        "rank": 3,
        "owner": "cloudflare",
        "name": "security-audit-skill",
        "fullName": "cloudflare / security-audit-skill",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "35,152",
        "forks": "2,211",
        "starsToday": "1,997",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,997★，日增是上次上榜时的十倍！3.52万★ 第5次登榜（9 月中 1.75万★，一个月翻倍）。Cloudflare 出的编码 agent 技能：多阶段安全审计，每个结论都要独立验证，并且输出机器可读的结果。",
        "problems": [
            "<strong>AI 写的代码没人验：</strong>生成速度快了十倍，安全评审还停在人工抽样。",
            "<strong>审计结论不可信：</strong>模型说「这里可能有注入」，没有证据链，工程师只能重查一遍。",
            "<strong>报告不能进流水线：</strong>自然语言写一堆，CI 读不了，也就没法卡住合并。"
        ],
        "usage": [
            "把技能装进支持 Agent Skills 的编码工具（Claude Code、Cursor、Codex 等）。",
            "在提交前或 CI 里触发多阶段审计，让每个发现都附上可验证的证据。",
            "读取机器可读的结果，接进流水线做阻断或分级处理。"
        ],
        "insights": [
            "<strong>一个月从 1.75 万涨到 3.52 万，今天日增翻十倍：</strong>安全审计这个品类过去一年一直不温不火，突然放量通常意味着一批团队开始把 AI 代码正式推上生产，评审流程得跟着补。",
            "<strong>「独立验证 + 机器可读」是它和普通审计提示词的分界：</strong>前者解决信任，后者只解决产出。模型说有问题不算数，能复现才算。",
            "<strong>本质是验证成本正在成为新的瓶颈：</strong>生成变便宜之后，确认生成物没问题的成本没降，反而因为量大了更高。谁把这部分自动化，谁就拿到了下一段的地基。"
        ],
        "tags": ["security", "agent-skill", "audit", "javascript", "devsecops"]
    },
    {
        "rank": 4,
        "owner": "stablyai",
        "name": "orca",
        "fullName": "stablyai / orca",
        "org": "Stably AI",
        "url": "https://github.com/stablyai/orca",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "100,584",
        "forks": "6,359",
        "starsToday": "1,543",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,543★，正式突破十万星！10.06万★ 第5次登榜（两天前 9.76万★）。Orca 是「同时指挥一支 Agent 舰队」的地方：Grok Bot、Claude Code 之类的编码 Agent 都能跑，用你自己的订阅额度，桌面、手机、远程运行时三端可用。",
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
            "<strong>破十万星，用了大约两个月：</strong>从 8 月的 4.38 万到现在，翻了一倍多。一个调度界面能长到这个量级，说明多 Agent 并行已经从玩法变成工作方式。",
            "<strong>它连续四天上榜且日增稳定在千级以上：</strong>这类工具没有模型发布那种爆发力，能维持这个斜率，靠的是团队客户在陆续接入。",
            "<strong>本质是 Agent 的入口从命令行挪到多端界面：</strong>CLI 服务愿意敲命令的人，多数人要的是一个能看进度、能随时接管的地方。"
        ],
        "tags": ["agent-orchestration", "multi-agent", "typescript", "desktop", "mobile"]
    },
    {
        "rank": 5,
        "owner": "Graphify-Labs",
        "name": "graphify",
        "fullName": "Graphify-Labs / graphify",
        "org": "Graphify-Labs",
        "url": "https://github.com/Graphify-Labs/graphify",
        "lang": "Python",
        "langClass": "py",
        "stars": "130,981",
        "forks": "12,588",
        "starsToday": "1,434",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,434★！13.10万★ 第4次登榜（7 月中 8.77万★，三个月涨了 4.3 万）。把整个代码库连同文档、SQL schema、配置文件、PDF 一起，转成一张可查询的知识图谱。以 /graphify 技能的形式接入 Claude Code、Cursor、Codex。",
        "problems": [
            "<strong>Agent 只能逐文件读：</strong>代码、文档、schema 分散在几种格式里，模型一次只能看一小块。",
            "<strong>关系比内容更重要：</strong>一个字段被谁写入、被哪个服务读走，散在三个地方，grep 拼不出来。",
            "<strong>上下文预算有限：</strong>把整个仓库塞进去不现实，只能靠人挑，挑错就白跑一轮。"
        ],
        "usage": [
            "按 README 安装（Python 项目）。",
            "对整个仓库跑一次索引，生成知识图谱。",
            "在 Claude Code / Cursor / Codex 里用 /graphify 查询，让 agent 按关系而不是按文件找答案。"
        ],
        "insights": [
            "<strong>三个月涨 4.3 万星：</strong>它不是新项目，是这个方向的先行者。这类工具的价值随代码库规模线性增长，团队越大越离不开。",
            "<strong>它和 headroom 是同一件事的两种做法：</strong>headroom 压缩输入，graphify 重建结构。一个把内容变短，一个让模型按关系跳跃，目标都是让有限的窗口装下更多有效信息。",
            "<strong>本质是给 Agent 造一张地图：</strong>模型不缺阅读能力，缺的是「该读哪里」的判断。图谱把这份判断预先算好，省掉的是试错。"
        ],
        "tags": ["knowledge-graph", "codebase", "agent-skill", "python", "rag"]
    },
    {
        "rank": 6,
        "owner": "Comfy-Org",
        "name": "ComfyUI",
        "fullName": "Comfy-Org / ComfyUI",
        "org": "Comfy Org",
        "url": "https://github.com/Comfy-Org/ComfyUI",
        "lang": "Python",
        "langClass": "py",
        "stars": "141,232",
        "forks": "16,702",
        "starsToday": "914",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +914★！14.12万★ 第3次登榜（两天前 13.92万★）。最有名的扩散模型图形界面：节点式工作流、API 与后端一体，官方自称「世界上最快的本地推理引擎」。在什么都往云上跑的这两年，它一直守着本地这一侧。",
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
            "<strong>连续三天在榜，日增稳在九百以上：</strong>它不是靠一次发布冲上来的，而是被持续使用。这类基础设施型项目的上榜频率，比新模型更能反映真实工作量。",
            "<strong>它和今天的安全审计、知识图谱构成一个反差：</strong>榜单上多数项目在优化「怎么用模型」，它在守「模型跑在谁的机器上」。",
            "<strong>本质是本地推理是最后一道保险：</strong>当模型、API、内容策略都由别人控制时，能自己跑一份完整管线，本身就是一种议价能力。"
        ],
        "tags": ["diffusion", "comfyui", "image-generation", "local-first", "python"]
    },
    {
        "rank": 7,
        "owner": "akitaonrails",
        "name": "ai-memory",
        "fullName": "akitaonrails / ai-memory",
        "org": "akitaonrails",
        "url": "https://github.com/akitaonrails/ai-memory",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "12,043",
        "forks": "854",
        "starsToday": "810",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +810★，日增又回到四位数附近！1.20万★ 第6次登榜（两天前 1.09万★）。给编码 Agent 的长期记忆方案，重点在「交接」：当你从一家的 Agent 换到另一家，之前积累的记忆能带过去。用 Rust 写，追求本地读写性能。",
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
            "<strong>第6次登榜，日增稳在七八百：</strong>它没有爆发式增长，但一直在。记忆类工具的曲线就是这样，一旦装进工作流，用户不会轻易卸载。",
            "<strong>它的定位仍然是最锋利的那一句：</strong>承认用户会换 Agent，并把「换的时候别失忆」做成产品。厂商不会做这件事，第三方做正好。",
            "<strong>本质是记忆正在从功能变成资产：</strong>当记忆能被导出、迁移、跨厂商带走，它就变成了用户自己的东西。"
        ],
        "tags": ["memory", "agent-handoff", "rust", "local-first", "coding-agent"]
    },
    {
        "rank": 8,
        "owner": "shiyu-coder",
        "name": "Kronos",
        "fullName": "shiyu-coder / Kronos",
        "org": "shiyu-coder",
        "url": "https://github.com/shiyu-coder/Kronos",
        "lang": "Python",
        "langClass": "py",
        "stars": "42,611",
        "forks": "7,045",
        "starsToday": "570",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +570★！4.26万★ 第4次登榜（两天前 4.14万★），连续两次上榜。Kronos：面向金融市场的「语言」基础模型，把 K 线、成交量这些行情数据当成一种语言来建模，而不是套用通用大模型。",
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
            "<strong>连续两次上榜：</strong>金融 AI 项目通常和市场行情同涨同跌，能在没有大行情的时候连续出现，说明它的用户是研究者，不是追涨的散户。",
            "<strong>「把行情当语言」是它的关键设计：</strong>先把 K 线离散成 token，再按语言模型的方式训练。领域模型的正确做法往往始于重新定义输入。",
            "<strong>本质是垂直基础模型在抢通用模型的活：</strong>通用模型什么都能聊，但在结构化、高噪声的领域里，一个只为这件事训练的模型更划算。"
        ],
        "tags": ["finance", "foundation-model", "time-series", "python", "quant"]
    },
    {
        "rank": 9,
        "owner": "supabase",
        "name": "supabase",
        "fullName": "supabase / supabase",
        "org": "Supabase",
        "url": "https://github.com/supabase/supabase",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "112,641",
        "forks": "16,826",
        "starsToday": "509",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +509★ 首次登榜！11.26万★。Supabase：基于 Postgres 的开发平台，给你一个专属数据库，用来搭 Web、移动端和 AI 应用。日增不高，但它出现在一张 AI 榜单上，说明又有一批人在搭新东西。",
        "problems": [
            "<strong>后端从零搭太慢：</strong>数据库、鉴权、存储、API 各配一遍，一周就没了。",
            "<strong>AI 应用需要向量与关系混用：</strong>纯向量库解决不了业务表之间的关联。",
            "<strong>托管服务锁死：</strong>数据和逻辑都在别人平台上，迁走成本高。"
        ],
        "usage": [
            "按 README 自托管，或直接用云版本。",
            "用 Postgres 建表，需要向量检索时装 pgvector 扩展。",
            "通过自动生成的 API 接入前端或 agent。"
        ],
        "insights": [
            "<strong>它上榜本身就是个信号：</strong>前十里九个是 agent 工具或模型，它是唯一一个「搭应用的地基」。基础工具回榜，通常说明有人在批量起新项目。",
            "<strong>「为 AI 应用设计」这句话值得注意：</strong>它不是把自己包装成 AI 产品，而是承认 AI 应用的底层还是数据库、鉴权和权限。这一层不性感，但绕不过去。",
            "<strong>本质是热点的下一层永远是基础设施：</strong>agent 越多，要存的会话、记忆、向量和权限就越多，最后都会落回一张 Postgres 表。"
        ],
        "tags": ["postgres", "backend", "typescript", "database", "infrastructure"]
    },
    {
        "rank": 10,
        "owner": "headroomlabs-ai",
        "name": "headroom",
        "fullName": "headroomlabs-ai / headroom",
        "org": "headroomlabs-ai",
        "url": "https://github.com/headroomlabs-ai/headroom",
        "lang": "Python",
        "langClass": "py",
        "stars": "77,008",
        "forks": "5,977",
        "starsToday": "477",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +477★！7.70万★ 第2次登榜（两天前 7.60万★）。在工具输出、日志、文件和 RAG 分块进入 LLM 之前先压缩：官方称编码 Agent 省 20% token、JSON 省 60 到 95%，答案不变。提供库、代理、MCP 服务器三种接入形态。",
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
            "<strong>连续两次上榜，日增还在四百以上：</strong>首登之后能留住人，说明省下来的 token 是真的能对上账单，不是跑分好看。",
            "<strong>它和 graphify 正好是一对：</strong>headroom 把输入变短，graphify 把结构建好。一个做减法，一个做索引，都在解决窗口有限这个硬约束。",
            "<strong>本质是上下文开始被当成带宽管理：</strong>压缩、去重、分级、缓存，这些网络传输里的老概念正搬到 LLM 的输入侧。窗口是带宽，token 是流量。"
        ],
        "tags": ["token-optimization", "compression", "mcp", "proxy", "python"]
    },
    {
        "rank": 11,
        "owner": "vllm-project",
        "name": "vllm",
        "fullName": "vllm-project / vllm",
        "org": "vLLM",
        "url": "https://github.com/vllm-project/vllm",
        "lang": "Python",
        "langClass": "py",
        "stars": "94,687",
        "forks": "23,717",
        "starsToday": "439",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +439★ 首次登榜！9.47万★。vLLM：高吞吐、省显存的 LLM 推理与服务引擎。过去两年几乎所有自建推理服务的团队都绕不开它，今天第一次出现在这张榜上。",
        "problems": [
            "<strong>自建推理很贵：</strong>显存利用率低、批处理做不好，同样的卡只能跑出别人一半的吞吐。",
            "<strong>并发一高就排队：</strong>请求长短不一，调度不当会让短请求被长请求堵住。",
            "<strong>上线门槛高：</strong>部署一套推理服务要懂并行、量化、KV cache。"
        ],
        "usage": [
            "安装：<pre><code>pip install vllm</code></pre>",
            "启动服务：<pre><code>vllm serve &lt;model&gt;</code></pre>，对外提供 OpenAI 兼容接口。",
            "按显存和延迟目标调批处理与并行参数。"
        ],
        "insights": [
            "<strong>9.47 万星却第一次上榜：</strong>这类底层项目不靠曝光活着，靠的是每个自建推理团队都会装一次。它上榜说明今天有一批人正在起服务，而不是在试用模型。",
            "<strong>它和 tokenspeed 那类新引擎不在一个阶段：</strong>新引擎卖「更快」，vLLM 卖「已经在生产里跑过」。这一层的竞争，稳定性的权重高于纸面参数。",
            "<strong>本质是推理成本是唯一每个团队都要自己付的账：</strong>模型可以买 API，电费和卡时买不到折扣，只能靠引擎把利用率榨出来。"
        ],
        "tags": ["inference", "serving", "python", "gpu", "infrastructure"]
    },
    {
        "rank": 12,
        "owner": "strelov1",
        "name": "freehire",
        "fullName": "strelov1 / freehire",
        "org": "strelov1",
        "url": "https://github.com/strelov1/freehire",
        "lang": "Go",
        "langClass": "go",
        "stars": "2,037",
        "forks": "229",
        "starsToday": "405",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +405★ 首登！2,037★，全榜星数最少的一个。freehire：给求职者用的开源搜索引擎。它和榜首那个求职工具同一天上榜，一个帮你搜岗位，一个帮你投岗位。",
        "problems": [
            "<strong>岗位信息被平台垄断：</strong>搜索排序按付费决定，求职者看到的不一定是最合适的。",
            "<strong>重复岗位满天飞：</strong>同一职位被多家猎头反复发布，筛一遍要半天。",
            "<strong>订阅才能用好功能：</strong>提醒、筛选、导出，样样要付费。"
        ],
        "usage": [
            "按 README 部署（Go 项目，可自托管）。",
            "接入或抓取目标岗位数据源。",
            "用搜索引擎按条件检索，导出结果给后续流程使用。"
        ],
        "insights": [
            "<strong>2,037 星就能上榜：</strong>日榜看的是当日增量。它今天被推上来，和榜首的求职工具撞在同一天，大概率是同一批人在转。",
            "<strong>它和 ai-job-search 拼起来是一条完整链路：</strong>一个负责找，一个负责投。这说明求职这件事正在被拆成可替换的环节，而不是绑死在某一个平台里。",
            "<strong>本质是信息不对称在被工具抹平：</strong>招聘平台的生意建立在「你找不到，我帮你找」上。一旦搜索和投递都能自己跑，平台剩下的就只有岗位存量。"
        ],
        "tags": ["job-search", "search-engine", "go", "open-source", "career"]
    },
    {
        "rank": 13,
        "owner": "twentyhq",
        "name": "twenty",
        "fullName": "twentyhq / twenty",
        "org": "Twenty HQ",
        "url": "https://github.com/twentyhq/twenty",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "58,828",
        "forks": "9,643",
        "starsToday": "105",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +105★！5.88万★ 第3次登榜（5 月底 4.73万★，五个月涨了 1.15 万）。Salesforce 的开源替代，定位是「为 AI 设计的 CRM」。日增只有三位数，但它代表的是另一条线：把企业软件重做成 agent 能直接操作的样子。",
        "problems": [
            "<strong>CRM 数据被困在 SaaS 里：</strong>字段、权限、自动化都锁在厂商的模型里，想接自己的 agent 很难。",
            "<strong>按人头收费：</strong>团队一大，CRM 账单比工资涨得还快。",
            "<strong>自动化写起来像配置语言：</strong>业务人员改不动，工程师不愿意改。"
        ],
        "usage": [
            "按 README 自托管，或用云版本。",
            "按自己的业务流程改数据模型与视图。",
            "通过 API 把 agent 接进来读写客户数据。"
        ],
        "insights": [
            "<strong>五个月涨 1.15 万星：</strong>涨幅不猛，但一直在。企业软件的替换周期本来就慢，这类项目的价值要看三年，不看三天。",
            "<strong>「为 AI 设计」这个定位现在还是期货：</strong>真正的差异要等 agent 能稳定读写业务数据之后才看得出来。今天它上榜，更多是因为开源替代这条线一直有人关心。",
            "<strong>本质是 agent 要干活就得有系统可操作：</strong>CRM、工单、财务这些系统不开放，agent 就只能停在聊天框里。开源企业软件是给 agent 铺路的那一半。"
        ],
        "tags": ["crm", "salesforce-alternative", "typescript", "open-source", "enterprise"]
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
    "date": "2026-10-21",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-21'
data['topic'] = '🔥 <strong>生成过剩之后的三副解药：帮你挑机会、帮你少写、帮你验证</strong> —— 今日日增最高的三个项目，刚好对应三种需求。MadsLorentzen/ai-job-search（+3,131★）第6次登榜，6.23万★，连续五天日增破千；strelov1/freehire（+405★）以 2,037 星首登，一个帮你搜岗位、一个帮你投岗位，求职第一次凑齐整条链路。DietrichGebert/ponytail（+2,051★）17.08万★ 首登，让 agent 像屋里最懒的资深开发一样思考，主张「最好的代码是你从来没写过的代码」——在一个比谁生成更多的年份，它反着来。cloudflare/security-audit-skill（+1,997★）第5次，一个月从 1.75万★ 翻到 3.52万★，多阶段安全审计、结论独立验证、输出机器可读，治的是 AI 代码没人验。Graphify-Labs/graphify（+1,434★）第4次，13.10万★，把代码库、文档、SQL 和 PDF 变成可查询的知识图谱，三个月涨 4.3 万。Agent 中间层继续在场：stablyai/orca（+1,543★）正式破十万星、akitaonrails/ai-memory（+810★）第6次、headroomlabs-ai/headroom（+477★）第2次，和 graphify 一起构成「压缩输入 / 重建结构」两条路线。基础设施也回来了：vllm-project/vllm（+439★）首登 9.47万★、supabase/supabase（+509★）首登、twentyhq/twenty（+105★）开源 Salesforce 替代。Comfy-Org/ComfyUI（+914★）第3次，shiyu-coder/Kronos（+570★）第4次。今日主线：当生成不再是瓶颈，瓶颈变成筛选、克制和验证，而这三件事恰好都是人的活。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
assert nf <= 6 or st == 0, f"栏位超限: 新面孔 {nf} / 连登 {st}"
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★ count={p['count']}")
