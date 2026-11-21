#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-21 榜单更新（gap=3，平铺日）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-21"

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


add("elementalsouls", "Claude-BugHunter", "Python", "14,679", "1,725", "1,622",
    "🔥 第 3 次上榜 +1,622★ —— 83 个 Claude Code 技能铺满渗透测试全流程，其中 58 个 hunt-* 是从 681 份公开 HackerOne 报告里拆出的检测模式，连 M365、Okta、vCenter 的 2024–2026 CVE 链都收进去了。",
    ["<strong>方法论碎片化：</strong>渗透测试的流程散在博客、付费课和几个人的笔记里，新手跑完一遍扫描器就当成结束了，缺的是从信息收集到复现到报告的非线性推进。",
     "<strong>Agent 没有攻击者姿态：</strong>Claude Code 默认把自己当写代码的助手，碰到 SSRF 绕过、原型链污染这类需要主动构造假设的活，得人一句句把提示词喂进去。",
     "<strong>范围控制靠人记：</strong>红队项目最容易出事的地方是越界，agent 没有天然边界感，授权清单常常只存在开工会议的 PPT 里。"],
    ["把仓库里的 skills 目录拷进 <pre><code>~/.claude/skills</code></pre> 或项目的 <pre><code>.claude/skills</code></pre>，重开 Claude Code 即生效。",
     "用 <pre><code>/bb-methodology</code></pre> 起手，按信息收集、威胁建模、验证、利用、报告五段推进，再按目标类型调 hunt-* 技能。",
     "需要看真实流量时接 Burp MCP，把请求响应交给 agent 判断，而不是让它凭空猜 payload。"],
    ["<strong>技能包在取代提示词模板：</strong>681 份报告压成 83 个可分发技能，压缩比本身就是产品价值，个人经验第一次能像依赖包一样被安装。",
     "<strong>Bug bounty 的知识正在变成可复用资产：</strong>过去这类方法只活在少数人的脑子里，现在被编码成按平台、按漏洞类拆分的文件树，新人的起点被抬高了。",
     "<strong>合规是这类包的第一风险：</strong>README 反复强调 authorized engagements，并给出 DVWA、Juice Shop 这类练习靶场，作者清楚越界的代价落在使用者身上。"],
    ["security", "claude-code", "skills", "red-team", "bug-bounty"])

add("firecrawl", "firecrawl", "TypeScript", "205,501", "10,746", "1,241",
    "🔥 首登 +1,241★ —— 20.5 万★ 的抓取基建，把网页转成 LLM 能直接吃的 Markdown，550+ 站点开箱可用，自托管和云 API 两条路都留着。",
    ["<strong>Token 花在噪声上：</strong>agent 抓回来的页面夹着导航、广告和 script，真正有用的正文不到三成，上下文窗口被杂讯吃掉。",
     "<strong>反爬和渲染挡在门外：</strong>requests 加 BeautifulSoup 遇到 JS 渲染和 Cloudflare 就整页空，自己维护 headless 浏览器又是一摊工程。",
     "<strong>结果形状不统一：</strong>同一件事在十个站点有十种 HTML 结构，要进 RAG 还得先写十套清洗规则。"],
    ["用 <pre><code>docker run -p 3002:3002 firecrawl/firecrawl</code></pre> 自托管，或者直接调云 API，按页计费。",
     "Python SDK 里 <pre><code>app.scrape_url(url, formats=['markdown'])</code></pre> 拿正文，crawl 模式可顺着链接抓整站。",
     "把它挂成 MCP 工具，agent 就同时有了 search 和 scrape 两种取数手段。"],
    ["<strong>抓取层被收进 agent 基建：</strong>它和向量库、编排框架站到了同一层，模型能力再强，取不到干净文本也白搭，20 万★ 是这个刚需的定价。",
     "<strong>AGPL 是商业策略的一部分：</strong>自托管免费，闭源产品内嵌要买授权，开源的边界被精确地画在了商业客户那一侧。",
     "<strong>550+ 站点的预配置才是真资产：</strong>通用爬虫谁都能写，几千小时的站点适配没法一夜补齐，这部分工作决定了它能不能替掉自研脚本。"],
    ["crawler", "rag", "markdown", "agent-infra", "self-hosted"])

add("zhouxiaoka", "autoclip", "Python", "12,353", "2,030", "979",
    "🔥 第 2 次上榜 +979★ —— 贴一个链接，本机出片：长视频自动切成竖屏短视频，字幕、封面、发布文案一起给，抖音、小红书、TikTok、Reels 都备了预设。",
    ["<strong>切点靠人找：</strong>一集 90 分钟的访谈要剪三条短视频，人工找爆点加调字幕两小时起步，第二天热度就过了。",
     "<strong>一稿多投要重做：</strong>竖屏比例、时长上限、封面尺寸每个平台都不一样，同一条内容得导出四遍。",
     "<strong>素材上传有顾虑：</strong>云端剪辑按次收费，客户的未公开访谈要先传给别人家的服务器。"],
    ["去 Releases 下桌面版（Tauri 打包，MIT 协议），安装后本地运行。",
     "贴视频链接或拖本地文件进来，选目标平台，等本地渲染出成品。",
     "切点不满意就进内置编辑器手动调，改完重新导出。"],
    ["<strong>软件免费加云端模型按量计费：</strong>这是今年桌面 AI 工具的主流定价，工具本体不赚钱，赚的是模型调用的分成。",
     "<strong>本地渲染降的是信任成本：</strong>做中文播客和企业访谈的团队最在意素材不出门，这一步比多给两个模板更能拿下他们。",
     "<strong>一键出片的上限是模板审美：</strong>它把重复劳动压掉了，但哪个 15 秒值得剪出来仍然要靠人判断，工具替代的是手不是眼。"],
    ["video-editing", "shortvideo", "local-first", "tauri", "content-tools"])

add("obra", "superpowers", "Shell", "322,986", "28,677", "890",
    "🔥 第 23 次上榜 +890★ —— 32.3 万★ 的老面孔，覆盖 15 个 coding agent 宿主，从 Claude Code、Codex、Cursor 一路排到 Hermes Agent，卖的是不让 agent 直接开写的开发方法论。",
    ["<strong>Agent 上手就写：</strong>没有流程约束时它会跳过调研和方案讨论，一口气产出几百行跑不通的代码，返工成本比一开始想清楚更高。",
     "<strong>技能格式各不相同：</strong>Claude Code 的 plugins、Codex 的 marketplace、Cursor 的 rules 互不兼容，同一套工作流要在每个宿主重写一遍。",
     "<strong>自评代替验证：</strong>agent 常把「已完成」当成事实，测试没跑、边界没测，交付时才发现。"],
    ["按自己宿主的 README 安装，Claude Code 走插件市场，Codex 走 marketplace add，也支持手动拷 skills 目录。",
     "照它的节奏走：头脑风暴 → 写计划 → 分步执行，每一步都要 agent 先给方案再动手。",
     "收尾时调它的 review 技能，让另一个 agent 视角检查实现和测试。"],
    ["<strong>23 次上榜说明它靠的不是新鲜度：</strong>真正的壁垒是宿主覆盖率，技能数量只是外壳，写得再好的方法如果只能装在 Claude Code 里，覆盖不到其他六成用户。",
     "<strong>它在给 agent 装纪律：</strong>当前模型的失败模式不是不会写，而是不愿意停，这套流程的核心动作就是强制它在动手前先输出计划。",
     "<strong>方法论正在变成可分发的中间层：</strong>模型厂商各自优化自家 agent 的默认行为，跨宿主的那一层留给了开源项目，这是它长期存在的理由。"],
    ["agent-workflow", "methodology", "skills", "coding-agent", "cross-platform"])

add("mjmirza", "app-store-compliance", "Shell", "2,902", "183", "869",
    "🔥 首登 +869★ —— 把 App Store 和 Google Play 的拒审理由做成 117 条可查清单，再配一个提交前自动跑的 guard，专门给 Claude Code 用。",
    ["<strong>条款藏得深：</strong>被拒最常见的不是功能问题，而是隐私清单缺失、权限说明含糊、账号删除路径没做，这些要求分散在两份很长的审核文档里。",
     "<strong>一次拒审就是几天：</strong>被退回后改完要重新排队，节奏被审核周期卡住，小团队最怕这种不可控的等待。",
     "<strong>检查没有卡点：</strong>团队知道要合规，但没把它变成提交前的自动检查，靠人记的结果就是每次都漏一项。"],
    ["当网页读 <pre><code>mjmirza.github.io/app-store-compliance</code></pre>，按拒审理由类别检索。",
     "把 guard 脚本接进 CI，提交前扫 Info.plist 和 AndroidManifest 里的隐私与权限声明。",
     "在 Claude Code 里让它对着条款解释具体拒审理由，比自己读一遍文档快。"],
    ["<strong>2,902★ 冲上 +869 说明痛点不在技术侧：</strong>分发阻塞是全端开发都要付的税，愿意为「少被拒一次」投入时间的团队比想象中多。",
     "<strong>把监管规则编码成可执行检查，是合规工具最现实的形态：</strong>清单能读，guard 能跑，两者一起才闭环，只有文档的产品很难被记住。",
     "<strong>它不解决审核本身：</strong>只是把可预测的失败提前暴露，剩下的不确定性仍然由平台掌握，工具的边界应该诚实地说清楚。"],
    ["app-store", "compliance", "ci", "mobile", "claude-code"])

add("jingyaogong", "minimind", "Python", "67,812", "8,864", "847",
    "🔥 第 3 次上榜 +847★ —— 3 块钱、2 小时，从 0 训出一个 64M 的对话模型，预训练、SFT、LoRA、DPO、GRPO、CISPO 的源码全在仓库里。",
    ["<strong>入门卡在显存：</strong>想亲手训一次模型的人，看官方脚本动辄八卡起步，教程只讲推理不讲训练，第一步就断了。",
     "<strong>链路缺环：</strong>数据清洗、tokenizer 训练、评测这些脏活大部分教程跳过，照着抄能跑通但不知道为什么这么写。",
     "<strong>RLHF 不讲清代码：</strong>PPO、DPO、GRPO 的差别在论文里是公式，在仓库里是几十行没注释的循环。"],
    ["clone 后按 README 装依赖，主线模型单卡 8GB 显存就能跑完预训练到微调。",
     "按 pretrain → sft → LoRA/DPO 的顺序走，每一步都有对应脚本和数据集说明。",
     "拿 HuggingFace 上的 MiniMind 集合做对照，比自己从零判断收敛更靠谱。"],
    ["<strong>教学型模型有稳定需求：</strong>67.8k★ 不是因为它能打，而是因为它是唯一把 RLHF 全家桶塞进能单卡跑完的体积里的项目。",
     "<strong>体积本身就是选题：</strong>主线版本约为 GPT-3 的 1/2700，这个数字让「参数规模」从宣传语变回可以动手算的工程量。",
     "<strong>3 块钱 2 小时是极强的传播钩子：</strong>它把训练这件事的门票价格写成了一句能被转发的话，比任何性能对比都好用。"],
    ["llm-training", "small-model", "rlhf", "education", "from-scratch"])

add("HKUDS", "CLI-Anything", "Python", "61,555", "5,582", "773",
    "🔥 第 8 次上榜 +773★ —— 给所有软件套一层 agent 能调的命令行外壳，CLI-Hub 上已经能直接装现成的包装器。",
    ["<strong>GUI 没有接口：</strong>桌面软件只有鼠标能操作的地方，agent 只能靠截屏加坐标点击，一次弹窗就全乱。",
     "<strong>每个应用重写一遍：</strong>自动化脚本按软件定制，Photoshop 一套、Blender 一套，维护成本比开发还高。",
     "<strong>像素输出不可组合：</strong>agent 需要的是结构化文本，截图里既没有参数也没有错误码。"],
    ["去 <pre><code>clianything.cc</code></pre> 的 CLI-Hub 找目标软件对应的包装器。",
     "按条目里的命令装上，直接在 shell 里跑，输出是结构化的。",
     "把命令写成 agent 的工具描述，让它按需调用而不是操作界面。"],
    ["<strong>8 次上榜说明这条路被反复验证：</strong>每次有新软件被包装进来，就多一个 agent 能进入的场景，积累效应很明显。",
     "<strong>把 agent 的接口面从像素拉回文本：</strong>稳定性和可测试性同时上来了，重跑一次不会因为按钮挪了两像素就失败。",
     "<strong>难点在长尾：</strong>Hub 的条目数决定实际可用面，热门软件早就有人写，真正难的是那些只有几十万用户但没人愿意适配的工具。"],
    ["cli", "agent-tools", "automation", "desktop", "interop"])

add("mvanhorn", "last30days-skill", "Python", "71,575", "6,342", "681",
    "🔥 第 5 次上榜 +681★ —— 跨 Reddit、X、YouTube、HN、Polymarket 抓最近 30 天的一手讨论，按点赞和真实资金排序，合成一份带信源的简报。",
    ["<strong>搜索结果被编辑过：</strong>搜索引擎给的是排过序的结论，热点常常滞后，SEO 内容把真实讨论挤到后面。",
     "<strong>跨平台要手工翻：</strong>想知道一个话题在社区里怎么吵，得开五个标签页对照，重复劳动且容易漏。",
     "<strong>标题和内容对不上：</strong>媒体标题党，实际讨论的焦点在评论区里，只看标题会写错方向。"],
    ["作为 agent skill 装上，用 <pre><code>/last30days</code></pre> 触发，指定话题和时间窗。",
     "可选平台范围，Polymarket 用在需要判断事件概率的选题上。",
     "输出的每条结论都带来源链接，写稿时可以直接核对。"],
    ["<strong>按互动量排序确实比按编辑权重好用：</strong>这套技能在这次选题里被我实际用过，社区里有人吵的题目才有人读。",
     "<strong>把预测市场赔率当信源：</strong>Polymarket 的价格是有人拿钱投票的结果，作为事件概率的参考比多数评论更有信息量。",
     "<strong>它解决的是注意力分配，不是真假判断：</strong>被讨论不等于被证实，这层仍然得自己核。"],
    ["research", "agent-skill", "trending", "community", "signal"])

add("cathrynlavery", "diagram-design", "HTML", "69,423", "4,660", "636",
    "🔥 第 8 次上榜 +636★ —— 让 agent 画图但不画 Mermaid：输出单文件 HTML+SVG，51 种图表类型，能按品牌色重绘。",
    ["<strong>Mermaid 出图没救：</strong>配色和排版都不可控，放进汇报材料一眼是机器生成的，改样式要改渲染器。",
     "<strong>设计工具改图成本高：</strong>架构图在 Figma 里拖一次很爽，结构变了要重画，版本越堆越乱。",
     "<strong>Agent 给的图是占位：</strong>多数 agent 画架构只会输出 ASCII 或方框，不能直接用。"],
    ["用 <pre><code>npx skills add cathrynlavery/diagram-design</code></pre> 装进 agent。",
     "用一句自然语言描述架构，比如前后端加缓存和数据库，让它出 HTML+SVG 单文件。",
     "要改品牌色就跑它的 onboarding 流程，也可以导入 drawio、mermaid、excalidraw 反推。"],
    ["<strong>审美可控比能生成更稀缺：</strong>69k★ 的图库型技能说明大家早就不缺出图能力，缺的是能直接放进交付物的图。",
     "<strong>单文件 HTML+SVG 是精心的取舍：</strong>不依赖渲染库，浏览器打开就是终稿，任何前端都能塞，代价是复杂布局要自己算。",
     "<strong>它明确反对 Mermaid：</strong>把设计品味当成卖点，是技能市场开始分层的一个信号。"],
    ["diagram", "svg", "agent-skill", "design", "visualization"])

add("Tracer-Cloud", "opensre", "Python", "13,708", "1,929", "466",
    "🔥 首登 +466★ —— Apache 2.0 的 CI 可靠性 agent，读失败的 run、追到根因、把补丁推上来让你审，模型用你自己的。",
    ["<strong>日志没人看：</strong>CI 红了只告诉你哪一步退出码非零，几千行日志里真正的报错藏在中段，翻一遍二十分钟。",
     "<strong>跨系统串联靠人肉：</strong>一次失败要同时看 CI、容器日志、监控告警三个地方，时间戳还得自己对。",
     "<strong>SaaS 排障要交日志：</strong>把私有仓库的构建日志上传给第三方工具，安全和合规往往过不了。"],
    ["装 CLI 并填自己的模型 key，支持的厂商见 README。",
     "接进 GitHub Actions，构建失败时自动触发排障。",
     "看它给出的根因判断和 diff，人工确认后再推。"],
    ["<strong>自托管加自带模型是给合规团队的：</strong>愿意为此付费的往往是跑私有 CI 的中大型公司，这类需求 SaaS 很难吃下。",
     "<strong>读日志比写代码更容易验收：</strong>根因对不对一眼能看出来，输出没有模糊地带，这是 agent 落地的好切口。",
     "<strong>public alpha 就冲上趋势：</strong>说明 CI 排障的缺口真实存在，但也意味着稳定性还不能进关键路径。"],
    ["ci-cd", "devops", "agent", "self-hosted", "reliability"])

add("google-research", "paper-orchestra", "Python", "5,493", "688", "454",
    "🔥 第 2 次上榜 +454★ —— Google Cloud AI Research 的多 agent 论文流水线，从实验日志和零散想法出发，出综述、正文、图表，最后给一份 LaTeX 稿。",
    ["<strong>时间花在排版上：</strong>写论文的大半精力用在文献综述和图表调整，真正的研究思考被压缩。",
     "<strong>日志到成稿要重写三遍：</strong>实验记录的散碎结论和论文的论证结构之间没有自动通道，每次都靠人重新组织。",
     "<strong>LaTeX 细节反复踩坑：</strong>投稿模板的引用格式、图表位置、双语摘要，改到最后一天还在调。"],
    ["按 README 装依赖，准备 ideas 和 experimental logs 作为输入。",
     "跑 Outline → Literature Review → Section Writing → Refinement → Plotting 五段流水。",
     "生成的 LaTeX 直接进 Overleaf 编译，图表和引用清单一起给出。"],
    ["<strong>官方出品代表一种立场：</strong>论文写作可以工序化，每个环节交给专门 agent，而不是让一个模型从头写到尾。",
     "<strong>先自动化综述这个顺序值得注意：</strong>综述是最耗时也最容易被质疑的部分，先做它等于先接管最重的体力活。",
     "<strong>5.4k★ 说明学术界态度分化：</strong>做研究的人反感自动写论文，做工具的人拿它当工作流样板，两边都在用它。"],
    ["research", "multi-agent", "latex", "academic", "automation"])

add("google-labs-code", "stitch-skills", "TypeScript", "11,124", "1,413", "315",
    "🔥 第 3 次上榜 +315★ —— Google Stitch 的官方 agent 技能包，按 Agent Skills 开放标准写，Codex、Gemini CLI、Claude Code、Cursor 都能装。",
    ["<strong>设计稿到代码靠手抄：</strong>Stitch 生成 UI 之后，把它们落到组件里没有任何交接机制，中间全靠人重新描述一遍。",
     "<strong>插件格式各自为政：</strong>同一套技能要分别适配 Codex 的 marketplace、Claude Code 的插件目录，官方维护也吃力。",
     "<strong>生成和构建两段断开：</strong>设计阶段的产出物在构建阶段用不上，两边模型看到的是不同的上下文。"],
    ["Codex 用一行 <pre><code>codex plugin marketplace add google-labs-code/stitch-skills --ref main</code></pre> 装全套。",
     "用 stitch-design 出界面方向，stitch-build 负责落地成代码和组件。",
     "其他宿主可以手动把 skills 目录拷进各自的 skills 路径。"],
    ["<strong>Google 按开放标准发自家技能：</strong>Stitch 是自家产品，技能却写成第三方标准格式，抢的是 agent 生态的默认入口。",
     "<strong>design 与 build 拆成两个插件：</strong>按工程阶段切分技能，比塞进一个大包更符合真实工作流。",
     "<strong>315 的日增靠官方身份撑住：</strong>内容本身不惊艳，趋势位更多来自 Google 在 agent 生态里的位置。"],
    ["ui-design", "agent-skill", "google", "frontend", "standard"])

add("FlashML-org", "FreeVideo", "Python", "3,913", "545", "293",
    "🔥 首登 +293★ —— 8GB 显存跑 MiniMax H3：本地生视频、最高 16MP 图片，三个平台都有安装包，v0.4 起还能让 Claude Code 自己生成和剪辑。",
    ["<strong>视频模型几乎都在云上：</strong>按秒计费，素材要上传，做企业宣传片的团队过不了数据审查。",
     "<strong>本地门槛高：</strong>视频生成模型常要 24GB 显存起步，普通笔记本直接劝退。",
     "<strong>生成到剪辑要转码：</strong>片段出来还得进剪辑软件拼接，中间格式转换和音画对齐全靠手工。"],
    ["下对应平台的安装包，Windows、macOS arm64、Linux AppImage 都在 Releases 里。",
     "选质量档位先出半分辨率预览，确认后再渲染全分辨率，节省试错时间。",
     "v0.4 之后可以让 agent 通过命令行生成一分钟以上的视频，并在时间线里编辑。"],
    ["<strong>8GB 显存是消费级显卡的门槛线：</strong>把线压到这里就打开了笔记本市场，这是它比抽象能力更实在的卖点。",
     "<strong>加 agent 支持等于把生成变成可编排的一步：</strong>模型只是工具，能被脚本调用才有规模化价值。",
     "<strong>本地推理用时间换显存：</strong>四个质量档位本质是让用户自己选要花多少分钟换多少细节。"],
    ["video-generation", "local-inference", "minimax", "desktop", "gpu"])

TOPIC = ("🔥 <strong>今日主题：技能包抢班，本地生成抢量。</strong>"
         "13 个项目里 6 个是 Agent 技能或插件——渗透测试（Claude-BugHunter）、App 审核（app-store-compliance）、"
         "画图（diagram-design）、UI 生成（stitch-skills）、选题调研（last30days-skill）、开发方法论（superpowers），"
         "共同点是把一个职业的经验压成可安装的目录；"
         "另一条线是生成能力从云端往本地搬，8GB 显存生视频（FreeVideo）、桌面机剪长视频（autoclip），"
         "按秒计费的生意在被拽下来。"
         "基建侧 firecrawl 打通取数、CLI-Anything 给软件造接口、opensre 把 CI 排障接走，agent 的作业范围在往运维和交付延伸。"
         "结论：这一轮的热度不在模型参数上，在「谁能定义 agent 的默认动作」——技能格式和宿主覆盖率，比多两个点的 benchmark 更决定谁被用起来。")

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
assert len(data["days"]) == 100, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-38s +%-6s %9s★ count=%d badge=%s" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"], p["badge"]))
