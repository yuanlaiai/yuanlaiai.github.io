#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-27 榜单更新（gap=3 平铺日：全部新面孔，13 条）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-27"

LANGCLASS = {
    "Python": "py", "TypeScript": "ts", "JavaScript": "js", "Shell": "sh",
    "Rust": "rs", "C": "c", "C++": "cpp", "HTML": "html", "CSS": "css",
    "Markdown": "md", "Go": "go", "C#": "cs", "Java": "java",
    "Kotlin": "kotlin", "Dart": "dart", "TeX": "tex", "Swift": "swift",
    "Zig": "zig",
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


# ---- 顺序即 rank：按 starsToday 降序 ----
add("elementalsouls", "Claude-BugHunter", "Python", "25,492", "2,604", "1,615",
    "🔥 当天最高 +1,615★ —— 2.5 万★，第 7 次上榜。85 个技能、16 个斜杠命令、681 份披露报告拆成四层：先想、再打 Web、再打边界、最后交付。",
    ["<strong>挖洞知识不成体系：</strong>方法、payload、绕过表散在博客和笔记里，实战时凑不齐一条完整链路。",
     "<strong>边界资产最难打：</strong>M365/Entra、Okta、vCenter、SSL-VPN 这些企业外围，公开资料只到 CVE 编号。",
     "<strong>写到报告就散架：</strong>严重性评级、OOS 反驳、PII 脱敏，每份报告都在重新发明流程。"],
    ["把 skills 目录放进 Claude Code 技能路径，重启后按话题自动触发对应技能。",
     "打 Web 应用时用 58 个 hunt-* 技能里的检测模式、payload 与链式模板，别再手搓字典。",
     "收尾走 triage-validation 的七问门禁与 VRT 评级，报告与证据脱敏一步到位。"],
    ["<strong>判断：</strong>四层结构（think / hunt / perimeter / ship）比技能数量更值钱，它把一次红队作业的完整流程框住了。",
     "<strong>判断：</strong>681 份报告里挑出 58 个类别的检测模式，这是把公开情报变成可执行动作的少数成功案例。",
     "<strong>判断：</strong>README 反复强调 stay in scope。工具越强，越需要把授权边界写进流程，否则第一批受害者会是使用者自己。"],
    ["security", "red-team", "claude-skills", "bug-bounty", "pentest"])

add("obra", "superpowers", "Shell", "328,002", "29,132", "916",
    "🔥 第 27 次上榜 —— +916★，32.8 万★。给编码 agent 装一套开发方法论：先问清要什么，再把规格拆成能读完的小块，然后才写代码。",
    ["<strong>一看到需求就开写：</strong>方向错了才发现，返工比从零做还贵。",
     "<strong>规格没人读完：</strong>几十页文档躺在仓库里，执行时无人对照。",
     "<strong>换个客户端就重教：</strong>Claude Code、Codex、Cursor 各有一套工作流，团队里三种习惯并存。"],
    ["按 README 的安装段挑客户端，十几家（含 Hermes Agent）都有对应命令。",
     "启动后它会追问真实目标，并把 spec 分块推给你确认。",
     "走偏时按 When Something Goes Wrong 一节的回退流程重来，不要在错的路上继续堆 prompt。"],
    ["<strong>判断：</strong>27 次上榜靠的不是新鲜度而是装机量，跨十几个客户端的安装表本身就是分发策略。",
     "<strong>判断：</strong>它卖的是纪律：把先想清楚再动手固化进流程，比升级模型便宜得多。",
     "<strong>判断：</strong>方法论类项目能长期霸榜，说明工具层已饱和，稀缺的是知道什么时候该让 agent 停下来问。"],
    ["agent", "methodology", "claude-code", "workflow", "skills"])

add("firecrawl", "firecrawl", "TypeScript", "211,383", "11,103", "833",
    "🔥 抓网页给 agent 吃 —— +833★，21.1 万★，第 5 次上榜。搜索、抓取、接 550+ 数据源走同一个 API，吐出来直接是干净 Markdown。",
    ["<strong>爬虫写完就失效：</strong>反爬一改解析全崩，维护像打地鼠。",
     "<strong>噪声吃掉上下文：</strong>抓下来一半是导航和广告，token 花在没用的地方。",
     "<strong>十套解析并行：</strong>搜索、网页、结构化站点各接各的，最后没人敢动。"],
    ["用官方 SDK 或 /scrape、/crawl 端点，一次调用拿到 markdown。",
     "不想托管就自部署开源版，跑在自己的机器上。",
     "配 /search 或数据源接口做检索增强，别把抓取和检索拆成两条线。"],
    ["<strong>判断：</strong>21 万★ 的爬虫项目，护城河在清洗加结构化，以及 550 个数据源的接入量。",
     "<strong>判断：</strong>开源版能自部署，托管服务才是收入来源。用之前先想清楚数据允不允许出门。",
     "<strong>判断：</strong>agent 的瓶颈正从模型不够聪明转向上下文太脏，这类基建继续吃红利。"],
    ["scraping", "rag", "api", "markdown", "data"])

add("zhouxiaoka", "autoclip", "Python", "17,400", "2,451", "733",
    "🔥 开源版 OpusClip —— +733★，1.74 万★，第 6 次上榜。v1.6 新增 6 种直播回放源，OBS 录完自动排队出片，还带 MCP server。",
    ["<strong>直播录完还得熬夜剪：</strong>两小时回放挑高光、裁切、配字幕，人工一晚上就没了。",
     "<strong>云端工具按月收费：</strong>素材上传队列排到明天，订阅费和隐私一起交代出去。",
     "<strong>一套素材要发五六个平台：</strong>比例、封面、标题每样重做一遍。"],
    ["从 releases 下桌面版，拖入链接、本地文件或 OBS/Twitch/YouTube/Kick/Discord 回放。",
     "接 OBS WebSocket（4455），下播后用 <pre><code>-c copy</code></pre> 无损切片并自动排队。",
     "接 MCP server 让 agent 触发剪辑，或用 Ollama/LM Studio + Whisper/SenseVoice 全离线跑。"],
    ["<strong>判断：</strong>直播场景是这类工具真正的现金牛：一场直播产生几十条候选片段，人工根本筛不过来。",
     "<strong>判断：</strong>MCP server 这个加法比多支持一个平台更关键，它把剪辑变成 agent 可调用的动作。",
     "<strong>判断：</strong>13 种语言界面，加上本地优先的主张，目标用户从一开始就是海外创作者。"],
    ["video", "clipping", "local-first", "mcp", "creator"])

add("cathrynlavery", "diagram-design", "HTML", "74,257", "4,993", "731",
    "🔥 让 agent 画好看的图 —— +731★，7.4 万★，第 10 次上榜。52 种图型，输出一个自包含的 HTML+SVG 文件，能抓你网站的配色和字体。",
    ["<strong>Mermaid 生成的图一眼假：</strong>阴影、圆角、字体全一样，放进方案书里掉档次。",
     "<strong>品牌一致性靠人盯：</strong>每张图都要手动改配色，改完十张已经不是一个风格。",
     "<strong>改图要回工具里：</strong>代理生成的图想微调，得重新描述一遍。"],
    ["<pre><code>npx skills add cathrynlavery/diagram-design</code></pre> 装进任意支持 Agent Skills 的客户端。",
     "直接用中文描述：给我一张前后端加 Redis 的架构图，或者 Q2 项目的影响/成本四象限。",
     "一句 onboard 到你的站点，它会把配色和字体拉下来，之后所有图同风格；也能从 drawio/mermaid/excalidraw/plantuml 导入。"],
    ["<strong>判断：</strong>「No shadows. No Mermaid slop.」这句挑衅写进了产品定位：图的审美是可交付物的一部分。",
     "<strong>判断：</strong>单文件 HTML+SVG 是个聪明选择，双击就能看，发微信、贴 Notion、进 PPT 都不用导出。",
     "<strong>判断：</strong>技能类项目反复上榜，说明真需求不在模型，在产出物的最后一公里。"],
    ["diagram", "agent-skills", "svg", "branding", "design"])

add("HKUDS", "CLI-Anything", "Python", "66,753", "6,106", "668",
    "🔥 给所有软件套一层 CLI 让 agent 能用 —— +668★，6.7 万★，第 12 次上榜。18 个真实应用 demo、2,461 个测试通过，cli-hub install 一键装别人的 harness。",
    ["<strong>GUI 软件没有 API：</strong>agent 只能截图点鼠标，慢且脆，改个版就失效。",
     "<strong>适配层写一次用一次：</strong>每个软件单独包装，写完没人复用。",
     "<strong>输出格式不统一：</strong>agent 解析全靠猜，换个软件就得改 prompt。"],
    ["<pre><code>pip install cli-anything-hub</code></pre>",
     "<pre><code>cli-hub install &lt;name&gt;</code></pre> 浏览并安装社区建好的 CLI。",
     "自建 harness 后提 PR，hub 立即更新。"],
    ["<strong>判断：</strong>12 次上榜说明「给软件装手脚」是长期需求，不是一时热度。",
     "<strong>判断：</strong>2,461 个测试与 18 个 demo 让产出可验证（CAD、3D 场景、字幕），这比 prompt 包装项目高一个层级。",
     "<strong>判断：</strong>中心化 hub 加社区 PR，抢的是 agent 与软件之间的标准接口，这个位置比单个工具值钱。"],
    ["cli", "agent", "harness", "automation", "agent-native"])

add("jingyaogong", "minimind", "Python", "72,074", "9,389", "667",
    "🔥 3 块钱 2 小时训出 64M 小模型 —— +667★，7.2 万★，第 6 次上榜。预训练到 RLHF、Agentic RL、蒸馏整条链路全开源，单卡可复现。",
    ["<strong>教程停在调 API：</strong>想从零训一个模型，找不到完整可跑的代码。",
     "<strong>论文与实现差一截：</strong>数据清洗、超参、训练细节，论文里不写全。",
     "<strong>RLHF 无处下手：</strong>PPO、DPO、GRPO 讲得多，能跑起来的项目少。"],
    ["<pre><code>git clone https://github.com/jingyaogong/minimind</code></pre> 后按 README 装依赖。",
     "下载数据集，按 Pretrain、SFT、LoRA/DPO、RLAIF 顺序跑各阶段脚本。",
     "同仓库还有 -V 视觉版、-O 多模态版、-dLM 扩散语言模型可参考。"],
    ["<strong>判断：</strong>主线模型约是 GPT-3 的 1/2700，价值不在能力，在每一环都能自己搓一遍。",
     "<strong>判断：</strong>覆盖 MoE、数据清洗、RLAIF（PPO/GRPO/CISPO）、Tool Use、Agentic RL，覆盖面比多数付费课程完整。",
     "<strong>判断：</strong>中文文档加单卡成本，是它反复上榜的原因：教学类项目复访率天然高于工具类。"],
    ["llm", "from-scratch", "training", "rl", "tutorial"])

add("mvanhorn", "last30days-skill", "Python", "76,155", "6,749", "664",
    "🔥 用投票和真金白银排序的搜索 —— +664★，7.6 万★，第 7 次上榜。Reddit、HN、Polymarket、GitHub 开箱即用，专利和招聘页也能查。",
    ["<strong>搜索引擎被 SEO 洗了：</strong>搜一个话题，前十条是内容农场。",
     "<strong>多平台要开一堆标签页：</strong>Reddit 一个界面、HN 一个、X 又一个，最后自己汇总。",
     "<strong>时效性无法控制：</strong>想要最近 30 天，只能一条条看日期。"],
    ["Claude Code：<pre><code>/plugin marketplace add mvanhorn/last30days-skill</code></pre> 再 install last30days。",
     "其它客户端：<pre><code>npx skills add mvanhorn/last30days-skill -g</code></pre> 全局安装。",
     "跑一次走完引导，解锁 X、YouTube、TikTok、arXiv、Techmeme，之后一句话出简报。"],
    ["<strong>判断：</strong>它把排序权交回给人：upvote、点赞、真金白银的下注，比编辑推荐难刷得多。",
     "<strong>判断：</strong>Polymarket 的赔率作为信号源很少见，对判断事件真伪比新闻标题可靠。",
     "<strong>判断：</strong>零配置就能跑，是这类 skill 扩散的关键，注册门槛每加一步就流失一半用户。"],
    ["research", "agent-skills", "search", "social", "briefing"])

add("superdesigndev", "treg", "Python", "9,698", "1,002", "501",
    "🔥 工具版的 OpenRouter —— +501★，9,698★，第 3 次上榜。一个 base URL 一个 token，调上千个按次计费的数据接口，不用挨个注册供应商。",
    ["<strong>数据接口按年订阅：</strong>Semrush $139/月、Moz $99/月、Crunchbase $99/月，只为跑一次也得买整年。",
     "<strong>要么没 API：</strong>邀请制、合作方专用、只开放应用审核，agent 根本接不上。",
     "<strong>密钥散在每个人本机：</strong>团队里谁的 key 都能看到，离职后没人回收。"],
    ["把 agent 指到一个 base URL 并带上 token，先搜任务再调用，按次计价。",
     "自托管也行，官方实例在 treg.to，团队自有密钥留在服务端不落地到 agent。",
     "新验证账号送 $1 额度，够把整条链路试通。"],
    ["<strong>判断：</strong>这是把「工具」当成模型来做路由：模型层已经收敛到几家，工具层还在野蛮生长，中间必然出现聚合层。",
     "<strong>判断：</strong>按次计价击中了 agent 的成本结构：任务是一次性的，订阅是持续的。",
     "<strong>判断：</strong>真正的资产是那些「没有公开 API」的账户，谁能合规地转售调用权，谁就握住定价权。"],
    ["tools", "api", "agent", "pricing", "router"])

add("Tracer-Cloud", "opensre", "Python", "16,010", "2,112", "326",
    "🔥 让 agent 修 CI —— +326★，1.6 万★，第 3 次上榜。CI 只告诉你挂了，它读失败日志、追到根因、把修复推给你审。自托管、用自己的模型。",
    ["<strong>CI 只说挂了不说原因：</strong>翻几百行日志找那一行报错。",
     "<strong>修复靠人肉：</strong>同一个 flaky 测试，三个月里修了五遍。",
     "<strong>日志不敢外传：</strong>托管型诊断服务要读你的构建日志和仓库结构。"],
    ["macOS/Linux：<pre><code>curl -fsSL https://install.opensre.com | bash -s -- -gh</code></pre>",
     "在代码仓库里运行 <pre><code>opensre</code></pre>，指向失败的 workflow run。",
     "它给出根因和补丁，你审完再合，模型与凭据都在自己这边。"],
    ["<strong>判断：</strong>CI 可靠性是个被低估的 agent 落点：输入结构清晰（日志+diff）、输出可验证（测试是否转绿）。",
     "<strong>判断：</strong>自托管加自带模型，卖的是合规而不是能力，这在企业采购里往往才是决定性因素。",
     "<strong>判断：</strong>README 明写 public alpha，现在上车的人是在替他们做集成测试，生产环境别急。"],
    ["ci-cd", "agent", "devops", "self-hosted", "reliability"])

add("google-labs-code", "stitch-skills", "TypeScript", "13,470", "1,593", "311",
    "🔥 Google Stitch 的官方技能包 —— +311★，1.3 万★，第 5 次上榜。设计、构建、工具三组插件，跟着 Agent Skills 开放标准走，Codex 和 Claude Code 都能装。",
    ["<strong>设计稿到代码断层：</strong>UI 图转成组件，样式、间距、状态全靠人补。",
     "<strong>每个客户端一套玩法：</strong>Codex 用 marketplace，Claude Code 用 npx，Cursor 又是另一套。",
     "<strong>设计系统对不齐：</strong>生成的组件和现有 token 打架。"],
    ["Codex：<pre><code>codex plugin marketplace add google-labs-code/stitch-skills --ref main</code></pre>",
     "Claude Code 与 Cursor：<pre><code>npx plugins add google-labs-code/stitch-skills</code></pre>",
     "按需只装 stitch-design、stitch-build、stitch-utilities 中的一组，别一次全拉。"],
    ["<strong>判断：</strong>Google 用开放标准发技能，等于承认客户端之争已经打完，先抢内容供给。",
     "<strong>判断：</strong>三组插件就是三段流水线：设计、构建、工具。拆得越细，越容易被别家复用。",
     "<strong>判断：</strong>与 Stitch 绑定意味着它是入口，不是独立工具，长期看价值随 Stitch 的采用率浮动。"],
    ["google", "agent-skills", "ui-design", "codegen", "plugin"])

add("cursor", "plugins", "TypeScript", "19,921", "2,200", "242",
    "🔥 Cursor 把 IDE 做成应用商店 —— +242★，1.99 万★，第 6 次上榜。Google 全家桶、Salesforce、GitHub、Playwright、X 都是带 manifest 的插件。",
    ["<strong>集成靠自己搓：</strong>接内部工具时每个团队各写一套胶水，不管版本，彼此不兼容。",
     "<strong>权限边界说不清：</strong>SaaS 授权散在各处脚本里，审计时讲不明白 agent 能碰什么。",
     "<strong>复用只能复制粘贴：</strong>没有可安装、可升级的分发单元。"],
    ["<pre><code>git clone https://github.com/cursor/plugins</code></pre> 每个目录自带 <pre><code>.cursor-plugin/plugin.json</code></pre>。",
     "从插件市场直接安装 third_party 下的 github、playwright、salesforce、google-sheets。",
     "照 create-plugin 脚手架写自己的集成，用 agent-compatibility 校验跨客户端兼容性。"],
    ["<strong>判断：</strong>比的不是模型，是哪家 SaaS 先被写成插件。这是 IDE 抢分发入口的老剧本。",
     "<strong>判断：</strong>manifest 比裸 MCP server 多出版本、作者、市场三件套，集成层竞争正从协议转向应用商店。",
     "<strong>判断：</strong>thermos 这类审查插件已经插手 code review，插件规范迟早要补安全边界。"],
    ["cursor", "plugins", "ai-ide", "mcp", "integrations"])

add("phone-harness", "phone-harness", "Python", "6,063", "638", "100",
    "🔥 让 agent 直接用你的手机 —— +100★，6,063★，第 2 次上榜。iPhone 走镜像、安卓走 adb、云机走账号，几行 Python 就能点屏幕、打字、读界面。",
    ["<strong>手机操作是自动化的死角：</strong>App 没有 API，脚本测试只能靠人点。",
     "<strong>Andr​oid 与 iOS 两套逻辑：</strong>adb 和镜像各写一遍，维护成本翻倍。",
     "<strong>云端真机贵且慢：</strong>跑一次回归测试，排队比执行久。"],
    ["<pre><code>phone-harness doctor</code></pre> 先检查环境：iPhone 要 macOS 15+ 与 iOS 18+ 镜像授权，安卓要 adb 与 USB 调试。",
     "内联 Python：<pre><code>open_app(\"Notes\")</code></pre>、<pre><code>tap_text(\"New Note\")</code></pre>、<pre><code>screen()</code></pre> 读界面文本。",
     "MCP 客户端加 <pre><code>https://mcp.phone-harness.com/mcp</code></pre>，或装 Hermes/OpenClaw 插件。"],
    ["<strong>判断：</strong>agent 的最后一公里是「有没有人手去点那个按钮」，手机是最大的一块空白。",
     "<strong>判断：</strong>用镜像和 adb 而不是越狱/Root，是在合规和安全之间选了个能规模化的点。",
     "<strong>判断：</strong>只出 100★ 却值得看，因为它补的是能力缺口，不是体验优化，天花板取决于 App 会不会封杀。"],
    ["mobile", "agent", "automation", "adb", "mcp"])

TOPIC = ("🔥 <strong>今日主题：agent 开始长出具体的手脚，技能包变成了分发单元。</strong>"
         "phone-harness 让它点手机、opensre 让它修 CI、autoclip 把剪辑变成 MCP 可调用的动作、treg 把上千个付费接口折成按次计费——这些项目的共同点是不再争论模型多聪明，直接去补 agent 够不到的地方。"
         "另一边，Claude-BugHunter、superpowers、diagram-design、stitch-skills 连续霸榜，说明竞争已经从「谁的模型强」转到「谁的技能包先被装进客户端」。"
         "判断：模型能力正在变成水电，接口和凭据才是稀缺资源；接下来一年，能赢的项目是那些握着别人拿不到的数据源与操作权的项目。")

with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

prior = {}
for day in data["days"]:
    for p in day["projects"]:
        k = (p.get("owner"), p.get("name"))
        prior[k] = max(prior.get(k, 0), p.get("count") or 0)

gap = (datetime.strptime(TODAY, "%Y-%m-%d")
       - datetime.strptime(data["lastUpdated"], "%Y-%m-%d")).days
if gap == 1:
    ypairs = {(p.get("owner"), p.get("name")) for p in data["days"][0]["projects"]}
    for p in P:
        p["badge"] = "连登" if (p["owner"], p["name"]) in ypairs else "新面孔"
    new = sorted([p for p in P if p["badge"] == "新面孔"],
                 key=lambda p: -int(p["starsToday"].replace(",", "")))[:6]
    streak = sorted([p for p in P if p["badge"] == "连登"],
                    key=lambda p: -int(p["starsToday"].replace(",", "")))[:6]
    P = new + streak
else:
    for p in P:
        p["badge"] = "新面孔"

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
assert len(data["days"]) == 104, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("gap=%d 写入完成：%s，%d 个项目，总天数 %d" % (gap, TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-40s %-6s +%-6s %9s★ count=%d" % (
        p["rank"], p["fullName"], p["badge"], p["starsToday"], p["stars"], p["count"]))
