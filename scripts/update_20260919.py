#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-19 (1-day gap, 双栏：新面孔 6 + 连登 6)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 19)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-18 榜上）══
    {
        "rank": 1,
        "owner": "asciimoo",
        "name": "hister",
        "fullName": "asciimoo / hister",
        "org": "asciimoo",
        "url": "https://github.com/asciimoo/hister",
        "lang": "Go",
        "langClass": "go",
        "stars": "4,997",
        "forks": "209",
        "starsToday": "889",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +889★ 首登即新面孔第一！自己的搜索引擎：索引你访问过的网页与本地文件的全文，从网页、终端、或通过 MCP 接入 AI 助手随时找回——数据完全留在本机。",
        "problems": [
            "<strong>浏览器历史找不回：</strong>看过的东西三天后就想不起来在哪个页面。",
            "<strong>云端笔记有隐私代价：</strong>把工作资料交给第三方索引，等于永久授权。",
            "<strong>AI 助手看不到你的资料：</strong>本地文件无法被助手检索，只能靠人肉复制粘贴。"
        ],
        "usage": [
            "下载发行版：<pre><code>https://github.com/asciimoo/hister/releases/latest</code></pre>",
            "索引网页历史与本地目录的全文内容。",
            "通过网页界面、终端或 MCP 让 AI 助手直接检索。"
        ],
        "insights": [
            "<strong>「你的搜索引擎」这个定位踩中了两个趋势：</strong>一是数据主权（索引留在本机），二是 MCP 成为本地数据的标准出口——不做产品界面，只做能被 AI 调用的记忆层。",
            "<strong>与榜单上的知识类项目形成对照：</strong>腾讯 WeKnora 解决的是「企业文档」，hister 解决的是「你个人的浏览与文件」——同一需求的两端，都在把「检索」变成基础设施。",
            "<strong>本质是搜索权的下放：</strong>搜索引擎过去是入口，如今个人可以自建索引——当 AI 需要长期记忆时，「谁掌握你的历史」就变成了一个架构选择，而不是隐私条款问题。"
        ],
        "tags": ["search", "local-first", "mcp", "go", "privacy"]
    },
    {
        "rank": 2,
        "owner": "addyosmani",
        "name": "agent-skills",
        "fullName": "addyosmani / agent-skills",
        "org": "Addy Osmani",
        "url": "https://github.com/addyosmani/agent-skills",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "96,489",
        "forks": "10,109",
        "starsToday": "675",
        "count": 9,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +675★！96.5K★ 第九次上榜（前天 8 登 95,413★）！把资深工程师的工作流固化成技能：定义 → 规划 → 构建 → 验证 → 评审 → 发布，每个阶段都有质量门禁。",
        "problems": [
            "<strong>Agent 代码质量随机：</strong>同一需求不同轮次产出差异巨大。",
            "<strong>流程无门禁：</strong>Agent 会直接开写，跳过需求澄清与验证。",
            "<strong>资深经验难传递：</strong>高工的判断标准留在脑子里。"
        ],
        "usage": [
            "安装：<pre><code>npx skills add addyosmani/agent-skills</code></pre>",
            "接入 Claude Code / Codex / Cursor 等 Agent。",
            "按阶段启用：从需求定义到发布评审的整套技能。"
        ],
        "insights": [
            "<strong>九天三次上榜（9、八登、今天九登）：</strong>8-10 时 85,320★，今天 96,489★——六周涨 11K★，且登榜节奏明显加快。",
            "<strong>它与今天的 OpenSpec 是同一件事的两面：</strong>一个给流程（六阶段技能），一个给规格（先写 spec 再让 AI 写码）——社区正在集体承认：Agent 的问题不是能力，是缺乏纪律。",
            "<strong>本质是工程规范的重新定价：</strong>当写代码的成本趋零，「什么算合格的代码」就成了最值钱的知识——技能库卖的不是能力，是判断标准。"
        ],
        "tags": ["agent-skills", "engineering", "quality-gates", "javascript", "claude-code"]
    },
    {
        "rank": 3,
        "owner": "coder",
        "name": "coder",
        "fullName": "coder / coder",
        "org": "Coder",
        "url": "https://github.com/coder/coder",
        "lang": "Go",
        "langClass": "go",
        "stars": "15,345",
        "forks": "1,135",
        "starsToday": "478",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +478★ 首登！自托管的云开发环境——给开发者和他们的 AI Agent 提供安全、隔离、可复制的远程工作空间，Agent 在受控环境里跑代码，而不是在你笔记本上。",
        "problems": [
            "<strong>Agent 在本地跑很危险：</strong>让它执行命令、装依赖，等同于把生产密钥交出去。",
            "<strong>环境不一致：</strong>「在我机器上能跑」的问题在 Agent 时代被放大。",
            "<strong>云端开发环境不自主：</strong>SaaS 方案把源码与密钥托管给第三方。"
        ],
        "usage": [
            "自托管部署：<pre><code>https://coder.com/docs/install</code></pre>",
            "用模板定义开发环境（语言、依赖、权限边界）。",
            "让开发者与 AI Agent 在同一套受控环境里协作。"
        ],
        "insights": [
            "<strong>一句「和他们的 Agent」点了题：</strong>README 标题已从「给开发者的环境」变成「给开发者和他们的 Agent 的环境」——基础设施的默认用户正在从人扩到 Agent。",
            "<strong>与 hister、rustfs、Octop 构成同一条线：</strong>自托管（环境）、私有索引（数据）、S3 替代（存储）——今天榜单上「数据主权」出现了四次，这是本周最连贯的趋势。",
            "<strong>本质是权限边界的重建：</strong>Agent 要能干活就必须有权限，于是「隔离的执行环境」从 DevOps 的优化项变成了安全的前置条件——这是 Agent 落地无法绕开的一层。"
        ],
        "tags": ["dev-environment", "self-hosted", "agent", "go", "remote"]
    },
    {
        "rank": 4,
        "owner": "anthropics",
        "name": "knowledge-work-plugins",
        "fullName": "anthropics / knowledge-work-plugins",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/knowledge-work-plugins",
        "lang": "Python",
        "langClass": "py",
        "stars": "24,921",
        "forks": "2,922",
        "starsToday": "299",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +299★！24.9K★ 第三次上榜（上次纪录为 5-25 的 16,633★，四个月涨 8.3K★）！Anthropic 官方的知识工作者插件库——把 Claude 变成你岗位、团队、公司的专家，为 Claude Cowork 打造，同时兼容 Claude Code。",
        "problems": [
            "<strong>通用助手不懂你的岗位：</strong>同一句指令，不同职能需要完全不同的产出。",
            "<strong>团队产出不一致：</strong>每个人调教方式不同，交付质量参差。",
            "<strong>工作流无法固化：</strong>「我喜欢怎么做」说不清，也没法让 AI 记住。"
        ],
        "usage": [
            "在 Claude Cowork（或 Claude Code）中安装插件。",
            "按角色启用：技能、连接器、斜杠命令一并打包。",
            "把团队的工作偏好与数据源写进插件配置。"
        ],
        "insights": [
            "<strong>官方亲自下场的信号：</strong>插件库由 Anthropic 维护，说明「角色化插件」被当成产品方向而非社区玩法——配合本周「Claude 聊天与 Cowork 合并」的报道，超级 app 的拼图正在补齐。",
            "<strong>四个月涨 8.3K★而中间没上榜：</strong>安静增长型项目，本次登榜更像被「Claude Cowork 合并」的新闻推上来。",
            "<strong>本质是「岗位知识」的产品化：</strong>把「我们团队怎么干活」打包成可安装的资产——这意味着组织经验第一次有了版本号。"
        ],
        "tags": ["plugins", "claude-cowork", "knowledge-work", "anthropic", "python"]
    },
    {
        "rank": 5,
        "owner": "Fission-AI",
        "name": "OpenSpec",
        "fullName": "Fission-AI / OpenSpec",
        "org": "Fission-AI",
        "url": "https://github.com/Fission-AI/OpenSpec",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "69,420",
        "forks": "4,235",
        "starsToday": "296",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +296★！69.4K★ 首登！给 AI 编码助手的「规格驱动开发」（SDD）：先让 AI 写清楚要做什么，达成一致之后才允许动手写代码——把最贵的返工成本挪到最便宜的一步。",
        "problems": [
            "<strong>AI 一上来就写码：</strong>方向理解偏了，代码越写越贵。",
            "<strong>需求藏在对话里：</strong>几十轮聊天之后没人知道最初要什么。",
            "<strong>改动无法追溯：</strong>没有规格文档，评审时无法判断是否偏离初衷。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @fission-ai/openspec</code></pre>",
            "初始化：<pre><code>openspec init</code></pre> 生成规格目录。",
            "让 Agent 先补全规格、经你确认后再实施；改动走同一条规格流程。"
        ],
        "insights": [
            "<strong>69.4K★ 首次登榜却不是新项目：</strong>这类项目的热度来自方法论共识的形成——「先规格后编码」被越来越多的团队当成默认做法。",
            "<strong>与 addyosmani/agent-skills 同日上榜：</strong>榜单上同时出现「流程技能」与「规格优先」，这是同一诉求的两种实现——社区正在给 Agent 立规矩。",
            "<strong>本质是给生成式开发装刹车：</strong>当写代码的成本趋零，返工成本就成了主要开销——规格检查点的价值，就是把错误拦在最便宜的地方。"
        ],
        "tags": ["spec-driven", "ai-coding", "workflow", "typescript", "sdd"]
    },
    {
        "rank": 6,
        "owner": "rustfs",
        "name": "rustfs",
        "fullName": "rustfs / rustfs",
        "org": "RustFS",
        "url": "https://github.com/rustfs/rustfs",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "33,216",
        "forks": "1,604",
        "starsToday": "267",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +267★！33.2K★ 首登！Rust 写的 S3 兼容高性能分布式对象存储——支持与 MinIO、Ceph 共存和迁移，瞄准的是「AI 时代的数据底座」。",
        "problems": [
            "<strong>对象存储被单一厂商绑定：</strong>MinIO 的许可变更与商业策略让用户被迫重新选型。",
            "<strong>海量数据成本失控：</strong>训练数据、日志、模型权重越堆越大，存储账单跑得比算力还快。",
            "<strong>迁移几乎不可能：</strong>换存储意味着停机与数据搬迁风险。"
        ],
        "usage": [
            "Docker 快速起步：<pre><code>docker run -d -p 9000:9000 rustfs/rustfs</code></pre>",
            "对接现有 S3 客户端与工具链。",
            "按需从 MinIO / Ceph 平滑迁移或共存。"
        ],
        "insights": [
            "<strong>选在 MinIO 争议之后发力：</strong>S3 兼容层是少数「许可变更就能引发迁移潮」的市场，Rust 重写带来的性能与内存优势是它的切口。",
            "<strong>今天榜单的第四条主权线：</strong>hister（索引）、coder（环境）、rustfs（存储）、Octop（助手）——四个自托管项目同日上榜，这在榜单历史上前所未见。",
            "<strong>本质是 AI 的物理成本被人重新计算：</strong>算力常被讨论，但真正随规模线性膨胀的是存储——谁把每 TB 成本压下来，谁就掌握 AI 数据层的话语权。"
        ],
        "tags": ["object-storage", "s3", "rust", "self-hosted", "minio"]
    },
    # ══ 连登（09-18 榜上继续）══
    {
        "rank": 7,
        "owner": "cloudflare",
        "name": "security-audit-skill",
        "fullName": "cloudflare / security-audit-skill",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "14,072",
        "forks": "694",
        "starsToday": "3,006",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 三连登且稳居榜首！今日 +3,006★（7,054★ → 10,517★ → 14,072★，两天翻一倍）！Cloudflare 官方安全审计技能，六阶段流程 + 独立验证，是自家全网漏洞发现系统的源头版本。",
        "problems": [
            "<strong>审计没有覆盖账本：</strong>查过什么、漏了什么，全凭记忆。",
            "<strong>Agent 结论不可信：</strong>缺独立验证，误报与幻觉混杂。",
            "<strong>结果无法交接：</strong>缺少机器可读产出，团队难以复用。"
        ],
        "usage": [
            "把技能装进 Claude Code / Codex 的 skills 目录。",
            "跑完六阶段，产出 architecture.md 与 coverage-ledger.json。",
            "每个候选漏洞交给独立验证 Agent 证伪后再入库。"
        ],
        "insights": [
            "<strong>两天翻倍、三连登居首：</strong>7,054★ → 14,072★，日增连续三天在 3,000★ 量级——这是榜单近期最强的单项目走势。",
            "<strong>「官方 + 生产验证」是这轮爆款的共同配方：</strong>Cloudflare、阿里、腾讯的项目都在用「我们在生产环境用了很久」当前提，而不是讲技术概念。",
            "<strong>本质是安全能力的组织化：</strong>把六阶段流程写成技能，等于把一家公司的安全方法论变成可安装资产——这是安全行业第一次能「分发方法论」。"
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
        "stars": "36,828",
        "forks": "2,562",
        "starsToday": "2,704",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 四连登，今日 +2,704★（31,699★ → 34,636★ → 36,828★）！阿里官方代码审查工具：确定性管线 + LLM Agent 混合架构，行级评论，内置 NPE / 线程安全 / XSS / SQL 注入规则集。",
        "problems": [
            "<strong>大厂 PR 洪流：</strong>人工 Review 成为交付瓶颈。",
            "<strong>纯模型评审不可靠：</strong>幻觉与漏报让工程师不敢采信。",
            "<strong>规则与语义割裂：</strong>静态检查抓不到语义，模型抓不住硬性缺陷。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/alibaba/open-code-review.git</code></pre>",
            "接入仓库与 CI，配置规则集与模型端点。",
            "在 PR 上获取行级评论与修复建议。"
        ],
        "insights": [
            "<strong>连续三天日增 2,700★ 以上：</strong>7-28 首登 14,772★，今天 36,828★——不到两个月翻 2.5 倍，是本周最稳的趋势项目。",
            "<strong>与同日的 OpenSpec、agent-skills 构成「审查三件套」：</strong>规格（事前）、规范（事中）、审查（事后）——质量体系被拆成三个热榜项目，说明团队真的在采购这条链。",
            "<strong>本质是审查从「人」变成「规则库」：</strong>谁积累的规则多、误报少，谁就定义了代码合格线的下限。"
        ],
        "tags": ["code-review", "agent", "go", "alibaba", "static-analysis"]
    },
    {
        "rank": 9,
        "owner": "Tencent",
        "name": "BrowserSkill",
        "fullName": "Tencent / BrowserSkill",
        "org": "Tencent",
        "url": "https://github.com/Tencent/BrowserSkill",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "5,407",
        "forks": "341",
        "starsToday": "1,306",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +1,306★（4,076★ → 5,407★）！腾讯开源：让 AI Agent 使用你「已登录的真实浏览器」而不打断你的工作，一个连接器打通十余种 Agent。",
        "problems": [
            "<strong>Agent 卡在登录态：</strong>操作后台与内部系统的第一步就是登录。",
            "<strong>新起浏览器实例：</strong>干净环境被风控盯上，验证码轮番。",
            "<strong>自动化抢屏：</strong>Agent 一操作，人就没法用机器。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Tencent/BrowserSkill.git</code></pre>",
            "装 CLI + 浏览器扩展，接入已登录会话。",
            "在 Claude Code / Codex / Cursor / DeepSeek Harness 等 Agent 中调用。"
        ],
        "insights": [
            "<strong>日增稳定在 1,300★ 量级：</strong>首登 1,350★、连登 1,306★——热度没有衰减，说明它踩中的是长期痛点而非话题。",
            "<strong>与 coder 同日上榜形成闭环：</strong>一个给 Agent「受控的浏览器登录态」，一个给 Agent「受控的执行环境」——企业正在为 Agent 划出可授权的活动范围。",
            "<strong>本质是把人的身份借给机器：</strong>这条路的效率提升有多大，隐私与合规的争议就有多大——「哪些站点不允许被 Agent 操作」迟早需要一份白名单规则。"
        ],
        "tags": ["browser", "agent", "automation", "tencent", "cli"]
    },
    {
        "rank": 10,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "262,174",
        "forks": "39,124",
        "starsToday": "958",
        "count": 9,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第三天，今日 +958★！262K★ 第九次上榜（260,221★ → 261,126★ → 262,174★）！Agent Harness 性能优化系统——技能、直觉、记忆、安全，跨 Claude Code / Codex / Opencode / Cursor。",
        "problems": [
            "<strong>Agent 效率无优化层：</strong>同一任务不同跑法成本差几倍。",
            "<strong>技能与记忆割裂：</strong>配置分散、彼此冲突。",
            "<strong>权限边界模糊：</strong>权限越大、约束越少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/affaan-m/ECC.git</code></pre>",
            "接入 Claude Code / Codex / Opencode / Cursor。",
            "启用技能、记忆与安全策略。"
        ],
        "insights": [
            "<strong>九登、262K★、日增仍在 1,000★ 附近：</strong>7-30 时 236,008★——两个月涨 26K★，长线标的的样本。",
            "<strong>与 coder、OpenSpec 同日上榜：</strong>优化层（ECC）、环境层（coder）、流程层（OpenSpec）——Agent 的配套体系正在成形，而不只是模型在进步。",
            "<strong>本质是 Agent 的运维层：</strong>跨宿主通用让它在宿主之争中保持中立，中立本身就是位置。"
        ],
        "tags": ["agent", "harness", "optimization", "memory", "javascript"]
    },
    {
        "rank": 11,
        "owner": "TencentCloud",
        "name": "Octop",
        "fullName": "TencentCloud / Octop",
        "org": "Tencent Cloud",
        "url": "https://github.com/TencentCloud/Octop",
        "lang": "Python",
        "langClass": "py",
        "stars": "4,014",
        "forks": "386",
        "starsToday": "569",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +569★（3,413★ → 4,014★）！腾讯云的自托管 AI 助手——多用户、多 Agent、本地优先，把个人助手升级为团队可共享的助手。",
        "problems": [
            "<strong>数据不能出内网：</strong>代码与客户数据经不起外传。",
            "<strong>个人助手无法共享：</strong>调教成果无法分发给团队。",
            "<strong>多 Agent 难共处：</strong>权限与角色缺少统一编排。"
        ],
        "usage": [
            "克隆自托管：<pre><code>git clone https://github.com/TencentCloud/Octop.git</code></pre>",
            "按角色配置多个 Agent，共享知识与工具。",
            "数据留本地，对接企业自有模型端点。"
        ],
        "insights": [
            "<strong>两天连续上榜：</strong>3,413★ → 4,014★，与 BrowserSkill 一起证明腾讯这轮开源不是一次性投放。",
            "<strong>今天榜单的第四条主权线：</strong>Octop（助手）、hister（索引）、coder（环境）、rustfs（存储）同日上榜——自托管从「备选方案」变成「默认架构」。",
            "<strong>本质是采购逻辑的变化：</strong>当数据出境与供应商锁定成为合规硬约束，「能否自托管」从加分项变成了准入门槛。"
        ],
        "tags": ["assistant", "self-hosted", "multi-agent", "local-first", "tencent"]
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
        "stars": "146,372",
        "forks": "23,700",
        "starsToday": "444",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +444★！146.4K★ 第三次上榜（145,849★ → 146,372★）！Anthropic 官方的终端 Agent——理解代码库、执行日常任务、处理 Git 流程，全走自然语言。",
        "problems": [
            "<strong>AI 与终端割裂：</strong>聊天窗口与真实仓库之间靠手工搬运。",
            "<strong>不懂项目上下文：</strong>看不到仓库结构与约定。",
            "<strong>执行不可审计：</strong>直接动文件与 Git 缺少过程控制。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g @anthropic-ai/claude-code</code></pre>",
            "在项目目录启动，用自然语言下达任务。",
            "执行测试、解释代码、处理 Git 工作流。"
        ],
        "insights": [
            "<strong>连续两日在榜：</strong>从 8-23 的 142,521★ 到现在 146,372★，品牌与开发者心智仍在积累。",
            "<strong>与 OpenSpec、agent-skills 形成互补：</strong>宿主负责执行，规格与技能负责纪律——终端 Agent 越强，配套规范的缺失就越明显。",
            "<strong>本质是官方宿主在生态中的锚点作用：</strong>第三方技能与插件都要围绕它做适配，这份「被适配」的优势比功能领先更持久。"
        ],
        "tags": ["agent", "coding", "cli", "anthropic", "terminal"]
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
    "date": "2026-09-19",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-19'
data['topic'] = '🔥 <strong>Cloudflare 审计技能三连登两天翻倍（7,054→14,072★）+ 阿里 code-review 四连登 36.8K★ + Agent 配套体系成形（OpenSpec 规格 + agent-skills 流程 + coder 环境）+ 自托管四连（hister / coder / rustfs / Octop）</strong> —— asciimoo/hister（+889★）私有搜索引擎首登。addyosmani/agent-skills（+675★）96.5K★ 九登。coder/coder（+478★）给开发者与 Agent 的自托管环境首登。anthropics/knowledge-work-plugins（+299★）Claude Cowork 官方插件库三登。Fission-AI/OpenSpec（+296★）69.4K★ 规格驱动开发首登。rustfs/rustfs（+267★）Rust 版 S3 对象存储首登。cloudflare/security-audit-skill（+3,006★）三连登稳居榜首，两天翻一倍。alibaba/open-code-review（+2,704★）36.8K★ 四连登，两个月翻 2.5 倍。Tencent/BrowserSkill（+1,306★）连登。affaan-m/ECC（+958★）262K★ 九登。TencentCloud/Octop（+569★）连登。anthropics/claude-code（+444★）146.4K★ 三登。今日两条明线：一、社区开始给 Agent 立规矩——规格（OpenSpec 事前）、流程（agent-skills 事中）、审查（阿里 code-review 事后）三个项目同日上榜，质量体系被拆成可采购的三件套；二、自托管一天占四席（私有搜索、开发环境、对象存储、团队助手），数据主权从备选变成默认架构。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:5]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
