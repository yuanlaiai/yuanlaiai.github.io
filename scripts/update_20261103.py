#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-03（距上次更新 2 天，flat day：全部新面孔）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-03"

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


add("vercel-labs", "agent-desktop", "Rust", "11,717", "796", "3,792",
    "🔥 亮点 —— 今日 +3,792★ 遥遥第一，1.17万★ 首登。Vercel Labs 出的电脑操作 CLI：走操作系统无障碍树读桌面应用，每个可操作元素给一个 ref，agent 点完再快照核对，不做像素匹配。",
    [
        "<strong>截图方案不可靠：</strong>让多模态模型看屏幕找按钮，分辨率一变、弹窗一挡就点错，还烧 token。",
        "<strong>坐标点击很脆：</strong>按 x/y 点击，窗口位置一动全废，重试成本比人操作还高。",
        "<strong>桌面应用没有 API：</strong>企业的报销、ERP、老客户端根本不给接口，agent 只能停在浏览器里。",
    ],
    [
        "用 npm 装上 CLI，<code>agent-desktop list-apps</code> 看能接管哪些应用。",
        "<code>agent-desktop snapshot --app Finder -i</code> 拿到带 ref 的交互元素 JSON。",
        "<code>agent-desktop click @s8f3k2p9:e8</code> 操作后重新快照核对，循环握在 agent 手里。",
    ],
    [
        "<strong>无障碍树才是 agent 该看的界面：</strong>它本来是为读屏软件准备的结构化描述，比截图像素更适合机器操作。",
        "<strong>Vercel 从 Web 摸到桌面：</strong>agent 的能力边界一直卡在「能操作什么」上，谁把操作系统这一层抽象掉，谁就拿到下一个入口。",
        "<strong>隐私是自己埋的雷：</strong>快照里可能有整屏私人内容，README 专门提示别进日志和上传，说明这条路绕不开数据外泄问题。",
    ],
    ["computer-use", "accessibility", "cli", "rust", "automation"])

add("D4Vinci", "Scrapling", "Python", "93,824", "9,000", "1,658",
    "🔥 亮点 —— +1,658★，9.38万★ 首登。一个爬虫框架里塞齐了普通请求、隐身浏览器、自适应解析和并发爬取，还带 MCP server 让 agent 直接调。",
    [
        "<strong>爬虫工具链是拼接的：</strong>请求一套库、渲染一套、解析又一套，反爬一升级就整条重写。",
        "<strong>网站改版就抓空：</strong>写死的 CSS 选择器，前端动一下结构，脚本全返回 None。",
        "<strong>agent 拿不到干净的网页：</strong>模型自己去 fetch，拿回来一堆脚本标签，token 全烧在垃圾上。",
    ],
    [
        "<code>pip install scrapling</code>，静态页用普通请求，需要 JS 时切隐身浏览器。",
        "用自适应元素追踪代替写死选择器，结构变了重新定位同类元素。",
        "起 MCP server 挂到 Claude Code 或 Cursor，让 agent 把抓取当成一个工具调用。",
    ],
    [
        "<strong>爬虫框架加上 MCP 就是 agent 的取数层：</strong>不改内核，只多开一个入口，就把十年的老工具接进了新生态。",
        "<strong>自适应选择器解决的是维护成本：</strong>爬虫死掉很少因为写不出代码，多因为对面改了三次前端。",
        "<strong>9 万★ 说明需求一直在：</strong>这一波 AI 没有让抓取消失，反而让抓取量涨了一个量级。",
    ],
    ["scraping", "mcp", "crawler", "python", "automation"])

add("Donchitos", "Claude-Code-Game-Studios", "Shell", "34,237", "4,700", "1,181",
    "🔥 亮点 —— +1,181★，3.42万★，连续第二天上榜。49 个代理、74 个技能、15 个 hook 拼出一个游戏工作室的编制，从策划、美术到 QA 各有分工。",
    [
        "<strong>一个人做游戏缺的不是码农：</strong>策划、美术、测试的角色没人补，代码写得再快也堆不出作品。",
        "<strong>单 agent 兼所有角色会自相矛盾：</strong>同一轮里既当策划又当 QA，产出互相打架。",
        "<strong>多 agent 没有交接规范：</strong>没有规则约束读写边界，每个角色都在改别人的文件。",
    ],
    [
        "克隆仓库，把 <code>.claude</code> 目录放进自己的游戏项目。",
        "按 README 触发工作流，先让策划代理出设计，再进实现。",
        "用 hook 管住每个角色的读写边界，避免互相覆盖。",
    ],
    [
        "<strong>第二天涨得比第一天还猛：</strong>11-01 是 +742，今天 +1,181，说明「给 agent 排编制」这个想法被更多人接受了。",
        "<strong>它卖的其实是组织结构：</strong>49 个代理的价值在分工和交接，不是提示词写得花。",
        "<strong>角色越多协调成本越高：</strong>74 个技能里每天用到的可能不到十个，剩下的是覆盖长尾的保险，也是理解门槛。",
    ],
    ["game-dev", "claude-code", "multi-agent", "workflow", "skills"])

add("mattpocock", "skills", "Shell", "310,902", "26,300", "1,164",
    "🔥 亮点 —— +1,164★，31.09万★，第 12 次上榜。Matt Pocock 的日常工程技能集：小而可组合、鼓励改成自己的，明确反对把流程收走的框架。",
    [
        "<strong>流程框架替你握方向盘：</strong>GSD、BMAD 这类方案接管流程后，出问题你连从哪查都不知道。",
        "<strong>大而全的规范比代码写得还慢：</strong>为了「规范」先写一堆文档，最后没人读。",
        "<strong>绑死某个 agent 就等于自废武功：</strong>模型一换代，写法全废。",
    ],
    [
        "按 README 的 30 秒流程装成 plugin。",
        "从一个小技能开始用，按自己的习惯改，别整套照搬。",
        "技能本身就是 markdown，任何模型都能读，直接看源码就能理解。",
    ],
    [
        "<strong>12 次上榜，累计记录仅次于 superpowers：</strong>内容全是 markdown 的仓库能长期占位，说明用户缺的是判断而不是代码。",
        "<strong>「不接管控制权」是最清醒的产品立场：</strong>不夺方向盘，就不用为跑偏负责。",
        "<strong>可组合意味着一定会被 fork：</strong>作者拿到影响力，不拿钱，这也是它敢全开的底气。",
    ],
    ["skills", "engineering", "typescript", "workflow", "composable"])

add("thedotmack", "claude-mem", "TypeScript", "111,383", "9,800", "1,138",
    "🔥 亮点 —— +1,138★，11.14万★，第 4 次上榜。给 Claude Code 加的持久记忆：自动记录工具调用、压缩成语义摘要，新会话开始时自己带回来。",
    [
        "<strong>新会话等于失忆：</strong>昨天定的命名、踩过的坑、读过的文件全清空，agent 从头再翻一遍仓库。",
        "<strong>CLAUDE.md 靠手写：</strong>写多了挤爆上下文，写少了等于没写，没人愿意每天维护。",
        "<strong>历史记录没人查：</strong>本地 jsonl 里躺着完整历史，agent 自己不会去检索。",
    ],
    [
        "用 <pre><code>npx claude-mem install</code></pre> 装（npm 全局装只给 SDK，不注册 hook）。",
        "重启 Claude Code，观察记录自动落到本地 SQLite，由常驻 worker 做摘要。",
        "需要回溯时让 agent 调 MCP 检索工具，按语义找过去操作。",
    ],
    [
        "<strong>两次上榜之间涨了 3,400★：</strong>记忆这类需求不是一次性好奇，用得越久越离不开。",
        "<strong>它卖的是「不用重新交代一遍」：</strong>省下的不是 token 是耐心，而耐心才是长期使用的真实成本。",
        "<strong>代价是又一个常驻服务：</strong>每个 agent 能力都变成一个本地进程，最后谁的机器上都是一排后台。",
    ],
    ["agent-memory", "claude-code", "context", "sqlite", "mcp"])

add("anomalyco", "hex", "Rust", "4,266", "300", "1,134",
    "🔥 亮点 —— +1,134★，4,266★ 首登。按住快捷键说话、松手就粘贴的本地听写工具，Mac/Windows/Linux 三端，语音模型跑在本地，文字不出机器。",
    [
        "<strong>云端听写把语音全传走：</strong>会议、客户对话、私人备注，一个字不落地过别人的服务器。",
        "<strong>系统自带听写只认本地语言：</strong>中英混说不认，专业词不认，标点全靠自己补。",
        "<strong>切换输入法打断思路：</strong>说着话突然要停下来打字修正，比全手打还慢。",
    ],
    [
        "从 anoma.ly/hex/download 下对应平台的安装包。",
        "第一次运行会下载语音模型，之后全程离线。",
        "按住快捷键说话，松手自动粘贴到当前窗口，侧边栏 Labs 里有实验功能。",
    ],
    [
        "<strong>本地语音已经是消费级能力：</strong>Whisper 级别的模型塞进桌面应用，隐私才第一次成为卖点而不是成本。",
        "<strong>anomalyco 同时在维护 OpenCode 和 Hex：</strong>一个团队做两件不相干的事，共同点是都要求数据不出本地。",
        "<strong>输入是 agent 时代最被低估的入口：</strong>键盘打字的速度，正在变成人和机器协作的瓶颈。",
    ],
    ["voice", "dictation", "local-first", "rust", "privacy"])

add("JustVugg", "colibri", "C", "46,976", "3,400", "803",
    "🔥 亮点 —— +803★，4.7万★，第 2 次上榜。纯 C 写的 MoE 推理引擎：744B 的 GLM-5.2 在 int4 下只占 9.9GB 内存，32 秒就绪，不需要 GPU。",
    [
        "<strong>大模型默认要显卡：</strong>想跑前沿开源模型，先买一张能装下权重的卡。",
        "<strong>MoE 的权重大部分是闲置的：</strong>每个 token 只激活一小部分专家，剩下的白占显存。",
        "<strong>量化工具链太重：</strong>换一个模型就要重配一遍推理栈。",
    ],
    [
        "从 GitHub Releases 下对应平台的二进制，或用一键安装脚本。",
        "<code>colibri run glm-5.2</code> 之类的命令直接跑，权重按需从磁盘流式读入。",
        "热专家常驻内存、温专家放 RAM、冷专家留磁盘，三层调度由引擎自己管。",
    ],
    [
        "<strong>它把瓶颈从显存换成了磁盘带宽：</strong>MoE 稀疏激活本来就有这个空间，只是之前没人认真做分层。",
        "<strong>9.9GB 跑 744B 是个分水岭：</strong>足够让一台普通台式机越过「能不能跑」的门槛，剩下的只是慢一点。",
        "<strong>纯 C、一家族一文件：</strong>刻意的低依赖选择，意味着它能在任何机器上编译，也意味着维护成本全压在作者身上。",
    ],
    ["moe", "inference", "local-llm", "c", "quantization"])

add("p-e-w", "heretic", "Python", "38,510", "3,100", "699",
    "🔥 亮点 —— +699★，3.85万★，第 4 次上榜。免训练的语言模型改造工具：去掉审查、压制废话、降低谄媚，一个下午在你自己的游戏主机上跑完。",
    [
        "<strong>对齐层的副作用写在输出里：</strong>拒答、套话、过度附和，用户想要信息却收到姿态。",
        "<strong>微调门槛高：</strong>改一个模型的行为，传统上要数据、算力、一整套训练管线。",
        "<strong>已有工具不够稳：</strong>早期的 abliteration 脚本要么崩，要么把模型改傻。",
    ],
    [
        "<code>pip install -U heretic-ai</code>，装 PyTorch 2.6+。",
        "选一个本地模型，工具自动搜索抑制方向并做权重正交化，全程不训练。",
        "跑完导到 Hugging Face，社区已用同一套流程发了上千个模型。",
    ],
    [
        "<strong>「免训练」是关键变化：</strong>模型行为的可编辑性一旦变成几十分钟的操作，对齐就不再是厂商独占的权力。",
        "<strong>它同时去掉审查和谄媚：</strong>说明这两件事在权重层是同一个方向，用户讨厌的不只是拒答，还有讨好。",
        "<strong>支持 MoE 和多模态：</strong>方法在往通用工具走，而不是某几个模型的补丁。",
    ],
    ["abliteration", "alignment", "local-llm", "fine-tuning", "open-weights"])

add("calesthio", "OpenMontage", "Python", "75,687", "10,009", "693",
    "🔥 亮点 —— +693★，7.57万★，第 6 次上榜。开源 agentic 视频生产系统：12 条生产管线、100 多个工具、700 多个制作知识文件。",
    [
        "<strong>做视频的链条太长：</strong>脚本、素材、配音、字幕、剪辑各用一个工具，中间靠人搬。",
        "<strong>单点 AI 工具只解决一段：</strong>生成画面的不管字幕，配音的不懂节奏。",
        "<strong>全流程交给黑箱服务：</strong>改不动、搬不走，风格被供应商锁死。",
    ],
    [
        "按 README 装 Python 依赖，配好 provider 的 key。",
        "选一条 pipeline，从脚本一路走到成片。",
        "扔一个喜欢的视频进去，让它反推风格再照着做。",
    ],
    [
        "<strong>两天连续加速：</strong>11-01 是 +583，今天 +693，热度不是一次性的推荐流量。",
        "<strong>700 个知识文件才是资产：</strong>模型谁都能调，制作经验得一条条写下来，这部分抄不走。",
        "<strong>AGPL 会挡住一部分商业使用：</strong>想在上面做产品的团队，先把授权问题想清楚。",
    ],
    ["video", "agentic", "pipeline", "production", "ffmpeg"])

add("FlashML-org", "FreeToken", "Python", "16,425", "1,609", "689",
    "🔥 亮点 —— +689★，1.64万★ 首登。边缘侧的 MoE 服务引擎：在游戏 PC 上跑 290B 级别的前沿开源模型，交互速度可用，背后有一篇论文。",
    [
        "<strong>前沿开源模型越来越跑不动：</strong>权重几百 GB，家用显卡装不下，云上又是另一笔账单。",
        "<strong>本地推理慢到没法交互：</strong>能跑不等于能用，几 token/s 的速度读一段代码都要等。",
        "<strong>服务栈是给机房写的：</strong>vLLM 这类引擎的假设是你有一整张卡。",
    ],
    [
        "从 flashml.ai 下载对应平台的版本。",
        "选一个支持的 MoE 模型，引擎按专家粒度调度显存和内存。",
        "用 OpenAI 兼容接口接进自己的客户端或 agent。",
    ],
    [
        "<strong>「数据中心级智能 + 你已有的硬件」：</strong>这句话正在成为 2026 年本地推理产品的标准话术，说明需求已经规模化。",
        "<strong>带论文的工程项目更容易被信任：</strong>它卖的不只是脚本，是一套调度方法。",
        "<strong>290B 和 colibri 的 744B 同天在榜：</strong>稀疏模型让「参数规模」和「硬件门槛」彻底脱钩，这是今年最实质的技术进展。",
    ],
    ["moe", "inference", "edge", "serving", "local-llm"])

add("karpathy", "nanochat", "Python", "60,149", "8,435", "551",
    "🔥 亮点 —— +551★，6.01万★ 首登。Karpathy 的最小 LLM 训练框架：一个 <code>--depth</code> 旋钮决定模型大小，48 美元训出 GPT-2 水平的模型，2 小时跑完。",
    [
        "<strong>训练 LLM 看起来像魔法：</strong>分词、预训练、微调、评测、推理分散在十几个仓库里。",
        "<strong>复现论文要读几万行代码：</strong>想学明白，先得啃一个工业级框架。",
        "<strong>调参无从下手：</strong>宽度、头数、学习率、权重衰减互相牵制，错一步就训崩。",
    ],
    [
        "租一台 8×H100 节点，按 README 装依赖。",
        "设 <code>--depth 26</code> 得到 GPT-2 能力，其他超参自动按最优算。",
        "训完在 CLI 里直接对话，整套代码不到万行。",
    ],
    [
        "<strong>48 美元是个有说服力的广告：</strong>2019 年要 4.3 万美元的事，现在一顿饭钱，成本落差本身就在教育市场。",
        "<strong>单旋钮设计是教学上的高明：</strong>把一维复杂度暴露给用户，其余交给自动推导，学习曲线立刻变缓。",
        "<strong>训练的门槛在降，不在于容易，在于可见：</strong>能把整条链路读完的人，才谈得上改进它。",
    ],
    ["llm-training", "education", "pytorch", "gpt", "minimal"])

add("shiyu-coder", "Kronos", "Python", "46,258", "4,100", "503",
    "🔥 亮点 —— +503★，4.63万★，第 5 次上榜。把 K 线当成一门语言来建模的金融基础模型，权重在 Hugging Face 上公开，带一个预测 BTC/USDT 24 小时的在线 demo。",
    [
        "<strong>量化模型多为私有：</strong>做得好的人不会开源，能拿到的多是回测过拟合的玩具。",
        "<strong>时间序列模型不懂市场结构：</strong>纯统计方法抓不住开收盘、跳空、量价配合这些规律。",
        "<strong>通用 LLM 不懂数字：</strong>把行情当文本喂进去，预测能力约等于随机。",
    ],
    [
        "从 Hugging Face 的 NeoQuasar 组织下载预训练权重。",
        "用 <code>pip install</code> 装推理包，输入 OHLCV 序列拿到预测。",
        "先看线上 demo（BTC/USDT 未来 24 小时）再决定要不要自己跑。",
    ],
    [
        "<strong>「金融市场的语言」这个类比是有意的：</strong>把 K 线当 token，就能复用序列建模的全部积累。",
        "<strong>开源权重和能赚钱之间隔着一整个市场：</strong>公开的模型很快会被套利抹平，真正的收益在数据和执行。",
        "<strong>第 5 次上榜说明金融是刚需：</strong>每一轮模型进步，第一个被追问的都是「能不能用来交易」。",
    ],
    ["finance", "timeseries", "foundation-model", "trading", "quant"])

add("blader", "humanizer", "Python", "64,239", "5,081", "460",
    "🔥 亮点 —— +460★，6.42万★ 首登。照着维基百科「AI 写作的迹象」那篇条目写的 agent 技能，专门删掉 AI 味：不改内容，只改腔调。",
    [
        "<strong>AI 文风一眼能认：</strong>破折号泛滥、三段排比、「不是 X 而是 Y」、每段都以金句收尾。",
        "<strong>读者会用文风判断可信度：</strong>看到那种腔调，先怀疑内容是不是也是生成的。",
        "<strong>改文风靠感觉：</strong>让模型「写得自然点」，它只会换一批套话。",
    ],
    [
        "把技能目录放进 Claude Code / Codex 的 skills 路径。",
        "让它过一遍已有文本，输出保留事实、换掉腔调的版本。",
        "对照 README 里的 before/after 例子调，比自己描述期望更准。",
    ],
    [
        "<strong>它的依据是一份「人类识别 AI」的清单：</strong>把判断标准写成规则，比让模型自由发挥可靠得多。",
        "<strong>文风成了产品：</strong>说明 AI 输出过剩之后，稀缺的是看起来不像 AI 的东西。",
        "<strong>这类技能没有技术壁垒，只有品味壁垒：</strong>规则谁都能抄，能不能写出准确的规则取决于写的人读不读得出来。",
    ],
    ["writing", "style", "agent-skill", "editing", "content"])

add("max-sixty", "worktrunk", "Rust", "10,287", "600", "437",
    "🔥 亮点 —— +437★，1.03万★ 首登。给并行 agent 工作流做的 Git worktree 管理器：三条命令替掉一串 git 手工操作。",
    [
        "<strong>并行跑 agent 要开多个工作区：</strong>git worktree 的命令又长又容易记错。",
        "<strong>分支和目录对不上：</strong>手动管理时，哪个目录在哪个分支全靠脑记。",
        "<strong>环境要重建：</strong>新工作区装依赖、拷缓存，一次十分钟起步。",
    ],
    [
        "<code>wt switch feat</code> 直接切到对应工作区。",
        "<code>wt switch -c -x claude feat</code> 建工作区、建分支、顺手起一个 Claude。",
        "<code>wt remove</code> 收尾，分支和工作区一起清。",
    ],
    [
        "<strong>工具在跟着工作方式变：</strong>以前一个人一个分支，现在一个人五个 agent 五个分支，git 的原语不够用了。",
        "<strong>「-x claude」这种参数最说明问题：</strong>它把 agent 当成了工作区的默认居民。",
        "<strong>copy-on-write 缓存是隐性成本控制：</strong>并行越多，重复构建越贵，省下来的时间才是并行真正的收益。",
    ],
    ["git", "worktree", "cli", "rust", "parallel-agents"])

TOPIC = ("🔥 <strong>今日主题：本地跑大模型，和给 agent 装手。</strong>"
         "榜单上半区在解决「把大模型塞进你自己的机器」：colibri 让 744B 的 MoE 只吃 9.9GB 内存，"
         "FreeToken 在游戏 PC 上跑 290B，nanochat 用 48 美元和 2 小时训出 GPT-2 水平的模型。"
         "下半区在解决「让 agent 接管你的桌面」：Vercel 的 agent-desktop 走无障碍树操作桌面应用，"
         "hex 做本地语音听写，worktrunk 给并行 agent 管 worktree，claude-mem 补记忆。"
         "两头说的是同一件事：算力成本在快速下降，接口成本在快速上升。"
         "今天的 +3,792★ 没有给任何一个模型，给的是一个「怎么点按钮」的 CLI。")

with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

# count = 1 + 历史最高出现次数（按 owner+name 匹配）
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
assert len(data["days"]) == 94, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-34s +%-6s %8s★ count=%d" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
