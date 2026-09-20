#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-20 (1-day gap, 双栏：新面孔 6 + 连登 5)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 20)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-19 榜上）══
    {
        "rank": 1,
        "owner": "trycua",
        "name": "cua",
        "fullName": "trycua / cua",
        "org": "Cua",
        "url": "https://github.com/trycua/cua",
        "lang": "HTML",
        "langClass": "html",
        "stars": "24,914",
        "forks": "1,711",
        "starsToday": "1,012",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,012★ 首登即新面孔第一！「给 AI Agent 一台能用的电脑」——开源桌面自动化驱动、隔离云桌面、本地 macOS 虚拟机、专职决策模型，还带评测计算机使用 Agent 的基准。",
        "problems": [
            "<strong>Agent 没有身体：</strong>模型能思考，但没有可以安全点击、输入、切窗口的执行环境。",
            "<strong>在真机上操作太危险：</strong>让 Agent 直接控制你的桌面，一次误操作就可能不可逆。",
            "<strong>跨系统难统一：</strong>macOS、Linux、Windows 各自一套自动化方案，团队要写三份代码。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/trycua/cua.git</code></pre>",
            "用驱动在本地 macOS 虚拟机或隔离云桌面里跑 Agent。",
            "接上基准测试评估 computer-use 能力，或做训练数据生成。"
        ],
        "insights": [
            "<strong>「Computer Use 2.0」这个说法值得注意：</strong>它把重点从「模型会不会点鼠标」转到「基础设施能不能规模化提供可用的电脑」——赛道从模型层下沉到执行层。",
            "<strong>隔离环境是它真正的卖点：</strong>本地 macOS 虚拟机 + 云桌面沙箱，等于给 Agent 划一个可随时重装的活动范围，这与今天 coder、昨天 rustfs 的思路完全一致。",
            "<strong>本质是把「风险」做成产品：</strong>Agent 越能干，误操作代价越大——谁提供可丢弃的执行环境，谁就掌握了 Agent 落地的第一道闸门。"
        ],
        "tags": ["computer-use", "agent", "virtualization", "benchmark", "mit"]
    },
    {
        "rank": 2,
        "owner": "Open-Dev-Society",
        "name": "OpenStock",
        "fullName": "Open-Dev-Society / OpenStock",
        "org": "Open Dev Society",
        "url": "https://github.com/Open-Dev-Society/OpenStock",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "16,496",
        "forks": "2,118",
        "starsToday": "752",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +752★ 首登！开源版行情平台——实时价格、个性化提醒、公司深度洞察，目标是替代昂贵的付费行情服务，「为所有人而建，永远免费」。",
        "problems": [
            "<strong>行情数据被订阅锁死：</strong>实时报价与提醒功能动辄每月几十上百美元。",
            "<strong>免费工具功能残缺：</strong>要么延迟严重，要么广告与推销邮件不断。",
            "<strong>数据无法自留：</strong>看过的图表、设过的提醒都留在别人服务器上。"
        ],
        "usage": [
            "克隆并部署：<pre><code>git clone https://github.com/Open-Dev-Society/OpenStock.git</code></pre>",
            "配置行情数据源与自选股。",
            "设置价格与事件提醒，长期数据留在自己的数据库。"
        ],
        "insights": [
            "<strong>教学型开源项目的又一次验证：</strong>Open Dev Society 是「边做真实产品边教开源协作」的组织，仓库里能看到 CodeRabbit、Inngest 等现代工程实践——它本身就是教材。",
            "<strong>为什么今天上榜：</strong>与 AI 无关，但与「AI 时代的金融焦虑」强相关——通胀、加息周期与 AI 泡沫讨论交织，散户对数据自主权的需求明显上升。",
            "<strong>本质是数据订阅制的裂缝：</strong>当开源能把「数据展示 + 提醒」这类表层功能复制出来，付费行情平台的溢价只能靠更低延迟与合规资质——这是典型的「基础设施商品化」路径。"
        ],
        "tags": ["stock-market", "open-source", "self-hosted", "typescript", "education"]
    },
    {
        "rank": 3,
        "owner": "vercel-labs",
        "name": "json-render",
        "fullName": "vercel-labs / json-render",
        "org": "Vercel Labs",
        "url": "https://github.com/vercel-labs/json-render",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "17,033",
        "forks": "906",
        "starsToday": "585",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +585★ 首登！Vercel Labs 的生成式 UI 框架——用提示词生成动态、个性化的界面，但只允许使用「预定义的组件与动作」，在自由度和可靠性之间划线。",
        "problems": [
            "<strong>模型生成的 UI 不可控：</strong>直接让大模型写前端，样式漂移、组件不存在、交互逻辑随时崩。",
            "<strong>个性化与稳定性冲突：</strong>为每个用户生成界面很诱人，但没人敢把它放进生产环境。",
            "<strong>组件规范没人遵守：</strong>设计系统写了文档，模型却照旧自由发挥。"
        ],
        "usage": [
            "安装：<pre><code>npm install @json-render/core</code></pre>",
            "用 JSON 描述可用组件与动作白名单。",
            "让模型在白名单内生成界面，前端按 schema 渲染。"
        ],
        "insights": [
            "<strong>与本周主线严丝合缝：</strong>它和 OpenSpec（先写规格）、Jev（类型安全输出）、Cloudflare 七评审员是同一个思路——把自由度收窄到可控范围，模型才能在关键路径上被信任。",
            "<strong>Vercel 的赌注在「生成式 UI」这个品类：</strong>不是让 AI 写代码，而是让界面本身变成模型可安全操作的产物——这条路如果成立，前端工程的分工会被改写。",
            "<strong>本质是给生成过程加约束而不是加能力：</strong>预定义组件白名单看似限制了模型，实际是把它从「演示品」变成了「可交付品」。"
        ],
        "tags": ["generative-ui", "framework", "typescript", "vercel", "agents"]
    },
    {
        "rank": 4,
        "owner": "higgsfield-ai",
        "name": "higgsfield",
        "fullName": "higgsfield-ai / higgsfield",
        "org": "higgsfield-ai",
        "url": "https://github.com/higgsfield-ai/higgsfield",
        "lang": "Jupyter Notebook",
        "langClass": "jl",
        "stars": "5,173",
        "forks": "933",
        "starsToday": "461",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +461★ 首登！一句「多节点训练，不用哭」概括的 GPU 编排与训练框架——容错、可扩展，支持 ZeRO-3 与 PyTorch FSDP，面向从十亿到万亿参数的大模型训练。",
        "problems": [
            "<strong>多机训练极难运维：</strong>节点一挂整个任务重跑，几百张卡的机时打水漂。",
            "<strong>万亿参数装不下：</strong>单卡显存再怎么优化也不够，必须做分片与流水并行。",
            "<strong>集群调度靠人肉：</strong>谁在用哪些卡、任务优先级如何，缺少统一管理层。"
        ],
        "usage": [
            "安装：<pre><code>pip install higgsfield</code></pre>",
            "按模板定义训练任务与资源需求（独占 / 非独占）。",
            "在集群上提交，框架负责调度、分片与容错重启。"
        ],
        "insights": [
            "<strong>与今天榜单的「个人化」路线形成强烈对照：</strong>一边是 cua 给单机 Agent 造沙箱，一边是它给上千张卡做编排——AI 基础设施同时向两端扩张。",
            "<strong>「不用哭」写进标题是精准的用户洞察：</strong>多节点训练的痛点从来不是算法，而是运维事故，能把这个痛点做成产品名说明团队真的跑过大规模集群。",
            "<strong>本质是算力利用率生意：</strong>当 GPU 成为最贵的资源，能少浪费一小时机时的框架，价值直接等于省下的电费与折旧——这类项目的热度会跟着算力价格一起波动。"
        ],
        "tags": ["gpu", "distributed-training", "orchestration", "llm", "fault-tolerant"]
    },
    {
        "rank": 5,
        "owner": "anthropics",
        "name": "financial-services",
        "fullName": "anthropics / financial-services",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/financial-services",
        "lang": "Python",
        "langClass": "py",
        "stars": "35,220",
        "forks": "5,236",
        "starsToday": "236",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +236★！35.2K★ 第二次上榜（6-17 首登时约 2,000★）！Anthropic 官方的「Claude for Financial Services」——投行、股票研究、私募、财富管理的参考 Agent、技能与数据连接器，同一套内容可装成插件也可走 Managed Agents API 部署。",
        "problems": [
            "<strong>金融场景不能瞎试：</strong>投行备忘录、估值模型、研究报告有严格的格式与合规要求。",
            "<strong>通用助手不懂行业流程：</strong>数据源、模板、审阅链路全是行业特有的。",
            "<strong>自建成本高：</strong>从提示词到连接器都要自己攒，且难以验证。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/anthropics/financial-services.git</code></pre>",
            "装成 Claude Cowork 插件，或用 Claude Managed Agents API 接到自己的流程引擎。",
            "按角色启用：投资银行、股票研究、私募、财富管理。"
        ],
        "insights": [
            "<strong>官方首次把「一个行业」做成开源套件：</strong>提示词、技能、数据连接器成套发布，且明确说「同一套内容，你选在哪里跑」——插件化与 API 双形态，等于把交付方式的选择权交给客户。",
            "<strong>三个月从 2,000★ 到 35.2K★：</strong>这是本周榜单里增幅最猛的项目，说明「模型公司直接交付行业方案」这条路被市场强烈认可。",
            "<strong>本质是模型公司的渠道革命：</strong>过去行业方案卖给咨询公司和系统集成商，现在模型公司自己开源——被挤压的中间层，正是那些靠「懂行业」收费的服务商。"
        ],
        "tags": ["financial-services", "agents", "claude", "anthropic", "industry"]
    },
    {
        "rank": 6,
        "owner": "mihail911",
        "name": "modern-software-dev-assignments",
        "fullName": "mihail911 / modern-software-dev-assignments",
        "org": "mihail911",
        "url": "https://github.com/mihail911/modern-software-dev-assignments",
        "lang": "Python",
        "langClass": "py",
        "stars": "4,437",
        "forks": "1,006",
        "starsToday": "174",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +174★ 首登！斯坦福 CS146S《现代软件开发》课程作业集——在 AI 编码时代重写软件工程课：不是教你写算法题，而是教你与 Agent 协作完成真实项目。",
        "problems": [
            "<strong>软件工程课没跟上 AI：</strong>还在教手写 CRUD 与算法题，学生毕业即被 Agent 工具淘汰。",
            "<strong>自学无路径：</strong>网上教程零散，缺少有批改、有项目的系统课程。",
            "<strong>课程材料不公开：</strong>名校课程只有校内学生能拿到作业与项目。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/mihail911/modern-software-dev-assignments.git</code></pre>",
            "按周完成作业：从需求拆解到 Agent 协作与代码评审。",
            "对照课程仓库自测，或作为企业内部培训教材。"
        ],
        "insights": [
            "<strong>课程仓库登上趋势榜本身就是信号：</strong>当「怎么和 AI 一起写软件」成为需要正式课程的技能，说明这套工作流已经从极客玩具变成职业要求。",
            "<strong>与今天榜单的教学型项目（OpenStock）呼应：</strong>一个是「边做产品边教开源」，一个是「把名校课程公开」——AI 时代的技术教育正在从封闭课程转向公开仓库。",
            "<strong>本质是职业门槛的重新划线：</strong>会背 API 的价值在下降，能拆解需求、给 Agent 立规格、审查产出的价值在上升——课程表的变化，往往比行业报告更早反映真实需求。"
        ],
        "tags": ["education", "software-engineering", "course", "python", "agents"]
    },
    # ══ 连登（09-19 榜上继续）══
    {
        "rank": 7,
        "owner": "cloudflare",
        "name": "security-audit-skill",
        "fullName": "cloudflare / security-audit-skill",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "17,506",
        "forks": "784",
        "starsToday": "2,375",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 四连登，今日 +2,375★！三天从 7,054★ 涨到 17,506★（2.5 倍）！Cloudflare 官方安全审计技能——六阶段流程 + 独立验证，自家全网漏洞发现系统的源头版本。",
        "problems": [
            "<strong>审计没有覆盖账本：</strong>查过什么、漏了什么全凭记忆。",
            "<strong>Agent 结论不可信：</strong>缺少独立验证，误报与幻觉混杂。",
            "<strong>产出无法交接：</strong>没有机器可读结果，团队难以复用。"
        ],
        "usage": [
            "把技能装进 Claude Code / Codex 的 skills 目录。",
            "跑完六阶段，产出 architecture.md 与 coverage-ledger.json。",
            "每个候选漏洞交给独立验证 Agent 证伪后再入库。"
        ],
        "insights": [
            "<strong>四连登且日增仍在 2,375★：</strong>7,054 → 10,517 → 14,072 → 17,506，四天涨 1.5 万星，是本周榜单最陡的一条曲线。",
            "<strong>「官方生产验证」继续压制话题项目：</strong>同期同类项目（个人开发的审计工具）无一能与之竞争——机构署名的可信度优势在这轮被放大。",
            "<strong>本质是方法论的可分发化：</strong>把六阶段流程写成技能文件，安全方法论第一次能像软件包一样被安装——这是安全行业从「顾问服务」走向「产品交付」的标志。"
        ],
        "tags": ["security", "agent-skills", "audit", "cloudflare", "javascript"]
    },
    {
        "rank": 8,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "263,335",
        "forks": "39,180",
        "starsToday": "1,012",
        "count": 10,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第四天、第十次上榜，今日 +1,012★！263K★（262,174★ → 263,335★）！Agent Harness 性能优化系统——技能、直觉、记忆、安全，跨 Claude Code / Codex / Opencode / Cursor。",
        "problems": [
            "<strong>Agent 效率没有优化层：</strong>同一任务不同跑法成本差几倍。",
            "<strong>技能与记忆割裂：</strong>配置分散、彼此冲突。",
            "<strong>权限边界模糊：</strong>权限越大、约束越少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/affaan-m/ECC.git</code></pre>",
            "接入 Claude Code / Codex / Opencode / Cursor。",
            "启用技能、记忆与安全策略。"
        ],
        "insights": [
            "<strong>十登、263K★、日增稳在 1,000★：</strong>7-30 时 236,008★——两个月涨 27K★，长线标的中最稳的一个。",
            "<strong>宿主越多它越有价值：</strong>今天榜单同时出现 claude-code（官方宿主）与 coder（自托管环境）、cua（沙箱），跨宿主的优化层自然成为公共基础设施。",
            "<strong>本质是 Agent 时代的运维中间件：</strong>不选边、服务所有边——中立位置本身就是最稀缺的资源。"
        ],
        "tags": ["agent", "harness", "optimization", "memory", "javascript"]
    },
    {
        "rank": 9,
        "owner": "addyosmani",
        "name": "agent-skills",
        "fullName": "addyosmani / agent-skills",
        "org": "Addy Osmani",
        "url": "https://github.com/addyosmani/agent-skills",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "97,435",
        "forks": "10,180",
        "starsToday": "729",
        "count": 10,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天、第十次上榜，今日 +729★！97.4K★ 逼近十万（96,489★ → 97,435★）！把资深工程师工作流固化成六个阶段技能的工程规范库。",
        "problems": [
            "<strong>Agent 代码质量随机：</strong>同一需求不同轮次产出差异巨大。",
            "<strong>流程无门禁：</strong>Agent 直接开写，跳过澄清与验证。",
            "<strong>经验难传递：</strong>高工的判断标准留在脑子里。"
        ],
        "usage": [
            "安装：<pre><code>npx skills add addyosmani/agent-skills</code></pre>",
            "接入 Claude Code / Codex / Cursor 等 Agent。",
            "按阶段启用：定义到发布的整套技能。"
        ],
        "insights": [
            "<strong>十天四次登上趋势榜：</strong>8-10 时 85,320★，今天 97,435★——六周涨 12K★，距十万星仅一步。",
            "<strong>与 json-render 同框很说明问题：</strong>一个是给 Agent 立流程（工程侧），一个是给生成过程加约束（UI 侧）——「约束优先」已成为本周最一致的技术共识。",
            "<strong>本质是判断标准的产品化：</strong>写代码的成本趋零，稀缺的是「什么算合格」，而技能库正是把这条标准写成了可安装的资产。"
        ],
        "tags": ["agent-skills", "engineering", "quality-gates", "javascript", "claude-code"]
    },
    {
        "rank": 10,
        "owner": "anthropics",
        "name": "claude-code",
        "fullName": "anthropics / claude-code",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-code",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "146,929",
        "forks": "23,760",
        "starsToday": "415",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第三天，今日 +415★！146.9K★（146,372★ → 146,929★）！Anthropic 官方的终端 Agent——理解代码库、执行日常任务、处理 Git 流程，全走自然语言。",
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
            "<strong>Anthropic 今天两个项目同时在榜：</strong>官方宿主（claude-code）+ 官方行业方案（financial-services）——一边提供执行环境，一边提供行业内容，这是模型公司少见的「双向交付」。",
            "<strong>三天连登且日增稳定：</strong>146K★ 的体量还能保持四百星以上的日增，说明官方宿主仍是新增开发者的默认入口。",
            "<strong>本质是生态锚点：</strong>第三方技能（Cloudflare 审计、addyosmani 技能库）都要围绕它适配——被适配的优势比功能领先更持久。"
        ],
        "tags": ["agent", "coding", "cli", "anthropic", "terminal"]
    },
    {
        "rank": 11,
        "owner": "coder",
        "name": "coder",
        "fullName": "coder / coder",
        "org": "Coder",
        "url": "https://github.com/coder/coder",
        "lang": "Go",
        "langClass": "go",
        "stars": "15,842",
        "forks": "1,152",
        "starsToday": "382",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +382★（15,345★ → 15,842★）！自托管的云开发环境——给开发者和他们的 AI Agent 提供安全、隔离、可复制的远程工作空间。",
        "problems": [
            "<strong>Agent 在本地跑很危险：</strong>执行命令、装依赖等同于交出密钥。",
            "<strong>环境不一致：</strong>「在我机器上能跑」的问题被 Agent 放大。",
            "<strong>云端环境不自主：</strong>SaaS 方案把源码与密钥托管给第三方。"
        ],
        "usage": [
            "自托管部署：<pre><code>https://coder.com/docs/install</code></pre>",
            "用模板定义开发环境与权限边界。",
            "让开发者与 AI Agent 在同一套受控环境里协作。"
        ],
        "insights": [
            "<strong>与 cua 同日上榜：</strong>一个给 Agent 一块隔离的开发机，一个给 Agent 一台可丢弃的电脑——「给 Agent 划活动范围」今天占了两个席位。",
            "<strong>连登说明需求持续：</strong>它不是话题项目，而是采购项——数据主权与权限隔离正在从讨论变成预算。",
            "<strong>本质是基础设施默认用户的迁移：</strong>当环境的第一用户从人变成 Agent，权限模型、审计日志、成本归因都要重做一遍。"
        ],
        "tags": ["dev-environment", "self-hosted", "agent", "go", "remote"]
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
    "date": "2026-09-20",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-20'
data['topic'] = '🔥 <strong>Anthropic 官方金融 Agent 套件回归（三个月 2000★→35.2K★）+ Cloudflare 审计技能四连登四天涨 1.5 万星 + Vercel 生成式 UI 框架 + cua 给 Agent 造可丢弃的电脑 + 斯坦福 AI 时代软件工程课上榜</strong> —— trycua/cua（+1,012★）给 AI Agent 一台能用的电脑，隔离环境首登。Open-Dev-Society/OpenStock（+752★）开源行情平台首登。vercel-labs/json-render（+585★）生成式 UI 框架首登，只允许预定义组件。higgsfield-ai/higgsfield（+461★）GPU 编排与训练框架首登。anthropics/financial-services（+236★）35.2K★ 官方行业方案二登。mihail911/modern-software-dev-assignments（+174★）斯坦福 CS146S 课程作业首登。cloudflare/security-audit-skill（+2,375★）四连登，四天 7,054→17,506★。affaan-m/ECC（+1,012★）263K★ 十登。addyosmani/agent-skills（+729★）97.4K★ 十登逼近十万。anthropics/claude-code（+415★）146.9K★ 三连登。coder/coder（+382★）连登。今日两条明线：一、「给能力加约束」成为共识——生成式 UI 限定组件白名单、审计技能用独立验证、工程技能设六阶段门禁、GPU 框架做容错编排，全是把自由度收窄到可交付；二、模型公司亲自下场做行业方案——Anthropic 把金融行业成套开源（插件与 API 双形态），被挤压的是靠「懂行业」收费的中间服务商。'

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
