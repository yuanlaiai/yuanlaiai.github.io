#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-23 榜单更新（gap=1，双栏：新面孔 1-6 / 连登 7-12）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-23"

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


# ------------------------------------------------ 新面孔 ----
add("jingyaogong", "minimind", "Python", "69,229", "9,042", "828",
    "🔥 第 4 次上榜 +828★ —— 隔一天回来，星数从 68,210 涨到 69,229。3 块钱、2 小时，从 0 训出 64M 对话模型，预训练到 GRPO 的源码全在仓库里。",
    ["<strong>入门卡在显存：</strong>想亲手训一次模型的人，看到官方脚本动辄八卡起步就停了，教程只讲推理不讲训练。",
     "<strong>链路缺环：</strong>数据清洗、tokenizer、评测这些脏活大部分教程跳过，照抄能跑通但不知道为何这么写。",
     "<strong>RLHF 不透明：</strong>PPO、DPO、GRPO 在论文里是公式，在仓库里是几十行没注释的循环，门外汉看不出差别。"],
    ["clone 后按 README 装依赖，主线模型单卡 8GB 显存能跑完预训练到微调。",
     "按 pretrain → sft → LoRA/DPO 的顺序走，每步都有脚本和数据集说明。",
     "用 HuggingFace 上的 MiniMind 集合做对照，比从零判断收敛更靠谱。"],
    ["<strong>回访型项目的日增最稳：</strong>它不靠发布新版本，靠的是每隔几周被新一轮人搜到，教育类内容天然周期性。",
     "<strong>69k★ 说明「教学型模型」有独立生态：</strong>它不比能力，比的是把 RLHF 全家桶塞进单卡能跑的体积里。",
     "<strong>体积本身就是选题：</strong>主线约为 GPT-3 的 1/2700，这个数字让参数规模从宣传语变回可以动手算的工程量。"],
    ["llm-training", "small-model", "rlhf", "education", "from-scratch"])

add("mvanhorn", "last30days-skill", "Python", "73,150", "6,464", "790",
    "🔥 第 6 次上榜 +790★ —— 隔一天回来，+790 比昨天的 +681 还高。跨 Reddit、X、YouTube、HN、Polymarket 抓最近 30 天讨论，按互动量和真金白银排序。",
    ["<strong>搜索结果被编辑过：</strong>引擎给的是排过序的结论，热点滞后，SEO 内容把真实讨论挤到后面。",
     "<strong>跨平台要手工翻：</strong>想知道一个话题怎么吵，得开五个标签页对照，重复劳动还容易漏。",
     "<strong>标题和内容对不上：</strong>媒体标题党，焦点实际在评论区，只看标题会写错方向。"],
    ["作为 agent skill 装上，用 <pre><code>/last30days</code></pre> 触发，指定话题与时间窗。",
     "可选平台范围，需要判断事件概率时把 Polymarket 加进来。",
     "输出的每条结论带来源链接，写稿时可直接核对。"],
    ["<strong>回访日增比首登更高，是个信号：</strong>68,210 到 73,150 的增长说明新用户在持续涌入，而不是一次性曝光。",
     "<strong>它把「注意力分配」做成了产品：</strong>先筛出有人在讨论的题，再判断真假，顺序反过来做的人大多白写。",
     "<strong>预测市场当信源的新常态：</strong>赔率是有人拿钱投票的结果，作为概率参考比评论区更有信息量。"],
    ["research", "agent-skill", "trending", "community", "signal"])

add("cathrynlavery", "diagram-design", "HTML", "70,684", "4,739", "624",
    "🔥 第 9 次上榜 +624★ —— 隔一天回来再涨 624，总星破 7 万。让 agent 画图但不画 Mermaid：单文件 HTML+SVG，51 种图表类型，能按品牌色重绘。",
    ["<strong>Mermaid 出图没救：</strong>配色和排版不可控，放进汇报一眼是机器画的，改样式要改渲染器。",
     "<strong>设计工具改图成本高：</strong>Figma 里拖一次很爽，结构变了要重画，版本越堆越乱。",
     "<strong>Agent 给的图是占位：</strong>多数 agent 画架构只会输出 ASCII 或方框，不能直接用。"],
    ["<pre><code>npx skills add cathrynlavery/diagram-design</code></pre> 装进 agent。",
     "用一句自然语言描述架构，让它出 HTML+SVG 单文件。",
     "要改品牌色跑 onboarding 流程，也能从 drawio、mermaid、excalidraw 导入反推。"],
    ["<strong>9 次上榜的图库型技能，说明它已经变成默认件：</strong>画图这件事被它接管之后，用户不再问「用什么工具画」。",
     "<strong>单文件输出是刻意的限制：</strong>不依赖渲染库，浏览器打开就是终稿，代价是复杂布局要自己算。",
     "<strong>反 Mermaid 是个精准定位：</strong>把设计品味当卖点，正好补上了多数 agent 出图最难看的那一块。"],
    ["diagram", "svg", "agent-skill", "design", "visualization"])

add("Tracer-Cloud", "opensre", "Python", "14,641", "1,981", "438",
    "🔥 第 2 次上榜 +438★ —— 11-21 首现时 +466，隔一天回来还有 +438，说明 CI 排障这个动作真有人接走了。Apache 2.0，模型自带。",
    ["<strong>日志没人看：</strong>CI 红了只告诉你哪个退出码非零，真正的报错藏在几千行日志中段。",
     "<strong>跨系统串联靠人肉：</strong>一次失败要同时看 CI、容器日志、监控告警，时间戳还得自己对。",
     "<strong>SaaS 排障要交日志：</strong>把私有仓库的构建日志上传给第三方，安全和合规往往过不了。"],
    ["装 CLI 并填自己的模型 key，支持的厂商见 README。",
     "接进 GitHub Actions，构建失败时自动触发排障。",
     "看它给出的根因判断和 diff，人工确认后再推。"],
    ["<strong>复访指数比首登更有说服力：</strong>首现 +466 隔天 +438，两个数字接近，说明进来的不是围观者而是使用者。",
     "<strong>读日志比写代码容易验收：</strong>根因对不对一眼能看出来，这是 agent 落地里少有的、标准清晰的任务。",
     "<strong>自托管加自带模型是合规门槛的解法：</strong>愿意为这条付费的往往是跑私有 CI 的公司，SaaS 吃不下这块。"],
    ["ci-cd", "devops", "agent", "self-hosted", "reliability"])

add("FlashML-org", "FreeVideo", "Python", "4,167", "642", "428",
    "🔥 第 2 次上榜 +428★ —— 11-21 首现 +293，今天 +428 反而加速。8GB 显存本地跑 MiniMax H3，生视频、生 16MP 图片，还能让 Claude Code 自己剪。",
    ["<strong>视频模型几乎都在云上：</strong>按秒计费，素材要上传，做企业宣传片的团队过不了数据审查。",
     "<strong>本地门槛高：</strong>视频生成模型常要 24GB 显存起步，普通笔记本直接劝退。",
     "<strong>生成到剪辑要转码：</strong>片段出来还得进剪辑软件拼接，格式转换和音画对齐全靠手工。"],
    ["下对应平台安装包，Windows、macOS arm64、Linux AppImage 都在 Releases 里。",
     "先出半分辨率预览，确认后再渲染全分辨率，节省试错时间。",
     "v0.4 之后可让 agent 通过命令行生成一分钟以上的视频，并在时间线里编辑。"],
    ["<strong>第二天比第一天涨得快，属于少见的加速曲线：</strong>通常是有人发了实际产出，用作品带来了第二波流量。",
     "<strong>8GB 显存是消费级显卡的门槛线：</strong>把线压到这里就打开了笔记本市场，这是它比抽象能力更实在的卖点。",
     "<strong>本地推理用时间换显存：</strong>四个质量档位本质是让用户自己选花多少分钟换多少细节。"],
    ["video-generation", "local-inference", "minimax", "desktop", "gpu"])

add("google-labs-code", "stitch-skills", "TypeScript", "12,116", "1,502", "425",
    "🔥 第 4 次上榜 +425★ —— 11-21 是 +315，隔一天回来涨到 +425。Google Stitch 官方技能包，按 Agent Skills 开放标准写，四个主流 agent 宿主都能装。",
    ["<strong>设计稿到代码靠手抄：</strong>Stitch 生成 UI 之后，落到组件里没有任何交接，中间全靠人重新描述。",
     "<strong>插件格式各自为政：</strong>同一套技能要分别适配 Codex 的 marketplace、Claude Code 的插件目录。",
     "<strong>生成和构建断开：</strong>设计阶段的产出物在构建阶段用不上，两边模型看到的是不同上下文。"],
    ["Codex 用 <pre><code>codex plugin marketplace add google-labs-code/stitch-skills --ref main</code></pre> 装全套。",
     "stitch-design 出界面方向，stitch-build 负责落地成代码和组件。",
     "其他宿主手动把 skills 目录拷进各自的 skills 路径。"],
    ["<strong>官方技能隔天回来且日增上升：</strong>说明它的用户不是围观 Google 新玩具的人，而是真在流水线里换工具的团队。",
     "<strong>design 与 build 拆成两个插件：</strong>按工程阶段切分技能，比塞进一个大包更符合真实工作流。",
     "<strong>开放标准是它的筹码：</strong>Stitch 是自家产品，技能却写成第三方格式，抢的是 agent 生态的默认入口。"],
    ["ui-design", "agent-skill", "google", "frontend", "standard"])

# ------------------------------------------------ 连登 ----
add("elementalsouls", "Claude-BugHunter", "Python", "18,915", "2,050", "2,037",
    "🔥 第 5 次上榜 +2,037★ —— 第三天连榜，日增还在加速：11-21 的 +1,622、11-22 的 +1,803，到今天 +2,037，三天总星从 14,679 涨到 18,915，净增 4,236。",
    ["<strong>方法论不落地：</strong>流程散在博客和付费课里，新手跑完扫描器就以为结束，缺从信息收集到复现到报告的非线性推进。",
     "<strong>Agent 没有攻击者姿态：</strong>Claude Code 默认是写代码的助手，碰到 SSRF 绕过、原型链污染这类要主动构造假设的活，得人一句句喂提示词。",
     "<strong>范围控制靠人记：</strong>授权清单常常只存在开工会议的 PPT 里，agent 没有天然边界感。"],
    ["把 skills 目录拷进 <pre><code>~/.claude/skills</code></pre> 或项目的 <pre><code>.claude/skills</code></pre>，重开 Claude Code。",
     "用 <pre><code>/bb-methodology</code></pre> 起手，按信息收集、威胁建模、验证、利用、报告五段推进。",
     "要看真实流量时接 Burp MCP，把请求响应交给 agent 判断。"],
    ["<strong>三连日增递增的项目极少见：</strong>1,622 → 1,803 → 2,037，这种曲线通常出现在有外部放大事件的时候，单靠榜单曝光爬不出这个斜率。",
     "<strong>83 个技能对应 681 份公开报告：</strong>这个压缩比是它唯一难以复制的地方，照抄目录也复现不了案例库。",
     "<strong>安全技能包压过通用开发工具：</strong>连着三天站在榜首，说明愿意给 agent 装攻击能力的人，比愿意给它装测试框架的人多。"],
    ["security", "claude-code", "skills", "red-team", "bug-bounty"])

add("firecrawl", "firecrawl", "TypeScript", "207,479", "10,843", "920",
    "🔥 第 3 次上榜 +920★ —— 三天连榜，日增 1,241 → 1,006 → 920 缓慢回落但没掉队，20.7 万★ 的体量还能日增近千，说明接入管线的人一直在来。",
    ["<strong>Token 花在噪声上：</strong>抓回来的页面夹着导航、广告和 script，有用正文不到三成。",
     "<strong>反爬挡在门外：</strong>requests 加 BeautifulSoup 遇到 JS 渲染和 Cloudflare 就整页空。",
     "<strong>输出形状不统一：</strong>十个站点十种 HTML 结构，进 RAG 前还得写十套清洗规则。"],
    ["<pre><code>docker run -p 3002:3002 firecrawl/firecrawl</code></pre> 自托管，或调云 API 按页计费。",
     "<pre><code>app.scrape_url(url, formats=['markdown'])</code></pre> 拿正文，crawl 模式抓整站。",
     "挂成 MCP 工具，agent 同时有 search 和 scrape 两种取数方式。"],
    ["<strong>20 万★ 级别的项目连续三天在榜，是基建类的典型形态：</strong>它不需要爆点，只需要每天有人新建一个管线时顺手接进来。",
     "<strong>缓慢回落而不是腰斩，说明需求是结构性的：</strong>热点项目的曲线通常第三天掉一半，它没有。",
     "<strong>AGPL 让两类客户各取所需：</strong>自托管免费拿能力，闭源产品内嵌就要谈授权，边界画得很精。"],
    ["crawler", "rag", "markdown", "agent-infra", "self-hosted"])

add("zhouxiaoka", "autoclip", "Python", "14,104", "2,192", "908",
    "🔥 第 4 次上榜 +908★ —— 昨天 +683 之后今天反弹到 +908，星数从 12,929 涨到 14,104。贴链接一键出片，本地渲染竖屏短视频。",
    ["<strong>切点靠人找：</strong>90 分钟的访谈剪三条短视频，人工找爆点加调字幕两小时起步。",
     "<strong>一稿多投要重做：</strong>竖屏比例、时长上限、封面尺寸每个平台都不同，同一条内容得导出四遍。",
     "<strong>素材上传有顾虑：</strong>云端剪辑按次收费，客户的未公开访谈要先传给别人的服务器。"],
    ["去 Releases 下桌面版（Tauri 打包，MIT），安装后本地运行。",
     "贴视频链接或拖本地文件，选目标平台，等本地渲染。",
     "切点不满意进内置编辑器手动调，改完重新导出。"],
    ["<strong>第四天反弹是内容工具特有的节奏：</strong>周末剪完的东西周一上班才开始发，工具的日增跟着发布周期走。",
     "<strong>它解决的是「多平台发布」的重复劳动：</strong>同一份内容适配四个平台，这个工作没有创造性，最该被工具吃掉。",
     "<strong>本地渲染是差异化：</strong>素材不出门这一条，对企业访谈和未发布内容比任何模板都重要。"],
    ["video-editing", "shortvideo", "local-first", "tauri", "content-tools"])

add("obra", "superpowers", "Shell", "324,636", "28,803", "838",
    "🔥 第 25 次上榜 +838★ —— 32.5 万★，连续第三天在榜。宿主覆盖 15 个 coding agent，卖的是不让 agent 直接开写的开发方法论。",
    ["<strong>Agent 上手就写：</strong>没有流程约束时会跳过调研和方案讨论，一口气产出几百行跑不通的代码。",
     "<strong>技能格式各不相同：</strong>Claude Code 插件、Codex marketplace、Cursor rules 互不兼容，同一套工作流要在每个宿主重写。",
     "<strong>自评代替验证：</strong>agent 把「已完成」当成事实，测试没跑、边界没测，交付时才暴露。"],
    ["按自己宿主的 README 安装，Claude Code 走插件市场，Codex 走 marketplace add，也可手动拷 skills 目录。",
     "照它的节奏走：头脑风暴 → 写计划 → 分步执行，每步都要求先给方案。",
     "收尾调 review 技能，让另一个 agent 视角检查实现和测试。"],
    ["<strong>25 次上榜已经不是热度问题，是基础设施化：</strong>装过的项目很少卸载，它在榜上等同于每天有新机器在装它。",
     "<strong>覆盖率比方法论更值钱：</strong>15 个宿主的适配没有技术难度，只有琐碎，愿意做的团队很少。",
     "<strong>它在给 agent 装纪律：</strong>当前模型的失败模式不是不会写，而是不愿意停，这套流程的核心动作是强制先输出计划。"],
    ["agent-workflow", "methodology", "skills", "coding-agent", "cross-platform"])

add("HKUDS", "CLI-Anything", "Python", "63,243", "5,743", "783",
    "🔥 第 10 次上榜 +783★ —— 第四天连榜，日增 769 → 783 几乎是一条直线。给所有软件套一层命令行外壳，CLI-Hub 上能直接装。",
    ["<strong>GUI 没有接口：</strong>只有鼠标能操作的地方，agent 只能截屏加坐标点击，一个弹窗就全乱。",
     "<strong>每个应用重写一遍：</strong>自动化脚本按软件定制，维护成本比开发还高。",
     "<strong>像素输出不可组合：</strong>截图里既没有参数也没有错误码。"],
    ["去 <pre><code>clianything.cc</code></pre> 的 CLI-Hub 找目标软件的包装器。",
     "按条目里的命令装上，直接在 shell 里跑，输出结构化。",
     "把命令写成 agent 的工具描述，让它按需调用而不是操作界面。"],
    ["<strong>四天几乎同速，是最健康的增长形态：</strong>它意味着每天都在解决同一批人的同一批问题，而不是被一次事件推上去。",
     "<strong>天花板在长尾：</strong>热门软件早有人写包装器，真正的活是那些没人愿意适配的中小工具。",
     "<strong>把接口面从像素拉回文本：</strong>稳定性和可测试性一起上来了，重跑不会因为按钮挪两像素就失败。"],
    ["cli", "agent-tools", "automation", "desktop", "interop"])

add("mjmirza", "app-store-compliance", "Shell", "4,515", "287", "755",
    "🔥 第 3 次上榜 +755★ —— 三天从 2,902★ 涨到 4,515★，涨了 55%。117 条拒审理由清单加提交前 guard，给 Claude Code 用。",
    ["<strong>条款藏得深：</strong>被拒多是隐私清单缺失、权限说明含糊、账号删除路径没做，要求分散在两份长文档里。",
     "<strong>一次拒审就是几天：</strong>改完要重新排队，小团队最怕这种不可控等待。",
     "<strong>检查没有卡点：</strong>团队知道要合规，但没把它变成提交前的自动检查。"],
    ["当网页读 <pre><code>mjmirza.github.io/app-store-compliance</code></pre>，按拒审理由类别检索。",
     "把 guard 脚本接进 CI，提交前扫 Info.plist 和 AndroidManifest 的隐私与权限声明。",
     "在 Claude Code 里让它对着条款解释具体拒审理由。"],
    ["<strong>三天涨 55% 是典型的团队内扩散：</strong>它落在提交节点上，谁踩过坑谁转给同事，一条链能带一整个团队。",
     "<strong>合规工具的价值不在准确率，在把隐性知识写成清单：</strong>117 条理由的颗粒度正好是能照着改的程度。",
     "<strong>它只有 Shell 和文档，没有模型：</strong>agent 时代的工具不一定要是 AI 产品，能被 agent 调用就够了。"],
    ["app-store", "compliance", "ci", "mobile", "claude-code"])

TOPIC = ("🔥 <strong>今日主题：12 条里 0 条首登。</strong>"
         "新面孔栏的 minimind、last30days-skill、diagram-design、opensre、FreeVideo、stitch-skills 全是回访，"
         "分别第 4、6、9、2、2、4 次上榜；连登栏则是昨天的原班人马。"
         "这不是抓取问题，是供给问题：通用榜 16 行里的非 AI 项（Ghost-Downloader、AFFiNE、nginx）占了三个位置，"
         "而 AI 侧真正的新项目一个都没冒出来。"
         "回访型项目的日增反而在涨——Claude-BugHunter 三连日增递增到 +2,037，autoclip 反弹到 +908，FreeVideo 从 +293 涨到 +428——"
         "说明存量用户还在往里装，但新项目没接上。"
         "结论：趋势榜现在反映的是安装惯性，不是创新速度；判断一个领域有没有真进展，看首登项目数比看总星数靠谱。")

# ---------------------------------------------------------------- mechanical
with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

prior = {}
for day in data["days"]:
    for p in day["projects"]:
        k = (p.get("owner"), p.get("name"))
        prior[k] = max(prior.get(k, 0), p.get("count") or 0)

gap = (datetime.strptime(TODAY, "%Y-%m-%d")
       - datetime.strptime(data["lastUpdated"], "%Y-%m-%d")).days
print("gap =", gap)

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
    P = sorted(P, key=lambda p: -int(p["starsToday"].replace(",", "")))

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
assert len(data["days"]) == 102, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-38s +%-6s %9s★ count=%d badge=%s" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"], p["badge"]))
