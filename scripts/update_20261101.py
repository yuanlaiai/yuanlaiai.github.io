#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-01（距上次更新 4 天，flat day：全部新面孔）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-01"

LANGCLASS = {
    "Python": "py", "TypeScript": "ts", "JavaScript": "js", "Shell": "sh",
    "Rust": "rs", "C": "c", "C++": "cpp", "HTML": "html", "CSS": "css",
    "Markdown": "md", "Go": "go", "C#": "cs", "Java": "java",
    "Kotlin": "kotlin", "Dart": "dart", "TeX": "tex", "Swift": "swift",
    "Zig": "zig",
}

P = []


def add(owner, name, lang, stars, forks, starsToday, count, description,
        problems, usage, insights, tags):
    P.append({
        "owner": owner,
        "name": name,
        "fullName": "%s / %s" % (owner, name),
        "org": owner,
        "url": "https://github.com/%s/%s" % (owner, name),
        "lang": lang,
        "langClass": LANGCLASS.get(lang, lang.lower()),
        "stars": stars,
        "forks": forks,
        "starsToday": starsToday,
        "count": count,
        "badge": "新面孔",
        "description": description,
        "problems": problems,
        "usage": usage,
        "insights": insights,
        "tags": tags,
    })


add("thedotmack", "claude-mem", "TypeScript", "107,920", "9,473", "1,723", 3,
    "🔥 亮点 —— 今日 +1,723★ 居首，10.79万★。给 Claude Code 装一层持久记忆：自动记录工具调用、压缩成语义摘要，新会话开始时自己带回来。",
    [
        "<strong>新会话等于失忆：</strong>昨天定下的命名、踩过的坑、读过的文件全部清空，agent 要从头再翻一遍仓库。",
        "<strong>CLAUDE.md 靠手写：</strong>写多了挤爆上下文，写少了等于没写，而且没人愿意每天维护。",
        "<strong>会话记录没人查：</strong>本地那些 jsonl 里躺着完整历史，agent 自己不会去检索。",
    ],
    [
        "用 <pre><code>npx claude-mem install</code></pre> 装（npm 全局装只给 SDK，不注册 hook）。",
        "重启 Claude Code，之后的观察记录自动落到本地 SQLite，由常驻 worker 做摘要压缩。",
        "需要回溯时让 agent 调 MCP 检索工具，按语义找过去的操作而不是全文翻。",
    ],
    [
        "<strong>记忆被拆出模型变成外挂：</strong>上下文窗口再大也装不下一个项目的全部历史，于是记忆成了插件、数据库和检索层。",
        "<strong>它值钱的地方在自动：</strong>手写 CLAUDE.md 的人不少，能坚持每天维护的几乎没有，省下的是重复解释的耐心。",
        "<strong>一个记忆插件的星数压过多数基础模型公司：</strong>用户愿意为「不用重新交代一遍」买单，代价是多一个本地服务常驻。",
    ],
    ["agent-memory", "claude-code", "context", "sqlite", "mcp"])

add("pbakaus", "impeccable", "Rust", "98,317", "5,797", "1,338", 4,
    "🔥 亮点 —— +1,338★，9.83万★。给编码 agent 一套设计词汇表：用 polish、bolder 调方向，用 critique、audit 做复核，专治千篇一律的 AI 界面。",
    [
        "<strong>agent 的审美是默认值：</strong>奶油底色、细衬线标题、胶囊按钮，同一个模型做十个网站长得像一个。",
        "<strong>审美说不成 prompt：</strong>「再高级一点」这类反馈，模型只能靠猜。",
        "<strong>改样式靠盲试：</strong>在源码里改一版、刷新、不满意、再改，一轮几分钟就过去了。",
    ],
    [
        "项目根目录跑 <pre><code>npx impeccable install</code></pre>，重载编辑器后用 <code>/impeccable init</code>。",
        "init 会读代码、只问推不出的信息，写进 PRODUCT.md；再用 <code>/impeccable document</code> 把现有视觉系统落到 DESIGN.md。",
        "<code>/impeccable live</code> 在 dev server 上开覆盖层，选中元素换方案，接受的直接写回源码。",
    ],
    [
        "<strong>把审美拆成动词是个办法：</strong>polish、bolder、critique、audit 各自有明确动作和验收标准，比形容词好使。",
        "<strong>先写上下文文件再下指令：</strong>PRODUCT.md 和 DESIGN.md 决定了后面所有命令的基准，这一步偷懒等于没装。",
        "<strong>支持二十个 harness 说明指令层没有壁垒：</strong>谁都能抄这套命令，差别落在文档和示例的质量上。",
    ],
    ["design", "coding-agent", "ui", "skills", "frontend"])

add("milind-soni", "OpenMausBot", "TypeScript", "9,662", "1,340", "1,303", 1,
    "🔥 亮点 —— +1,303★，9,662★ 首登。Grok Bot 的开源替代：侧边栏每个 bot 都是本地跑的 Claude/Codex 真代理，各有性格、模型、云电脑和接好的应用，用聊天的方式指挥。",
    [
        "<strong>官方 bot 关在自己生态里：</strong>模型、记忆、连接的应用都由厂商决定，你只能用它给的入口。",
        "<strong>一套人格应付所有事：</strong>写代码、查资料、盯邮件需要不同的工作方式，却共用同一个助手。",
        "<strong>长任务看不见过程：</strong>扔进去一句话，中间做了什么你无从判断，出问题只能重来。",
    ],
    [
        "从 openmausbot.com 下 macOS/Windows/Ubuntu 的 Electron 客户端。",
        "给每个 bot 配模型（本地 Claude 或 Codex）和人格，各自接自己的应用。",
        "做重要操作时弹审批，跑起来的过程在聊天窗口里直接可见。",
    ],
    [
        "<strong>「agent 当联系人」是交互上的迁移：</strong>不再是一个输入框，而是一排有分工的同事，人是管理者的角色。",
        "<strong>底层跑本地 Claude/Codex 说明上层不掌握模型：</strong>这类产品的竞争力全在编排和界面，模型一换就得跟着换。",
        "<strong>开源替代会一直压着官方定价：</strong>功能能对上的部分，用户没有理由为闭源多付钱。",
    ],
    ["ai-agent", "electron", "local-first", "chat", "typescript"])

add("pingdotgg", "t3code", "TypeScript", "35,662", "8,790", "1,148", 1,
    "🔥 亮点 —— +1,148★，3.57万★ 首登。自称 agent harness 控制台：iOS、安卓、网页、桌面四端接管本机上跑的 Claude Code、Codex、Cursor、Grok Build，出门也能盯任务。",
    [
        "<strong>agent 跑在本机，人一走开就断线：</strong>编译跑起来、任务排队中，你只能回工位看。",
        "<strong>各家 CLI 一套界面：</strong>同时用三四家 agent 的人，要记四套快捷键和日志格式。",
        "<strong>远程接入要么买云 IDE，要么自己搭隧道：</strong>两条路都不便宜，也都不好维护。",
    ],
    [
        "先装并登录至少一个 provider，比如 <code>codex login</code> 或 <code>claude auth login</code>。",
        "装桌面端，或直接用 app.t3.codes 网页版。",
        "手机 App 连同一台机器，接管已经开始或排队中的会话。",
    ],
    [
        "<strong>控制面和模型层正在分开：</strong>它一家都不生产模型，卖点恰恰是「你手上哪家都能接」。",
        "<strong>作者明说不卖东西、允许 fork：</strong>这一层的竞争是体验，不是锁定，锁不住的东西才需要靠好用取胜。",
        "<strong>远程优先意味着编程场景从桌前挪到口袋：</strong>agent 跑得越久，人越不需要守着，入口的重量会从 IDE 往手机移。",
    ],
    ["coding-agent", "remote", "multi-provider", "electron", "mobile"])

add("Orkas-AI", "Orkas", "JavaScript", "6,300", "380", "1,044", 1,
    "🔥 亮点 —— +1,044★，6,300★ 首登。本地优先的多代理桌面：Commander 把目标拆成待办，拉上专家代理和你已有的 Claude Code、Codex、OpenCode、Hermes-Agent 一起做完。",
    [
        "<strong>单个 agent 只会答一轮：</strong>项目跨天就断线，昨天的规则、记忆、文件全要重新交代。",
        "<strong>多个 CLI 之间没有分工：</strong>手上同时装着几家 agent，谁做什么全靠人临时分配。",
        "<strong>自动化散在各处：</strong>定时任务写在脚本、cron、快捷指令里，没有统一排期。",
    ],
    [
        "官网下 macOS/Windows 客户端，内置模型送 500 credits，也可以接自己的 key 或本地 OpenAI 兼容端点。",
        "建一个 project，把目标、规则、记忆、文件放进去，后续会话接着往下走。",
        "用 to-do 拆分人和 agent 的任务，打开 auto-advance 让团队自己领下一项，定时任务按小时/日/周跑。",
    ],
    [
        "<strong>它把「项目」而不是「会话」当成一等对象：</strong>这是 2026 年 agent 产品最明显的分水岭，会话类工具解决不了跨天的工作。",
        "<strong>调度器的意义是把多家 agent 变成可替换的工人：</strong>底层换模型不心疼，编排层才积累资产。",
        "<strong>本地优先同时回应了两件事：</strong>token 账单和「数据不出机器」，后者对企业比前者重要得多。",
    ],
    ["multi-agent", "local-first", "orchestration", "desktop", "automation"])

add("HKUDS", "DeepTutor", "Python", "52,849", "6,469", "1,034", 2,
    "🔥 亮点 —— +1,034★，5.28万★，第二次上榜。港大数据智能实验室的终身个性化辅导系统：按掌握度生成学习路径，带学习者/监护人账号和自己的 CLI。",
    [
        "<strong>聊天机器人记不住你学到哪：</strong>答得对，但每次都要重新描述自己的水平和目标。",
        "<strong>题库产品的路径是固定的：</strong>所有人都走同一条线，不会为某一个人的薄弱点重排。",
        "<strong>辅导过程不可追溯：</strong>学完不知道哪里没懂，家长和老师也看不到过程。",
    ],
    [
        "按 README 起后端服务，或直接用 DeepTutor CLI 的 agent 接口。",
        "上传教材、论文或题库，系统按来源生成 Mastery 掌握路径。",
        "学习者账号做练习，监护人账号看进度和卡点。",
    ],
    [
        "<strong>教育是最早被 agent 重写的领域：</strong>它天生需要长期记忆、个性化路径和可追溯记录，正好是这一代 agent 的短板与卖点。",
        "<strong>「有来源的路径」是对幻觉的工程回应：</strong>每一条建议都指回上传的教材，比说「我懂了」有用。",
        "<strong>港大团队连续出项目：</strong>学术机构已经不只是发论文，而是在和公司抢产品化的位置。",
    ],
    ["education", "tutoring", "personalized", "rag", "hkuds"])

add("lightpanda-io", "browser", "Zig", "39,273", "1,909", "929", 1,
    "🔥 亮点 —— +929★，3.93万★ 首登。用 Zig 从零写的无头浏览器，专给 agent 和爬虫：100 个页面占 123MB 内存、跑 5 秒，Chromium 是 2GB、46 秒。",
    [
        "<strong>抓一百个页面烧 2GB 内存：</strong>云上按内存计价，爬虫的成本大头是浏览器本身。",
        "<strong>Chromium 启动慢：</strong>agent 每一步操作都要等一个完整浏览器起来。",
        "<strong>全套功能只用得上一小部分：</strong>抓数据不需要 GPU 渲染、扩展和完整的 CSS 引擎，但都得装上。",
    ],
    [
        "用 Homebrew 或包管理器装 nightly 版，也可直接下二进制。",
        "<code>lightpanda serve</code> 起 CDP 服务，给 Puppeteer、Playwright 当后端。",
        "<code>lightpanda agent</code> 用自然语言驱动：导航、点流程、填表、抓结构化数据。",
    ],
    [
        "<strong>为单一用途重写基础设施：</strong>AI 把抓取量推高之后，通用浏览器的冗余第一次变成了真金白银的账单。",
        "<strong>省十六倍内存等于把爬虫成本砍一个数量级：</strong>这类改进不会出现在模型榜单上，但决定了 agent 能不能大规模跑。",
        "<strong>AGPL 的选择说明它要卖云服务：</strong>开源引擎加托管收费，是这个位置唯一能持续的商业模式。",
    ],
    ["headless-browser", "zig", "crawler", "automation", "infra"])

add("mattpocock", "skills", "Shell", "308,422", "25,955", "883", 11,
    "🔥 亮点 —— +883★，30.84万★，第 11 次上榜。Matt Pocock 日常用的工程技能集：小而可组合、鼓励改成自己的，明确反对 GSD、BMAD、Spec-Kit 那种把流程收走的框架。",
    [
        "<strong>流程框架接过方向盘：</strong>GSD、BMAD 这类方案替你管流程，出了 bug 你连从哪查都不知道。",
        "<strong>大而全的规范写起来比代码慢：</strong>为了「规范」先写一堆文档，最后没人读。",
        "<strong>换模型要整套重学：</strong>绑死某个 agent 的写法，模型一换代就全废。",
    ],
    [
        "按 README 的 30 秒安装流程装成 plugin。",
        "从一个小技能开始用，按自己习惯改，别整套照搬。",
        "技能本身是 markdown，任何模型都能读，直接读源码就能理解。",
    ],
    [
        "<strong>30 万★ 的仓库里主要是 markdown：</strong>用户收藏的是经验和判断，不是可执行代码。",
        "<strong>「不接管控制权」是这一代技能作者最清醒的立场：</strong>不夺走方向盘，就不会在被追责时无话可说。",
        "<strong>可组合意味着会被 fork：</strong>作者拿到的是影响力而不是收入，这也是它敢全开放的原因。",
    ],
    ["skills", "engineering", "typescript", "workflow", "composable"])

add("anthropics", "skills", "Python", "185,908", "21,946", "754", 2,
    "🔥 亮点 —— +754★，18.59万★，第二次上榜。Anthropic 官方的技能示例库：从画图、做音乐到测试 Web 应用、生成 MCP server，配套 agentskills.io 标准。",
    [
        "<strong>官方文档只讲概念：</strong>技能到底能干什么，得自己一个个试。",
        "<strong>社区技能质量参差：</strong>没有基准，装十个不如自己写一个。",
        "<strong>格式各家不一致：</strong>Claude、Cursor、Codex 的技能目录结构各有一套。",
    ],
    [
        "克隆仓库，按技能目录结构放进本地的 skills 目录。",
        "用 <code>/plugin</code> 安装，或直接复制某个技能去改。",
        "重点参考 MCP server 生成、Web 应用测试这几个样例，改造成自己的。",
    ],
    [
        "<strong>官方下场做示例：</strong>说明技能生态还处在需要教材的阶段，厂商必须自己把样板铺出来。",
        "<strong>标准由模型厂商定义：</strong>agentskills.io 一旦成为默认，第三方只能跟随格式，无法重写规则。",
        "<strong>示例库的星数会长期高于单点工具：</strong>它是入口，用户学技能的第一站就是这里。",
    ],
    ["skills", "anthropic", "examples", "mcp", "standard"])

add("Donchitos", "Claude-Code-Game-Studios", "Shell", "31,209", "4,276", "742", 1,
    "🔥 亮点 —— +742★，3.12万★ 首登。把一个 Claude Code 会话变成游戏工作室：49 个代理、74 个技能、15 个 hook、14 条规则，模拟从策划、美术到 QA 的分工。",
    [
        "<strong>一个人做游戏缺的不是写代码的人：</strong>策划、美术、测试的角色没人补，代码写得再快也堆不出一个作品。",
        "<strong>一个 agent 兼所有角色会打架：</strong>同一轮里既当策划又当 QA，输出互相矛盾。",
        "<strong>多 agent 没有交接规范就是吵架：</strong>没有规则约束，每个角色都在改别人的东西。",
    ],
    [
        "克隆仓库，把 <code>.claude</code> 目录放进自己的游戏项目。",
        "按 README 触发对应工作流，让策划代理先出设计，再进实现。",
        "靠 hook 约束每个角色的读写边界，避免互相覆盖。",
    ],
    [
        "<strong>它卖的其实是组织结构：</strong>49 个代理的价值在编制和流程，不在提示词技巧。",
        "<strong>角色越多协调成本越高：</strong>74 个技能里真正每天用到的可能不到十个，剩下的是覆盖长尾场景的保险。",
        "<strong>它验证了一件事：</strong>agent 的能力上限，取决于你给它排的编制，而不是它自己有多聪明。",
    ],
    ["game-dev", "claude-code", "multi-agent", "workflow", "skills"])

add("obra", "superpowers", "Shell", "310,080", "27,586", "665", 20,
    "🔥 亮点 —— +665★，31万★，第 20 次上榜，本榜单最长连续记录。给编码 agent 的一整套开发方法论：让它先问清你要做什么，再动手写，支持 16 种 harness。",
    [
        "<strong>agent 一看到需求就写代码：</strong>写完才发现方向错了，返工比重写还贵。",
        "<strong>长任务中途跑偏没人拦：</strong>做到一半偏离目标，等发现时已经改了几十个文件。",
        "<strong>每家 CLI 要各写一遍流程：</strong>换工具就得重新配一套，经验沉淀不下来。",
    ],
    [
        "按 README 选自己用的 harness 安装，16 种里有 Claude Code、Codex、Cursor、Copilot、Gemini CLI。",
        "从一个技能开始用，不必全装。",
        "出问题按 README 的 When Something Goes Wrong 一节逐项排查。",
    ],
    [
        "<strong>20 次上榜是最长的复利记录：</strong>方法论类项目不像工具那样被替代，它跟着用户换工具一路迁移。",
        "<strong>它的对手不是别的技能库，是用户的惰性：</strong>问清目标再动手，比直接要代码慢一步，多数人忍不住。",
        "<strong>「先问再写」一旦被模型厂商内置，这类仓库的价值会立刻缩水：</strong>它现在站在模型的补丁位上，位置并不牢。",
    ],
    ["methodology", "skills", "coding-agent", "workflow", "shell"])

add("Graphify-Labs", "graphify", "Python", "140,048", "13,363", "660", 5,
    "🔥 亮点 —— +660★，14万★，第五次上榜。把代码、PDF、SQL、配置、截图变成可查询的知识图谱：本地 AST 解析、每条边有解释、不走向量库。",
    [
        "<strong>agent 每次都要重读整个仓库：</strong>同样的文件翻十遍，token 和时间都浪费在这上面。",
        "<strong>grep 找不到跨文件的关系：</strong>这个函数被谁调用、这段配置影响哪条链路，文本搜索给不出答案。",
        "<strong>向量检索给不出「为什么」：</strong>召回了相关片段，但说不清它和当前问题怎么连上的。",
    ],
    [
        "在 Claude Code / Cursor / Codex / Gemini CLI 里输入 <code>/graphify .</code>。",
        "产物落在 graphify-out/：graph.html 可交互，GRAPH_REPORT.md 列关键节点和反常连接。",
        "把 obsidian/ 目录当 vault 打开，或长期保留 graph.json 供几周后再查。",
    ],
    [
        "<strong>「不走向量库」是清晰的路线选择：</strong>赌可解释性比召回率重要，每条边都能追到出处。",
        "<strong>71.5 倍省 token 的说法要打折看：</strong>但方向没错，图谱把「重复读文件」换成了「一次性建关系」。",
        "<strong>导出成 Obsidian vault 是个聪明的妥协：</strong>承认 agent 和人的入口可以共用，工具不用独占用户的知识库。",
    ],
    ["knowledge-graph", "code-analysis", "claude-code", "obsidian", "ast"])

add("calesthio", "OpenMontage", "Python", "73,991", "9,700", "583", 5,
    "🔥 亮点 —— +583★，7.4万★，第五次上榜。开源的 agentic 视频生产系统：12 条生产管线、100 多个工具、700 多个技能与制作知识文件，把编码助手改成视频工作室。",
    [
        "<strong>做视频的链条太长：</strong>脚本、素材、配音、字幕、剪辑，每一步换一个工具，中间靠人搬。",
        "<strong>单点 AI 工具只解决一段：</strong>生成画面的不管字幕，配音的不懂节奏，拼起来全靠手工。",
        "<strong>全流程交给黑箱服务：</strong>改不动、搬不走，风格和能力都被供应商锁死。",
    ],
    [
        "按 README 装 Python 依赖，配好 provider 的 key。",
        "选一条 pipeline，从脚本一路走到成片。",
        "扔一个你喜欢的视频进去，让它反推风格再照着做。",
    ],
    [
        "<strong>视频正在重复代码走过的路：</strong>从单点工具拼装，走向有流水线和交接规范的工程化。",
        "<strong>700 个知识文件才是它的资产：</strong>模型谁都能调，制作经验得一条条写下来。",
        "<strong>AGPL 会挡住一部分商业使用：</strong>想在上面做产品的团队，得先把授权问题想清楚。",
    ],
    ["video", "agentic", "pipeline", "production", "ffmpeg"])

TOPIC = ("🔥 <strong>今日主题：给同一个模型造外设。</strong>"
         "停更四天后回来的榜单，13 个项目里没有一个是新模型：claude-mem 补记忆，"
         "impeccable 补审美，t3code 和 Orkas 做调度台，Anthropic 官方、Matt Pocock、"
         "superpowers 三家一起做方法论，OpenMontage 和 Game Studios 干脆让编码助手改行做视频和游戏。"
         "唯一往下挖基础设施的是 LightPanda，用 Zig 重写浏览器把爬虫内存砍到十六分之一。"
         "当所有人都在造外设，说明模型本身已经够用，卡住人的是记忆、上下文和流程；"
         "真正的进展不在榜上，在那些没人愿意发 star 的接口层里。")

with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

# 排序：全部新面孔（gap=4 → flat day），按 starsToday 降序
P.sort(key=lambda p: -int(p["starsToday"].replace(",", "")))
for i, p in enumerate(P, 1):
    p["rank"] = i

new_day = {"date": TODAY, "label": "今天", "icon": "", "projects": P}

# 标签按真实 gap 平移
today = datetime.strptime(TODAY, "%Y-%m-%d")
for day in data["days"]:
    d = (today - datetime.strptime(day["date"], "%Y-%m-%d")).days
    if d <= 0:
        day["label"] = "今天"
    elif d == 1:
        day["label"] = "昨天"
    elif d == 2:
        day["label"] = "前天"
    else:
        day["label"] = "%d天前" % d

data["days"].insert(0, new_day)
data["lastUpdated"] = TODAY
data["topic"] = TOPIC

# 断言：badge 全部设置
assert all(p.get("badge") in ("新面孔", "连登") for p in data["days"][0]["projects"])
assert len(data["days"]) == 93, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，新增 %d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
print("rank 顺序：")
for p in P:
    print("  %2d. %-32s +%-6s %8s★ count=%d" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
