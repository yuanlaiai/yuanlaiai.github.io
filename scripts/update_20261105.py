#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-05（距上次更新 2 天，flat day：全部新面孔）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-05"

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


add("NVIDIA", "auto-ontology", "Python", "6,456", "509", "2,707",
    "🔥 亮点 —— 今日 +2,707★ 第一，6,456★ 首登。NVIDIA 开源的语义层框架：把企业元数据编成知识图谱，告诉 agent 每个指标怎么定义、数字从哪来、能不能拿来算。",
    [
        "<strong>agent 查数快但不敢用：</strong>问一句营收，它给一个数，你没法确认这个营收和财务口径是不是同一个。",
        "<strong>同名指标到处不一致：</strong>BI 里一套定义、数据仓库一套、业务表格又一套，agent 撞上哪个算哪个。",
        "<strong>生成 SQL 没有验收：</strong>查询跑出来了，结果对不对没人校验，错了也没人知道错在哪。",
    ],
    [
        "克隆仓库，<code>cp .env.example .env</code> 填 NVIDIA API key（build.nvidia.com 申请）。",
        "用 Docker Compose 起示例，接 Wide World Importers 这个微软示例销售库先跑通。",
        "通过 MCP、CLI 或 API 把上下文层接进自己的 agent，生成查询时对着认证过的定义校验并返回来源。",
    ],
    [
        "<strong>它不生成任何内容，只负责让生成可信：</strong>在所有人都往上堆功能的时点，NVIDIA 卖的是约束。",
        "<strong>把「指标定义」变成可查询对象：</strong>这一步做完，agent 的分析才可能被财务部门接受，否则永远停在 demo。",
        "<strong>每次纠错回写进本体：</strong>用得越久越准，这是数据资产能复利的地方，也是它敢开源的原因。",
    ],
    ["ontology", "text-to-sql", "semantic-layer", "mcp", "nvidia"])

add("vercel-labs", "agent-desktop", "Rust", "16,213", "1,131", "2,173",
    "🔥 亮点 —— +2,173★，1.62万★，连续第二次上榜。两天涨了 4,496★。走操作系统无障碍树操作桌面应用的 CLI，元素带 ref，点完再快照核对，不做像素匹配。",
    [
        "<strong>截图方案不可靠：</strong>让多模态模型看屏幕找按钮，分辨率一变或弹窗一挡就点错，还烧 token。",
        "<strong>坐标点击太脆：</strong>窗口一移动，整段脚本报废。",
        "<strong>桌面应用没有接口：</strong>报销、ERP、老客户端不给 API，agent 只能停在浏览器里。",
    ],
    [
        "<code>agent-desktop list-apps</code> 看能接管哪些应用。",
        "<code>agent-desktop snapshot --app Finder -i</code> 返回带 ref 的交互元素 JSON。",
        "<code>agent-desktop click @s8f3k2p9:e8</code> 操作后重新快照，循环控制权留给 agent。",
    ],
    [
        "<strong>两天翻一倍还多：</strong>11,717★ 到 16,213★，说明桌面操作不是小众需求，浏览器内的 agent 早就撞到天花板了。",
        "<strong>无障碍树是被忽视的现成基础设施：</strong>它本来为读屏软件而生，结构化程度恰好够机器用。",
        "<strong>Vercel 在做入口生意：</strong>网页之后是桌面，谁先抽象掉操作系统这一层，谁就握住 agent 的行动能力。",
    ],
    ["computer-use", "accessibility", "cli", "rust", "automation"])

add("mattpocock", "skills", "Shell", "314,285", "26,340", "2,053",
    "🔥 亮点 —— +2,053★，31.43万★，第 13 次上榜。日常工程技能集，小而可组合、鼓励改成自己的，明确反对把流程收走的框架。",
    [
        "<strong>流程框架替你握方向盘：</strong>出问题时你连从哪查都不知道。",
        "<strong>大而全的规范比代码慢：</strong>文档写一堆，最后没人读。",
        "<strong>绑死某个 agent 等于自废武功：</strong>模型换代，写法全废。",
    ],
    [
        "按 README 的 30 秒流程装成 plugin。",
        "从一个小技能开始，按自己习惯改，不必整套照搬。",
        "技能就是 markdown，换任何模型都能读，直接看源码就能理解。",
    ],
    [
        "<strong>13 次上榜，且这次日增破了 2,000：</strong>上榜次数多不等于热度衰减，方法论类项目反而越用越快。",
        "<strong>内容全是 markdown 却压在大量代码库上面：</strong>说明这一层竞争的是判断，不是实现。",
        "<strong>它站在模型的补丁位上：</strong>「先问再写」一旦被厂商内置，这类仓库要重新找位置。",
    ],
    ["skills", "engineering", "typescript", "workflow", "composable"])

add("D4Vinci", "Scrapling", "Python", "97,406", "10,209", "1,661",
    "🔥 亮点 —— +1,661★，9.74万★，连续第二次上榜。爬虫框架里塞齐普通请求、隐身浏览器、自适应解析和并发爬取，带 MCP server 给 agent 直接调。",
    [
        "<strong>爬虫工具链靠拼：</strong>请求、渲染、解析各一套，反爬升级就整条重写。",
        "<strong>网站改版就抓空：</strong>写死的选择器，前端一动全返回 None。",
        "<strong>agent 拿不到干净网页：</strong>模型自己 fetch，拿回一堆脚本标签，token 全烧在垃圾上。",
    ],
    [
        "<code>pip install scrapling</code>，静态页走普通请求，要 JS 时切隐身浏览器。",
        "用自适应元素追踪代替写死选择器，结构变了重新定位同类元素。",
        "起 MCP server 挂到 Claude Code 或 Cursor，让 agent 把抓取当工具调用。",
    ],
    [
        "<strong>两天涨 3,600★：</strong>爬虫这个「老」需求在被 agent 重新拉动，因为 agent 要读的数据远多于人要读的。",
        "<strong>加一个 MCP 入口就接进新生态：</strong>不改内核的改造，比推倒重写更符合工程现实。",
        "<strong>维护成本才是爬虫的真问题：</strong>脚本死掉很少因为写不出代码，多因为对面改了三次前端。",
    ],
    ["scraping", "mcp", "crawler", "python", "automation"])

add("harry0703", "MoneyPrinterTurbo", "Python", "139,579", "22,254", "1,056",
    "🔥 亮点 —— +1,056★，13.96万★ 首登。一个主题或关键词，自动完成脚本、配音、素材、字幕、配乐、剪辑，出高清短视频，带 Agent、WebUI、API、CLI 四种入口。",
    [
        "<strong>短视频生产是流水线活：</strong>脚本、配音、找素材、上字幕、配乐、剪辑，每一步换一个工具。",
        "<strong>单点 AI 只解决一段：</strong>生成画面的不懂节奏，配音的不管字幕对齐。",
        "<strong>批量做号没有工程化：</strong>想一天出十条，全靠人手重复劳动。",
    ],
    [
        "用 Docker 或 Python 环境起 WebUI，填好模型服务的 API key（支持 Kimi、OpenAI、Claude 等）。",
        "输入主题，或直接用自己的脚本；每个环节都可以替换成自定义内容。",
        "接到 API 或 CLI 上批量生成，任务历史和生成设置可导出恢复。",
    ],
    [
        "<strong>13.96 万★ 的仓库做的是「拼装」而不是「发明」：</strong>把现成模型按工序串起来，价值在流程编排。",
        "<strong>四种入口暴露了它的真实用户：</strong>小白用 WebUI，工作室用 API 和 CLI 批量跑。",
        "<strong>这类工具的天花板由平台决定：</strong>模板化的短视频在算法里越来越难起量，工具再顺也解决不了内容同质。",
    ],
    ["short-video", "automation", "tts", "ffmpeg", "content"])

add("github", "spec-kit", "Python", "147,661", "13,250", "750",
    "🔥 亮点 —— +750★，14.77万★ 首登。GitHub 官方出的规格驱动开发工具包：先把需求和验收写清楚，再让 agent 实现，配套可搜索的扩展、预设、工作流目录。",
    [
        "<strong>agent 写代码快，但方向经常错：</strong>需求在脑子里，agent 猜出来的东西和你要的不是一个。",
        "<strong>验收标准说不清：</strong>「做得差不多」这种标准，agent 只能靠自由发挥。",
        "<strong>换了三个 agent 三套流程：</strong>经验沉不下来，每次重新解释一遍规范。",
    ],
    [
        "装 Python 3.11+ 和 uv，克隆仓库后跑官方安装流程。",
        "用 <code>specify</code> 系列命令建规格、拆任务，选择对应的流程（新功能、修 bug、评估想法）。",
        "用 <code>specify extension search</code>、<code>preset search</code> 找社区扩展，注意官方明说目录不等于审核。",
    ],
    [
        "<strong>GitHub 亲自下场定流程：</strong>规格驱动开发从社区实践变成了平台级默认，这对生态的影响大于任何一个技能库。",
        "<strong>目录化是这一步的关键设计：</strong>把流程本身做成可搜索、可安装的包，方法论第一次有了分发机制。",
        "<strong>它和 mattpocock 那派站在对立面：</strong>一个要管流程，一个坚决不管，用户会用脚投票。",
    ],
    ["spec-driven", "workflow", "github", "agents", "sdd"])

add("scenario-labs", "skills", "Python", "2,781", "257", "674",
    "🔥 亮点 —— +674★，2,781★ 首登。把图像、视频、音频、3D 生成接进任意 agent 的技能集：先选对模型、生成前先报价，再动手。",
    [
        "<strong>生成模型太多挑不过来：</strong>同一张图，不同模型的价格和效果差几倍，选错就是浪费。",
        "<strong>Agent 花钱没有感觉：</strong>一次生成几分钱，批量跑起来账单吓人。",
        "<strong>专业软件的操作知识写不进 prompt：</strong>Blender、Maya、ZBrush 的流程靠人传。",
    ],
    [
        "按 README 的安装命令把技能装到 Claude Code、Cursor、Codex 等 agent。",
        "让技能按任务挑模型并先给出价格估算，确认后再生成。",
        "做 3D 或游戏资产时用对应的 DCC 技能族，前提是本机装着那套软件。",
    ],
    [
        "<strong>「生成前先报价」是这轮 agent 工具里少见的财务意识：</strong>说明用户已经从尝鲜转向算成本。",
        "<strong>技能把模型选择这件事外包了：</strong>用户不必知道哪个模型好，只需要说清要什么。",
        "<strong>DCC 技能族需要本机装软件：</strong>知识能打包，工具链不能，这是它绕不过的边界。",
    ],
    ["skills", "media", "3d", "pricing", "mcp"])

add("garrytan", "gstack", "TypeScript", "139,656", "20,668", "608",
    "🔥 亮点 —— +608★，13.97万★，第 3 次上榜。YC 总裁 Garry Tan 把自己每天用的 Claude Code 配置开源了：23 个工具分别扮演 CEO、工程经理、设计师、评审、QA、安全和发布工程师。",
    [
        "<strong>一个人创业没有同事可商量：</strong>产品方向、架构、设计、测试全自己扛。",
        "<strong>agent 只写代码不管质量：</strong>能跑就算完成，生产环境的坑要等上线才发现。",
        "<strong>角色缺失导致盲区：</strong>没人做安全审计，没人认真做 QA。",
    ],
    [
        "两次粘贴完成安装，约 30 秒。",
        "跑 <code>/office-hours</code> 描述你在做什么，它会反驳你的框架并写一份设计文档。",
        "在分支上跑 <code>/review</code> 找生产环境的 bug，在 staging 上跑 <code>/qa</code> 用真实浏览器验证。",
    ],
    [
        "<strong>名人开源比工具本身值钱：</strong>23 个命令谁都能写，但「YC 总裁每天在用」这句话就是分发渠道。",
        "<strong>他把公司角色拆成了 agent 岗位：</strong>这比「一个全能助手」更贴近真实的软件开发分工。",
        "<strong>全 Markdown、MIT、让人 fork：</strong>这类项目的收益不在代码，在于确立自己的方法论话语权。",
    ],
    ["claude-code", "skills", "startup", "workflow", "ycombinator"])

add("max-sixty", "worktrunk", "Rust", "11,332", "426", "546",
    "🔥 亮点 —— +546★，1.13万★，连续第二次上榜。给并行 agent 工作流做的 Git worktree 管理器，三条命令替掉一串手工 git 操作。",
    [
        "<strong>并行跑 agent 要开多个工作区：</strong>git worktree 命令又长又容易记错。",
        "<strong>分支和目录对不上号：</strong>哪个目录在哪个分支全靠脑记。",
        "<strong>环境要重建：</strong>新工作区装依赖、拷缓存，十分钟起步。",
    ],
    [
        "<code>wt switch feat</code> 直接切到对应工作区。",
        "<code>wt switch -c -x claude feat</code> 建工作区、建分支、顺手起一个 Claude。",
        "<code>wt remove</code> 收尾，分支和工作区一起清。",
    ],
    [
        "<strong>连续两天在榜，说明并行已经成了默认工作方式：</strong>一个人同时跑五个 agent，git 的原语明显不够用。",
        "<strong>「-x claude」这个参数最说明问题：</strong>工具已经把 agent 当成工作区的默认居民。",
        "<strong>copy-on-write 缓存省的是隐性成本：</strong>并行越多，重复构建越贵，这才是并行的真实账单。",
    ],
    ["git", "worktree", "cli", "rust", "parallel-agents"])

add("Thysrael", "Horizon", "Python", "12,829", "1,841", "540",
    "🔥 亮点 —— +540★，1.28万★ 首登。自建的 AI 新闻雷达：聚合 RSS、Hacker News、Reddit、Telegram、X、GitHub 和财经源，按你写的评分标准筛选，每天出中英文简报。",
    [
        "<strong>信息源太散：</strong>十几个站点和频道刷一遍，一上午就没了。",
        "<strong>推荐算法决定你读什么：</strong>你关心什么由平台判断，改不了标准。",
        "<strong>简报工具不懂取舍：</strong>要么全推给你，要么漏掉关键的那一条。",
    ],
    [
        "克隆仓库，<code>uv sync</code> 装依赖，或 <code>pip install -e .</code>。",
        "在配置里加源（RSS、HN、Reddit、X、GitHub 等），写自己的评分标准和阈值。",
        "让它每天定时生成中英文简报，同一条新闻在多个 profile 里按不同规则处理；本地模型可以接 Ollama。",
    ],
    [
        "<strong>它把「编辑判断」变成了可配置项：</strong>评分标准和阈值是这套系统的核心，不是抓取。",
        "<strong>支持 Ollama 是个明确信号：</strong>媒体订阅这种高频任务，用户不愿意按 token 付费。",
        "<strong>做信息分发的工具在往个人手里走：</strong>当每个人都能自建雷达，平台算法的解释权会被一点点拿走。",
    ],
    ["news", "rss", "briefing", "llm", "automation"])

add("The-PR-Agent", "pr-agent", "Python", "15,015", "2,105", "506",
    "🔥 亮点 —— +506★，1.5万★ 首登。最早的 PR 自动评审工具，一行 GitHub Action 就能接入，也可以本地 CLI 对某个 PR 跑评审。",
    [
        "<strong>PR 评审是瓶颈：</strong>代码等人看，等的过程中上下文全丢了。",
        "<strong>人工评审不稳定：</strong>今天严明天松，同一个问题这次提下次不提。",
        "<strong>买商业评审服务贵：</strong>按席位收费，小团队用不起。",
    ],
    [
        "在仓库里加 <code>.github/workflows/pr-agent.yml</code>，配好 OPENAI_KEY 和 token。",
        "或本地 <code>pip install \"pr-agent[github]\"</code> 后跑 <code>pr-agent --pr_url ... review</code>。",
        "按 provider 装对应的 SDK extra，需要全支持就装 <code>pr-agent[all]</code>。",
    ],
    [
        "<strong>「最早的那个」是它最大的资产：</strong>在同类工具满天飞之后仍能上榜，靠的是历史位置和心智占位。",
        "<strong>README 专门注明不是某家的免费版：</strong>说明这条赛道已经出现品牌混淆，市场在成熟也在内卷。",
        "<strong>评审自动化先落地在 PR：</strong>因为它是研发流程里唯一有明确输入输出的环节，好验收。",
    ],
    ["code-review", "pull-request", "ci", "llm", "devtools"])

add("Usagi-org", "ai-goofish-monitor", "Python", "17,333", "2,926", "242",
    "🔥 亮点 —— +242★，1.73万★ 首登。用 Playwright 加多模态模型做闲鱼监控：自然语言建任务，按价格、区域、包邮条件筛选，命中就推飞书、企业微信、Bark 或 Telegram。",
    [
        "<strong>好价商品活不过几分钟：</strong>等你自己刷到，已经被别人拍下。",
        "<strong>筛选条件太粗：</strong>平台只能按关键词和价格区间，看不出成色和猫腻。",
        "<strong>多账号容易被风控：</strong>手动切号、换 IP，效率极低。",
    ],
    [
        "克隆仓库，<code>cp .env.example .env</code> 填配置，<code>docker compose up -d</code>。",
        "打开 Web 管理界面建任务，用自然语言描述你要什么，配 AI 评分标准。",
        "绑定通知渠道（ntfy、企业微信、Bark、Telegram、Webhook），配 Cron 定时跑。",
    ],
    [
        "<strong>多模态模型在这类场景才显出价值：</strong>判断商品成色、识别图片里的坑，比关键词匹配有用得多。",
        "<strong>账号池和代理轮换说明对抗成本：</strong>平台风控和工具一直在互相升级，这类项目天然短命，热度靠实用性撑。",
        "<strong>它同时是消费工具和套利工具：</strong>信息差被工具抹平之后，卖家那边也会开始定价博弈。",
    ],
    ["ecommerce", "monitoring", "multimodal", "playwright", "china"])

add("microsoft", "VibeVoice", "Python", "55,429", "6,245", "214",
    "🔥 亮点 —— +214★，5.54万★，第 2 次上榜。微软的开源语音栈：TTS 之外还有流式 ASR，能边听边转写「谁说了什么」，还有压到 CPU 上跑的 BitNet 版本。",
    [
        "<strong>会议转写分不清谁在说：</strong>一整段文字没有说话人，纪要等于白做。",
        "<strong>语音模型离不开显卡：</strong>想在本地或边缘跑，先得有一张卡。",
        "<strong>长音频一段段切：</strong>切碎了丢上下文，拼起来前言不搭后语。",
    ],
    [
        "从 Hugging Face 的 microsoft/vibevoice 集合下模型权重。",
        "TTS 用 Colab 示例先跑通；ASR 用官方 playground 试「谁说了什么」。",
        "边缘场景用 VibeASR.cpp 的 BitNet 版本，纯 CPU 推理。",
    ],
    [
        "<strong>语音这条线今年在往「结构化」走：</strong>从转成文字，到转成带说话人和时间轴的数据。",
        "<strong>压到 CPU 是真正的分水岭：</strong>语音入口要常驻，常驻的东西不能占着显卡。",
        "<strong>微软把 TTS 和 ASR 一起开源：</strong>语音交互的两端都在自己手里，才有机会定义标准。",
    ],
    ["voice", "tts", "asr", "microsoft", "edge"])

add("google", "skills", "Python", "22,126", "1,881", "199",
    "🔥 亮点 —— +199★，2.21万★，第 2 次上榜。Google 官方的 Agent Skills 仓库，覆盖 Google Cloud 等自家产品，一条 <code>npx skills add</code> 就能装。",
    [
        "<strong>云服务的知识和 agent 隔着一层：</strong>文档写得全，但 agent 不知道什么时候该用哪条命令。",
        "<strong>各家技能格式不统一：</strong>装一个能用的技能，先得读半天结构说明。",
        "<strong>配置容易错：</strong>认证、权限、区域这些参数，错一个就卡半天。",
    ],
    [
        "<code>npx skills add google/skills</code>，按提示选技能和目标 agent。",
        "可以选项目级或全局安装，装完用 <code>npx skills update</code> 更新。",
        "按技能分组的目录挑，比如先装认证授权那组再把云资源操作接上。",
    ],
    [
        "<strong>云厂商把 SDK 文档改写成技能：</strong>这是它们能想到的最便宜的生态投入，一次写好，所有 agent 都能读。",
        "<strong>Google 和 Anthropic 都在发官方技能库：</strong>标准之争已经开始了，格式统一之前，用户是受益方。",
        "<strong>它真正的对手不是技能库，是各家自己的 CLI：</strong>装技能和让人去读文档，抢的是同一批操作。",
    ],
    ["skills", "google-cloud", "agents", "cli", "standards"])

TOPIC = ("🔥 <strong>今日主题：从能生成到敢用。</strong>"
         "榜首 NVIDIA auto-ontology 一行内容都不生成，它只做一件事：告诉 agent 这个指标怎么定义、数字从哪来、能不能信。"
         "同样的逻辑在别处重复出现：scenario-labs 的技能先报价再生成，pr-agent 在合并前拦一道，"
         "spec-kit 把需求和验收写死在实现之前，VibeVoice 把语音模型压到 CPU 上以便常驻。"
         "生成能力已经过剩，稀缺的是验收。"
         "这也解释了为什么两份 skills 库（Google 官方、mattpocock）和一个工作流框架能同时在前排："
         "大家不再比谁会生成，开始比谁能证明生成的东西可用。")

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
assert len(data["days"]) == 95, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-38s +%-6s %8s★ count=%d" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
