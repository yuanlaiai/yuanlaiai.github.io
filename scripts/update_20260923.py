#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-23 (2-day gap -> 平铺，全部新面孔)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 23)
gap_days = (today - last).days  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    {
        "rank": 1,
        "owner": "google",
        "name": "ax",
        "fullName": "google / ax",
        "org": "Google",
        "url": "https://github.com/google/ax",
        "lang": "Go",
        "langClass": "go",
        "stars": "7,525",
        "forks": "351",
        "starsToday": "2,324",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,324★ 登顶！Google 的声明式 Agent 编排器：四个原语（Task 隔离任务 / Workspace 预热工作区 / Gateway 出站白名单 / Model 模型选择），kubectl 式 CLI（apply / watch / ssh / suspend / resume），宣称可在一个集群里跑数十亿个 Agent 任务。",
        "problems": [
            "<strong>Agent 既不是微服务也不是批处理：</strong>它积累状态、需要严格隔离、往外调模型与工具，没人看着还会在循环里烧钱——现有基础设施两头都不合适。",
            "<strong>断了就得从头来：</strong>一个任务跑四十分钟中途失败，既不知道做到哪一步，也没法接着做。",
            "<strong>沙箱要自己拼：</strong>容器、网络白名单、凭证轮换、闲置成本控制，全都得团队自己写一遍。"
        ],
        "usage": [
            "装 CLI：<pre><code>go install github.com/google/ax/cmd/ax@latest</code></pre>",
            "写一份 YAML（Workspace + Task）后 <pre><code>ax apply -f task.yaml</code></pre>",
            "用 <pre><code>ax watch</code></pre> 看状态、<pre><code>ax ssh</code></pre> 进沙箱、<pre><code>ax suspend / ax resume</code></pre> 挂起与续跑。需要自备 Kubernetes 集群与镜像仓库。"
        ],
        "insights": [
            "<strong>它把 Agent 当成第三种工作负载：</strong>官方 README 的原话是「既不是无状态微服务，也不是跑完就退出的批处理」——这句话点破了过去两年所有部署方式都是将就的。",
            "<strong>suspend / resume 才是野心所在：</strong>暂停闲置 Agent 并从断点精确续跑，等于把「Agent 大部分时间在等待」这件事变成可定价的资源。",
            "<strong>本质是编排层的卡位战：</strong>云厂商真正赚钱的是承载应用的运行环境——谁掌握调度器，谁就掌握工作负载的归属，「Agent 跑在谁的调度器上」比「用谁的模型」更靠前。"
        ],
        "tags": ["ai-agents", "orchestration", "kubernetes", "golang", "google"]
    },
    {
        "rank": 2,
        "owner": "mvt-project",
        "name": "mvt",
        "fullName": "mvt-project / mvt",
        "org": "mvt-project",
        "url": "https://github.com/mvt-project/mvt",
        "lang": "Python",
        "langClass": "py",
        "stars": "14,067",
        "forks": "1,355",
        "starsToday": "441",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +441★！14.1K★ 老工具回归：Amnesty International 安全实验室 2021 年随「Pegasus 计划」发布的移动取证工具，用来在 Android / iOS 设备上找出间谍软件痕迹；今天上榜的直接原因是刚合并的 v3 分支带来了破坏性变更。",
        "problems": [
            "<strong>被入侵往往查不出来：</strong>商业间谍软件的痕迹藏在系统日志与配置里，普通人连入口在哪都不知道。",
            "<strong>取证门槛高：</strong>要靠命令行与数字取证经验，非技术背景的当事人无法自证。",
            "<strong>证据易失：</strong>手机一重启、一升级，关键日志就可能消失，取证窗口极短。"
        ],
        "usage": [
            "安装：<pre><code>pip install mvt</code></pre>",
            "备份设备后跑 <pre><code>mvt-ios check-backup --iocs STIX2_FILE ./backup</code></pre>",
            "对照 IOC 指标（如 Pegasus 的 STIX2 文件）定位可疑进程与配置。"
        ],
        "insights": [
            "<strong>上榜的不是新项目而是新接口：</strong>维护了五年的工具今天冲上榜单，是 v3 分支的破坏性变更把所有下游脚本打断了——老基建的版本升级本身就是事件。",
            "<strong>「取证能力」正在变成公共品：</strong>Amnesty 把最贵的取证方法开源，等于把「谁能证明自己被监控」这件事从机构特权变成可复制流程。",
            "<strong>本质是权力关系的技术化：</strong>当监控工具商业化到可以按目标出售，反制手段只能是同样公开、同样可验证的开源工具——军备竞赛的两边，一边收费一边免费，这本身就是答案。"
        ],
        "tags": ["forensics", "security", "ios", "android", "amnesty"]
    },
    {
        "rank": 3,
        "owner": "anthropics",
        "name": "financial-services",
        "fullName": "anthropics / financial-services",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/financial-services",
        "lang": "Python",
        "langClass": "py",
        "stars": "36,304",
        "forks": "5,311",
        "starsToday": "436",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +436★！36.3K★ 模型公司卖行业成品：投行、股票研究、私募与财富管理的参考 Agent、技能与数据连接器——Pitch Agent（路演材料）、Market Researcher（市场研究）、GL Reconciler（总账对账），附带 /comps、/dcf 这类斜杠命令。一套源码两种交付：装成 Cowork 插件，或走 Managed Agents API 部署在你自己的流程引擎后面。",
        "problems": [
            "<strong>行业 Agent 要自己从零搭：</strong>模型会写代码，但不知道投行的 pitch book 该怎么组织、估值模型该怎么摆。",
            "<strong>数据连着哪都用不了：</strong>行情、财报、内部总账各有各的接口，接一次换一次。",
            "<strong>合规没人担责：</strong>Agent 直接输出结论，出了错没有审计链条。"
        ],
        "usage": [
            "作为 Claude Cowork 插件安装，或按 managed-agent-cookbooks 走 <pre><code>/v1/agents</code></pre> 部署。",
            "按垂直行业挑选技能与斜杠命令（如 /comps 可比公司、/dcf 现金流折现）。",
            "接上数据连接器后让 Agent 起草备忘录、模型与对账表——每一步都停在人工签字前。"
        ],
        "insights": [
            "<strong>「每次输出等人签字」被写进免责声明：</strong>仓库明确说 Agent 不做投资建议、不执行交易、不记总账、不批准开户，所有产出都停在待人工签核——把责任边界当产品说明来写，这在半年前还很少见。",
            "<strong>一套源码两种交付是真正的信号：</strong>既能当 Cowork 插件卖席位，也能当 API 塞进客户自己的流程引擎——模型公司不再只卖能力，开始卖「哪里跑你说了算」。",
            "<strong>本质是行业知识的产品化：</strong>过去这些流程锁在咨询公司与分析师的脑子里，现在被拆成可安装的技能包——定价权正从「会做的人」转向「定义标准流程的人」。"
        ],
        "tags": ["financial-services", "ai-agents", "claude", "enterprise", "skills"]
    },
    {
        "rank": 4,
        "owner": "agent-substrate",
        "name": "substrate",
        "fullName": "agent-substrate / substrate",
        "org": "Agent Substrate",
        "url": "https://github.com/agent-substrate/substrate",
        "lang": "Go",
        "langClass": "go",
        "stars": "2,943",
        "forks": "383",
        "starsToday": "301",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +301★ 首登！它就是 google/ax 的执行底座：面向 Agent 的沙箱运行时，宣称比标准容器运行时高 10 倍沙箱密度、恢复低于 500 毫秒、每秒 500 次以上挂起与恢复，同时支持 microVM 与 gVisor，带零信任的内核与网络隔离。",
        "problems": [
            "<strong>跑不可信代码不敢用 Docker：</strong>普通容器隔离强度不够，Agent 生成的代码风险更高。",
            "<strong>密度与安全难兼得：</strong>一个 Agent 一台虚拟机最安全，但成本和启动延迟都受不了。",
            "<strong>Agent 大半时间在空转：</strong>等模型、等人、等工具结果，却一直占着资源计费。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/agent-substrate/substrate.git</code></pre>",
            "按文档接入控制面 API，选择 microVM 或 gVisor 作为沙箱后端。",
            "用 actor 生命周期接口管理 Agent 的创建、挂起与恢复（AX 正是消费这套接口）。"
        ],
        "insights": [
            "<strong>它和上层同一天上榜，这是罕见的：</strong>调度器（AX）与沙箱运行时（Substrate）同时被看见，说明大家开始关心「Agent 住在哪」这一整条栈，而不只是框架好不好用。",
            "<strong>核心是把操作系统思路搬过来：</strong>把一大堆闲着的 actor 映射到少量 worker 上做复用，和操作系统把上万线程映射到几个核上是同一招——被复用的对象换成了 Agent。",
            "<strong>本质是闲置资源的重新定价：</strong>Agent 的经济性不在峰值算力，而在「等待期几乎零成本」——谁先做到毫秒级挂起恢复，谁就能把 AI 的计费单位从「小时」改成「秒」。"
        ],
        "tags": ["sandbox", "microvm", "gvisor", "ai-agents", "infrastructure"]
    },
    {
        "rank": 5,
        "owner": "dream-num",
        "name": "univer",
        "fullName": "dream-num / univer",
        "org": "dream-num",
        "url": "https://github.com/dream-num/univer",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "15,352",
        "forks": "1,368",
        "starsToday": "202",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +202★ 重新上榜！2022 年建仓的全栈同构 Office SDK：表格、文档、幻灯片、画布、关系表、PDF 一套运行时，Canvas 渲染 + 公式引擎 + 插件架构 + 浏览器与 Node 同构的 Facade API。变化在于简介已被改成「The Office Harness for AI Agents」。",
        "problems": [
            "<strong>Office 能力无法嵌进产品：</strong>想在自己应用里放一张能算的表格，商业组件贵、开源组件弱。",
            "<strong>模型改不动文件：</strong>Agent 能写代码，却常常读不出表格里的公式依赖与文档结构。",
            "<strong>渲染两端不一致：</strong>浏览器算一遍、服务端再算一遍，结果还对不上。"
        ],
        "usage": [
            "安装：<pre><code>npm install @univerjs/presets</code></pre>",
            "用 Facade API 在浏览器或 Node 端创建表格、文档、幻灯片实例。",
            "按需要挂插件扩展公式、协同或自定义渲染。"
        ],
        "insights": [
            "<strong>一个四年的老项目靠改定位回到榜单：</strong>代码没变多少，简介从「开源 Office 套件」换成「Agent 的 Office Harness」——同一份资产在 Agent 叙事里被重新定价。",
            "<strong>「同构」这个词在 Agent 时代突然值钱：</strong>浏览器和服务端跑同一套渲染与公式引擎，意味着 Agent 在服务端改的东西，人打开页面看到的就是同一个结果。",
            "<strong>本质是 Agent 需要自己的办公桌：</strong>Agent 处理的不再只是代码和文本，还有表格、合同、汇报——谁提供那张桌子，谁就握住了 Agent 与人交接的界面。"
        ],
        "tags": ["office-sdk", "spreadsheet", "typescript", "ai-agents", "chinese"]
    },
    {
        "rank": 6,
        "owner": "superdesigndev",
        "name": "treg",
        "fullName": "superdesigndev / treg",
        "org": "Superdesign",
        "url": "https://github.com/superdesigndev/treg",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,191",
        "forks": "217",
        "starsToday": "197",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +197★ 首登！自称「Agent 工具的 OpenRouter」：一个 base URL、一个 token，就能调用 3,000+ 端点、覆盖 60+ 供应商（SEO 外链、社媒趋势、人物与公司信息、广告、抓取、图像与视频生成），按次计价低至一美分，不用逐个注册。团队自己的密钥、技能与 CLI 也能让每个成员的 Agent 调用，凭证不出服务器。可自托管。",
        "problems": [
            "<strong>好工具都在订阅墙后面：</strong>Semrush $139/月、Moz $99/月、Crunchbase $99/月、Apollo $59/座——为跑一次任务买一个月不划算。",
            "<strong>还有些工具根本没有公开 API：</strong>邀请制、合作方制、应用审核制，Agent 连门票都拿不到。",
            "<strong>密钥散落在每个人机器上：</strong>团队的 API key 分布在多台电脑与多个 Agent 配置里，谁用过、花多少，没人说得清。"
        ],
        "usage": [
            "自托管：<pre><code>git clone https://github.com/superdesigndev/treg.git</code></pre>",
            "把 Agent 的 base URL 指向 treg，配一个 token。",
            "按「任务」而非「工具」检索并调用，费用按次从团队预付余额里扣。"
        ],
        "insights": [
            "<strong>它卖的不是工具而是「门槛」：</strong>把 60 家供应商的注册、计费与合规一次性吞掉，按一美分一次转售——中间商的价值来自订阅制与按次使用之间的错配。",
            "<strong>凭证不出服务器这句是关键：</strong>团队密钥集中在服务端、Agent 只拿到一个 token，等于给 Agent 的权限管理划了一条边界——这是企业敢用 Agent 的前提。",
            "<strong>本质是订阅制的拆解：</strong>过去十年 SaaS 靠「包月」把轻度用户变成稳定收入，Agent 一来，调用方变成了机器且用量不可预测——按次计价的中间层会越来越多。"
        ],
        "tags": ["ai-agents", "registry", "credentials", "mcp", "developer-tools"]
    },
    {
        "rank": 7,
        "owner": "browser-use",
        "name": "video-use",
        "fullName": "browser-use / video-use",
        "org": "browser-use",
        "url": "https://github.com/browser-use/video-use",
        "lang": "Python",
        "langClass": "py",
        "stars": "25,814",
        "forks": "3,115",
        "starsToday": "155",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +155★！25.8K★ 用 coding agent 剪视频：把原始素材丢进文件夹，跟 Claude Code 聊，拿回 final.mp4。删掉口癖与废镜头、自动调色、每个切点加 30 毫秒音频淡入淡出、按你风格烧字幕、用 HyperFrames / Remotion / Manim 并行生成动画叠加，并在每个切点自评渲染结果后才给你看。",
        "problems": [
            "<strong>剪辑软件的学习成本：</strong>预设、菜单、时间线，光找功能就耗掉创作精力。",
            "<strong>重复劳动占比高：</strong>删口癖、对齐字幕、调色、做动效，全是机械动作。",
            "<strong>结果不敢信：</strong>自动剪辑一把梭，切点错了、音频爆了就整段重来。"
        ],
        "usage": [
            "把 README 里的安装提示词粘进 Claude Code（也支持 Codex / Hermes / Openclaw）。",
            "配置 ffmpeg 与 ElevenLabs API key，注册成 Agent 技能。",
            "素材放进文件夹后对话式剪辑，产出 final.mp4，会话记忆写进 project.md。"
        ],
        "insights": [
            "<strong>它把「剪辑」重新定义成对话：</strong>没有预设、没有时间线，只有素材文件夹和一句需求——这类工具真正替代的不是 Pr，而是「先学软件再表达」的旧流程。",
            "<strong>自评这一步比剪辑本身重要：</strong>在每个切点边界先自检再交付，正是 Agent 落地最缺的验收环节——能自己验的 Agent 才敢放手用。",
            "<strong>本质是能力从软件转移到意图：</strong>当 ffmpeg 链路由 Agent 现场拼装，人的工作从「操作工具」变成「描述标准」——谁定义好标准，谁的产出就稳定。"
        ],
        "tags": ["video-editing", "ai-agents", "claude-code", "ffmpeg", "automation"]
    },
    {
        "rank": 8,
        "owner": "davila7",
        "name": "claude-code-templates",
        "fullName": "davila7 / claude-code-templates",
        "org": "davila7",
        "url": "https://github.com/davila7/claude-code-templates",
        "lang": "Python",
        "langClass": "py",
        "stars": "31,095",
        "forks": "3,537",
        "starsToday": "113",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +113★！31.1K★ 的配置文件生意：Claude Code 的配置与监控 CLI，管理 agents、斜杠命令、hooks 与 MCP 模板，还带一个实时监控面板（aitmpl.com）。",
        "problems": [
            "<strong>配置文件越堆越乱：</strong>CLAUDE.md、agents、hooks、MCP 各写各的，团队里没人知道哪份在生效。",
            "<strong>上手先翻文档：</strong>新成员要花半天才能把 Agent 配到能用。",
            "<strong>运行状态看不见：</strong>Agent 跑了什么、花了多少、卡在哪一步，全靠猜。"
        ],
        "usage": [
            "用 npm 安装后从模板库挑选 agents、命令与 hooks。",
            "把选好的模板写进项目配置，团队成员共享同一套。",
            "打开监控面板观察会话与调用情况。"
        ],
        "insights": [
            "<strong>31K★ 说明配置本身就是个产品：</strong>官方 CLI 足够强，但「怎么配、配什么」是另一门生意——两年里长到 3 万星，靠的是模板而不是模型。",
            "<strong>它是 AGENTS.md 之争的下游产业：</strong>当各家 Agent 对配置文件的支持越来越乱，围绕「配置怎么管」的第三方工具必然出现——标准之争的赢家还没定，工具商已经开始收租。",
            "<strong>本质是默认值的争夺：</strong>模板决定了新项目一开始用什么技能、什么权限、什么模型——默认值即分发渠道。"
        ],
        "tags": ["claude-code", "configuration", "templates", "developer-tools", "mcp"]
    }
]

# 规整顺序与编号：按日增降序（本日为 2 天间隔，全部新面孔平铺）
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

today_projects = sorted(today_projects, key=lambda p: -_today(p))
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels by real gap (2 days)
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
    "date": "2026-09-23",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-23'
data['topic'] = '🔥 <strong>Agent 运行时的地基与上层同日登榜 + 模型公司开始卖行业成品</strong> —— google/ax（+2,324★）登顶：Google 的声明式 Agent 编排器（Task / Workspace / Gateway / Model 四原语、kubectl 式 CLI、可挂起续跑），而它的执行底座 agent-substrate/substrate（+301★）同一天出现在榜上：10 倍沙箱密度、低于 500 毫秒恢复、microVM 与 gVisor。anthropics/financial-services（+436★）36.3K★：投行与私募的参考 Agent 与技能包，一套源码两种交付（Cowork 插件或 Managed Agents API），免责声明写明「每次输出都停在人工签字前」。mvt-project/mvt（+441★）14.1K★：Amnesty 国际的移动取证工具合并 v3 破坏性变更。dream-num/univer（+202★）15.4K★：2022 年建仓的开源 Office SDK 把简介改成「The Office Harness for AI Agents」。superdesigndev/treg（+197★）给 Agent 当工具中间商：3,000+ 端点、按次一美分、凭证不出服务器。browser-use/video-use（+155★）25.8K★：用 coding agent 剪片，每个切点先自评再交付。davila7/claude-code-templates（+113★）31.1K★：Claude Code 配置模板与监控面板。今日两条明线：一、运行时层被整体看见——一个管调度，一个管沙箱；二、Agent 的经济关系在成形：模型公司卖行业成品、工具中间商把订阅拆成按次计费、老项目靠换定位重新定价。'

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
