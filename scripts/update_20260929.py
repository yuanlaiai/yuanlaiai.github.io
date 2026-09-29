#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-29 (1-day gap, 双栏满栏：新面孔 6 + 连登 6)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 29)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-28 榜上）══
    {
        "rank": 1,
        "owner": "rohitg00",
        "name": "ai-engineering-from-scratch",
        "fullName": "rohitg00 / ai-engineering-from-scratch",
        "org": "rohitg00",
        "url": "https://github.com/rohitg00/ai-engineering-from-scratch",
        "lang": "Python",
        "langClass": "py",
        "stars": "60,850",
        "forks": "10,477",
        "starsToday": "1,287",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,287★ 重新上榜（两天前 58,551★ → 60,850★）！6 万星的手写课程：523 节课、20 个阶段、约 342 小时，覆盖 Python / TypeScript / Rust / Julia，每节课都产出一个可复用产物（提示词、技能、Agent、MCP 服务器）。作者引用的数据是「84% 的学生已经在用 AI 工具，只有 18% 觉得自己能专业地用」。",
        "problems": [
            "<strong>会用工具不等于会做系统：</strong>会写提示词的人很多，能从零搭出检索、评测、部署链路的很少。",
            "<strong>教程只讲不敢动手：</strong>大部分课程停在概念与 API 调用，不碰底层实现。",
            "<strong>学完没有作品：</strong>刷完课手上空空，面试与项目都拿不出东西。"
        ],
        "usage": [
            "挑一个目标（从零打基础 / 直接做 Agent / 专攻某个方向）而不是从头刷 523 课。",
            "按阶段推进，每节课跟着实现并留下可复用产物。",
            "支持十二种语言的落地页，中文读者可直接看简体中文入口。"
        ],
        "insights": [
            "<strong>它在一周内第二次上榜，而且这次更高：</strong>58,551★ → 60,850★，课程类项目的热度通常是单次脉冲，反复回来说明缺口是结构性的。",
            "<strong>它和 PageIndex 构成今天的两端：</strong>一个教你从零实现包括检索在内的整条链路，一个给出「检索该怎么做」的新思路——教学与前沿在同一天被同一批人关注。",
            "<strong>本质是岗位需求在倒逼课程结构：</strong>当「AI 工程师」成为职位，培训市场先于教育体系反应，而课程目录本身就是一份招聘需求清单。"
        ],
        "tags": ["education", "ai-engineering", "course", "llm", "mcp"]
    },
    {
        "rank": 2,
        "owner": "NVIDIA",
        "name": "OpenShell",
        "fullName": "NVIDIA / OpenShell",
        "org": "NVIDIA",
        "url": "https://github.com/NVIDIA/OpenShell",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "9,975",
        "forks": "1,373",
        "starsToday": "978",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +978★ 首登！英伟达给 Agent 造的沙箱运行时：官方定位是「面向成批自主 Agent 的安全私有运行时」。它的出发点是承认 Agent 必须能读文件、装包、调 API、用凭证，所以目标不是禁掉这些能力，而是在给足能力的同时不让它碰到你的数据、密钥和网络——你在策略里声明每个 Agent 能碰什么，OpenShell 负责执行。做法有两层：内核级执行（对每次文件访问、系统调用与网络连接做运行时策略拦截）加形式化验证（策略变更生效前先算清它会放行什么）。Apache-2.0，PyPI 上可装。",
        "problems": [
            "<strong>给 Agent 权限就是给风险：</strong>能读文件、装包、调 API 才能干活，但每一步都可能碰到不该碰的东西。",
            "<strong>策略写完不知道放行了什么：</strong>权限规则越写越多，谁也没算过叠加起来到底允许了哪些组合。",
            "<strong>出事才发现拦不住：</strong>应用层拦截可以绕过，容器隔离又挡不住合法的系统调用。"
        ],
        "usage": [
            "安装：<pre><code>pip install openshell</code></pre>（Apache-2.0，文档在 docs.nvidia.com/openshell）",
            "用策略声明每个 Agent 能访问的文件、系统调用与网络范围。",
            "策略变更先走形式化验证，确认放行范围后再应用；Agent 各自跑在隔离沙箱里。"
        ],
        "insights": [
            "<strong>这是今天全网新闻里那套东西的开源实现：</strong>多家外媒同日报道英伟达发布 agent 安全系统，The Verge 说它能在毫秒级围住失控 Agent，路透说它本来可以拦住 Hugging Face 那次入侵。它上了 GitHub 榜单，说明厂商的回应方式变了——不是发白皮书，是发仓库。",
            "<strong>「内核级 + 形式化验证」这个组合值得记住：</strong>大多数 Agent 安全方案停在应用层的提示词与过滤器，而这件事的解法被做成了操作系统级的事：拦系统调用、算清策略后果。安全从话术变成了基础设施。",
            "<strong>本质是安全被产品化：</strong>上周还是「厂商呼吁监管」和「学界警告」，这周已经有一个可以 pip 安装的运行时。真正的问题是，当安全成为英伟达的产品线，它同时也就成了卖点——而这恰恰是它最容易被质疑的地方。"
        ],
        "tags": ["agent-sandbox", "security", "formal-verification", "nvidia", "rust"]
    },
    {
        "rank": 3,
        "owner": "VectifyAI",
        "name": "PageIndex",
        "fullName": "VectifyAI / PageIndex",
        "org": "VectifyAI",
        "url": "https://github.com/VectifyAI/PageIndex",
        "lang": "Python",
        "langClass": "py",
        "stars": "36,779",
        "forks": "3,224",
        "starsToday": "822",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +822★ 重新上榜！3.68 万星的无向量检索方案：它的原话是「不要向量库、不要切块」，因为向量检索按语义相似度匹配，而相似不等于相关。它把文档建成树状索引，让检索通过推理去定位内容，官方说法是「像人一样读文档」。SDK 支持本地模式（索引、检索、对话全在自己机器上跑，用你自己的模型 key），另有云版本与面向海量语料的文件级索引层。",
        "problems": [
            "<strong>相似度检索答非所问：</strong>长文档、专业文档里，语义最近的段落常常不是真正的答案所在。",
            "<strong>切块破坏上下文：</strong>把文档切成片段再检索，跨章节的论证关系直接丢失。",
            "<strong>向量库运维成本：</strong>上亿向量要维护索引与嵌入更新，换模型就得重算一遍。"
        ],
        "usage": [
            "安装：<pre><code>pip install -U pageindex</code></pre>",
            "本地模式下载入文档，生成树状索引（文本 PDF 走快速索引）。",
            "用自然语言提问，由索引树推导出相关段落，再交给模型作答。"
        ],
        "insights": [
            "<strong>它挑战的是 RAG 的默认前提：</strong>两年来的标准答案是把文档切块、嵌入、向量检索，它直接把这一层去掉，改让模型顺着文档结构推理——这是一次对基础假设的公开质疑，能攒到 3.68 万星说明质疑有市场。",
            "<strong>本地模式是它 8 月的关键更新：</strong>索引、检索、对话全部跑在自己机器上，用自己的模型 key，配合今天同榜的其他项目看，「数据不出本机」已经成了默认卖点而不是加分项。",
            "<strong>本质是检索重心的转移：</strong>当嵌入模型越来越便宜，瓶颈就从「找得到相似的」变成了「判断得对相关性」——前者是算力问题，后者是推理问题，而推理正是这一代模型最贵的地方。"
        ],
        "tags": ["rag", "retrieval", "reasoning", "agentic-ai", "python"]
    },
    {
        "rank": 4,
        "owner": "t8y2",
        "name": "dbx",
        "fullName": "t8y2 / dbx",
        "org": "t8y2",
        "url": "https://github.com/t8y2/dbx",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "21,659",
        "forks": "2,071",
        "starsToday": "460",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +460★ 首登！2.1 万星的轻量数据库客户端：25 MB 装下 100 多种数据库的连接能力，覆盖 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、SQL Server 与达梦；桌面端、Docker、CLI 三种形态，内置 AI 助手与 MCP Server。有中文文档，赞助方里能看到多家国内云与安全厂商。",
        "problems": [
            "<strong>数据库客户端越做越重：</strong>装一个图形客户端要几百兆，连着几种数据库就得装好几套。",
            "<strong>跨库切换成本高：</strong>MySQL 用一套、Redis 用一套、MongoDB 再来一套，快捷键与习惯全要重学。",
            "<strong>让 AI 查数据要另外搭桥：</strong>想让模型直接读库，得自己写连接层与权限控制。"
        ],
        "usage": [
            "从 Releases 下载对应平台安装包，或用 Docker 镜像启动。",
            "配置连接串后在同一条界面里管理 100 多种数据库。",
            "启用内置 AI 助手或 MCP Server，让 Agent 走统一入口访问数据。"
        ],
        "insights": [
            "<strong>25 MB 这个数字是它的全部卖点：</strong>在客户端软件普遍膨胀到几百兆的今天，把 100 多种数据库协议塞进 25 MB，本身就是一次工程能力的展示——轻量不是省事，是难度更高的选择。",
            "<strong>内置 MCP Server 说明客户端也在抢入口：</strong>数据库客户端过去是给人用的，现在要给 Agent 用——谁能成为 Agent 读数据的第一道门，谁就掌握了这句话的解释权。",
            "<strong>本质是工具链的重新分层：</strong>当 AI 能写 SQL 之后，客户端的价值从「帮你写查询」转向「帮你管权限与连接」——工具的护城河从功能数量换成了入口位置。"
        ],
        "tags": ["database", "rust", "mcp", "cli", "developer-tools"]
    },
    {
        "rank": 5,
        "owner": "oblien",
        "name": "openship",
        "fullName": "oblien / openship",
        "org": "oblien",
        "url": "https://github.com/oblien/openship",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "13,579",
        "forks": "1,211",
        "starsToday": "436",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +436★ 首登！1.36 万星的自托管部署平台，自带 CI/CD：指向一个仓库，它负责构建、发布、路由与 TLS 证书；桌面应用、网页面板、CLI 三种入口。三种跑法也交代得很清楚：桌面版的控制面只在你打开应用时运行，什么都不常驻、不暴露；团队或需要 push-to-deploy 就自托管服务器；不想运维就用云版本。",
        "problems": [
            "<strong>部署平台绑住你的应用：</strong>用托管平台省事，但代码、构建与证书都捏在别人手里。",
            "<strong>自建 CI/CD 太重：</strong>自己搭一套流水线，光维护就跑掉一个人。",
            "<strong>小团队的中间地带没人管：</strong>要么全托管，要么从零自建，缺一个「一条命令起一套」的选项。"
        ],
        "usage": [
            "桌面版：下载应用，本地跑控制面，通过 SSH 驱动你的服务器。",
            "自托管：<pre><code>openship up</code></pre> 起控制面，再接仓库开 push-to-deploy。",
            "不想运维也可以直接用云版本，应用跑在托管沙箱里。"
        ],
        "insights": [
            "<strong>它把「桌面版只在你打开时运行」写进说明：</strong>这是一句少见的产品承诺——多数自托管工具默认你会常驻一台服务器，它反过来先服务只有一台机器的人。安全与成本考量被放在了功能表之前。",
            "<strong>与 Vercel 那种路线形成了对照：</strong>同一个需求（指向仓库就能上线），一条路是交出去换省心，一条路是拿回来换控制权——今天榜上自托管项目占了多个席位，这个选择正在被大量团队重做。",
            "<strong>本质是托管红利的重新分配：</strong>过去十年云平台用「省运维」换走了控制权，现在这类工具把省下的那部分工程复杂度装进一个二进制里还回来——省事和控制权第一次不再互斥。"
        ],
        "tags": ["self-hosted", "deployment", "ci-cd", "typescript", "paas"]
    },
    {
        "rank": 6,
        "owner": "willfaust",
        "name": "Madeira",
        "fullName": "willfaust / Madeira",
        "org": "willfaust",
        "url": "https://github.com/willfaust/Madeira",
        "lang": "C",
        "langClass": "c",
        "stars": "1,025",
        "forks": "178",
        "starsToday": "229",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +229★ 首登！把 Windows PC 游戏跑在未越狱 iPhone 上的研究项目：Wine（ARM64EC）负责 Windows 兼容层，FEX-Emu 做 x86-64 到 ARM64 的指令翻译，DXMT 把 Direct3D 11 翻成 Metal，整个东西作为单个 Mach 进程运行，wineserver 变成一个线程。作者列出的实测状态很老实：Thumper 和 ULTRAKILL 可玩，另一款游戏能进到游玩阶段但也出现过无法解释的崩溃，控制还不稳定。",
        "problems": [
            "<strong>平台墙：</strong>iPhone 上跑 Windows 游戏，过去只有越狱这一条路。",
            "<strong>三层翻译叠加的性能损耗：</strong>指令集、系统调用、图形 API 各需要一层转换，每层都在吃性能。",
            "<strong>JIT 限制：</strong>iOS 上启用即时编译需要调试器附加，这决定了它无法上架、只能侧载。"
        ],
        "usage": [
            "用侧载方式安装（需要 Apple ID 签名，免费账号的凭据 7 天过期，需要每周重装）。",
            "按文档准备 StikDebug 以启用 JIT。",
            "导入游戏后运行；作者说明这是研究项目而非产品，各游戏兼容性差异很大。"
        ],
        "insights": [
            "<strong>它把三层翻译缝成了一个进程：</strong>x86-64 到 ARM64、Windows 到 POSIX、D3D11 到 Metal，通常这三件事各是一个项目，这里被压进单个 Mach 进程——工程上的难点不在任何一层，而在它们的接缝。",
            "<strong>作者的表述方式本身就是一种信号：</strong>「这是研究项目不是产品，会有粗糙边缘、每个游戏不同的怪癖与破坏性变更」——反而因为这份老实，它能安心地只把两个游戏做到可玩就发出来。",
            "<strong>本质是平台边界的持续渗透：</strong>封闭平台的历史就是被这类项目一层层削薄的历史，先跑通一个游戏，再跑通十个——真正的变化从来不是某次发布会宣布的，而是有人在周末把一条路走通了。"
        ],
        "tags": ["wine", "ios", "emulation", "fex-emu", "reverse-engineering"]
    },
    # ══ 连登（09-28 已在榜）══
    {
        "rank": 7,
        "owner": "debpalash",
        "name": "VoiceStudio",
        "fullName": "debpalash / VoiceStudio",
        "org": "debpalash",
        "url": "https://github.com/debpalash/VoiceStudio",
        "lang": "Python",
        "langClass": "py",
        "stars": "46,448",
        "forks": "5,270",
        "starsToday": "4,712",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +4,712★（42,258★ → 46,448★）！完全本地的 ElevenLabs 开源替代：646 种语言的声音克隆、音色设计、视频配音、听写、转写与有声书制作，默认引擎基于 k2-fsa/OmniVoice；提供本地 API 与 MCP 供 Agent 调用，远程服务与用量统计都要你主动同意才启用。",
        "problems": [
            "<strong>声音能力都在云上：</strong>克隆自己的声音要上传样本，配音按字数付费，数据还留在别人服务器。",
            "<strong>订阅制锁住产量：</strong>有声书、批量配音一上量，按字符计费的成本立刻失控。",
            "<strong>多语言覆盖名不副实：</strong>商业服务宣称的语言数，小语种往往要先掏钱试错。"
        ],
        "usage": [
            "一行脚本安装（macOS / Linux）：<pre><code>curl -fsSL https://voicestudio.sh/install | sh</code></pre>",
            "在工作区里克隆音色、设计新音色或导入模型。",
            "给视频配音、生成有声书与批量任务，或通过本地 API / MCP 接给自己的 Agent。"
        ],
        "insights": [
            "<strong>连登第二天冲到全榜日增第一，两日累计 +7,986★：</strong>从 42,258★ 到 46,448★，本地语音这条路的需求被一次验证——它不是「小众爱好者」，是付费用户真在用。",
            "<strong>它和 PageIndex、OpenShell 同一天上榜不是巧合：</strong>一个把推理算在本地，一个把策略执行放在内核，一个把语音推理放在自己的显卡上——三种「能力自己持有」的实现。",
            "<strong>本质是订阅制的拆解：</strong>按字符计费的语音服务一旦遇到本地方案就失去定价权，只要显卡跑得动，边际成本就是电费。"
        ],
        "tags": ["text-to-speech", "voice-cloning", "local-first", "mcp", "tauri"]
    },
    {
        "rank": 8,
        "owner": "vectorize-io",
        "name": "hindsight",
        "fullName": "vectorize-io / hindsight",
        "org": "Vectorize",
        "url": "https://github.com/vectorize-io/hindsight",
        "lang": "Python",
        "langClass": "py",
        "stars": "42,024",
        "forks": "5,637",
        "starsToday": "2,541",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第三天，今日 +2,541★（39,892★ → 42,024★）！会学习的 Agent 记忆系统：官方说法是「多数记忆系统只是回放对话历史，Hindsight 要做的是让 Agent 真的学会」，在 LongMemEval 长期记忆基准上拿到最准成绩，配 arXiv 论文、Python / JS 客户端、MCP 与嵌入式模式，另有云托管。",
        "problems": [
            "<strong>长对话记不住重点：</strong>上下文一长，早期关键信息被稀释，Agent 反复问已经说过的事。",
            "<strong>RAG 只解决「找得到」：</strong>向量检索能捞出片段，不会把经验沉淀成判断。",
            "<strong>记忆散落各处：</strong>对话历史、工具结果、项目约定各存一份，换个 Agent 就全丢。"
        ],
        "usage": [
            "起服务：<pre><code>pip install hindsight-api</code></pre>，或在 Python 里用嵌入式模式。",
            "接客户端：<pre><code>pip install hindsight-client</code></pre> 或 npm 包，两行代码包住 LLM 调用。",
            "给 Agent 挂 MCP 服务器，或用官方的 coding agent 集成。"
        ],
        "insights": [
            "<strong>连登第三天破 4.2 万星，五天累计从 26,963★ 涨到 42,024★：</strong>涨幅超过 55%，而且今天仍有两千多日增——记忆这条线已经从热点变成默认组件。",
            "<strong>它与 PageIndex 是同一个问题的两种解法：</strong>一个把记忆压缩成会学习的结构，一个把文档读成可推理的树——两者的共同点是不再相信「相似度就是相关性」。",
            "<strong>本质是上下文经济的拐点：</strong>上下文再大也按 token 计费，而「学会」是压缩——谁能把经历压成更少 token 而不丢判断，谁就同时赢了能力和成本。"
        ],
        "tags": ["agent-memory", "ai-agents", "longMemEval", "mcp", "python"]
    },
    {
        "rank": 9,
        "owner": "paperclipai",
        "name": "paperclip",
        "fullName": "paperclipai / paperclip",
        "org": "Paperclip",
        "url": "https://github.com/paperclipai/paperclip",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "93,944",
        "forks": "15,984",
        "starsToday": "2,412",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第三天，今日 +2,412★（91,823★ → 93,944★）！把 AI Agent 当员工管的应用，官方那句话是「如果 OpenClaw 是员工，Paperclip 就是公司」：定义目标、招团队（任何厂商的 Agent 都行）、批预算、看仪表盘；看着像任务管理器，底下是组织架构、预算、治理与目标对齐。",
        "problems": [
            "<strong>Agent 越多越乱：</strong>开着十几个 Agent，没人说得清谁在做什么、做到哪一步。",
            "<strong>目标对不齐：</strong>每个 Agent 都能干活，但没人把它们指向同一个业务目标。",
            "<strong>花钱没数：</strong>没有预算与成本视图，跑飞的账单只能在月底发现。"
        ],
        "usage": [
            "起 Node.js 服务与 React 前端：<pre><code>git clone https://github.com/paperclipai/paperclip.git</code></pre>",
            "定义业务目标，招入你自己的 Agent（任意厂商）。",
            "审批策略、设定预算后开跑，在仪表盘上跟踪工作与花费。"
        ],
        "insights": [
            "<strong>连登第三天逼近 9.4 万星：</strong>三天从 87,914★ 涨到 93,944★，日增稳定在两千以上——「把 Agent 当组织管」不是一时好奇。",
            "<strong>它和 OpenShell 是同一天的两道防线：</strong>OpenShell 在系统层管每个 Agent 能碰什么，Paperclip 在组织层管谁负责什么、花多少——一个管能力边界，一个管责任边界。",
            "<strong>本质是管理动作的自动化：</strong>过去自动化执行，现在开始自动分配与问责——谁定目标、谁批预算、谁背结果，这套流程被搬进了软件。"
        ],
        "tags": ["ai-agents", "orchestration", "autonomous-org", "typescript", "openclaw"]
    },
    {
        "rank": 10,
        "owner": "mvschwarz",
        "name": "openrig",
        "fullName": "mvschwarz / openrig",
        "org": "mvschwarz",
        "url": "https://github.com/mvschwarz/openrig",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "2,095",
        "forks": "157",
        "starsToday": "733",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +733★（1,435★ → 2,095★）！官方那句话把定位讲清楚了：「harness 包的是一个模型，rig 包的是你的 harness」。一份 YAML 定义 Agent 团队，一条命令启动，Claude Code 和 Codex 可以待在同一个 rig 里当一套系统管理；向 lead agent 说你要的结果，它跨团队协调专家。要求 Node 20/22/24 与 tmux，macOS 或 Linux。",
        "problems": [
            "<strong>终端会话堆成山：</strong>同时开好几个 Agent，谁在做什么、上下文停在哪，全靠脑子记。",
            "<strong>多个 harness 互不相通：</strong>Claude Code 和 Codex 各干各的，任务与结论无法接力。",
            "<strong>上下文无法续接：</strong>会话一关团队的上下文就散了，下次要从头讲一遍。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @openrig/cli</code></pre>（需 Node 20/22/24 与 tmux）",
            "用 YAML 把团队和角色写进 rig，一条命令启动。",
            "向 lead agent 描述目标，由它调度专家，产出与会话留存在固定地址上。"
        ],
        "insights": [
            "<strong>连登第二天日增翻倍：</strong>+733★（首日 +781★ 之后仍在加速），两天从 1,435★ 涨到 2,095★——小体量项目能保持这个斜率，说明踩中的是真实工作流痛点。",
            "<strong>「rig 包 harness」这层抽象正在被快速接受：</strong>与 Paperclip 同榜，一大一小两种尺度都在回答「多个 agent 怎么当一套系统用」。",
            "<strong>本质是把「人管 Agent」换成「Agent 管 Agent」：</strong>lead agent 调度 specialist，人只处理需要拍板的决策——组织结构的中间层正在被搬进软件。"
        ],
        "tags": ["agent-harness", "multi-agent", "claude-code", "codex-cli", "tmux"]
    },
    {
        "rank": 11,
        "owner": "dream-num",
        "name": "univer",
        "fullName": "dream-num / univer",
        "org": "dream-num",
        "url": "https://github.com/dream-num/univer",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "21,622",
        "forks": "1,828",
        "starsToday": "692",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第三天，今日 +692★（20,996★ → 21,622★）！2022 年建仓的开源 Office SDK，简介是「The Office Harness for AI Agents」：表格、文档、幻灯片、画布、关系表、PDF 一套运行时，Canvas 渲染 + 公式引擎 + 插件架构 + 浏览器与 Node 同构的 Facade API。",
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
            "<strong>连登第三天，六天累计从 15,352★ 到 21,622★：</strong>改一个定位带来的增长持续了一周，说明「Agent 的办公桌」这个需求被反复确认。",
            "<strong>它和 dbx 是同一件事的两种载体：</strong>一个让 Agent 读写表格文档，一个让 Agent 读写数据库——Agent 需要接触的「业务数据入口」正在被逐个补齐。",
            "<strong>本质是资产重定价：</strong>技术周期切换时，最先受益的往往不是新项目，而是早就把事做好、只差一个说法的老项目。"
        ],
        "tags": ["office-sdk", "spreadsheet", "typescript", "ai-agents", "chinese"]
    },
    {
        "rank": 12,
        "owner": "cs341-illinois",
        "name": "coursebook",
        "fullName": "cs341-illinois / coursebook",
        "org": "University of Illinois Urbana-Champaign",
        "url": "https://github.com/cs341-illinois/coursebook",
        "lang": "TeX",
        "langClass": "tex",
        "stars": "2,828",
        "forks": "257",
        "starsToday": "569",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +569★（2,287★ → 2,828★）！伊利诺伊大学 CS 341「系统编程」课程的开源教材：C 语言、Linux、POSIX，从命令行、进程、信号、并发一路讲到 internals，由 Angrave 早年的 wikibook 实验标准化而来，同时提供 PDF、HTML、EPUB 与 wiki 四种格式，LaTeX 源码全公开。",
        "problems": [
            "<strong>系统编程门槛高：</strong>进程、信号、并发这些概念看文档看得懂，写起来就错。",
            "<strong>好课程锁在学校里：</strong>讲义与录像不外流，校外的人拿不到系统的学习路径。",
            "<strong>底层知识被工具遮蔽：</strong>AI 会写代码之后，不理解系统反而更容易写出线上事故。"
        ],
        "usage": [
            "直接读在线 HTML 版或下载 PDF / EPUB。",
            "跟着章节在 Linux 环境里手写 C 代码，跑并发与信号实验。",
            "课程页可对照 CS 341 的作业与讲义，LaTeX 源码可自行编译。"
        ],
        "insights": [
            "<strong>连登第二天日增翻倍（+265★ → +569★）：</strong>一本系统编程教材在这个时间点被持续放大，指向的是同一件事：AI 越会写代码，越需要对机器本身有直觉的人。",
            "<strong>它与 OpenShell 形成了今天的闭环：</strong>OpenShell 在内核层拦系统调用，coursebook 教人理解进程与系统调用——同一个知识层，一个产品化了，一个还在教人怎么读。",
            "<strong>本质是基础知识在工具时代的重新定价：</strong>工具越强，越容易掩盖理解不足，而系统层的错误代价最高——这类开源教材会持续被重新发现。"
        ],
        "tags": ["systems-programming", "c", "linux", "textbook", "education"]
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
    "date": "2026-09-29",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-29'
data['topic'] = '🔥 <strong>安全被做成产品：英伟达的 Agent 运行时首日登榜 + 无向量检索回归 + 本地化继续外扩</strong> —— NVIDIA/OpenShell（+978★）首日近万星：英伟达给成批自主 Agent 造的安全运行时，你用策略声明每个 Agent 能碰什么，它靠内核级拦截（每次文件访问、系统调用、网络连接）加形式化验证（策略生效前先算清会放行什么）来执行。这正对应今天外媒报道的那套系统——The Verge 说它能毫秒级围住失控 Agent，路透说它本来可以拦住 Hugging Face 那次入侵。VectifyAI/PageIndex（+822★）3.68 万星：不要向量库、不要切块，因为相似不等于相关，检索要靠推理。debpalash/VoiceStudio（+4,712★）连登第二天冲到全榜日增第一，两日累计 +7,986★，46,448★。rohitg00/ai-engineering-from-scratch（+1,287★）6 万星。t8y2/dbx（+460★）25 MB 装下 100 多种数据库的客户端，内置 MCP。oblien/openship（+436★）自托管部署平台。willfaust/Madeira（+229★）在未越狱 iPhone 上跑 Windows 游戏。连登：paperclip（+2,412★）9.4 万星、hindsight（+2,541★）4.2 万星、openrig（+733★）、univer（+692★）、coursebook（+569★）。今日三条主线：一、安全从呼吁变成可安装的运行时，厂商用仓库而不是白皮书来回答质疑；二、检索与记忆都在放弃「相似度就是相关性」这个前提，转向推理；三、能力自己持有成为默认卖点——本地语音、本地索引、自托管部署、内核级策略执行，同一个方向的不同实现。'

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
