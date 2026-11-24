#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-24 榜单更新（gap=1 双栏：新面孔 6 + 连登 6）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-24"

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


# ---------------- 新面孔 ----------------
add("cursor", "plugins", "TypeScript", "19,046", "2,057", "359",
    "🔥 官方插件仓库落地 —— 今日 +359★，1.9 万★，第 5 次上榜。Google 全家桶、Salesforce、GitHub、Playwright、X 都写成了带 manifest 的插件，Cursor 把 IDE 做成了应用商店。",
    ["<strong>集成靠自己搓：</strong>把内部工具接进 AI 编辑器，历史上是每个团队各写一套胶水，没人管版本，彼此不兼容。",
     "<strong>权限边界说不清：</strong>第三方 SaaS 的授权散在各个自定义脚本里，审计时讲不明白 agent 到底能碰哪些数据。",
     "<strong>复用只能复制粘贴：</strong>想用别人写好的集成，没有可安装、可升级的分发单元，prompt 一贴就散。"],
    ["<pre><code>git clone https://github.com/cursor/plugins</code></pre> 每个插件目录自带 <pre><code>.cursor-plugin/plugin.json</code></pre>，读 manifest 即知它暴露的能力。",
     "从 Cursor 插件市场直接安装 third_party 下的 github、playwright、salesforce、google-sheets 等。",
     "照 create-plugin 脚手架写自己的集成，再用 agent-compatibility 插件校验与其它 agent 客户端是否兼容。"],
    ["<strong>判断：</strong>Cursor 今天比的不是模型，是哪家的 SaaS 先被写成插件。Google Docs/Sheets/Slides、Salesforce、Zoom、Docusign、X 一字排开，这是 IDE 抢分发入口的老剧本。",
     "<strong>判断：</strong>manifest 化比裸 MCP server 更进一步，前者有版本、有作者、有市场，后者只是协议。集成层的竞争正从协议转向应用商店。",
     "<strong>判断：</strong>thermos 这类「分支深度审查 + 并行子代理」插件已经把手伸到 code review 与合并流程，插件规范迟早要补上安全边界一章。"],
    ["cursor", "plugins", "ai-ide", "mcp", "integrations"])

add("microsoft", "markitdown", "Python", "198,198", "15,028", "246",
    "🔥 微软的文档清洗工 —— +246★，19.8 万★，第 5 次上榜。PDF、Word、PPT、Excel、音频、YouTube 统统转 Markdown，喂模型之前先把结构留住。",
    ["<strong>版面信息全丢：</strong>PDF 和 PPT 直接进模型，表格错行、标题当正文，检索质量从第一步就开始漏。",
     "<strong>八种库各自为政：</strong>Excel、Epub、ZIP、音频各要一套解析，维护成本比模型调用还高。",
     "<strong>上传即出门：</strong>交给云端转换服务，等于把内部文档送出去，合规先卡住。"],
    ["<pre><code>pip install 'markitdown[all]'</code></pre> 一次装齐 PDF/Office/音频支持。",
     "代码里两行：<pre><code>from markitdown import MarkItDown\nMarkItDown().convert('a.pdf').text_content</code></pre>",
     "命令行批量：<pre><code>markitdown report.docx &gt; report.md</code></pre>，再喂给分块与向量化流程。"],
    ["<strong>判断：</strong>RAG 的效果上限在清洗这一步就定了。README 明说输出「给人看不是最优，给文本分析工具用」，这句话本身就是对工程化 RAG 的承认。",
     "<strong>判断：</strong>19.8 万★ 意味着「文档转 Markdown」已经是事实标准管道。微软不是靠模型赢，是把脏活做成了一个库。",
     "<strong>判断：</strong>README 开头那段安全警告（按当前进程权限读写，非信任输入要收窄 convert_* 调用）值得直接抄进团队代码评审清单。"],
    ["markdown", "document", "rag", "python", "microsoft"])

add("google-research", "paper-orchestra", "Python", "6,248", "806", "241",
    "🔥 Google 把写论文拆成流水线 —— +241★，6,248★，第 3 次上榜。大纲、文献、成稿、润色、画图五个 agent 接力，输出能直接套会议模板的 LaTeX。",
    ["<strong>中间那段最耗人：</strong>从「想法 + 实验日志」到投稿稿，文献综述要翻几十篇，图表要重画，模板一改全乱。",
     "<strong>多 agent 各写一段容易互相矛盾：</strong>引言承诺的结论，到方法节就消失了。",
     "<strong>格式返工：</strong>CVPR、ACL 模板要求不同，每次投稿等于重排一遍。"],
    ["<pre><code>conda create -n paper_orchestra python=3.11 &amp;&amp; pip install -r requirements.txt</code></pre>",
     "在 <pre><code>.env</code></pre> 里填 SEMANTIC_SCHOLAR_API_KEY 与 OPENAI_API_KEY 或 VERTEX_AI_PROJECT。",
     "<pre><code>python paper_writing_cli.py --raw_materials_dir ./raw --latex_template_dir templates/cvpr2025 --use_plotting true</code></pre>"],
    ["<strong>判断：</strong>卖点不是「AI 写论文」，是把不可控的多 agent 写作收敛成有模板、有检查点的流水线。模板目录本身就是约束条件。",
     "<strong>判断：</strong>要 Semantic Scholar key 加 GPT/Gemini 调用，说明核心是检索与编排，不是自研模型。这类框架的壁垒在 prompt 与评估集，不在算力。",
     "<strong>判断：</strong>学界的代写争议不会因为工具好用就消失，但它先把文献综述这段最机械的活自动化了，投稿门槛因此前移。"],
    ["multi-agent", "research", "latex", "google", "automation"])

add("p-e-w", "heretic", "Python", "42,937", "5,366", "194",
    "🔥 不改权重也能改性格 —— +194★，4.3 万★，第 7 次上榜。用对比 prompt 加打分器做白盒「消磁」，一下午在自己的显卡上跑完。",
    ["<strong>微调的门槛太高：</strong>去掉拒答行为要算力和标注数据，普通人做不了。",
     "<strong>abliteration 靠口口相传：</strong>参数散在论文和脚本里，调错一个就废掉模型。",
     "<strong>效果无法度量：</strong>跑完只有体感，不知道拒答率降了多少、能力掉了多少。"],
    ["<pre><code>pip install -U heretic-llm</code></pre>",
     "<pre><code>heretic Qwen/Qwen3-4B-Instruct-2507</code></pre> 默认动作就是去拒答。",
     "换目标行为用 config.nosyco.toml、config.noslop.toml、config.emotions.toml，或用 <pre><code>HERETIC_CONFIG_FILE</code></pre> 指路径。"],
    ["<strong>判断：</strong>默认动作是去拒答，no-slop、no-humor、no-sycophancy 都只是配置项。工具本身中立，用法决定它在谁手里。",
     "<strong>判断：</strong>README 引了第三方 MMLU/GSM8K 对比，说比同类 abliteration 更「外科手术」。可复现的第三方评测比自吹 demo 更能撑住 4 万★。",
     "<strong>判断：</strong>训练无关加 4bit 量化，把模型改造成本压到一张游戏显卡。开源权重的「可修改性」从口号变成了命令行。"],
    ["llm", "abliteration", "model-editing", "quantization", "safety"])

add("openvinotoolkit", "openvino", "C++", "12,390", "3,686", "187",
    "🔥 Intel 的推理工具箱回到榜上 —— +187★，1.2 万★，第 2 次上榜。把训练好的模型压到 CPU、核显和 NPU 上跑，先别急着买卡。",
    ["<strong>离开独显就慢：</strong>模型在 PyTorch 里正常，一到只有核显的机器上就卡到不能用。",
     "<strong>后端各一套坑：</strong>ONNX、TensorRT、各家 NPU SDK 写法不同，同一模型要维护多套部署代码。",
     "<strong>量化掉点无感：</strong>压完精度掉了，没人告诉你掉在哪一层。"],
    ["<pre><code>pip install openvino</code></pre>，也有 conda、brew、npm 的 openvino-node。",
     "两步拿到推理对象：<pre><code>ov.convert_model(...)</code></pre> 后 <pre><code>ov.compile_model(..., 'CPU')</code></pre>，设备名换成 GPU 或 NPU 即可。",
     "跑 LLM 用配套的 openvino.genai，量化用 NNCF，对照官方 benchmark 页面看收益。"],
    ["<strong>判断：</strong>它在榜上说明边缘推理这条线仍在热。云端 GPU 越贵，想把模型压进现有硬件的人越多。",
     "<strong>判断：</strong>多后端加多硬件，真正省下的不是算力费，是「同一份模型到处部署」的工程成本。",
     "<strong>判断：</strong>它和 vLLM 不在一个赛道。一个抢吞吐，一个抢手边这台机器能不能跑；端侧 agent 落地绕不开后者。"],
    ["inference", "openvino", "intel", "edge-ai", "optimization"])

add("Imbad0202", "academic-research-skills", "Python", "58,382", "4,457", "160",
    "🔥 把论文流程写成 Claude 技能 —— +160★，5.8 万★，第 4 次上榜。研究、写作、评审、修改、定稿五个阶段各有 skill，还带 Zenodo DOI 和七种语言文档。",
    ["<strong>一段段生成，前后不连贯：</strong>用 AI 写论文最常见的结果是每一节都通顺，合起来不像一篇。",
     "<strong>流程每次重启：</strong>不同期刊格式、审稿意见回应，全靠人脑记着走。",
     "<strong>经验不可复用：</strong>好用的 prompt 躺在聊天记录里，换个人就得重教。"],
    ["<pre><code>/plugin marketplace add Imbad0202/academic-research-skills</code></pre>",
     "<pre><code>/plugin install academic-research-skills</code></pre> 装完即可用。",
     "<pre><code>/ars-plan</code></pre> 用苏格拉底式提问把论文结构走一遍，再逐节推进。"],
    ["<strong>判断：</strong>CC BY-NC 4.0 加 Zenodo DOI，作者是按学术软件的标准在做这个项目，许可与引用都替使用者想好了。",
     "<strong>判断：</strong>把研究流程切成分阶段 skill，比一个万能 prompt 稳。技能包类仓库能连续上榜，原因就在于分发单元变了。",
     "<strong>判断：</strong>非商用许可意味着它很难进企业流水线，但对研究生和个人研究者，这是最快的起点。"],
    ["claude-skills", "research", "academic", "writing", "plugin"])

# ---------------- 连登 ----------------
add("elementalsouls", "Claude-BugHunter", "Python", "20,809", "2,187", "1,833",
    "🔥 今日全场最高 +1,833★ —— 2 万★，第 6 次上榜。84 个技能、15 个 slash command、681 条已披露报告模式覆盖 24 类漏洞，装进 Claude Code 就能开工。",
    ["<strong>挖洞靠个人经验：</strong>思路散在笔记和脑子里，交接等于重新摸索。",
     "<strong>同类漏洞反复踩：</strong>没有一个可检索的已披露模式库，每次从零开始。",
     "<strong>准备工作的隐形耗时：</strong>靶场搭好、报告模板写完，半天过去了。"],
    ["把仓库里的 skills 目录放进 Claude Code 的技能路径，重启会话。",
     "用 15 个 slash command 进入具体环节：侦察、枚举、利用、写报告。",
     "接 Burp MCP 后在授权范围内跑，README 声明只在授权红队与公开靶场（DVWA、Juice Shop、Hacker101）验证过。"],
    ["<strong>判断：</strong>把别人的披露报告整理成可执行模式，才是这个仓库的资产。681 条里 433 条逐条标注出处，这种可审计性在安全圈很稀缺。",
     "<strong>判断：</strong>24 类漏洞加企业身份与基础设施攻击矩阵，覆盖的是外网红队的标准作业面，不是脚本合集。",
     "<strong>判断：</strong>合法性完全取决于使用者的授权边界。榜上很少有项目把这句话写进 README 第一段。"],
    ["security", "red-team", "claude-skills", "bug-bounty", "pentest"])

add("HKUDS", "CLI-Anything", "Python", "64,337", "5,866", "1,075",
    "🔥 给所有软件套一层 CLI 让 agent 能用 —— +1,075★，6.4 万★，第 11 次上榜。18 个真实应用 demo、2,461 个测试通过，cli-hub install 一键装别人的 harness。",
    ["<strong>GUI 软件没有 API：</strong>agent 只能靠截图点鼠标，慢且脆，一次改版就失效。",
     "<strong>适配层写一次用一次：</strong>每个软件单独写包装，写完没人复用。",
     "<strong>输出格式不统一：</strong>agent 解析结果全靠猜，换个软件就得改 prompt。"],
    ["<pre><code>pip install cli-anything-hub</code></pre>",
     "<pre><code>cli-hub install &lt;name&gt;</code></pre> 浏览并安装社区已建好的 CLI。",
     "自己建 harness 后提 PR，hub 会立即更新，门槛比发布一个 SDK 低。"],
    ["<strong>判断：</strong>它赌的是明天的用户是 agent。把 GUI 软件降维成命令行，是最笨也最稳的给 agent 装手脚的办法。",
     "<strong>判断：</strong>2,461 个测试、18 个 demo 让产出物可验证（CAD、3D 场景、字幕、示意图），这比同类 prompt 包装项目高一个层级。",
     "<strong>判断：</strong>中心化 hub 加社区提 PR，本质是在抢 agent 与软件之间的标准接口，这个位置比单个工具值钱。"],
    ["cli", "agent", "harness", "automation", "agent-native"])

add("obra", "superpowers", "Shell", "325,623", "28,881", "1,006",
    "🔥 第 26 次上榜的老熟脸 —— +1,006★，32.5 万★。给编码 agent 装一套开发方法论：先问清要什么，再分块读规格，然后才写代码。",
    ["<strong>一看到需求就开写：</strong>agent 写到一半发现方向错了，返工比从头做还贵。",
     "<strong>规格没人读完：</strong>几十页文档写完就躺在仓库里，执行时没人对照。",
     "<strong>换客户端就重教：</strong>不同 agent 的工作流各说各话。"],
    ["按 README 的安装段选自己的客户端：Claude Code、Codex、Cursor、Gemini CLI、Copilot CLI、Hermes Agent 等十几个都有对应命令。",
     "启动后它会主动追问真实目标，并把 spec 拆成能读完的小块。",
     "走偏了按 When Something Goes Wrong 一节的回退流程重来，而不是继续堆 prompt。"],
    ["<strong>判断：</strong>26 次上榜已经不靠新鲜度，靠装机量。跨十几个客户端的安装表就是它的分发策略。",
     "<strong>判断：</strong>它卖的不是技能，是纪律：把先想清楚再动手固化进流程，比任何模型升级都省钱。",
     "<strong>判断：</strong>方法论类项目能长期霸榜，说明工具层已饱和，稀缺的是知道什么时候不该让 agent 继续写。"],
    ["agent", "methodology", "claude-code", "workflow", "skills"])

add("firecrawl", "firecrawl", "TypeScript", "208,494", "10,896", "990",
    "🔥 抓网页给 agent 吃 —— +990★，20.8 万★，第 4 次上榜。搜索、抓取、接 550+ 数据源走同一个 API，吐出来直接是干净 Markdown。",
    ["<strong>爬虫写完就失效：</strong>反爬策略一改，解析全崩，维护像打地鼠。",
     "<strong>噪声吃掉上下文：</strong>抓下来的页面一半是导航和广告，token 花在没用的地方。",
     "<strong>十套解析并行：</strong>搜索、网页、结构化站点各接各的，最后没人敢动。"],
    ["用官方 SDK 或 /scrape、/crawl 端点，一次调用拿到 markdown。",
     "不想托管就自部署开源版，跑在自己的机器上。",
     "配 /search 或数据源接口做检索增强，别把抓取和检索拆成两条线。"],
    ["<strong>判断：</strong>20.8 万★ 的爬虫项目，护城河不在爬，在清洗加结构化，以及 550 个数据源的接入量。",
     "<strong>判断：</strong>开源版能自部署，但托管服务才是主要收入。用之前先想清楚数据允不允许出门。",
     "<strong>判断：</strong>agent 的瓶颈正从模型不够聪明转向喂进去的上下文太脏，这类基础设施还会继续吃红利。"],
    ["scraping", "rag", "api", "markdown", "data"])

add("zhouxiaoka", "autoclip", "Python", "15,103", "2,254", "981",
    "🔥 一条链接剪出短视频 —— +981★，1.5 万★，第 5 次上榜。本地跑，自动找高光、跟踪人脸、烧字幕、出封面，适配抖音、小红书、B 站和 Shorts。",
    ["<strong>人工过一遍太慢：</strong>两小时播客剪成切片，选段和裁切能占掉半天。",
     "<strong>素材不想上传：</strong>云端剪辑等于把原始文件交出去，访谈类内容更敏感。",
     "<strong>配套工作琐碎：</strong>字幕、封面、标题每样都要单独做一遍。"],
    ["从 releases 下载桌面版（Tauri 构建，Windows/macOS/Linux）。",
     "拖入链接、本地文件或直播回放，选平台比例后导出。",
     "完全离线：配 Ollama 或 LM Studio 加 Whisper / SenseVoice，自带 API key 则走云端模型。"],
    ["<strong>判断：</strong>本地优先、MIT 许可、自带 key 三种模式，直接把素材不出门做成了卖点，这在同类闭源工具里少见。",
     "<strong>判断：</strong>13 种语言的界面说明它从第一天就瞄准海外创作者，不只是国内短视频工具。",
     "<strong>判断：</strong>真实对手是剪映的自动化功能。开源项目的优势是流程可改、能接自己的模型。"],
    ["video", "clipping", "local-first", "captions", "creator"])

add("jingyaogong", "minimind", "Python", "69,962", "9,116", "727",
    "🔥 3 块钱 2 小时训出 64M 小模型 —— +727★，7 万★，第 5 次上榜。从预训练到 RLHF、Agentic RL、蒸馏整条链路全开源，单卡可复现。",
    ["<strong>教程停在调 API：</strong>想从零训一个模型，找不到完整可跑的代码。",
     "<strong>论文与实现差一截：</strong>训练细节、数据清洗、超参，论文里不会写全。",
     "<strong>RLHF 无处下手：</strong>PPO、DPO、GRPO 讲得多，能跑起来的项目少。"],
    ["<pre><code>git clone https://github.com/jingyaogong/minimind</code></pre> 后按 README 装依赖。",
     "下载 MiniMind 数据集，按 Pretrain、SFT、LoRA/DPO、RLAIF 顺序跑各阶段脚本。",
     "同一仓库还有 MiniMind-V 视觉版、-O 多模态版、-dLM 扩散语言模型可参考。"],
    ["<strong>判断：</strong>主线模型约是 GPT-3 的 1/2700，价值不在能力，在每一个环节都能自己搓一遍。",
     "<strong>判断：</strong>覆盖 MoE、数据清洗、RLAIF（PPO/GRPO/CISPO）、Tool Use、Agentic RL，这份覆盖面比很多付费课程完整。",
     "<strong>判断：</strong>中文项目、中文文档、单卡成本，是它反复上榜的原因：教学类项目的复访率天然高于工具类。"],
    ["llm", "from-scratch", "training", "rl", "tutorial"])

TOPIC = ("🔥 <strong>今日主题：热度不在模型，在「AI 怎么被装进软件」。</strong>"
         "Cursor 把官方插件写成带 manifest 的应用商店、CLI-Anything 给 GUI 软件套一层命令行、superpowers 给编码 agent 灌方法论，三者抢的是同一个位置：agent 与现有软件之间的接口。"
         "另一条线是上下文清洗，markitdown 把文档转成 Markdown、firecrawl 把网页洗成干净输入，它们的共同前提是模型已经够用，脏数据才是瓶颈。"
         "判断：工具层已经饱和，接下来比的是谁定义标准、谁掌握分发。")

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
assert len(data["days"]) == 103, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-40s %-6s +%-6s %9s★ count=%d" % (
        p["rank"], p["fullName"], p["badge"], p["starsToday"], p["stars"], p["count"]))
