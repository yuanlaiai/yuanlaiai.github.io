#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-13（距上次更新 6 天，flat day：全部新面孔）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-13"

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


add("GoogleChrome", "modern-web-guidance-src", "TypeScript", "4,220", "246", "1,875",
    "🔥 亮点 —— 今日 +1,875★ 第一，4,220★ 首登。Chrome、Edge、Firefox、MDN 四家团队共同维护的网页最佳实践技能集：把平台知识和浏览器兼容性数据塞进编码 agent，让它别再写过时写法。",
    [
        "<strong>agent 的网页知识停在训练截止日：</strong>新 API 它不知道，旧写法它很熟。",
        "<strong>兼容性没人查：</strong>写进代码的属性只在最新版浏览器能用，上线后才发现。",
        "<strong>过时代码到处复制：</strong>一个仓库里的老写法被 agent 学去，扩散到下一个项目。",
    ],
    [
        "<code>npx modern-web-guidance@latest install</code>，走交互向导选择要装的技能。",
        "<code>npx modern-web-guidance@latest search \"animate a dialog modal backdrop\"</code> 检索相关指南。",
        "<code>npx modern-web-guidance@latest legacy-scan .</code> 扫出仓库里的过时模式再改。",
    ],
    [
        "<strong>四家浏览器团队联合维护：</strong>「教 agent 写现代网页」这件事，厂商自己不出手就没人能保证准确。",
        "<strong>源码仓库和发布仓库分开：</strong>内容要像产品一样校准、评测、治理，说明技能也开始有质量和版本管理的诉求。",
        "<strong>技能在这一层变成兼容性数据的载体：</strong>它的价值不在提示词写得好，在于背后那份数据谁在维护。",
    ],
    ["web", "skills", "browser-compat", "chrome", "best-practices"])

add("Alishahryar1", "free-claude-code", "Python", "69,714", "10,808", "895",
    "🔥 亮点 —— +895★，6.97万★ 首登。一个路由层，把 12 个 harness（Claude Code、Codex、Pi、OpenCode 等）接到任意 provider 的模型上，AGPL 授权，作者明确声明与 Anthropic 无关。",
    [
        "<strong>各家 CLI 锁死自家模型：</strong>想换模型就得换工具，工作流全重学。",
        "<strong>订阅额度用完就得停：</strong>换个 provider 续上，但 harness 不认。",
        "<strong>多套配置各写一遍：</strong>团队里有人用 Claude Code，有人用 Codex，模型和 key 各管各的。",
    ],
    [
        "用 uv 装上，选一个 provider 配好 key。",
        "把客户端指向本地路由，12 个 harness 都能走。",
        "按需开启可选集成，用它自带的管理命令维护安装。",
    ],
    [
        "<strong>名字借的是别人的品牌，做的事是把品牌拆开：</strong>它存在的意义就是让 harness 和模型解绑。",
        "<strong>AGPL 说明作者预期会被商用集成：</strong>改过的版本必须开源，这是他给自己留的护栏。",
        "<strong>这类路由层一多，绑定就成了纸面上的商业模式：</strong>用户随时能把工具换个模型继续用。",
    ],
    ["router", "claude-code", "multi-provider", "harness", "agpl"])

add("openai", "codex-security", "TypeScript", "12,836", "1,007", "754",
    "🔥 亮点 —— +754★，1.28万★ 首登。OpenAI 的 Codex 安全工具：扫仓库或 git 变更、验证候选漏洞、生成补丁、复核已有修复，还能起草 SECURITY.md 和威胁模型。",
    [
        "<strong>漏洞报告误报成堆：</strong>找十个九个是假的，工程师干脆不看。",
        "<strong>修完不知道有没有真修好：</strong>补丁合进去，漏洞可能换个形式还在。",
        "<strong>威胁模型没人写：</strong>安全评审要的文档，一直是靠事后补。",
    ],
    [
        "<code>@openai/codex-security</code> 的 CLI 直接扫仓库、指定路径或 git 变更。",
        "在 Codex 里选安全 workflow，或接 TypeScript SDK、GitHub Action 做自动化。",
        "对候选漏洞先验证再出补丁，最后复核修复结果，按自己的 rubric 定级。",
    ],
    [
        "<strong>「验证候选」和「复核修复」分成两步，是安全工具和代码补全的分界线。</strong>",
        "<strong>OpenAI 自己做安全工具，等于承认 agent 写的代码需要配套的检查：</strong>生成和验收必须成对出现。",
        "<strong>按自家 rubric 定级：</strong>它在给企业一套能写进流程的口径，这比多扫出几个洞更有用。",
    ],
    ["security", "codex", "sast", "openai", "cli"])

add("NVIDIA", "SkillSpector", "Python", "25,786", "2,284", "297",
    "🔥 亮点 —— +297★，2.58万★ 首登。装技能之前先扫一遍的安全扫描器。NVIDIA 在 31,132 个技能样本里发现 26.1% 存在漏洞、5.2% 疑似恶意意图。",
    [
        "<strong>技能以隐式信任执行：</strong>装上就能读文件、发网络请求、跑 shell，几乎没人审。",
        "<strong>来源无法判断：</strong>一个 SKILL.md 加几个脚本，看不出作者想干什么。",
        "<strong>装错一次代价很大：</strong>agent 拿着你的凭据跑别人写的指令。",
    ],
    [
        "pip 装好后对技能目录跑扫描。",
        "报告分漏洞、恶意模式、安全风险三类，用来判断「这个技能能不能装」。",
        "接入 NVIDIA Verified Skills 流水线，在发布前扫描、评估、签名。",
    ],
    [
        "<strong>26.1% 这个数字比任何提醒都有效：</strong>技能生态默认的信任假设已经破产。",
        "<strong>扫描之后还要签名：</strong>NVIDIA 想当技能的证书颁发机构，这条路和软件供应链的包签名是同一套逻辑。",
        "<strong>以后「谁验过这个技能」会和「这个包有没有 CVE」一样，成为安装前的必查项。</strong>",
    ],
    ["security", "skills", "scanner", "supply-chain", "nvidia"])

add("ZhuLinsen", "daily_stock_analysis", "Python", "71,275", "57,218", "272",
    "🔥 亮点 —— +272★，7.13万★，第 4 次上榜。LLM 驱动的多市场股票分析系统：多源行情、实时新闻、决策看板，结果推到企业微信、飞书、Telegram、Discord、Slack 或邮箱。",
    [
        "<strong>盯盘和复盘靠人：</strong>盘后想回顾当天逻辑，只能凭记忆。",
        "<strong>行情和新闻散在多个源：</strong>拼一遍半小时，还容易漏。",
        "<strong>自建推送要写一堆胶水：</strong>定时、格式化、发到 IM，每样都要自己接。",
    ],
    [
        "用 Docker 或 GitHub Actions 部署，后者零成本定时跑。",
        "配好数据源和推送渠道，收盘后自动分析。",
        "看板看当日结论，IM 里直接收推送，不用另外开页面。",
    ],
    [
        "<strong>「零成本定时运行」是它能被持续用起来的关键：</strong>分析再好，每天手动跑一次就没人用。",
        "<strong>带 arXiv 编号说明作者想把工程做成可引用的方法：</strong>这类项目开始往研究靠，是为了建立可信度。",
        "<strong>推送渠道全选国内 IM，用户画像很清楚：</strong>它不打算做全球产品，先服务好自己的场景。",
    ],
    ["finance", "stock", "llm", "automation", "china"])

add("kajisho5", "ffmpeg-skill", "Python", "5,373", "463", "224",
    "🔥 亮点 —— +224★，5,373★ 首登。给编码 agent 一个本地视频编辑器：42 个 FFmpeg 工具，每个都有机器可读的输入输出契约，agent 剪完还会自己验一遍成片。",
    [
        "<strong>agent 剪视频靠拼 ffmpeg 命令：</strong>参数错一个，静默失败，输出文件是坏的也不报错。",
        "<strong>云剪辑 API 有成本和隐私问题：</strong>素材要上传，按次计费。",
        "<strong>剪完不知道对不对：</strong>没有校验环节，错的东西直接交付。",
    ],
    [
        "装 skill 或 npm 包，也可以走 MCP 接进客户端。",
        "让 agent 从 42 个工具里选动作、给参数、跑一遍。",
        "跑完检查输出契约，确认时长、编码、音轨都符合预期再交付。",
    ],
    [
        "<strong>真正的设计是「机器可读契约 + 自检」，不是命令本身：</strong>命令谁都会写，能验证结果才是工程化。",
        "<strong>不联网、不要 API key、只用 Python 标准库：</strong>它要求在任何机器上无摩擦跑起来。",
        "<strong>把视频这种重活拆成 42 个可调用动作，agent 才接得住：</strong>颗粒度决定了模型能不能用对。",
    ],
    ["video", "ffmpeg", "skills", "mcp", "local"])

add("alibaba", "open-code-review", "Go", "50,209", "3,727", "206",
    "🔥 亮点 —— +206★，5.02万★，第 5 次上榜。阿里开源的代码评审工具：确定性工程加 agent 的混合架构，选文件、分组这类不能出错的步骤交给代码保证，语言模型只负责判断。",
    [
        "<strong>纯 prompt 评审结果不稳定：</strong>换个措辞，结论就变了。",
        "<strong>重要改动被漏掉：</strong>模型挑文件靠感觉，大改动的核心文件反而没看。",
        "<strong>评审意见落不了地：</strong>说得挺好，改起来无从下手。",
    ],
    [
        "按文档部署，接进自己的仓库。",
        "把它放进 PR 流程，让每次提交都过一遍。",
        "用它内置的文件选择和分组逻辑控制评审范围，模型只在选定范围内判断。",
    ],
    [
        "<strong>它明确承认纯语言驱动的评审不可靠，这是诚实的设计判断：</strong>能出错的步骤不该交给模型。",
        "<strong>「不能错的部分写成代码」是 agent 工程化的通用解法：</strong>这套思路正在从评审扩散到测试、发布。",
        "<strong>阿里开源内部工具，抢的是企业评审流程的默认选项：</strong>规模背书比功能列表更能说服大客户。",
    ],
    ["code-review", "alibaba", "hybrid", "go", "ci"])

add("ahujasid", "mcp-for-blender", "Python", "34,277", "3,117", "140",
    "🔥 亮点 —— +140★，3.43万★ 首登。把 Blender 接进任意 LLM 的 MCP 插件（原 blender-mcp）：用提示词做建模、搭场景、改对象。",
    [
        "<strong>3D 软件学习曲线陡：</strong>建模、材质、灯光各一套操作，脚本 API 更绕。",
        "<strong>模型不懂场景里的实际对象：</strong>说「把那个桌子加高」，它不知道哪个是桌子。",
        "<strong>做原型先得学会工具：</strong>想法到原型之间隔着一整套软件。",
    ],
    [
        "装 PyPI 包（已改名 mcp-for-blender），旧的 blender-mcp 配置不用动。",
        "在 Blender 里启用 MCP 服务。",
        "把支持 MCP 的客户端连上去，用自然语言改场景。",
    ],
    [
        "<strong>改名说明它想摆脱「某个模型专用」的印象：</strong>MCP 让插件变成通用接口，不再绑一家。",
        "<strong>3D 是最难被纯文本吃下的领域：</strong>能做起来靠的是把操作映射成 API 调用，而不是让模型理解几何。",
        "<strong>第三方集成在这个生态里已是常态：</strong>官方软件的 AI 能力，往往先由社区补上。",
    ],
    ["blender", "mcp", "3d", "llm", "plugin"])

add("anthropics", "claude-plugins-official", "Python", "47,110", "4,888", "134",
    "🔥 亮点 —— +134★，4.71万★ 首登。Anthropic 自己的插件仓库和官方 Claude Code 插件市场。现在第三方插件统一从 claude.ai 目录提交，原仓库里的 marketplace.json 正在收回给自家插件用。",
    [
        "<strong>插件来源杂：</strong>装之前不知道谁在维护、更新频率如何。",
        "<strong>市场分散在多个仓库：</strong>用户找插件要先搞清楚哪个才是官方的。",
        "<strong>质量没有统一门槛：</strong>同样的功能，几个版本互相打架。",
    ],
    [
        "第三方插件去 claude.ai/directory/manage 提交，会被分发到各 Claude 产品。",
        "官方插件直接从本仓库装。",
        "README 明确提示：先确认信任，再安装、更新或使用。",
    ],
    [
        "<strong>把分发口收到自己站上，是平台化的标准动作：</strong>git 仓库退回成「自家插件的家」。",
        "<strong>官方提示「先确认信任再装」，和 SkillSpector 的扫描出现在同一周：</strong>安全议题已经从边缘走到台面。",
        "<strong>插件目录一旦集中，排序就成了新的分发权力：</strong>这和当年应用商店的逻辑一模一样。",
    ],
    ["plugins", "anthropic", "marketplace", "claude-code", "distribution"])

add("headroomlabs-ai", "headroom", "Python", "79,537", "6,226", "125",
    "🔥 亮点 —— +125★，7.95万★ 首登。agent 的上下文压缩层：一个 55,957 token 的提示压到 24,340 token 再发给模型，而第 67 条里那行 FATAL 原样保留。",
    [
        "<strong>工具输出和日志把上下文塞爆：</strong>真正有用的几行淹没在几万行里。",
        "<strong>压缩总会丢关键行：</strong>摘要一压，报错信息没了。",
        "<strong>RAG 召回块太长：</strong>挤掉问题本身，模型开始答跑偏。",
    ],
    [
        "接进 agent 管道的中间层，压缩工具输出、日志、文件和 RAG 块。",
        "按内容类型选策略：日志重结构，文档重语义。",
        "用关键行保留做校验，确认压完还读得懂。",
    ],
    [
        "<strong>它拿「FATAL 那行有没有活下来」当卖点：</strong>压缩的评价标准应该是保真，不是压缩率。",
        "<strong>上下文压缩正在变成独立的基础设施层：</strong>和记忆、检索分开做，说明分工已经开始。",
        "<strong>一个压缩库的星数超过多数模型工具：</strong>token 成本是最真实、最普遍的痛点。",
    ],
    ["context", "compression", "tokens", "infra", "logs"])

add("volcengine", "OpenViking", "Python", "42,171", "3,477", "111",
    "🔥 亮点 —— +111★，4.22万★ 首登。火山引擎的 agent 上下文数据库：把记忆、知识 RAG、会话状态统一到一个库里，主打自我演化。",
    [
        "<strong>记忆、知识库、会话状态各存一处：</strong>检索时要拼，拼错了就答错。",
        "<strong>RAG 只解决「查到」，不解决「记住」：</strong>同一件事问两次，答案不一致。",
        "<strong>换框架就迁一次数据：</strong>记忆没法带走，等于被工具锁住。",
    ],
    [
        "按文档部署服务，接官方 SDK。",
        "把 agent 的记忆和知识都写进同一个库，用统一接口检索。",
        "用 studio 做可视化调试，看上下文里到底存了什么。",
    ],
    [
        "<strong>「上下文数据库」这个品类是今年才定型的：</strong>大家在把 prompt 工程改造成数据工程。",
        "<strong>火山引擎做这件事，是想在模型之外握住数据这一层：</strong>模型会换，数据不会。",
        "<strong>「自我演化」这种说法要看实现，别被词带走：</strong>能验证的是检索命中率和一致性，不是形容词。",
    ],
    ["context", "database", "memory", "rag", "volcengine"])

add("backnotprop", "plannotator", "TypeScript", "10,277", "779", "100",
    "🔥 亮点 —— +100★，1.03万★ 首登。给 agent 做的批注工作台：在计划、规格、markdown、HTML 和 diff 上标注，反馈直接回到 agent，支持 Amp、Claude Code、Codex、Copilot。",
    [
        "<strong>方案只能整段接受或整段打回：</strong>想改其中一行，只能重新描述一遍需求。",
        "<strong>评审记录散在聊天里：</strong>三天后想找回当时的判断，翻不到。",
        "<strong>让人读长输出很累：</strong>一段几千字的计划，注意力撑不到最后。",
    ],
    [
        "装好后用 <code>/plannotator-annotate</code> 打开文件、目录或网址。",
        "在 inbox 里收待审的工件，批注完把反馈一次性发回 agent。",
        "Codex 上换成 <code>!plannotator review</code> 或对应的技能命令。",
    ],
    [
        "<strong>它解决的是「人怎么给 agent 提意见」，这比生成能力更影响日常效率。</strong>",
        "<strong>标注是比对话更精确的输入形式：</strong>指到具体一行，比形容词管用。",
        "<strong>支持多家 harness，说明这一层也在去绑定：</strong>人机协作界面不该属于某一家 agent。",
    ],
    ["review", "annotation", "human-in-the-loop", "agents", "tui"])

add("block", "buzz", "Rust", "37,170", "4,929", "95",
    "🔥 亮点 —— +95★，3.72万★，第 2 次上榜。Block 的人机协作工作区：人在频道里，agent 也在频道里，一起建东西，中继服务器自己拥有。1.0 已迁到 block/buzz-app。",
    [
        "<strong>agent 的产出散在个人会话里：</strong>团队看不见，也没法接手下一个人继续。",
        "<strong>协作平台不给 agent 留位置：</strong>agent 只能当个机器人挂件。",
        "<strong>工作流都跑在别人的服务器上：</strong>对合规敏感的公司不敢用。",
    ],
    [
        "按文档自托管中继，数据留在自己机器上。",
        "建频道把人拉进来，再把 agent 作为成员接进同一个频道。",
        "需要插件扩展就上 1.0 版本，注意它标注插件 API 还是预览状态。",
    ],
    [
        "<strong>把 agent 当频道成员而不是工具，是组织层面的变化：</strong>它有了身份、可见性和交接。",
        "<strong>自托管中继说明它瞄准的是不愿把工作流放上公有云的公司。</strong>",
        "<strong>两次上榜但热度都不高：</strong>这个方向还没到爆发点，卡在「团队真的会把 agent 当同事吗」。",
    ],
    ["collaboration", "agents", "self-hosted", "workspace", "rust"])

TOPIC = ("🔥 <strong>今日主题：技能成了攻击面。</strong>"
         "OpenAI 的 codex-security 扫代码漏洞，NVIDIA 的 SkillSpector 专扫技能本身——"
         "在一个 31,132 个技能的样本里，26.1% 有漏洞、5.2% 疑似恶意意图。"
         "同一天 Anthropic 把插件目录收进官方入口并提示「确认信任再装」，"
         "Chrome、Edge、Firefox、MDN 四家联合维护一套网页最佳实践技能。"
         "技能从个人技巧变成了要扫描、要签名、要走审核的软件包，这条产业链今天第一次完整出现在榜上。"
         "剩下的一半榜单也在做同一件事：给 agent 加约束——阿里用工程逻辑兜住评审，"
         "headroom 压上下文但保住 FATAL 那行，plannotator 让人逐行批注。"
         "生成能力没人再争，都在争验收。")

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
assert len(data["days"]) == 97, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-44s +%-6s %8s★ count=%d" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
