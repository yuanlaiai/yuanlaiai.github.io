#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-18 (1-day gap, 双栏：新面孔 6 + 连登 6)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 18)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-17 榜上）══
    {
        "rank": 1,
        "owner": "Tencent",
        "name": "BrowserSkill",
        "fullName": "Tencent / BrowserSkill",
        "org": "Tencent",
        "url": "https://github.com/Tencent/BrowserSkill",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "4,076",
        "forks": "288",
        "starsToday": "1,350",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,350★ 首登即新面孔第一！腾讯开源：让 AI Agent 用你「已经登录的真实浏览器」干活，而且不打断你手上的工作——CLI + 扩展，一个连接器打通十余种 Agent。",
        "problems": [
            "<strong>Agent 拿不到登录态：</strong>让它操作后台、邮箱、内部系统，第一步就卡在登录与会话。",
            "<strong>另起一个浏览器实例：</strong>干净环境反被风控识别，验证码与二次验证轮番上。",
            "<strong>自动化会抢走你的屏幕：</strong>Agent 一操作，人类就没法用同一台机器干活。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Tencent/BrowserSkill.git</code></pre>",
            "安装 CLI 与浏览器扩展，接入你已登录的浏览器会话。",
            "在 Cursor / Claude Code / Codex / OpenClaw / CodeBuddy / WorkBuddy / Pi / DeepSeek Harness 等 Agent 中调用。"
        ],
        "insights": [
            "<strong>腾讯一周内的第二个登榜项目：</strong>昨天是 WeKnora（知识），今天是 BrowserSkill（手），国内大厂开始成体系地开源 Agent 基建，而不是零散发布。",
            "<strong>卖点是「不打断你」：</strong>复用真实登录态而不是启动干净实例——这是 Agent 落地最后一公里的真实痛点，也是隐私争议的起点（哪些站点允许被 Agent 操作，目前没有共识）。",
            "<strong>兼容清单本身就是行业地图：</strong>它一口气列出了十余种 Agent 宿主，等于押注「Agent 框架会长期碎片化」——做跨框架连接器，比做其中一个框架更安全。"
        ],
        "tags": ["browser", "agent", "automation", "tencent", "cli"]
    },
    {
        "rank": 2,
        "owner": "anthropics",
        "name": "claude-code",
        "fullName": "anthropics / claude-code",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-code",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "145,849",
        "forks": "23,622",
        "starsToday": "538",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +538★！145.8K★ 时隔 26 天回归（上次 8-23 为 142,521★）！Anthropic 官方的终端 Agent——理解你的代码库、执行日常任务、处理 Git 流程，全部走自然语言命令。",
        "problems": [
            "<strong>AI 与终端割裂：</strong>模型在网页里聊，改代码还得手工复制粘贴。",
            "<strong>不懂项目上下文：</strong>通用助手看不到仓库结构、依赖与约定。",
            "<strong>缺少可审计执行：</strong>让 AI 直接动文件与 Git，过程不可控。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @anthropic-ai/claude-code</code></pre>",
            "在项目目录启动，用自然语言下达任务。",
            "让它执行测试、解释代码、处理 Git 工作流。"
        ],
        "insights": [
            "<strong>回归的时机很准：</strong>本周 Google 宣布允许全体工程师使用 Claude 编码、Anthropic 又把聊天与 Cowork 合并——品类定义者在新一轮新闻密度中重新被搜索与收藏。",
            "<strong>与今天榜单的宿主之争同台：</strong>claude-code（终端）、cline（IDE/桌面）、BrowserSkill（浏览器）、Octop（自托管桌面）同框——「Agent 住在哪」正是当下竞争最激烈的层。",
            "<strong>26 天涨 3,328★：</strong>在大量免费替代品出现的背景下仍保持增长，说明官方宿主在「能力更新速度」上仍有不可替代性。"
        ],
        "tags": ["agent", "coding", "cli", "anthropic", "terminal"]
    },
    {
        "rank": 3,
        "owner": "TencentCloud",
        "name": "Octop",
        "fullName": "TencentCloud / Octop",
        "org": "Tencent Cloud",
        "url": "https://github.com/TencentCloud/Octop",
        "lang": "Python",
        "langClass": "py",
        "stars": "3,413",
        "forks": "352",
        "starsToday": "386",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +386★ 首登！腾讯云的自托管 AI 助手——多用户、多 Agent、本地优先，把「个人助手」升级成团队可共享的助手。",
        "problems": [
            "<strong>企业数据不能出内网：</strong>SaaS 助手用着方便，但代码库与客户数据经不起外传。",
            "<strong>个人助手无法共享：</strong>一个人调教好的助手，团队其他人用不上。",
            "<strong>多 Agent 难以共处：</strong>不同角色、不同权限的 Agent 缺少统一编排。"
        ],
        "usage": [
            "克隆并自托管：<pre><code>git clone https://github.com/TencentCloud/Octop.git</code></pre>",
            "按用户与角色配置多个 Agent，共享同一套知识与工具。",
            "数据留在本地，按需对接企业内部的模型端点。"
        ],
        "insights": [
            "<strong>腾讯今天实际占了三个名额：</strong>BrowserSkill（首登）、Octop（首登）、WeKnora（连登）——一天之内，知识、手、助手本体三条线同时上榜，这种密度在榜单历史上少见。",
            "<strong>「多用户」才是企业级的分水岭：</strong>消费级助手比的是聪明，企业级比的是权限、审计与共享——这也是自托管路线唯一能建立差异的地方。",
            "<strong>local-first 是合规压力下的默认答案：</strong>本周另一条新闻是 Anthropic 指控中国公司蒸馏、以及各国对数据出境的收紧——本地优先从「极客偏好」变成了「采购前提」。"
        ],
        "tags": ["assistant", "self-hosted", "multi-agent", "local-first", "tencent"]
    },
    {
        "rank": 4,
        "owner": "cline",
        "name": "cline",
        "fullName": "cline / cline",
        "org": "Cline",
        "url": "https://github.com/cline/cline",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "68,545",
        "forks": "7,413",
        "starsToday": "381",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +381★！68.5K★ 首登！开源编码 Agent 的三种形态：IDE 插件、终端 CLI、桌面应用——自带你的模型密钥，Apache-2.0 许可，企业无需担心许可费。",
        "problems": [
            "<strong>闭源 Agent 的成本与合规：</strong>按席位订阅的编码助手在团队规模化后账单陡增。",
            "<strong>模型被绑定：</strong>只能用手册允许的模型与推理端点。",
            "<strong>形态单一：</strong>习惯 IDE 的人不想去终端，习惯终端的人不想进 IDE。"
        ],
        "usage": [
            "IDE 安装：在 VS Code / JetBrains 插件市场搜索 Cline。",
            "终端：<pre><code>npm install -g cline</code></pre>",
            "配置自己的模型与密钥（支持多供应商），按任务选择形态。"
        ],
        "insights": [
            "<strong>「三种形态」是它的核心策略：</strong>不赌用户在哪工作，而是把所有入口都占住——这与今天榜单上其它 Agent 宿主的思路正好相反（它们各守一个入口）。",
            "<strong>Apache-2.0 是企业采购的通行证：</strong>在合规敏感的组织里，许可证类型往往比功能差异更能决定采用。",
            "<strong>首登就带着 68.5K★ 说明存量巨大：</strong>它不是新项目，而是长期在榜外积累的成熟工具——今天被趋势榜重新发现，通常意味着某个功能节点（多形态/多模型）刚被社区大规模讨论。"
        ],
        "tags": ["coding-agent", "ide", "cli", "open-source", "typescript"]
    },
    {
        "rank": 5,
        "owner": "roboflow",
        "name": "supervision",
        "fullName": "roboflow / supervision",
        "org": "Roboflow",
        "url": "https://github.com/roboflow/supervision",
        "lang": "Python",
        "langClass": "py",
        "stars": "50,794",
        "forks": "4,828",
        "starsToday": "327",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +327★！50.8K★ 时隔三个月回归（6-8 时 42,961★，净增 7.8K★）！Roboflow 的可复用计算机视觉工具库——标注、追踪、区域计数、视频处理，把检测模型输出变成能用的业务逻辑。",
        "problems": [
            "<strong>检测输出不可直接用：</strong>模型给框，业务要的是计数、越界判断与轨迹追踪。",
            "<strong>每个项目重复造轮子：</strong>可视化、NMS、追踪各写一遍，质量参差。",
            "<strong>从 demo 到部署断层：</strong>Notebook 里跑得通，接到视频流就崩。"
        ],
        "usage": [
            "安装：<pre><code>pip install supervision</code></pre>",
            "把检测/分割结果交给它做标注、追踪、区域统计。",
            "组合 Zone / Tracker / Annotator 搭出业务画面。"
        ],
        "insights": [
            "<strong>LLM 霸榜环境里的稳定增长：</strong>6 月二登 42,961★ → 今天 50,794★，三个月净增 7.8K★，热度完全不依赖 AI 话题周期。",
            "<strong>视觉是「物理 AI」的底座：</strong>机器人、工业质检、自动驾驶的落地都绕不开目标检测与追踪——语言模型的热度掩盖了这条线的真实规模。",
            "<strong>它的价值在「后半段」：</strong>训练框架已经商品化，而把模型输出变成可交付业务逻辑的那一段仍然碎片——工具库吃的是这段的确定性收益。"
        ],
        "tags": ["computer-vision", "tracking", "python", "detection", "tools"]
    },
    {
        "rank": 6,
        "owner": "n8n-io",
        "name": "n8n",
        "fullName": "n8n-io / n8n",
        "org": "n8n",
        "url": "https://github.com/n8n-io/n8n",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "204,952",
        "forks": "60,743",
        "starsToday": "319",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +319★！205K★ 时隔 26 天回归（8-23 时 201,805★）！工作流自动化平台 + 原生 AI 能力：可视化画布与自定义代码并存，自带部署或云端皆可，1500+ 集成。",
        "problems": [
            "<strong>AI 落地缺少编排层：</strong>模型能跑单点任务，跨系统的业务流程仍需人肉串联。",
            "<strong>纯代码自动化门槛高：</strong>业务方无法参与，改动全靠工程师排期。",
            "<strong>SaaS 编排的合规顾虑：</strong>流程数据经过第三方服务器。"
        ],
        "usage": [
            "自托管：<pre><code>docker run -it --rm --name n8n -p 5678:5678 docker.n8n.io/n8nio/n8n</code></pre>",
            "在画布上串联触发、AI 节点与 1500+ 集成。",
            "复杂逻辑用代码节点兜底，版本化保存工作流。"
        ],
        "insights": [
            "<strong>与 Jev 那条路线形成对照：</strong>一边是「把智能压成 if 语句」，一边是「让业务自己画出流程」——企业更信哪一种，看 n8n 的 205K★ 就有答案。",
            "<strong>26 天涨 3,147★ 且是 fair-code：</strong>非完全开源的许可模式（fair-code）在商业上被反复验证——对基础设施类项目，「开源核心 + 云托管」仍是唯一跑通的路径。",
            "<strong>「1500+ 集成」是真正的护城河：</strong>编排工具的价值从不在引擎，而在能连上多少系统——这条护城河需要十年积累，也是它难以被 AI 原生工具取代的原因。"
        ],
        "tags": ["automation", "workflow", "integrations", "self-hosted", "typescript"]
    },
    # ══ 连登（09-17 榜上继续）══
    {
        "rank": 7,
        "owner": "cloudflare",
        "name": "security-audit-skill",
        "fullName": "cloudflare / security-audit-skill",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "10,517",
        "forks": "561",
        "starsToday": "3,606",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天即登顶！今日 +3,606★（昨天 7,054★ → 今天 10,517★，一天涨 3,463★）——Cloudflare 官方安全审计技能，六阶段流程 + 独立验证，是自家全网漏洞发现系统的源头版本。",
        "problems": [
            "<strong>安全审计没有账本：</strong>查过哪些攻击面、谁查的，全凭记忆。",
            "<strong>Agent 报告不可信：</strong>缺少独立验证，误报与幻觉混在一起。",
            "<strong>产出无法交接：</strong>没有机器可读的结构化结果，团队无法复用。"
        ],
        "usage": [
            "把技能装进 Claude Code / Codex 等 Agent 的 skills 目录。",
            "跑完六阶段，产出 architecture.md 与 coverage-ledger.json。",
            "每个候选漏洞交给独立验证 Agent 去证伪，只保留可确认项。"
        ],
        "insights": [
            "<strong>一天翻 1.5 倍：</strong>7,054★ → 10,517★，从「新面孔」直接变成日榜第一——企业官方署名的技能，扩散速度明显快于个人项目。",
            "<strong>与昨天的 Claude-Red 组成一对：</strong>一个防守（审计）、一个进攻（红队），共用同一套 Agent 技能机制——这周榜单最清晰的主题就是「安全技能化」。",
            "<strong>本质是把可信度工程化：</strong>让另一个 Agent 去证伪，等于把「谁来验证」这道信任题转成了流程题——这是安全 Agent 能被企业采用的前提。"
        ],
        "tags": ["security", "agent-skills", "audit", "cloudflare", "javascript"]
    },
    {
        "rank": 8,
        "owner": "alibaba",
        "name": "open-code-review",
        "fullName": "alibaba / open-code-review",
        "org": "Alibaba",
        "url": "https://github.com/alibaba/open-code-review",
        "lang": "Go",
        "langClass": "go",
        "stars": "34,636",
        "forks": "2,462",
        "starsToday": "3,290",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连续第二天日增 3,000+★！31,699★ → 34,636★，今日 +3,290★！阿里官方代码审查工具：确定性管线 + LLM Agent，行级评论，内置 NPE / 线程安全 / XSS / SQL 注入规则集。",
        "problems": [
            "<strong>大厂 PR 洪流：</strong>每天成千上万次提交，人工 Review 成为瓶颈。",
            "<strong>纯模型评审不可靠：</strong>幻觉与漏报让工程师不敢采信。",
            "<strong>规则与语义割裂：</strong>静态检查抓不到语义，模型抓不住硬性缺陷。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/alibaba/open-code-review.git</code></pre>",
            "接入仓库与 CI，选择规则集与模型端点。",
            "在 PR 上直接获得行级评论与修复建议。"
        ],
        "insights": [
            "<strong>连续两天日增 3,000+★：</strong>7-28 首登 14,772★，今天 34,636★——不到两个月翻 2.3 倍，靠的不是话题而是「被验证过的规则集」。",
            "<strong>与 Cloudflare 同框说明同一件事：</strong>本轮爆发的项目都带着机构署名与生产环境验证，个人玩具类项目在这两周基本没有登顶机会。",
            "<strong>本质是「审查权」的迁移：</strong>机审覆盖确定性缺陷后，人类 Reviewer 的时间被挤向架构判断——代码质量门槛从「谁看得多」变成「谁的规则库更全」。"
        ],
        "tags": ["code-review", "agent", "go", "alibaba", "static-analysis"]
    },
    {
        "rank": 9,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "261,126",
        "forks": "39,088",
        "starsToday": "1,173",
        "count": 8,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +1,173★！261K★ 第八次上榜（昨天 260,221★）！Agent Harness 性能优化系统——技能、直觉、记忆、安全，跨 Claude Code / Codex / Opencode / Cursor 通用。",
        "problems": [
            "<strong>Agent 效率没有优化层：</strong>同一任务不同跑法成本差几倍。",
            "<strong>技能与记忆割裂：</strong>配置分散、彼此打架。",
            "<strong>权限边界模糊：</strong>Agent 权限越大，约束越少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/affaan-m/ECC.git</code></pre>",
            "接入 Claude Code / Codex / Opencode / Cursor。",
            "启用技能、记忆与安全策略。"
        ],
        "insights": [
            "<strong>八登、261K★、日增仍过千：</strong>7-30 时 236,008★，如今 261,126★——两个月涨 25K★，是榜单里最稳的长青标的。",
            "<strong>与 claude-code、cline 同台：</strong>宿主之争越激烈，跨宿主的「优化层」越有价值——ECC 的位置就像当年的运维工具：不选边，服务所有边。",
            "<strong>本质是 Agent 的中间件：</strong>模型、框架、技能各自迭代飞快，中间必然长出一层做协调与约束——占住这层就掌握了 Agent 的「操作系统」。"
        ],
        "tags": ["agent", "harness", "optimization", "memory", "javascript"]
    },
    {
        "rank": 10,
        "owner": "Tencent",
        "name": "WeKnora",
        "fullName": "Tencent / WeKnora",
        "org": "Tencent",
        "url": "https://github.com/Tencent/WeKnora",
        "lang": "Go",
        "langClass": "go",
        "stars": "26,160",
        "forks": "3,548",
        "starsToday": "1,123",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +1,123★！25,235★ → 26,160★！腾讯开源的 LLM 知识平台——文档变 RAG、RAG 变推理 Agent、最后长成会自我维护的 Wiki。",
        "problems": [
            "<strong>企业文档沉睡：</strong>资料堆在网盘里，没人能问出答案。",
            "<strong>RAG 上线即烂：</strong>知识库无人维护，几周就失真。",
            "<strong>问答不沉淀：</strong>结论不回流，同一问题反复检索。"
        ],
        "usage": [
            "部署：<pre><code>git clone https://github.com/Tencent/WeKnora.git</code></pre>",
            "导入原始文档，自动建索引与推理 Agent。",
            "开启自维护 Wiki，把问答结论写回知识库。"
        ],
        "insights": [
            "<strong>连登与两个腾讯新项目同榜：</strong>BrowserSkill（手）、Octop（助手本体）、WeKnora（记忆）——一天三个名额，腾讯在 Agent 基建上是成编制投入。",
            "<strong>日增翻倍仍不及自家新项目：</strong>说明榜单的新鲜度机制在起作用——老项目热，但新面孔的势能更高。",
            "<strong>「自维护 Wiki」是它真正的差异点：</strong>把 RAG 从一次性检索变成持续累积，等于让知识库自己长大——这是知识资产第一次可以脱离专家记忆独立存在。"
        ],
        "tags": ["rag", "knowledge-base", "agent", "go", "tencent"]
    },
    {
        "rank": 11,
        "owner": "alphaXiv",
        "name": "OpenResearch",
        "fullName": "alphaXiv / OpenResearch",
        "org": "alphaXiv",
        "url": "https://github.com/alphaXiv/OpenResearch",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "4,924",
        "forks": "304",
        "starsToday": "940",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +940★！4,370★ → 4,924★！把 Claude Code、Codex、OpenCode、Cursor 变成研究 Agent 的本地工作台——读文献、提假设、跑实验、产出研究工件。",
        "problems": [
            "<strong>科研流程断裂：</strong>文献、笔记、实验代码分散在十几个工具。",
            "<strong>编码 Agent 不懂科研：</strong>会写代码，不懂假设检验与文献综述。",
            "<strong>未发表想法不敢上云：</strong>第三方服务托管研究数据风险高。"
        ],
        "usage": [
            "下载桌面版：<pre><code>https://github.com/alphaXiv/OpenResearch/releases/latest</code></pre>",
            "接入已有的编码 Agent。",
            "按「文献 → 假设 → 实验 → 工件」推进研究。"
        ],
        "insights": [
            "<strong>连登且涨幅高于首登：</strong>昨天 +1,036★、今天 +940★，两天合计近 2,000★——小体量项目靠日增进榜的典型形态。",
            "<strong>与 Jev 的内核假设一致：</strong>两者都在说「通用聊天模型不是终点」——一个把智能压成判定，一个把智能组织成研究流程。",
            "<strong>本质是科研成本结构被改写：</strong>当文献综述与实验脚手架交给 Agent，研究者的稀缺能力从「执行力」转向「提问的品味」。"
        ],
        "tags": ["research", "agent", "rust", "local-first", "science"]
    },
    {
        "rank": 12,
        "owner": "NationalSecurityAgency",
        "name": "ghidra",
        "fullName": "NationalSecurityAgency / ghidra",
        "org": "NSA",
        "url": "https://github.com/NationalSecurityAgency/ghidra",
        "lang": "Java",
        "langClass": "java",
        "stars": "78,451",
        "forks": "8,680",
        "starsToday": "912",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +912★！78.5K★ 第四次上榜（昨天 77,740★）！NSA 开源的逆向工程框架——反汇编、反编译、脚本化分析，二进制世界的基础设施。",
        "problems": [
            "<strong>逆向工具昂贵：</strong>商业反编译器年费数千美元。",
            "<strong>二进制黑箱：</strong>没有源码就无法审计漏洞与后门。",
            "<strong>分析无法协作：</strong>缺少可脚本化、可版本化的流程。"
        ],
        "usage": [
            "下载发行版：<pre><code>https://github.com/NationalSecurityAgency/ghidra/releases</code></pre>",
            "导入二进制，自动反汇编与反编译。",
            "用脚本批量做特征扫描与漏洞定位。"
        ],
        "insights": [
            "<strong>四登、四天涨 4,900★：</strong>8-29 首登 73,517★，今天 78,451★——AI 生成代码越多，能看懂二进制的人越值钱。",
            "<strong>与 Cloudflare 审计技能、Claude-Red 同框：</strong>源码审计（技能化）、红队方法论（技能化）、二进制逆向（工具化）——三个方向同时扩容，本周的安全主题完整闭环。",
            "<strong>本质是供应链安全的最后一道人工防线：</strong>当依赖越来越深、代码越来越由 AI 生成，能拆开看的手艺反而成了稀缺资源。"
        ],
        "tags": ["reverse-engineering", "security", "ghidra", "java", "binary-analysis"]
    }
]

# Shift labels for 1-day gap (accurate offset: +1)
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
    "date": "2026-09-18",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-18'
data['topic'] = '🔥 <strong>腾讯一天三项目登榜（BrowserSkill + Octop + WeKnora）+ Cloudflare 审计技能连登即登顶 + 阿里 code-review 连续两天日增 3000★ + Claude Code / Cline 回归 —— Agent 宿主之争白热化</strong> —— Tencent/BrowserSkill（+1,350★）让 Agent 用你已登录的真实浏览器，首登。anthropics/claude-code（+538★）145.8K★ 时隔 26 天回归。TencentCloud/Octop（+386★）腾讯云自托管多用户助手首登。cline/cline（+381★）68.5K★ 三形态开源编码 Agent 首登。roboflow/supervision（+327★）50.8K★ 计算机视觉工具库三个月后回归。n8n-io/n8n（+319★）205K★ 工作流自动化回归。cloudflare/security-audit-skill（+3,606★）连登第二天直接登顶，一天翻 1.5 倍。alibaba/open-code-review（+3,290★）34.6K★ 三登，两个月翻 2.3 倍。affaan-m/ECC（+1,173★）261K★ 八登。Tencent/WeKnora（+1,123★）连登。alphaXiv/OpenResearch（+940★）研究 Agent 连登。NationalSecurityAgency/ghidra（+912★）78.5K★ 四登。今日三条明线：一、机构署名项目全面压制个人玩具（Cloudflare、阿里、腾讯、洛克希德式的 NSA 都带着生产验证）；二、Agent 宿主之争白热化（终端 claude-code、IDE/桌面 cline、浏览器 BrowserSkill、自托管 Octop 同台）；三、安全技能形成完整闭环（源码审计 + 红队方法论 + 二进制逆向）。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:5]]}")

# Verify badge present on every project
assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
