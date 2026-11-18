#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-18（gap=1，双列日：新面孔 6 + 连登 6）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-18"

LANGCLASS = {
    "Python": "py", "TypeScript": "ts", "JavaScript": "js", "Shell": "sh",
    "Rust": "rs", "C": "c", "C++": "cpp", "HTML": "html", "CSS": "css",
    "Markdown": "md", "Go": "go", "C#": "cs", "Java": "java",
    "Kotlin": "kotlin", "Dart": "dart", "TeX": "tex", "Swift": "swift",
    "Zig": "zig", "Ruby": "rb",
}

P = []


def add(owner, name, lang, stars, forks, starsToday, badge, description,
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
        "badge": badge,
        "description": description,
        "problems": problems,
        "usage": usage,
        "insights": insights,
        "tags": tags,
    })


# ---------- 新面孔 ----------
add("google-research", "paper-orchestra", "Python", "3,894", "497", "1,529", "新面孔",
    "🔥 亮点 —— 今日 +1,529★，3,894★ 首登。Google Cloud AI Research 的多代理论文写作框架：把零散的想法和实验日志，变成可投稿的 LaTeX 稿，含文献综述和自动生成的图表。",
    [
        "<strong>写论文最耗时的不是实验：</strong>综述、行文、排版、画图，每样都吃掉几天。",
        "<strong>思路和素材是散的：</strong>实验日志、灵感、截图像扔进一个抽屉，写的时候整理不动。",
        "<strong>多代理框架各写各的：</strong>段落之间风格断裂，读起来像几个人拼的。",
    ],
    [
        "按 README 装依赖，准备想法和实验日志作为输入。",
        "框架自动拆成大纲、文献、章节、图表几个子任务分工。",
        "产出 LaTeX 稿，自行通读校对后再投稿。",
    ],
    [
        "<strong>论文写作被拆成流水线，是学术生产的信号：</strong>投稿量会涨，评审压力会更大。",
        "<strong>它做的是「有素材的整合」而非「凭空生成」：</strong>输入是实验日志，这决定了它没法替你造假。",
        "<strong>Google 研究团队自己开源工具，等于把审稿人未来要面对的东西先交给作者。</strong>",
    ],
    ["research", "papers", "multi-agent", "latex", "google"])

add("mvanhorn", "last30days-skill", "Python", "69,709", "6,226", "1,062", "新面孔",
    "🔥 亮点 —— +1,062★，6.97万★，第 4 次上榜。一个研究技能：跨 Reddit、X、YouTube、HN、Polymarket 和全网检索，再合成一份带来源的简报。",
    [
        "<strong>查资料靠人肉翻：</strong>Reddit、X、YouTube 各刷一遍，一天没了。",
        "<strong>结论没有来源：</strong>模型凭记忆答，说得像真的但对不上任何出处。",
        "<strong>没有互动信号：</strong>分不清哪些是热点、哪些只是有人写过。",
    ],
    [
        "把技能装进 agent，说一句「last30 某话题」就够了。",
        "它自行跑多源检索，按互动量排序，抓 YouTube 字幕。",
        "输出带引用的合成结论，缺 key 的源会明说而不是假装有。",
    ],
    [
        "<strong>它对缺数据的处理方式才是专业的地方：</strong>Reddit 没 key、X 没登录会直接写出来，而不是假装调查过。",
        "<strong>研究技能的价值在「承认不知道」：</strong>这恰好是模型自答最难做到的部分。",
        "<strong>1,062★ 的单日涨幅说明，做研究的 agent 已经被日常化了。</strong>",
    ],
    ["research", "skills", "synthesis", "sources", "agent"])

add("jingyaogong", "minimind", "Python", "66,439", "8,718", "772", "新面孔",
    "🔥 亮点 —— +772★，6.64万★，第 2 次上榜。中文圈最有名的「从零训模型」教程：两小时、单卡，从分词到对话训出一个 64M 参数的小模型。",
    [
        "<strong>训练 LLM 看起来像大厂专属：</strong>数据、算力、框架，门槛全在门口。",
        "<strong>教程只讲片段：</strong>预训练讲一套、微调讲另一套，串不起来。",
        "<strong>跑完不知道对不对：</strong>损失降了，但模型在说什么没人验证。",
    ],
    [
        "按 README 下数据，装好依赖。",
        "单卡跑预训练 + 微调，两小时左右出结果。",
        "用它自带的对话脚本试效果，再改超参对比。",
    ],
    [
        "<strong>两小时这个数字是关键设计：</strong>把一个不可企及的东西压进一顿午饭的时间，人才会真的动手。",
        "<strong>64M 参数不是为了好用，是为了看得懂：</strong>整个流程能在一台机器上读完。",
        "<strong>它和 nanochat 是同一个思路的两种语言版本：</strong>训练的门槛在降，理解的門槛才是真正的门槛。",
    ],
    ["llm-training", "education", "pytorch", "chinese", "from-scratch"])

add("p-e-w", "heretic", "Python", "41,891", "5,100", "620", "新面孔",
    "🔥 亮点 —— +620★，4.19万★，第 4 次上榜。免训练的语言模型改造工具：去掉审查、压制废话、降低谄媚，一个下午在你自己的机器上跑完。",
    [
        "<strong>对齐层写在输出里：</strong>拒答、套话、过度附和，用户要信息却收到姿态。",
        "<strong>微调门槛高：</strong>改行为要数据、算力、一整套管线。",
        "<strong>早期工具不稳：</strong>要么崩，要么把模型改傻。",
    ],
    [
        "<code>pip install -U heretic-ai</code>，装 PyTorch 2.6+。",
        "选一个本地模型，自动搜索抑制方向并做权重正交化，全程不训练。",
        "跑完导到 Hugging Face，社区已用同一流程发了上千个模型。",
    ],
    [
        "<strong>「免训练」让模型行为变成可编辑的：</strong>对齐不再是厂商独占的权力。",
        "<strong>它同时去掉审查和谄媚：</strong>说明这两件事在权重层是同一个方向。",
        "<strong>支持 MoE 和多模态，说明方法在往通用工具走，而不是某几个模型的补丁。</strong>",
    ],
    ["abliteration", "alignment", "local-llm", "fine-tuning", "open-weights"])

add("HKUDS", "CLI-Anything", "Python", "59,441", "5,396", "384", "新面孔",
    "🔥 亮点 —— +384★，5.94万★，第 7 次上榜。「今天的软件给人用，明天的用户是 agent」：给各种软件生成 CLI，让 agent 能操作它们，配一个 CLI-Hub 社区仓库。",
    [
        "<strong>软件都是给人设计的：</strong>GUI 里的按钮和菜单，agent 只能靠截图去猜。",
        "<strong>每家软件各写一套接口：</strong>想让 agent 用，就要一家一家接。",
        "<strong>调用没有可复现的轨迹：</strong>agent 这次点对了，下次不一定。",
    ],
    [
        "<code>pip install cli-anything-hub</code>，然后 <code>cli-hub install &lt;name&gt;</code> 装社区做好的 CLI。",
        "让 agent 用生成的 CLI 操作软件，配合预览和轨迹循环。",
        "想支持的软件可以去仓库提交 wishlist 或自己写一个 harness。",
    ],
    [
        "<strong>它赌的是「CLI 是 agent 最舒服的接口」：</strong>文本进文本出，比视觉操作稳得多。",
        "<strong>CLI-Hub 是这套思路的关键：</strong>没有社区供给，单个 CLI 只是玩具。",
        "<strong>第 7 次上榜说明这方向一直在被需要：</strong>让老软件接上新用户，是长期的活。",
    ],
    ["cli", "agents", "integration", "hub", "automation"])

add("ethanplusai", "sellbird", "Python", "6,433", "1,332", "358", "新面孔",
    "🔥 亮点 —— +358★，6,433★ 首登。跑在你自己 Claude 或 ChatGPT 订阅上的开源外呼平台：找公司、找决策人、验邮箱、写冷邮件、发出去、处理回信，默认没有你的批准什么都不发。",
    [
        "<strong>冷邮件工具按席位收费：</strong>小团队先用不起，见效了才敢加人。",
        "<strong>发出去就收不回：</strong>批量群发翻车一次，域名信誉没了。",
        "<strong>名单和话术靠猜：</strong>不知道对方是不是决策人，也不知道该说什么。",
    ],
    [
        "按 README 装到本地，接自己的模型订阅。",
        "让它按 ICP 找公司和决策人，验证邮箱后再起草。",
        "在 Outbox 里逐条批准，默认不批准不发送。",
    ],
    [
        "<strong>「默认不批准不发送」是这个产品最重要的设计：</strong>外呼的风险全在发送那一下。",
        "<strong>跑在用户自己的订阅上，等于把 SaaS 成本转成已有额度：</strong>这是 2026 年开源工具的标准打法。",
        "<strong>原名 Harvey，改名说明这类工具在被大模型厂商挤压时需要重新定位。</strong>",
    ],
    ["sales", "outbound", "automation", "local-first", "email"])

# ---------- 连登 ----------
add("elementalsouls", "Claude-BugHunter", "Python", "10,748", "1,480", "2,322", "连登",
    "🔥 亮点 —— 今日 +2,322★ 全场最高，1.07万★，连续第二天上榜，一天翻了一倍多。红队技能包：83 个技能、15 个斜杠命令、681 套公开漏洞报告模式。",
    [
        "<strong>红队工作依赖经验：</strong>同一个洞，老手三分钟看出来，新手翻一天文档。",
        "<strong>方法论散在博客和报告里：</strong>想查「这类漏洞别人怎么打的」，得自己搜。",
        "<strong>工具链割裂：</strong>Burp、命令行、浏览器、脚本各一套，中间靠手抄。",
    ],
    [
        "把技能目录放进 Claude Code 的 skills 路径。",
        "按 15 个斜杠命令选阶段：侦察、验证、利用、写报告。",
        "接上 Burp 的 MCP，让 agent 直接看请求和响应。",
    ],
    [
        "<strong>从 +1,007 到 +2,322，一天翻倍：</strong>安全团队在集中试用，这类工具的传播靠内部转介绍。",
        "<strong>681 套报告模式是另一种资产：</strong>可审计的案例库，比模型能力更难复制。",
        "<strong>它昨天还是新面孔，今天就成了连登组第一，说明红队的窗口刚打开。</strong>",
    ],
    ["security", "red-team", "skills", "claude-code", "pentest"])

add("affaan-m", "ECC", "JavaScript", "306,208", "45,081", "1,109", "连登",
    "🔥 亮点 —— +1,109★，30.6万★，第 15 次上榜，连续第二天。自称 agent harness 操作系统：计划、测试、实现、评审、验证、记住、改进，装一次就变成 agent 的工作方式。",
    [
        "<strong>每个 prompt 都在重建流程：</strong>今天让它先写测试，明天忘了。",
        "<strong>上下文塞满就忘事：</strong>前面定下的规则，后面自己违反。",
        "<strong>重复的成功没有沉淀：</strong>做对一次，下次还要重新教。",
    ],
    [
        "装成插件，按 harness 选路径（Claude Code 支持最好）。",
        "按 plan→test→implement→review→verify→remember 循环跑任务。",
        "重复有效的做法被固化成技能，下次直接调用。",
    ],
    [
        "<strong>连续两天上榜，日增 1,109：</strong>它不是靠新鲜感，是靠流程留人。",
        "<strong>「优化上下文窗口，其余全部持久化」是它全部设计的浓缩。</strong>",
        "<strong>30.6 万★ 里真正跑起来的人可能不到百分之一，但这不妨碍它成为共识符号。</strong>",
    ],
    ["methodology", "harness", "memory", "skills", "workflow"])

add("obra", "superpowers", "Shell", "319,806", "28,527", "823", "连登",
    "🔥 亮点 —— +823★，31.98万★，第 22 次上榜，连续第二天。给编码 agent 的开发方法论：先问清你要做什么再动手，支持 16 种 harness。",
    [
        "<strong>agent 一看到需求就写代码：</strong>写完才发现方向错了。",
        "<strong>长任务跑偏没人拦：</strong>发现时已经改了几十个文件。",
        "<strong>每家 CLI 各写一遍流程。</strong>",
    ],
    [
        "按 README 选自己用的 harness 安装。",
        "从一个技能开始用，不必全装。",
        "出问题按 When Something Goes Wrong 排查。",
    ],
    [
        "<strong>22 次上榜，已经是一种基础设施级别的位置。</strong>",
        "<strong>它和 ECC 同天连登，说明「方法论」这一层被两个不同流派同时验证。</strong>",
        "<strong>「先问再写」还没有被模型厂商内置，这是它还能站着的原因。</strong>",
    ],
    ["methodology", "skills", "coding-agent", "workflow", "shell"])

add("google-labs-code", "stitch-skills", "TypeScript", "10,310", "1,361", "369", "连登",
    "🔥 亮点 —— +369★，1.03万★，连续第二天上榜。Google Stitch 的技能库，遵循 Agent Skills 开放标准，六种以上 agent 都能装。",
    [
        "<strong>生成的界面接不进真实工程。</strong>",
        "<strong>各家设计工具各一套操作。</strong>",
        "<strong>agent 不知道设计规范。</strong>",
    ],
    [
        "Codex 里加 marketplace 再装插件，或用 CLI 走 sparse 安装。",
        "装 stitch-design 和 stitch-build 两组插件。",
        "用 Stitch MCP server 把设计和代码串起来。",
    ],
    [
        "<strong>第二天继续涨，说明它不是一次发布带来的曝光，而是持续被安装。</strong>",
        "<strong>遵循开放标准是缺标准的厂商唯一的扩张方式。</strong>",
        "<strong>设计到代码这段的竞争点，已经从「生成得像」变成「接得进」。</strong>",
    ],
    ["design", "skills", "google", "frontend", "mcp"])

add("kajisho5", "ffmpeg-skill", "Python", "7,950", "739", "349", "连登",
    "🔥 亮点 —— +349★，7,950★，连续第二天上榜。给编码 agent 的本地视频编辑器：42 个 FFmpeg 工具，每个都有机器可读的输入输出契约。",
    [
        "<strong>拼 ffmpeg 命令容易静默失败。</strong>",
        "<strong>云剪辑 API 要上传素材。</strong>",
        "<strong>剪完没有验收环节。</strong>",
    ],
    [
        "装 skill 或 npm 包，也可以走 MCP。",
        "让 agent 从 42 个工具里选动作、给参数、跑一遍。",
        "跑完检查输出契约，确认时长、编码、音轨都对。",
    ],
    [
        "<strong>连续两天在榜，两天共涨约 3,900★：</strong>视频是 agent 最想接又最难接的活。",
        "<strong>「机器可读契约」比工具数量重要：</strong>能不能验证才对。",
        "<strong>它把可运行性放在功能之前：</strong>不联网、只用标准库。",
    ],
    ["video", "ffmpeg", "skills", "mcp", "local"])

add("NVIDIA", "SkillEvaluator", "Python", "3,539", "495", "323", "连登",
    "🔥 亮点 —— +323★，3,539★，连续第二天上榜。技能的质检流水线：三层分别回答「安不安全、合不合规、好不好用」，一条命令接进 CI。",
    [
        "<strong>技能多了没法比：</strong>同样功能的十个技能，谁更好全靠自己试。",
        "<strong>合不合规没人验：</strong>跑崩了才知道。",
        "<strong>改动没有回归测试：</strong>改一行提示词，行为可能全变。",
    ],
    [
        "<code>skillevaluator tier1 ./my-skill --no-llm</code> 先跑静态校验。",
        "配好模型后跑三层完整评估，拿到质量分和报告。",
        "<code>skillevaluator ci init</code> 生成 CI 模板，每次改动都过一遍。",
    ],
    [
        "<strong>连续两天在榜，和 BugHunter 的暴涨形成对照：</strong>一个在攻，一个在守，同时被需要。",
        "<strong>把质检做成 CI 模板，等于把技能当代码管：</strong>这是这个生态成熟的标志。",
        "<strong>静态层不需要模型就能挡掉低级问题，成本设计得很清醒。</strong>",
    ],
    ["skills", "evaluation", "quality", "ci", "nvidia"])

TOPIC = ("🔥 <strong>今日主题：连登的比新来的更猛。</strong>"
         "Claude-BugHunter 昨天 +1,007，今天 +2,322，一天翻倍。"
         "连登的六席被同一个方向占满：红队技能包、技能质检、两条方法论、Google 的设计技能、视频技能——都在给 agent 加纪律。"
         "新面孔是另一端：PaperOrchestra 一天 +1,529★ 写论文，last30days 把研究做成技能，MiniMind 两小时训一个小模型，"
         "CLI-Anything 想让所有老软件变成 agent 能操作的命令行。"
         "一边在守（审查、质检、红队），一边在攻（自动研究、自动写作、自动外呼），"
         "中间那层是接口：谁把软件变成 agent 能用的形状，谁就决定 agent 能走多远。")

with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

prior = {}
for day in data["days"]:
    for p in day["projects"]:
        k = (p.get("owner"), p.get("name"))
        prior[k] = max(prior.get(k, 0), p.get("count") or 0)

new = [p for p in P if p["badge"] == "新面孔"]
strk = [p for p in P if p["badge"] == "连登"]
new.sort(key=lambda p: -int(p["starsToday"].replace(",", "")))
strk.sort(key=lambda p: -int(p["starsToday"].replace(",", "")))
assert len(new) <= 6 and len(strk) <= 6, (len(new), len(strk))
ordered = new + strk
for i, p in enumerate(ordered, 1):
    p["rank"] = i
    p["count"] = 1 + prior.get((p["owner"], p["name"]), 0)

new_day = {"date": TODAY, "label": "今天", "icon": "", "projects": ordered}

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
assert len(data["days"]) == 99, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目（新面孔 %d / 连登 %d），总天数 %d" % (
    TODAY, len(ordered), len(new), len(strk), len(data["days"])))
for p in ordered:
    print("  %2d. [%s] %-40s +%-6s %8s★ count=%d" % (
        p["rank"], p["badge"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
