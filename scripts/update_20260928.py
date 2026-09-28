#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-28 (1-day gap, 双栏：新面孔 5 + 连登 3)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 28)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-27 榜上）══
    {
        "rank": 1,
        "owner": "debpalash",
        "name": "VoiceStudio",
        "fullName": "debpalash / VoiceStudio",
        "org": "debpalash",
        "url": "https://github.com/debpalash/VoiceStudio",
        "lang": "Python",
        "langClass": "py",
        "stars": "42,258",
        "forks": "4,973",
        "starsToday": "3,274",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,274★ 首登！4.2 万星：完全本地的 ElevenLabs 开源替代，支持 646 种语言的声音克隆、音色设计、视频配音、听写、转写与有声书制作。默认引擎基于 k2-fsa/OmniVoice，另有模型可选；提供本地 API 与 MCP 供 Agent 调用，可选的远程 worker 与远程服务都靠自愿开启，用量统计需要你同意才会上报。",
        "problems": [
            "<strong>语音能力都在云上：</strong>克隆一个自己的声音要上传样本，配音要按字数付费，数据还留在别人服务器。",
            "<strong>订阅制锁住产量：</strong>有声书、批量配音这类工作一上量，按字符计费的成本立刻失控。",
            "<strong>多语言门槛：</strong>646 种语言的覆盖在商业服务里基本是空话，小语种往往要先掏钱试错。"
        ],
        "usage": [
            "一行脚本安装（macOS / Linux）：<pre><code>curl -fsSL https://voicestudio.sh/install | sh</code></pre>",
            "在工作区里克隆音色、设计新音色或导入模型。",
            "给视频配音、生成有声书与批量任务，或通过本地 API / MCP 接给自己的 Agent。"
        ],
        "insights": [
            "<strong>它把「本地优先」从文本搬到了声音：</strong>过去两年自持运动集中在文档、相册、知识库，声音一直是云服务的地盘，因为推理开销大。4.2 万星说明本地推理的算力门槛已经跨过去了。",
            "<strong>带 MCP 是这次的关键动作：</strong>配音与转写接成 Agent 能直接调用的工具，意味着声音生产可以整段交给自动化流程，而不只是给人用的软件。",
            "<strong>本质是订阅制的又一次拆解：</strong>按字符计费的语音服务，遇到本地方案就等于失去了定价权——只要你的显卡跑得动，边际成本就是电费。"
        ],
        "tags": ["text-to-speech", "voice-cloning", "local-first", "mcp", "tauri"]
    },
    {
        "rank": 2,
        "owner": "mvschwarz",
        "name": "openrig",
        "fullName": "mvschwarz / openrig",
        "org": "mvschwarz",
        "url": "https://github.com/mvschwarz/openrig",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "1,435",
        "forks": "125",
        "starsToday": "781",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +781★ 首登！官方那句话把定位讲清楚了：「harness 包的是一个模型，rig 包的是你的 harness」。用一份 YAML 定义你的 Agent 团队，一条命令启动，Claude Code 和 Codex 可以待在同一个 rig 里当一套系统管理；向 lead agent 说你要的结果，它跨团队协调专家，把结果和需要你拍板的事端回来。要求 Node 20/22/24 与 tmux，macOS 或 Linux。",
        "problems": [
            "<strong>终端会话堆成山：</strong>同时开好几个 Agent，谁在做什么、上下文停在哪，全靠脑子记。",
            "<strong>多个 harness 互不相通：</strong>Claude Code 和 Codex 各干各的，任务和结论无法互相接力。",
            "<strong>上下文无法续接：</strong>会话一关，团队的上下文就散了，下次要从头讲一遍。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @openrig/cli</code></pre>（需 Node 20/22/24 与 tmux）",
            "用 YAML 把团队和角色写进 rig，一条命令启动。",
            "向 lead agent 描述目标，由它调度专家，产出与会话留存在固定地址上。"
        ],
        "insights": [
            "<strong>它接的是上周刚成型的那层抽象：</strong>「harness」刚成为品类词（strands 的 harness-sdk、univer 的 Office Harness），openrig 已经在 harness 之上再做一层编排——每出现一层新抽象，很快就会出现管理这一层抽象的工具。",
            "<strong>README 里那段「启动会写入 provider hooks 与工作区信任设置，请先备份」很实在：</strong>这类工具要接管你的 Agent 配置才能工作，权限边界是它必须先交代清楚的事——这本身就是 Agent 工具开始成熟的标志。",
            "<strong>本质是把「人管 Agent」换成「Agent 管 Agent」：</strong>lead agent 调度 specialist，人只处理需要拍板的决策——组织结构的中间层正在被搬进软件。"
        ],
        "tags": ["agent-harness", "multi-agent", "claude-code", "codex-cli", "tmux"]
    },
    {
        "rank": 3,
        "owner": "byoungd",
        "name": "up",
        "fullName": "byoungd / up",
        "org": "byoungd（韩先凯 / 离谱）",
        "url": "https://github.com/byoungd/up",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "64,430",
        "forks": "6,498",
        "starsToday": "310",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +310★ 重新上榜！6.4 万星的中文书稿《人生进阶指南》，副标题是「AI 时代终身学习指南」。它 2017 年从《离谱的英语学习指南》起步，九年里长成覆盖英语、AI 学习、项目开发、资源层创业与人生复盘的长文，核心循环是「发现问题 → 主动学习 → 与 AI 协作 → 完成真实任务 → 保存证据 → 复盘迁移」，中文 EPUB / PDF 可下载。",
        "problems": [
            "<strong>答案变便宜了，判断没变便宜：</strong>几秒钟能拿到解释、代码和计划表，但没人告诉你哪个问题值得追问、哪条证据可以信。",
            "<strong>学完没留下东西：</strong>刷完教程手上没有作品，也没法向别人证明自己会做。",
            "<strong>把经验当规律：</strong>网上大量「过来人路径」把个人经历包装成普适方法，照着走容易翻车。"
        ],
        "usage": [
            "下载中文 EPUB 或 PDF（也有英文版）直接读。",
            "按 01 建立基础 / 02 借工具放大能力 / 03 进入真实生活 三段推进。",
            "跟着书里的循环做一遍：挑一个真实任务，用 AI 协作完成并留下证据。"
        ],
        "insights": [
            "<strong>九年长跑的项目在 AI 周重新上榜：</strong>2017 年的英语学习指南能长到今天，靠的不是工具热度，是「学习」这个需求本身在 AI 时代变得更急——书里那句「AI 让答案前所未有地廉价」，正是它重新被需要的原因。",
            "<strong>它做了一件很硬的分类：</strong>把内容明确分成研究结论（给来源、说清证据边界）、个人经验（不冒充普遍规律）、待验证假设（允许想象但要交给行动检验）——这份克制在中文学习类内容里少见。",
            "<strong>本质是「可迁移能力」的重新定价：</strong>当具体技能被 AI 快速拉平，剩下值钱的是提问、核验、把建议变成作品、并为判断负责——这四件事恰好都是 AI 替不了的。"
        ],
        "tags": ["chinese", "learning", "ai-guide", "career", "ebook"]
    },
    {
        "rank": 4,
        "owner": "cs341-illinois",
        "name": "coursebook",
        "fullName": "cs341-illinois / coursebook",
        "org": "University of Illinois Urbana-Champaign",
        "url": "https://github.com/cs341-illinois/coursebook",
        "lang": "TeX",
        "langClass": "tex",
        "stars": "2,287",
        "forks": "221",
        "starsToday": "265",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +265★ 首登！伊利诺伊大学 CS 341「系统编程」课程的开源教材：C 语言、Linux、POSIX，从命令行、进程、信号、并发一路讲到 internals，由 Angrave 早年的 wikibook 实验标准化而来，同时提供 PDF、HTML、EPUB 与 wiki 四种格式，LaTeX 源码全公开。",
        "problems": [
            "<strong>系统编程门槛高：</strong>进程、信号、并发这些概念看文档看得懂，写起来就错。",
            "<strong>教材依赖学校：</strong>好课程内容锁在课件与录像里，校外的人拿不到系统的路径。",
            "<strong>底层知识被工具遮蔽：</strong>AI 会写代码之后，不理解系统反而更容易写出线上事故。"
        ],
        "usage": [
            "直接读在线 HTML 版或下载 PDF / EPUB。",
            "跟着章节在 Linux 环境里手写 C 代码，跑并发与信号实验。",
            "课程页可对照 CS 341 的作业与讲义，LaTeX 源码可自行编译。"
        ],
        "insights": [
            "<strong>它的价值在 AI 时代反而上升：</strong>AI 把写代码变容易之后，区分水平的不再是语法，而是对进程、内存与并发的直觉——能读懂系统的人才知道 AI 写的代码会在哪里崩。",
            "<strong>与今天同榜的学习类项目是同一件事的两面：</strong>一个教你用 AI 完成真实任务，一个教你理解 AI 之下那层机器——两个都在补同一种缺口。",
            "<strong>本质是基础知识在工具时代的重新定价：</strong>工具越强，越容易掩盖理解不足，而系统层的错误代价最高——这类开源教材会持续被重新发现。"
        ],
        "tags": ["systems-programming", "c", "linux", "textbook", "education"]
    },
    {
        "rank": 5,
        "owner": "NawfalMotii79",
        "name": "PLFM_RADAR",
        "fullName": "NawfalMotii79 / PLFM_RADAR",
        "org": "NawfalMotii79",
        "url": "https://github.com/NawfalMotii79/PLFM_RADAR",
        "lang": "PLSQL",
        "langClass": "plsql",
        "stars": "25,637",
        "forks": "5,874",
        "starsToday": "145",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +145★ 首登！2.5 万星、五千多次 fork 的开源硬件项目：AERIS-10，10.5 GHz 脉冲线性调频相控阵雷达，目标是低成本可复现。软件 MIT、硬件 CERN-OHL-P 开源，当前状态标着 Alpha、功能仍在开发中。",
        "problems": [
            "<strong>雷达是高价黑箱：</strong>相控阵系统长期只有国防与航空预算玩得起，个人和小团队连物料清单都拿不到。",
            "<strong>方案不可复现：</strong>论文给了指标但不给设计文件，想自己搭只能从头试。",
            "<strong>知识壁垒：</strong>射频、天线阵列与信号处理分散在几个学科，缺一条打通的设计路径。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/NawfalMotii79/PLFM_RADAR.git</code></pre>",
            "按硬件文档准备射频前端、阵列与信号采集链路。",
            "用配套软件做脉冲压缩与目标检测，注意项目仍处 Alpha 阶段。"
        ],
        "insights": [
            "<strong>开放硬件在走开源软件二十年前的路：</strong>软件开源用许可证换生态，硬件现在用 CERN-OHL-P 做同样的事——物料清单、设计文件、软件全公开，剩下的门槛就只剩工艺和预算。",
            "<strong>2.5 万星与五千多次 fork 说明需求在哪：</strong>fork 数接近星数的四分之一，比例远高于一般项目——这不是有人点赞，是真的有人准备动手做。",
            "<strong>本质是传感能力的外溢：</strong>当雷达这类感知设备的成本被开源方案压下来，受益的不只是爱好者，还有农业、气象、无人机避障这些原本用不起的领域——能力的扩散往往先发生在没人注意的硬件层。"
        ],
        "tags": ["radar", "open-hardware", "phased-array", "cern-ohl", "rf"]
    },
    # ══ 连登（09-27 已在榜）══
    {
        "rank": 6,
        "owner": "vectorize-io",
        "name": "hindsight",
        "fullName": "vectorize-io / hindsight",
        "org": "Vectorize",
        "url": "https://github.com/vectorize-io/hindsight",
        "lang": "Python",
        "langClass": "py",
        "stars": "39,892",
        "forks": "5,324",
        "starsToday": "4,413",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +4,413★（33,749★ → 39,892★）！会学习的 Agent 记忆系统：官方说法是「多数记忆系统只是回放对话历史，Hindsight 要做的是让 Agent 真的学会」，在 LongMemEval 长期记忆基准上拿到最准成绩，配 arXiv 论文、Python / JS 客户端、MCP 服务器与嵌入式模式，另有云托管版本。",
        "problems": [
            "<strong>长对话记不住重点：</strong>上下文一长，早期关键信息被稀释，Agent 反复问已经说过的事。",
            "<strong>RAG 只解决「找得到」：</strong>向量检索能捞出片段，不会把经验沉淀成判断。",
            "<strong>记忆散落各处：</strong>对话历史、工具结果、项目约定各存一份，换个 Agent 就全丢。"
        ],
        "usage": [
            "起服务：<pre><code>pip install hindsight-api</code></pre>，或在 Python 里直接用嵌入式模式。",
            "接客户端：<pre><code>pip install hindsight-client</code></pre> 或 npm 包，两行代码包住 LLM 调用即可接入。",
            "给 Agent 挂 MCP 服务器，或用官方的 coding agent 集成。"
        ],
        "insights": [
            "<strong>今天全榜日增最高：</strong>+4,413★，比它昨天首登时的 +2,147★ 翻了一倍，四天累计从 26,963★ 涨到 39,892★——记忆这条线的热度不是发布脉冲，是持续导流。",
            "<strong>它与 paperclip 同时连登，说明两件事被一起接受了：</strong>给 Agent 记忆，和把 Agent 当组织管——一个解决「记得住」，一个解决「管得清」，是同一批团队在补的两块短板。",
            "<strong>本质是上下文经济的拐点：</strong>上下文再大也按 token 计费，而「学会」是压缩——谁能把经历压成更少 token 而不丢判断，谁就同时赢了能力和成本。"
        ],
        "tags": ["agent-memory", "ai-agents", "longMemEval", "mcp", "python"]
    },
    {
        "rank": 7,
        "owner": "paperclipai",
        "name": "paperclip",
        "fullName": "paperclipai / paperclip",
        "org": "Paperclip",
        "url": "https://github.com/paperclipai/paperclip",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "91,823",
        "forks": "15,819",
        "starsToday": "3,185",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +3,185★（87,914★ → 91,823★）！把 AI Agent 当员工管的应用，官方那句话是「如果 OpenClaw 是员工，Paperclip 就是公司」：定义目标、招团队（任何厂商的 Agent 都行）、批预算、看仪表盘；看着像任务管理器，底下是组织架构、预算、治理与目标对齐。",
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
            "<strong>连登第二天突破 9 万星：</strong>从 87,914★ 到 91,823★，日增仍在 3,000 以上——「管理 Agent 的组织层」不是好奇，是积压需求。",
            "<strong>它与 openrig 是同一问题的两种尺度：</strong>openrig 管一个团队的几个 harness，Paperclip 管一家公司的岗位与预算——组织层的抽象正在同时向上下两侧生长。",
            "<strong>本质是管理动作的自动化：</strong>过去自动化的是执行，现在开始自动分配与问责——谁定目标、谁批预算、谁背结果，这套流程被搬进了软件。"
        ],
        "tags": ["ai-agents", "orchestration", "autonomous-org", "typescript", "openclaw"]
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
        "stars": "20,996",
        "forks": "1,785",
        "starsToday": "1,105",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +1,105★（19,723★ → 20,996★）！2022 年建仓的开源 Office SDK，简介是「The Office Harness for AI Agents」：表格、文档、幻灯片、画布、关系表、PDF 一套运行时，Canvas 渲染 + 公式引擎 + 插件架构 + 浏览器与 Node 同构的 Facade API。",
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
            "<strong>连登第二天站上 2.1 万星：</strong>四天里从 15,352★ 涨到 20,996★，改个定位换来的这轮增长还没结束。",
            "<strong>它与 VoiceStudio 构成今天的自持组合：</strong>一个把办公文件留在本地，一个把声音留在本地——凡是过去必须上云的能力，都在被本地推理逐个拿回来。",
            "<strong>本质是资产重定价：</strong>技术周期切换时，最先受益的往往不是新项目，而是早就把事做好、只差一个说法的老项目。"
        ],
        "tags": ["office-sdk", "spreadsheet", "typescript", "ai-agents", "chinese"]
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
    "date": "2026-09-28",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-28'
data['topic'] = '🔥 <strong>全本地语音替代品首登 + harness 之上再长出一层编排 + 记忆与组织两条线同时加速</strong> —— debpalash/VoiceStudio（+3,274★）4.2 万星首登：完全本地的 ElevenLabs 开源替代，646 种语言的克隆、音色设计、配音、听写、有声书，还带本地 API 与 MCP 给 Agent 调用。vectorize-io/hindsight（+4,413★）今天全榜日增最高，四天从 26,963★ 涨到 39,892★：会学习的 Agent 记忆系统。paperclipai/paperclip（+3,185★）连登突破 9.1 万星：把 Agent 当员工管。mvschwarz/openrig（+781★）提出「harness 包的是一个模型，rig 包的是你的 harness」：一份 YAML 定义 Agent 团队，Claude Code 与 Codex 同场协作，Node 与 tmux 环境。dream-num/univer（+1,105★）连登站上 2.1 万星。byoungd/up（+310★）6.4 万星中文书稿《人生进阶指南》：把内容分成研究结论、个人经验与待验证假设三类。cs341-illinois/coursebook（+265★）伊利诺伊大学系统编程开源教材。NawfalMotii79/PLFM_RADAR（+145★）2.5 万星、五千多次 fork 的开源 10.5 GHz 相控阵雷达。今日三条主线：一、本地化边界继续外扩——文本、文档、相册之后是语音；二、抽象层继续加高，harness 刚成品类词，rig 已经在编排多个 harness；三、记忆与组织两条线同时加速，一个解决记得住，一个解决管得清。'

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
