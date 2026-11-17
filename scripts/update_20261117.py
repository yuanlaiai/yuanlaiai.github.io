#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-17（距上次更新 4 天，flat day：全部新面孔）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-17"

LANGCLASS = {
    "Python": "py", "TypeScript": "ts", "JavaScript": "js", "Shell": "sh",
    "Rust": "rs", "C": "c", "C++": "cpp", "HTML": "html", "CSS": "css",
    "Markdown": "md", "Go": "go", "C#": "cs", "Java": "java",
    "Kotlin": "kotlin", "Dart": "dart", "TeX": "tex", "Swift": "swift",
    "Zig": "zig", "Ruby": "rb",
}

P = []


def add(owner, name, lang, stars, forks, starsToday, description,
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
        "badge": "新面孔",
        "description": description,
        "problems": problems,
        "usage": usage,
        "insights": insights,
        "tags": tags,
    })


add("obra", "superpowers", "Shell", "318,962", "28,436", "1,905",
    "🔥 亮点 —— 今日 +1,905★ 第一，31.9万★，第 21 次上榜，仍是本榜单最长记录。给编码 agent 的一整套开发方法论：先问清你要做什么，再动手写，支持 16 种 harness。",
    [
        "<strong>agent 一看到需求就写代码：</strong>写完才发现方向错了，返工比重写还贵。",
        "<strong>长任务中途跑偏没人拦：</strong>等发现时已经改了几十个文件。",
        "<strong>每家 CLI 各写一遍流程：</strong>换工具就得重配一套。",
    ],
    [
        "按 README 选自己用的 harness 安装。",
        "从一个技能开始用，不必全装。",
        "出问题按 When Something Goes Wrong 一节逐项排查。",
    ],
    [
        "<strong>21 次上榜，日增还能到 1,905★：</strong>方法论类项目不吃新鲜度，靠的是每次换工具都能跟着迁移。",
        "<strong>它站在模型的补丁位上：「先问再写」一旦被厂商内置，价值会立刻缩水，但现在还没有。</strong>",
        "<strong>31.9 万★ 里大部分是收藏而非使用，这个数字衡量的是共识，不是活跃度。</strong>",
    ],
    ["methodology", "skills", "coding-agent", "workflow", "shell"])

add("dream-num", "univer", "TypeScript", "28,667", "2,608", "1,776",
    "🔥 亮点 —— +1,776★，2.87万★，第 4 次上榜。开源的 Office SDK：从 Sheets 和 Docs 起步，把表格、文档、协作、文件处理接进自己的应用或 agent，号称「搭一个自己的 AI 办公室」。",
    [
        "<strong>在线表格文档只能买不能改：</strong>想嵌到自己产品里，要么用别人的 UI，要么自己从零写。",
        "<strong>agent 处理文档靠转换：</strong>读写 xlsx、docx 要来回转格式，公式和样式一路丢。",
        "<strong>协作能力是黑盒：</strong>多人同时编辑的冲突解决，自己实现极难。",
    ],
    [
        "装 <code>@univerjs/core</code> 等包，按文档起一个最小可用的表格。",
        "按需加插件：公式、协作、导入导出、打印。",
        "把渲染层当组件嵌进自己的应用，业务逻辑和数据留在自己这边。",
    ],
    [
        "<strong>「AI 办公室」的说法背后是入口之争：</strong>谁承载表格和文档，谁就承载 agent 的产出。",
        "<strong>它做的是被微软和谷歌锁住的那一层：</strong>SDK 化之后，第三方产品不必再自研编辑器。",
        "<strong>四次上榜，说明企业需求一直在：</strong>消费级热度不高，但采购单在这里。",
    ],
    ["office", "sdk", "spreadsheet", "collaboration", "typescript"])

add("ag-ui-protocol", "ag-ui", "TypeScript", "19,772", "2,048", "1,444",
    "🔥 亮点 —— +1,444★，1.98万★ 首登。一个把任何 agent 接到任何应用的开放协议，npm 和 PyPI 双端发布，正面对标「前端该怎么消费 agent 的流式输出」。",
    [
        "<strong>每个 agent 框架一套流式格式：</strong>前端接一个后端就要重写一遍解析。",
        "<strong>状态同步靠人肉约定：</strong>agent 改了什么、界面该更新什么，没有统一说法。",
        "<strong>换框架等于重做前端：</strong>LangGraph 一套、自研一套，前端代码全废。",
    ],
    [
        "前端装 <code>@ag-ui/core</code>，后端装 <code>ag-ui-protocol</code>。",
        "按协议发事件：消息增量、工具调用、状态更新各走各自的类型。",
        "后端换框架时保持协议不变，前端不用改。",
    ],
    [
        "<strong>协议层出现，说明 agent 已经进入「要接界面」的阶段：</strong>之前大家关心的是它能不能跑，现在关心它怎么被看。",
        "<strong>MCP 管 agent 到工具，AG-UI 管 agent 到人：</strong>两条协议把 agent 的两端都规范化了。",
        "<strong>双端发版是关键信号：</strong>作者知道这件事必须两边同时装才有意义。",
    ],
    ["protocol", "frontend", "streaming", "agents", "typescript"])

add("elementalsouls", "Claude-BugHunter", "Python", "8,171", "1,264", "1,007",
    "🔥 亮点 —— +1,007★，8,171★ 首登。一个红队技能包：83 个技能、15 个斜杠命令、681 套公开漏洞报告模式（433 套逐条可查），覆盖 24 类核心漏洞，还接 Burp 的 MCP。",
    [
        "<strong>红队工作高度依赖经验：</strong>同一个洞，老手三分钟看出来，新手翻一天文档。",
        "<strong>方法论散在博客和报告里：</strong>想查「这类漏洞别人怎么打的」，得自己搜。",
        "<strong>工具链割裂：</strong>Burp、命令行、浏览器、脚本各一套，中间靠手抄。",
    ],
    [
        "把技能目录放进 Claude Code 的 skills 路径。",
        "按 15 个斜杠命令选阶段：侦察、验证、利用、写报告。",
        "接上 Burp 的 MCP，让 agent 直接看请求和响应。",
    ],
    [
        "<strong>681 套披露报告才是它真正的资产：</strong>技能本身不难写，难的是把实战案例拆成可复用的模式。",
        "<strong>强调「433 套逐条可查」是刻意的：</strong>安全领域最怕编造，可审计性比覆盖面更能建立信任。",
        "<strong>红队是 agent 最危险也最有效的场景：</strong>它需要判断力，正好是模型最缺的那部分。",
    ],
    ["security", "red-team", "skills", "claude-code", "pentest"])

add("NVIDIA", "SkillEvaluator", "Python", "3,171", "450", "969",
    "🔥 亮点 —— +969★，3,171★ 首登。技能的质检流水线：三层分别回答「安不安全、合不合规、好不好用」，一条命令就能接进 CI，检查每次技能改动。",
    [
        "<strong>技能多了没法比：</strong>同样功能的十个技能，谁更好全靠自己试。",
        "<strong>合不合规没人验：</strong>技能有没有按 harness 的规范写，只有跑崩了才知道。",
        "<strong>改动没有回归测试：</strong>改一行提示词，行为可能全变。",
    ],
    [
        "<code>skillevaluator tier1 ./my-skill --no-llm</code> 先跑静态校验。",
        "配好 provider 和模型后跑三层完整评估，得到质量分和报告。",
        "<code>skillevaluator ci init</code> 在仓库里生成 CI 模板，每次改动都过一遍。",
    ],
    [
        "<strong>它和 SkillSpector 是同一条流水线的前后两段：</strong>一个查有没有洞，一个查值不值得用。",
        "<strong>做成 CI 模板是把门禁前移：</strong>技能质量从此不是装完再说，而是提交时就卡住。",
        "<strong>三层拆开的设计很务实：</strong>静态校验不需要模型，成本低，能挡住大部分低级问题。",
    ],
    ["skills", "evaluation", "quality", "ci", "nvidia"])

add("tradermonty", "claude-trading-skills", "Python", "6,726", "1,390", "771",
    "🔥 亮点 —— +771★，6,726★ 首登。给个人投资者的交易技能集：市场复盘、技术图表、经济日历、选股器一套流程。作者明确说目标不是让 AI 替你决定买卖。",
    [
        "<strong>交易靠情绪：</strong>该复盘的时候不复盘，该止损的时候拖。",
        "<strong>流程没有留痕：</strong>三个月后想复盘当时的判断，只剩一句「感觉不对」。",
        "<strong>信号服务不靠谱：</strong>收钱给代码的，赚的是你的订阅费。",
    ],
    [
        "装技能后先跑市场复盘流程，把当天的逻辑写下来。",
        "用图表和日历技能做标的筛选和事件提醒。",
        "按它的日志模板记录交易计划，隔一段时间回看自己的决策习惯。",
    ],
    [
        "<strong>它明确拒绝「替你下单」，这个定位比功能更值钱：</strong>投资领域里，敢说自己不管决策的工具反而可信。",
        "<strong>技能在这里的作用是逼人走流程：</strong>复盘、记录、检查，都是人懒起来最先省掉的步骤。",
        "<strong>订阅制信号服务正在被这类开源工具替代：</strong>用户要的不是结论，是不被割的流程。",
    ],
    ["trading", "skills", "investing", "workflow", "finance"])

add("alibaba", "open-code-review", "Go", "53,394", "4,387", "764",
    "🔥 亮点 —— +764★，5.34万★，第 6 次上榜。阿里开源的代码评审工具：确定性工程加 agent 的混合架构，选文件、分组这类不能出错的步骤交给代码，语言模型只负责判断。",
    [
        "<strong>纯 prompt 评审结果不稳定：</strong>换个措辞，结论就变了。",
        "<strong>重要改动被漏掉：</strong>模型挑文件靠感觉。",
        "<strong>评审意见落不了地：</strong>说得挺好，改起来无从下手。",
    ],
    [
        "按文档部署，接进自己的仓库。",
        "放进 PR 流程，每次提交都过一遍。",
        "用它的文件选择和分组逻辑控制范围，模型只在范围内判断。",
    ],
    [
        "<strong>一周内第二次上榜，日增从 206 涨到 764：</strong>企业评审流程的改造比消费级工具更慢，但一旦开始推就不再回头。",
        "<strong>「不能错的写成代码」这套思路正在扩散：</strong>从评审到测试到发布，都能看到同一个模式。",
        "<strong>规模背书比功能列表更有说服力：</strong>阿里两个字就是它最好的营销。",
    ],
    ["code-review", "alibaba", "hybrid", "go", "ci"])

add("affaan-m", "ECC", "JavaScript", "305,013", "44,919", "718",
    "🔥 亮点 —— +718★，30.5万★，第 14 次上榜。自称 agent harness 操作系统：一套「计划、测试、实现、评审、验证、记住、改进」的闭环，装一次就变成 agent 的工作方式。",
    [
        "<strong>每个 prompt 都在重建流程：</strong>今天让它先写测试，明天忘了，行为就变了。",
        "<strong>上下文塞满就忘事：</strong>前面定下的规则，后面自己违反。",
        "<strong>重复的成功没有沉淀：</strong>做对一次，下次还要重新教。",
    ],
    [
        "把 ECC 装成插件，按 harness 选对应路径（Claude Code 支持最好）。",
        "让它按 plan→test→implement→review→verify→remember 的循环跑任务。",
        "重复有效的做法会被固化成技能，下次直接调用。",
    ],
    [
        "<strong>「优化上下文窗口，其余全部持久化」这句话概括了它全部设计：</strong>记忆不该挤在窗口里。",
        "<strong>14 次上榜、30.5 万★，但它的实际门槛也最高：</strong>必须先认同这套流程，才谈得上用。",
        "<strong>它和 superpowers 是同一赛道的两个答案：</strong>一个强调方法，一个强调把方法变成系统。",
    ],
    ["methodology", "harness", "memory", "skills", "workflow"])

add("backnotprop", "plannotator", "TypeScript", "12,891", "1,293", "691",
    "🔥 亮点 —— +691★，1.29万★，第 2 次上榜。给 agent 做的批注工作台：在计划、规格、markdown、HTML 和 diff 上标注，反馈直接回到 agent。",
    [
        "<strong>方案只能整段接受或打回：</strong>想改一行，只能重新描述需求。",
        "<strong>评审记录散在聊天里：</strong>三天后翻不回来。",
        "<strong>长计划读不完：</strong>几千字的输出，注意力撑不到最后。",
    ],
    [
        "用 <code>/plannotator-annotate</code> 打开文件、目录或网址。",
        "在 inbox 里收待审工件，批注完一次性发回。",
        "Codex 上换成 <code>!plannotator review</code>。",
    ],
    [
        "<strong>四天涨了 2,600★：</strong>人机协作界面这个空位一直存在，只是之前没人认真做。",
        "<strong>标注比对话更精确：</strong>指到具体一行，比「再优化一下」有效得多。",
        "<strong>它把 agent 的产出当成需要过稿的稿件：</strong>这个心理模型比工具本身更有价值。",
    ],
    ["review", "annotation", "human-in-the-loop", "agents", "tui"])

add("Graphify-Labs", "graphify", "Python", "149,325", "14,360", "615",
    "🔥 亮点 —— +615★，14.93万★，第 6 次上榜。把代码、PDF、SQL、配置和截图变成可查询知识图谱的技能：本地 AST 解析、每条边有解释、不走向量库。",
    [
        "<strong>agent 每次重读整个仓库：</strong>同样文件翻十遍，token 全花在这。",
        "<strong>grep 找不到跨文件关系：</strong>谁调用了谁、改动影响哪条链路，文本搜索给不出。",
        "<strong>向量检索给不出「为什么」：</strong>召回了片段，说不清它怎么连上的。",
    ],
    [
        "在 Claude Code / Cursor / Codex 里输入 <code>/graphify .</code>。",
        "看 graphify-out/ 里的 graph.html 和 GRAPH_REPORT.md。",
        "导出的 obsidian/ 目录可直接当 vault 打开。",
    ],
    [
        "<strong>「不走向量库」是明确的路线选择：</strong>赌可解释性比召回率重要。",
        "<strong>一周内两次上榜：</strong>上下文成本压得越紧，结构化检索的价值越明显。",
        "<strong>它承认人和 agent 可以共用一套知识入口：</strong>所以宁可导出 Obsidian vault 也不自建界面。",
    ],
    ["knowledge-graph", "code-analysis", "claude-code", "obsidian", "ast"])

add("Tencent", "LoopForge", "Go", "2,803", "408", "590",
    "🔥 亮点 —— +590★，2,803★ 首登。腾讯开源的交付编排：在沙箱工作区里和编码 agent 对话，跑可重复的 SOP，人来批准什么能上线。支持 CodeBuddy、Codex、Claude Code。",
    [
        "<strong>agent 直接改生产代码：</strong>没人拦，出事只能回滚。",
        "<strong>团队各跑各的流程：</strong>同一个仓库，每个人的 agent 用法都不一样。",
        "<strong>交付靠记性：</strong>哪一步该谁批准，全在脑子里。",
    ],
    [
        "装 <code>loopforge-cli</code>，起一个沙箱工作区。",
        "把团队的交付流程写成 SOP 脚本，agent 按它执行。",
        "关键节点停下来等人批准，再继续往下走。",
    ],
    [
        "<strong>「沙箱 + SOP + 人工批准」是企业引入 agent 的三个必要条件，它一次全给了。</strong>",
        "<strong>腾讯把它开源，等于把内部实践变成行业默认选项：</strong>和阿里 open-code-review 是同一个套路。",
        "<strong>编排层的竞争不看模型能力，看谁能把审批流讲清楚：</strong>因为买单的是流程负责人，不是工程师。",
    ],
    ["orchestration", "sop", "sandbox", "tencent", "delivery"])

add("kajisho5", "ffmpeg-skill", "Python", "7,510", "692", "367",
    "🔥 亮点 —— +367★，7,510★，第 2 次上榜。给编码 agent 的本地视频编辑器：42 个 FFmpeg 工具，每个都有机器可读的输入输出契约，agent 剪完自己验一遍。",
    [
        "<strong>拼 ffmpeg 命令容易静默失败：</strong>参数错一个，输出文件是坏的也不报错。",
        "<strong>云剪辑 API 要上传素材：</strong>成本和隐私都是问题。",
        "<strong>剪完没有验收环节：</strong>错的东西直接交付。",
    ],
    [
        "装 skill 或 npm 包，也可以走 MCP 接进客户端。",
        "让 agent 从 42 个工具里选动作、给参数、跑一遍。",
        "跑完检查输出契约，确认时长、编码、音轨都对。",
    ],
    [
        "<strong>四天涨 2,100★：</strong>视频是 agent 最想接又最难接的活，能自检的方案一下就被认出来了。",
        "<strong>「机器可读契约」这个设计比工具数量重要：</strong>42 个还是 100 个无所谓，能不能验证才对。",
        "<strong>只用 Python 标准库、不联网：</strong>它把可运行性放在了功能之前。",
    ],
    ["video", "ffmpeg", "skills", "mcp", "local"])

add("google-labs-code", "stitch-skills", "TypeScript", "9,925", "1,298", "350",
    "🔥 亮点 —— +350★，9,925★ 首登。Google Stitch（AI 生成界面）的技能库，遵循 Agent Skills 开放标准，Codex、Antigravity、Gemini CLI、Claude Code、Cursor、OpenCode 都能装。",
    [
        "<strong>生成的界面接不进真实工程：</strong>设计稿和代码之间还隔着一层人工转换。",
        "<strong>各家设计工具各一套：</strong>换工具就得重学一遍操作。",
        "<strong>agent 不知道设计规范：</strong>生成的组件和现有系统对不上。",
    ],
    [
        "Codex 里加 marketplace 再装插件，或用 CLI 走 sparse 安装。",
        "装 stitch-design 和 stitch-build 两组插件。",
        "用 Stitch MCP server 把设计和代码串起来。",
    ],
    [
        "<strong>Google 把 Stitch 做成技能库，等于承认 AI 生成界面要落在工程里才有用。</strong>",
        "<strong>它主动遵循 Agent Skills 开放标准：</strong>没有自家标准的厂商，只能用别人的标准去抢生态。",
        "<strong>设计到代码这一段的工具，竞争点已经从「生成得像」变成「接得进」。</strong>",
    ],
    ["design", "skills", "google", "frontend", "mcp"])

add("usestrix", "strix", "Python", "76,206", "8,646", "325",
    "🔥 亮点 —— +325★，7.62万★，第 5 次上榜。开源的 AI 渗透测试工具：agent 带着 HTTP 拦截代理、浏览器利用、shell 和自写 PoC 的沙箱，去把你的应用打一遍再修。",
    [
        "<strong>渗透测试要请人：</strong>周期长、按次收费，小团队排不上。",
        "<strong>漏洞发现和修复是两拨人：</strong>报告交过来，修复还得自己研究。",
        "<strong>CI 里没有安全测试：</strong>漏洞总是上线后才被发现。",
    ],
    [
        "装 Docker 和任意支持的 LLM key，跑官网的一键安装脚本。",
        "设 <code>STRIX_LLM</code> 指定模型，<code>strix --target ./app-directory</code> 开扫。",
        "把扫描接进 CI，在合并前挡住漏洞。",
    ],
    [
        "<strong>它给 agent 配的是渗透测试员的完整工具带：</strong>拦截代理、浏览器利用、shell、PoC 沙箱，一样不少。",
        "<strong>和 SkillSpector、codex-security 放在一起看，安全这条线一周内出现了四种不同切法。</strong>",
        "<strong>「发现并修复」出现在同一句描述里，说明安全工具也在往闭环走。</strong>",
    ],
    ["security", "pentest", "agents", "ci", "docker"])

TOPIC = ("🔥 <strong>今日主题：技能开始有质检。</strong>"
         "NVIDIA 在技能生命周期的两端各放了一个工具：上周的 SkillSpector 查技能有没有洞，"
         "今天的 SkillEvaluator 用三层流水线评技能好不好，还能一条命令接进 CI，卡住每次技能改动。"
         "生产端同时放量：Claude-BugHunter 一个包塞 83 个红队技能、681 套公开漏洞报告模式，"
         "Google 放出 Stitch 技能库，ECC 号称 72 个 agent 和 327 个技能。"
         "接线层也冒出来了：ag-ui 定义 agent 与前端的交互协议，腾讯 LoopForge 用 SOP 编排 CodeBuddy、Codex 和 Claude Code 的交付。"
         "技能一多就得评，协议一多就得通，这是同一件事的两面。")

with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

prior = {}
for day in data["days"]:
    for p in day["projects"]:
        k = (p.get("owner"), p.get("name"))
        prior[k] = max(prior.get(k, 0), p.get("count") or 0)

P.sort(key=lambda p: -int(p["starsToday"].replace(",", "")))
for i, p in enumerate(P, 1):
    p["rank"] = i
    p["count"] = 1 + prior.get((p["owner"], p["name"]), 0)

new_day = {"date": TODAY, "label": "今天", "icon": "", "projects": P}

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

assert all(p.get("badge") in ("新面孔", "连登") for p in data["days"][0]["projects"])
assert len(data["days"]) == 98, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-44s +%-6s %8s★ count=%d" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
