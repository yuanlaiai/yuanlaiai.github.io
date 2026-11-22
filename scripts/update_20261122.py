#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-22 榜单更新（gap=1，双栏：新面孔 1-6 / 连登 7-12）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-22"

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
add("cursor", "plugins", "TypeScript", "18,139", "1,981", "260",
    "🔥 第 5 次上榜 +260★ —— Cursor 官方的插件仓库，每个插件是根目录下一个独立文件夹，自带 .cursor-plugin/plugin.json 清单，从教学、记忆维护到分支深度审查都有人写。",
    ["<strong>插件各写各的：</strong>同一个团队里有人在 rules 里塞规范、有人在 MCP 里接服务、有人手写 slash command，新人进来找不到统一的入口。",
     "<strong>上下文不沉淀：</strong>agent 每轮对话都要重新交代项目约定，AGENTS.md 靠人手更新，写多了没人读，写少了不管用。",
     "<strong>审查靠自觉：</strong>分支提交前该看什么没有清单，安全问题和正确性问题混在风格争议里一起被放过。"],
    ["把插件目录拷到项目的 <pre><code>.cursor/plugins/</code></pre> 下，或在 Cursor 的插件面板里按清单安装。",
     "continual-learning 这类插件会从对话记录里抽取要点，增量更新 AGENTS.md，只留高信号条目。",
     "cursor-team-kit 和 thermos 覆盖 CI、代码审查、发布与验证，适合团队统一装同一套。"],
    ["<strong>清单即接口：</strong>把插件规范做成仓库里的一个 json，等于让第三方也能按同一格式提交，Cursor 在复制 VS Code 扩展市场的路子。",
     "<strong>记忆插件化是今年的新动向：</strong>continual-learning 这种「从对话里提炼 AGENTS.md」的插件，说明上下文管理正从模型侧挪到工程侧。",
     "<strong>官方仓库只有 18k★，热度不在代码量上：</strong>它卖的是生态位，装它的人是在赌 Cursor 成为团队默认编辑器。"],
    ["cursor", "plugins", "agent-tools", "memory", "code-review"])

add("openvinotoolkit", "openvino", "C++", "11,954", "3,652", "200",
    "🔥 第 2 次上榜 +200★ —— 英特尔的推理部署工具包，把训练好的模型优化后跑在 CPU、核显和 NPU 上，Python、Node、conda、brew 都能装。",
    ["<strong>模型落不了地：</strong>实验室里 PyTorch 跑得好好的模型，到客户那台没有独显的机器上就卡成幻灯片。",
     "<strong>硬件碎片化：</strong>同一份权重要在 x86 CPU、Intel 核显、NPU 上分别调优，量化、算子融合、内存布局每个后端一套说法。",
     "<strong>端侧没有标准路径：</strong>ONNX 只是中间格式，量化到 int8 之后的精度损失和速度收益要反复试。"],
    ["<pre><code>pip install openvino</code></pre> 或 brew 安装，先用模型转换工具把 ONNX/PyTorch 模型转成 IR。",
     "用 <pre><code>benchmark_app</code></pre> 在目标机器上测延迟和吞吐，再决定量化和线程配置。",
     "生成式模型走 openvino.genai 子项目，它给了 LLM 推理和连续批处理的封装。"],
    ["<strong>端侧推理是今年被低估的战场：</strong>云端 API 便宜，但延迟、隐私和断网三个问题只有本地能解，工具包的日增说明这部分需求在回流。",
     "<strong>英特尔在拿软件补硬件：</strong>核显和 NPU 的算力拼不过独显，靠工具链把利用率做上去，是它唯一能打的牌。",
     "<strong>11,954★ 不算高，但它是长跑型项目：</strong>这类基建不看热度看装机量，出现在趋势榜更像是被新硬件周期带上来的。"],
    ["inference", "edge-ai", "intel", "quantization", "deployment"])

add("microsoft", "markitdown", "Python", "197,599", "14,953", "182",
    "🔥 第 5 次上榜 +182★ —— 微软的轻量转换器，把 Word、PPT、Excel、PDF 转成保留标题、表格、链接结构的 Markdown，专门喂给 LLM。",
    ["<strong>喂给模型的文本是垃圾：</strong>PDF 抽出来一坨没有结构的字符串，标题和正文混在一起，表格变成错位的数字堆。",
     "<strong>格式太多各写一套：</strong>docx 用 python-docx、pptx 用 python-pptx、xlsx 再换一个库，每种格式的解析坑都不一样。",
     "<strong>结构在转换中丢失：</strong>层级、列表、表格关系一旦丢了，模型读到的信息量就少一半，检索也召回不准。"],
    ["<pre><code>pip install markitdown[all]</code></pre>，然后 <pre><code>markitdown file.pdf > out.md</code></pre> 直接转。",
     "代码里调 <pre><code>MarkItDown().convert(path)</code></pre>，批量处理时按需启用各格式的可选依赖。",
     "不可信输入场景下只用最窄的 convert_stream / convert_local，避免进程权限被文件路径利用。"],
    ["<strong>197k★ 说明文档解析是 RAG 的第一道坎：</strong>模型再强，喂进去的是错位的表格也答不对，转 Markdown 这个动作决定了检索质量的上限。",
     "<strong>微软把工具做成最小可组合件：</strong>不做平台、不做 UI，只做格式转换，反而成了各家管线的默认依赖。",
     "<strong>它有明确的安全边界提示：</strong>README 一开头就讲 I/O 权限，说明这类工具在企业内网落地时最先被问的是攻击面。"],
    ["markdown", "document-parsing", "rag", "microsoft", "converter"])

add("p-e-w", "heretic", "Python", "42,505", "5,285", "144",
    "🔥 第 7 次上榜 +144★ —— 不训练、只改权重方向：用一个下午在你游戏本上把开源模型的拒答倾向、谄媚和套话一起消掉。",
    ["<strong>拒答挡住了研究：</strong>做安全评测或红队的人，模型对敏感话题一律回「我不能协助」，实验做不下去。",
     "<strong>微调成本高：</strong>想改行为通常要准备数据集、跑 SFT 或 RLHF，一张卡几小时起步，改完还掉通用能力。",
     "<strong>副作用没法量化：</strong>手工调 ablation 强度，改完不知道模型整体退化了多少，只能凭感觉。"],
    ["<pre><code>pip install heretic-llm</code></pre>，指定本地模型路径直接跑，不需要数据集。",
     "默认用 ARA（任意秩消融）修改器，配合 Optuna 的 TPE 优化器搜索参数。",
     "用 scorer 插件给「拒答率」「谄媚度」「能力保持」分别设目标，让优化器在多目标间找解。"],
    ["<strong>把模型编辑做成了可调参数的工程问题：</strong>ARA 加 TPE 的组合，等于把「改行为」从炼丹变成有目标函数的搜索。",
     "<strong>训练-free 是它的传播力来源：</strong>不用数据、不用算力集群，一个人一下午就能复现，这比论文里的指标更能带来 star。",
     "<strong>风险跟着能力走：</strong>同一套方法既能做安全研究也能做规避对齐，AGPL 协议挡不住滥用，这类项目的伦理争议会一直跟着它。"],
    ["model-editing", "abliteration", "safety", "training-free", "llm"])

add("github", "spec-kit", "Python", "150,950", "13,557", "126",
    "🔥 第 4 次上榜 +126★ —— GitHub 官方的规格驱动开发工具包，用 /specify 起步，把「想做什么」写成规格，再让 agent 按规格实现、按规格验收。",
    ["<strong>Agent 边写边猜：</strong>需求只在对话里说了一遍，实现到一半方向偏了，回头发现连「完成」的定义都没写下来。",
     "<strong>文档和代码两张皮：</strong>设计文档在 wiki 里烂掉，代码按另一套逻辑演进，没人知道哪个是准的。",
     "<strong>修 bug 没有流程：</strong>报错就改，改完不知道根因是什么、改了什么、怎么验证没回归。"],
    ["<pre><code>uvx --from git+https://github.com/github/spec-kit.git specify init my-project</code></pre> 初始化项目。",
     "用 /specify 写规格、/plan 出技术方案、/tasks 拆任务，三步之后才允许写代码。",
     "修 bug 和评估想法是两个独立扩展，按需装上，不必走同一套流程。"],
    ["<strong>GitHub 在给 agent 立规矩：</strong>它把「先写规格」变成官方推荐的默认动作，等于承认自由发挥的编码 agent 在生产环境里不靠谱。",
     "<strong>150k★ 的量级说明 SDD 已经不是小众方法论：</strong>规格成为可执行资产之后，代码变成它的实现细节，这个转向对工程管理的影响比工具本身大。",
     "<strong>三个独立入口的设计值得注意：</strong>建功能、修 bug、评估想法各走一条路，说明作者不想把方法论做成一刀切的仪式。"],
    ["spec-driven", "sdd", "coding-agent", "github", "workflow"])

add("phone-harness", "phone-harness", "Python", "5,459", "567", "125",
    "🔥 第 2 次上榜 +125★ —— 让 agent 用你的手机：iPhone 抓镜像窗口做 OCR 再注入点击，安卓走 adb，云手机走同一套接口。",
    ["<strong>移动端没有自动化入口：</strong>桌面有命令行和 API，手机上绝大多数操作只能人手点，批量任务没法交给 agent。",
     "<strong>跨平台脚本要重写：</strong>iOS 的自动化限制严，安卓的 adb 是另一套，同一件事写两遍还不通用。",
     "<strong>App 内数据出不来：</strong>预约、抢号、签到这类操作在 App 里，没有开放接口，网页版又常常缺功能。"],
    ["<pre><code>phone-harness config set platform ios|android</code></pre> 选定默认设备。",
     "iPhone 端开启镜像窗口，脚本读 OCR 文本、发点击滑动输入；安卓端走 USB 或 Wi-Fi 的 adb。",
     "同一份脚本换平台不用改，云手机通过同一层接口接入。"],
    ["<strong>它绕开的是「App 没有 API」这个结构性问题：</strong>OCR 加输入注入等于给任何 App 补一层机器可用的接口，代价是速度和稳定性。",
     "<strong>OCR 只看文本不看图标：</strong>README 自己写明了这个限制，无标签按钮仍然需要人，这也是它现在只能做半自动的原因。",
     "<strong>5,459★ 的小项目能上榜：</strong>说明「让 agent 碰我的手机」是明确的需求缺口，但设备解锁、验证码这些环节决定了它短期内进不了生产。"],
    ["mobile", "agent-tools", "ocr", "adb", "automation"])

# ------------------------------------------------ 连登 ----
add("elementalsouls", "Claude-BugHunter", "Python", "16,223", "1,841", "1,803",
    "🔥 连登第 4 天 +1,803★ —— 昨天 +1,622 已经是榜首，今天又涨了 1,803，总星从 14,679 跳到 16,223，一天加了近 1,544。",
    ["<strong>方法论不落地：</strong>渗透测试的流程散在博客和付费课里，新手跑完扫描器就以为结束了，缺从信息收集到复现到报告的非线性推进。",
     "<strong>Agent 没有攻击者姿态：</strong>Claude Code 默认是写代码的助手，碰到 SSRF 绕过、原型链污染这类需要主动构造假设的活，得人一句句喂提示词。",
     "<strong>范围控制靠人记：</strong>授权清单常常只存在开工会议的 PPT 里，agent 没有天然边界感。"],
    ["把 skills 目录拷进 <pre><code>~/.claude/skills</code></pre> 或项目的 <pre><code>.claude/skills</code></pre>，重开 Claude Code。",
     "用 <pre><code>/bb-methodology</code></pre> 起手，按信息收集、威胁建模、验证、利用、报告五段推进。",
     "需要看真实流量时接 Burp MCP，把请求响应交给 agent 判断。"],
    ["<strong>连续两天各涨 1,600 以上，说明它在被装机而不是被阅读：</strong>技能包的传播路径是安装和转发目录，装完就留在机器里，日增因此有复利。",
     "<strong>83 个技能对应 681 份公开报告：</strong>这个压缩比是它唯一难以复制的地方，别人照抄目录也复现不了案例库。",
     "<strong>榜首两天的信号意义大于数字：</strong>安全类技能包第一次在日榜上压过通用开发工具，说明愿意为 agent 装攻击能力的人比想象中多。"],
    ["security", "claude-code", "skills", "red-team", "bug-bounty"])

add("firecrawl", "firecrawl", "TypeScript", "206,306", "10,787", "1,006",
    "🔥 连登第 2 天 +1,006★ —— 昨天首登 +1,241，今天继续站在第二，总量 20.6 万★，抓取基建的需求没有随热点波动。",
    ["<strong>Token 花在噪声上：</strong>agent 抓回来的页面夹着导航、广告和 script，有用正文不到三成。",
     "<strong>反爬挡在门外：</strong>requests 加 BeautifulSoup 遇到 JS 渲染和 Cloudflare 就整页空，自建 headless 又是一摊工程。",
     "<strong>输出形状不统一：</strong>同一件事在十个站点有十种 HTML 结构，进 RAG 前还得写十套清洗规则。"],
    ["<pre><code>docker run -p 3002:3002 firecrawl/firecrawl</code></pre> 自托管，或直接调云 API 按页计费。",
     "<pre><code>app.scrape_url(url, formats=['markdown'])</code></pre> 拿正文，crawl 模式可抓整站。",
     "挂成 MCP 工具，agent 就同时有 search 和 scrape 两种取数方式。"],
    ["<strong>连续两天高位说明它不是被热点推起来的：</strong>抓取层属于一旦接进管线就不太会换的依赖，star 增长更接近装机量的镜像。",
     "<strong>AGPL 让它能同时服务两类客户：</strong>自托管用户免费拿能力，闭源产品内嵌就要谈授权，开源边界画得很精。",
     "<strong>550+ 站点的预配置是真资产：</strong>通用爬虫谁都能写，几千小时的站点适配没法一夜补齐。"],
    ["crawler", "rag", "markdown", "agent-infra", "self-hosted"])

add("obra", "superpowers", "Shell", "323,801", "28,721", "883",
    "🔥 连登第 24 天 +883★ —— 32.4 万★，第 24 次上榜。这个数字本身已经比任何单日涨幅更有信息量：它在榜上活了一个多月。",
    ["<strong>Agent 上手就写：</strong>没有流程约束时会跳过调研和方案讨论，一口气产出几百行跑不通的代码。",
     "<strong>技能格式各不相同：</strong>Claude Code 的插件、Codex 的 marketplace、Cursor 的 rules 互不兼容，同一套工作流要在每个宿主重写。",
     "<strong>自评代替验证：</strong>agent 把「已完成」当成事实，测试没跑、边界没测，交付时才暴露。"],
    ["按自己宿主的 README 安装，Claude Code 走插件市场，Codex 走 marketplace add，也支持手动拷 skills 目录。",
     "照它的节奏走：头脑风暴 → 写计划 → 分步执行，每步都要 agent 先给方案。",
     "收尾调 review 技能，让另一个 agent 视角检查实现和测试。"],
    ["<strong>24 天上榜是同一种机制的结果：</strong>它不靠新功能留人，靠的是宿主列表在变长，每接一个新 agent 就多一批用户重新 star。",
     "<strong>覆盖率比方法论更值钱：</strong>15 个宿主的适配工作没有技术难度，只有琐碎，愿意做的团队很少。",
     "<strong>它在给 agent 装纪律：</strong>当前模型的失败模式不是不会写，而是不愿意停，这套流程的核心动作就是强制先输出计划。"],
    ["agent-workflow", "methodology", "skills", "coding-agent", "cross-platform"])

add("HKUDS", "CLI-Anything", "Python", "62,140", "5,638", "769",
    "🔥 连登第 9 天 +769★ —— 继续给软件套命令行外壳，昨天 +773 今天 +769，两天几乎同速，说明使用面在稳步铺开而不是脉冲式爆红。",
    ["<strong>GUI 没有接口：</strong>只有鼠标能操作的地方，agent 只能截屏加坐标点击，一个弹窗就全乱。",
     "<strong>每个应用重写一遍：</strong>自动化脚本按软件定制，Photoshop 一套、Blender 一套，维护成本比开发还高。",
     "<strong>像素输出不可组合：</strong>截图里既没有参数也没有错误码，agent 拿不到可以判断的结构化结果。"],
    ["去 <pre><code>clianything.cc</code></pre> 的 CLI-Hub 找目标软件对应的包装器。",
     "按条目里的命令装上，直接在 shell 里跑，输出是结构化的。",
     "把命令写成 agent 的工具描述，让它按需调用而不是操作界面。"],
    ["<strong>两天同速增长比爆发更能说明问题：</strong>脉冲式项目通常在第二天腰斩，它稳在 770 左右，意味着每天有新增用户在装。",
     "<strong>这条路的天花板在长尾：</strong>热门软件早就有人写包装器，真正的活是把那些没人愿意适配的中小工具一个个补上。",
     "<strong>把接口面从像素拉回文本：</strong>稳定性和可测试性一起上来了，重跑一次不会因为按钮挪两像素就失败。"],
    ["cli", "agent-tools", "automation", "desktop", "interop"])

add("mjmirza", "app-store-compliance", "Shell", "3,468", "214", "720",
    "🔥 连登第 2 天 +720★ —— 昨天首登 2,902★，今天 3,468★，一天涨了 566 星、日增仍有 720，小仓库被移动团队当成提交前卡点装走了。",
    ["<strong>条款藏得深：</strong>被拒的原因多是隐私清单缺失、权限说明含糊、账号删除路径没做，要求分散在两份很长的审核文档里。",
     "<strong>一次拒审就是几天：</strong>改完要重新排队，小团队最怕这种不可控等待。",
     "<strong>检查没有卡点：</strong>团队知道要合规，但没把它变成提交前的自动检查，靠人记必然漏项。"],
    ["当网页读 <pre><code>mjmirza.github.io/app-store-compliance</code></pre>，按拒审理由类别检索。",
     "把 guard 脚本接进 CI，提交前扫 Info.plist 和 AndroidManifest 里的隐私与权限声明。",
     "在 Claude Code 里让它对着条款解释具体拒审理由，比自己读一遍文档快。"],
    ["<strong>2,902★ 的小仓库一天加 566 星，是典型的「被团队内部分享」曲线：</strong>它解决的问题在提交节点上，谁踩过坑谁就会转给同事。",
     "<strong>合规工具的价值不在准确率，在把隐性知识写成清单：</strong>117 条理由的颗粒度，正好是能照着改的程度。",
     "<strong>它只有 Shell 和文档，没有模型：</strong>这说明 agent 时代的工具不一定要是 AI 产品，能被 agent 调用就够了。"],
    ["app-store", "compliance", "ci", "mobile", "claude-code"])

add("zhouxiaoka", "autoclip", "Python", "12,929", "2,077", "683",
    "🔥 连登第 3 天 +683★ —— 贴链接一键出片，本地渲染竖屏短视频，昨天 +979 之后今天仍有 683，热度在回落但没掉队。",
    ["<strong>切点靠人找：</strong>一集 90 分钟的访谈剪三条短视频，人工找爆点加调字幕两小时起步。",
     "<strong>一稿多投要重做：</strong>竖屏比例、时长上限、封面尺寸每个平台都不一样，同一条内容得导出四遍。",
     "<strong>素材上传有顾虑：</strong>云端剪辑按次收费，客户的未公开访谈要先传给别人的服务器。"],
    ["去 Releases 下桌面版（Tauri 打包，MIT 协议），安装后本地运行。",
     "贴视频链接或拖本地文件，选目标平台，等本地渲染。",
     "切点不满意就进内置编辑器手动调，改完重新导出。"],
    ["<strong>第二天回落到 683 属于正常曲线：</strong>工具类项目首日靠新鲜感，第二天看的是真正用起来的人有多少，这个数说明留存还行。",
     "<strong>它的竞争对手不是剪映而是时间：</strong>一条访谈剪三条，人工两小时、工具十分钟，省下来的时间就是它的定价依据。",
     "<strong>本地渲染是它的差异化：</strong>素材不出门这一条，对企业访谈和未发布内容来说比任何模板都重要。"],
    ["video-editing", "shortvideo", "local-first", "tauri", "content-tools"])

TOPIC = ("🔥 <strong>今日主题：技能包的第二天，比第一天更狠。</strong>"
         "通用榜 16 行里 11 行是昨天上过的项目，真正的新面孔日增最高只有 +260；"
         "而昨天的头名 Claude-BugHunter 连着两天各涨 1,600 以上，app-store-compliance 从 2,902★ 冲到 3,468★，"
         "autoclip 第三天还有 +683。"
         "技能包的传播方式是安装不是阅读，装进机器就留下来了，日增因此有复利；"
         "通用工具则要靠新功能续命，firecrawl、CLI-Anything 两天同速说明它们已经变成管线里的固定件。"
         "反过来看今天的六个新面孔——cursor/plugins、openvino、markitdown、heretic、spec-kit、phone-harness——全是复访老人或老基础设施，"
         "没有新品类长出来。"
         "结论：这一轮趋势榜的驱动力是装机量和团队内部转发，不是发布新项目；判断一个项目能不能留住，看第二天和第三天的日增，别看第一天。")

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
assert len(data["days"]) == 101, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-38s +%-6s %9s★ count=%d badge=%s" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"], p["badge"]))
