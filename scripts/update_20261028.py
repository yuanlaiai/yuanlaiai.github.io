#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-28 (4-day gap, 无昨日榜→平铺结构, 14 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 28)
gap_days = (today - last).days  # 4
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（4天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "hmjz100",
        "name": "LinkSwift",
        "fullName": "hmjz100 / LinkSwift",
        "org": "hmjz100",
        "url": "https://github.com/hmjz100/LinkSwift",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "33,846",
        "forks": "2,388",
        "starsToday": "3,209",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,209★ 拿下日增第一！3.38万★ 首登。一个基于 JavaScript 的网盘直链获取工具，支持百度、阿里云、移动、天翼、迅雷、夸克、UC、123 共八家网盘，从「网盘直链下载助手」改出来的。和 AI 没有任何关系。",
        "problems": [
            "<strong>网盘下载被客户端绑死：</strong>想批量拿文件就得装一堆客户端，还要登录。",
            "<strong>限速卡在非会员：</strong>同样的文件，付费与否是两个速度。",
            "<strong>多平台各一套规则：</strong>八家网盘的分享链接格式和鉴权方式都不一样。"
        ],
        "usage": [
            "按 README 安装脚本（浏览器脚本管理器或本地运行）。",
            "打开网盘分享页，用脚本解析出直链。",
            "把直链交给下载工具，绕开客户端。"
        ],
        "insights": [
            "<strong>一个和 AI 无关的工具拿了第一：</strong>这是这一周最值得记的信号。当榜单头部被一个「省事」的小工具占住，说明围观新模型的热情在退，用户回到具体麻烦上。",
            "<strong>它解决的是最原始的需求：</strong>同样的文件，我想用自己的下载器、自己的速度拿到。这类工具一直在灰色地带，能不能长期存在取决于平台策略和合规，而不是代码质量。",
            "<strong>本质是工具的价值和它是否时髦无关：</strong>八家网盘各改一次接口，它就失效一次；但只要平台还在限速，它就还会被重新需要。"
        ],
        "tags": ["netdisk", "download", "javascript", "utility", "self-hosted"]
    },
    {
        "rank": 2,
        "owner": "HKUDS",
        "name": "DeepTutor",
        "fullName": "HKUDS / DeepTutor",
        "org": "HKU DS",
        "url": "https://github.com/HKUDS/DeepTutor",
        "lang": "Python",
        "langClass": "py",
        "stars": "47,268",
        "forks": "5,886",
        "starsToday": "2,376",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,376★ 首登即 4.73万★！港大数据智能实验室（做过 CLI-Anything 的那个组）的新项目：DeepTutor，定位是「终身个性化辅导」。不是刷题工具，是把一个长期的学习关系交给模型来维护。",
        "problems": [
            "<strong>一对一辅导太贵：</strong>好老师的时间稀缺，多数人一辈子没体验过因材施教。",
            "<strong>通用聊天记不住你：</strong>每次都要重新说明自己学到哪、哪里卡住。",
            "<strong>题库不等于教学：</strong>会给答案的工具很多，能判断你缺哪一块的很少。"
        ],
        "usage": [
            "按 README 部署（Python 项目）。",
            "设定学习目标与当前水平，让它生成学习路径。",
            "在持续对话中积累你的薄弱点，按进度调整内容。"
        ],
        "insights": [
            "<strong>首登就 4.73 万星：</strong>这个体量说明项目已经跑了一段时间，今天才被推上日榜。教育类项目很少有这样陡的起点，通常靠的是学术圈和留学生群体的口碑。",
            "<strong>「终身」两个字是它的野心：</strong>题库和刷题是一次性生意，长期辅导是订阅生意。要成立，模型必须真的记住这个人几个月前的错误，这正好接上这一年在做的记忆层。",
            "<strong>本质是教育被拆成了两个市场：</strong>知识获取几乎免费了，判断「你现在该学什么」依然昂贵。后者才是这门生意真正的定价点。"
        ],
        "tags": ["education", "tutoring", "personalization", "python", "memory"]
    },
    {
        "rank": 3,
        "owner": "Nutlope",
        "name": "hallmark",
        "fullName": "Nutlope / hallmark",
        "org": "Nutlope",
        "url": "https://github.com/Nutlope/hallmark",
        "lang": "CSS",
        "langClass": "css",
        "stars": "40,033",
        "forks": "2,087",
        "starsToday": "2,109",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,109★！4.00万★ 第4次登榜（7 月中 8,397★，三个多月涨了近四倍）。一个反 AI-slop 的设计技能，给 Claude Code、Cursor、Codex 用。名字本身就是主张：不要千篇一律的「AI 脸」。",
        "problems": [
            "<strong>AI 做出来的界面长得一样：</strong>紫色渐变、圆角卡片、居中大标题，一眼就能认出是生成的。",
            "<strong>审美没法用提示词描述：</strong>说「好看一点」，模型只会加阴影和动效。",
            "<strong>返工成本高：</strong>生成十版都差不多，最后还是要人重画。"
        ],
        "usage": [
            "把技能装进 Claude Code / Cursor / Codex。",
            "在生成界面之前先让它按技能里的规则确定排版、层级和配色。",
            "生成后对照规则检查，删掉模板化的装饰。"
        ],
        "insights": [
            "<strong>三个多月从 8,397 涨到 4 万：</strong>设计技能不是新品类，但它的增速在最近明显加快。原因很直接：AI 生成的页面已经多到让人反感，「不像 AI 做的」本身成了需求。",
            "<strong>它和今天另外三个项目构成一条线：</strong>hallmark 管「别像 AI」，impeccable 管「怎么调风格」，ai-design-skills 管「有哪些风格」，thinkrail 管「在哪儿写」。四件东西拼起来，是一套给 agent 用的设计工作环境。",
            "<strong>本质是审美正在被写成规则：</strong>好设计过去靠品味，品味没法传递。现在它被拆成可执行的约束，装进技能里，让模型照着做。这是把人的判断变成基础设施。"
        ],
        "tags": ["design", "agent-skill", "css", "anti-slop", "frontend"]
    },
    {
        "rank": 4,
        "owner": "togg53192-cmd",
        "name": "jailbreaks",
        "fullName": "togg53192-cmd / jailbreaks",
        "org": "togg53192-cmd",
        "url": "https://github.com/togg53192-cmd/jailbreaks",
        "lang": "",
        "langClass": "",
        "stars": "6,432",
        "forks": "928",
        "starsToday": "1,478",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,478★ 首登！6,432★。仓库说明只有一句：我所有越狱的合集。没有代码，没有框架，就是把试探模型边界的提示词汇在一起。它今天冲进前四，说明这条线一直有人在看。",
        "problems": [
            "<strong>边界不透明：</strong>模型能做什么、不能做什么，文档说不清，只能试。",
            "<strong>安全测试没有公开语料：</strong>红队要素材，官方不会给。",
            "<strong>规则更新快：</strong>这次有效的写法，下个版本就失效。"
        ],
        "usage": [
            "浏览仓库里的分类，了解常见的提示词手法。",
            "在自有模型或获得授权的环境里做安全评估。",
            "把有效样本整理成测试用例，纳入回归。"
        ],
        "insights": [
            "<strong>一个纯文本仓库能进前四：</strong>它没有一行产品代码，价值全在「哪些话能突破限制」这份经验上。这类仓库的存在，说明模型的安全边界仍然是靠外部社区在测绘。",
            "<strong>它和同榜的 Claude-Red、Cloudflare 审计技能是一体两面：</strong>厂商做防守，民间做试探，中间靠公开的越狱样本互相校准。缺了任何一边，边界都会失真。",
            "<strong>本质是安全研究没有中立的观察位：</strong>想知道墙有多高，只能去撞。这也是为什么这类仓库永远会存在，也永远会处在争议里。"
        ],
        "tags": ["jailbreak", "ai-safety", "red-team", "prompt", "research"]
    },
    {
        "rank": 5,
        "owner": "pbakaus",
        "name": "impeccable",
        "fullName": "pbakaus / impeccable",
        "org": "pbakaus",
        "url": "https://github.com/pbakaus/impeccable",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "91,377",
        "forks": "5,405",
        "starsToday": "1,471",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,471★！9.14万★ 第3次登榜（7 月底 5.15万★，三个月涨了 4 万）。给编码 agent 的一套设计词汇：用 polish、bolder 这类词调方向，用 critique、audit 做检查，目标是在东西发出去之前抓住 AI slop。",
        "problems": [
            "<strong>跟模型说「好看」没用：</strong>形容词太模糊，模型只会往模板上靠。",
            "<strong>风格无法复用：</strong>这次调对了，下次换个项目又要重来。",
            "<strong>问题发现得太晚：</strong>上线之后才看出排版和层级不对。"
        ],
        "usage": [
            "按 README 接入编码 agent（Rust 实现，提供命令行入口）。",
            "用 polish、bolder 这类指令调整现有界面。",
            "发布前跑 critique 与 audit，把问题挡在合并之前。"
        ],
        "insights": [
            "<strong>三个月涨 4 万星：</strong>它的核心不是代码，是一套词汇。给模型一套可执行的词，比给它一段描述有效得多，这是今年工具设计里最实用的一条经验。",
            "<strong>它和 hallmark 分工清楚：</strong>hallmark 给规则，impeccable 给词汇。前者告诉你别做什么，后者告诉你往哪调。两个都上榜，说明这个需求已经细到需要两套工具。",
            "<strong>本质是「设计」正在被翻译成模型能听懂的语言：</strong>过去设计师靠参考图和经验沟通，现在要靠动词和约束。谁能把品味转成指令，谁就定义了 AI 时代的设计流程。"
        ],
        "tags": ["design", "agent-skill", "rust", "cli", "frontend"]
    },
    {
        "rank": 6,
        "owner": "elayadesign",
        "name": "ai-design-skills",
        "fullName": "elayadesign / ai-design-skills",
        "org": "elayadesign",
        "url": "https://github.com/elayadesign/ai-design-skills",
        "lang": "",
        "langClass": "",
        "stars": "10,616",
        "forks": "758",
        "starsToday": "1,395",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,395★ 首登！1.06万★。仓库描述是空的，从命名看是一套给 AI 用的设计技能合集。空描述还能冲进前六，说明它是被设计圈直接推上来的，不需要解释自己是谁。",
        "problems": [
            "<strong>技能散落在各处：</strong>每个人各写一份，格式和标准都不统一。",
            "<strong>不知道从哪套开始：</strong>设计流程有好几个环节，新手缺一份清单。",
            "<strong>空描述难判断质量：</strong>仓库不说清适用场景，用户只能靠 star 数猜。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/elayadesign/ai-design-skills.git</code></pre>",
            "按目录结构挑需要的技能，装进你的编码 agent。",
            "对照 README 的说明串成一条从需求到成品的流程。"
        ],
        "insights": [
            "<strong>空描述 + 1,395 日增：</strong>这是今天最反常的一条。没有说明文档的项目通常靠内部推荐传播，它的用户大概已经在设计社群里知道它是什么。",
            "<strong>它是这条设计线的第三块拼图：</strong>hallmark 管底线，impeccable 管调节，它管流程。三件东西同一天在榜，说明设计技能已经从单点技巧长成了体系。",
            "<strong>本质是设计师在给自己造工具：</strong>这批仓库的作者大多不是工程师，是设计师。他们把自己的工作方法写成技能，交给 agent 执行，这是专业能力第一次以这种形式被分发。"
        ],
        "tags": ["design", "agent-skills", "ui", "frontend", "collection"]
    },
    {
        "rank": 7,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra (Jesse Vincent)",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "306,977",
        "forks": "27,321",
        "starsToday": "1,096",
        "count": 19,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,096★！30.70万★ 第19次登榜，突破三十万星。一套 Agent 技能框架加软件开发方法论，作者是 Perl 圈的老面孔 Jesse Vincent。它把技能做成可以像软件包一样安装、卸载的东西。",
        "problems": [
            "<strong>Agent 技能没法管理：</strong>散落在各个文件夹和聊天记录里，装了什么、还剩什么都不清楚。",
            "<strong>方法论缺席：</strong>模型能力够强，却没人告诉它该按什么流程干活。",
            "<strong>平台不通用：</strong>在 A 工具里能用的技能，换到 B 工具就废。"
        ],
        "usage": [
            "安装 CLI：<pre><code>npm install -g superpowers</code></pre>",
            "搜索技能：<pre><code>superpowers search &quot;test generator&quot;</code></pre>",
            "安装技能：<pre><code>superpowers install writing-plans</code></pre>，自动配置到当前编辑器。"
        ],
        "insights": [
            "<strong>第19次登榜、突破三十万星：</strong>它从 5 月的 18.9 万涨到现在，五个月增加了 11.8 万。榜单换了几十次面孔，它几乎每次都在，这已经不是热度，是默认安装。",
            "<strong>今天它和三个设计技能同榜：</strong>一个技能管理框架，加上三套具体技能。生态分层已经很清楚了，底层管安装和版本，上层管具体领域。这和 npm 生态的结构一模一样。",
            "<strong>本质是技能正在变成一种新的软件品类：</strong>有包管理器、有版本、有作者署名、有垂直分类。它比插件轻，比提示词重，恰好卡在能被分发的位置上。"
        ],
        "tags": ["agent-framework", "skills", "shell", "cli", "methodology"]
    },
    {
        "rank": 8,
        "owner": "JetBrains",
        "name": "thinkrail",
        "fullName": "JetBrains / thinkrail",
        "org": "JetBrains",
        "url": "https://github.com/JetBrains/thinkrail",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "4,592",
        "forks": "239",
        "starsToday": "1,075",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,075★ 首登！4,592★。JetBrains 出的轻量 IDE，主打 vibe coding：它会围绕你的工作方式自我定制。老牌 IDE 厂商第一次用「轻」和「随你变」来定义一款编辑器，而不是功能多。",
        "problems": [
            "<strong>重型 IDE 启动慢：</strong>为了改两行代码，要等一整套索引和插件加载完。",
            "<strong>界面不能随人变：</strong>多数编辑器的布局是固定的，用户只能适应它。",
            "<strong>AI 功能像外挂：</strong>补全和对话被塞进侧栏，和编辑动作是两张皮。"
        ],
        "usage": [
            "按 README 安装（TypeScript 项目，桌面端）。",
            "用自然语言描述任务，让它生成并修改代码。",
            "按自己的习惯调整布局，让它围绕工作流成形。"
        ],
        "insights": [
            "<strong>JetBrains 亲自下场做轻量编辑器：</strong>这家公司过去二十年的策略是把功能做全，现在推一个「围绕你自我定制」的产品，等于承认重型 IDE 这条路已经走到边际收益递减。",
            "<strong>首日 4,592 星不算高，但意义不同：</strong>大厂新品上榜通常靠品牌带来的初始关注，真正的考验是三个月后还在不在。它的对手不是 VS Code，是用户已经形成的习惯。",
            "<strong>本质是编辑器在向 agent 让位：</strong>当代码主要由模型写，IDE 的重心从「人怎么敲」转向「人怎么审」。JetBrains 这一步，是在重写自己的产品假设。"
        ],
        "tags": ["ide", "vibe-coding", "typescript", "jetbrains", "developer-tools"]
    },
    {
        "rank": 9,
        "owner": "nightly-labs",
        "name": "openbot",
        "fullName": "nightly-labs / openbot",
        "org": "nightly-labs",
        "url": "https://github.com/nightly-labs/openbot",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "2,928",
        "forks": "289",
        "starsToday": "1,053",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,053★ 首登！2,928★。本地优先的桌面工作区，用来养一群常驻的 AI 队友：Codex、Claude、Grok 各自有独立工作区、任务队列、文件共享和浏览器。定位不是「一个 agent」，是「一间办公室」。",
        "problems": [
            "<strong>多个 Agent 互相看不见：</strong>各开一个窗口，文件和进度没法共享。",
            "<strong>任务没有队列：</strong>同时派几件事，谁先谁后全靠人记。",
            "<strong>数据要上云：</strong>想让 agent 常驻，就得把文件交给别人的服务器。"
        ],
        "usage": [
            "按 README 安装桌面端（TypeScript，本地运行）。",
            "为每个 Agent 分配独立工作区和任务队列。",
            "通过共享目录共享文件，按需给它浏览器权限。"
        ],
        "insights": [
            "<strong>2,928 星、日增破千：</strong>典型的新面孔爆发，基数小、增速快。它踩中的是「多个 agent 同时干活」这个刚出现的场景。",
            "<strong>「本地优先」是它和 orca 的分界：</strong>orca 做的是多端调度加远程运行时，openbot 做的是把办公室放在自己电脑上。同一个需求，一个往云走，一个往本地走。",
            "<strong>本质是 Agent 的组织形态在演化：</strong>从单个助手，到一支舰队，再到有工位、队列和共享文件夹的团队。人在这个结构里的角色，正在从操作者变成管理者。"
        ],
        "tags": ["multi-agent", "local-first", "desktop", "typescript", "workspace"]
    },
    {
        "rank": 10,
        "owner": "makecindy",
        "name": "cindy",
        "fullName": "makecindy / cindy",
        "org": "makecindy",
        "url": "https://github.com/makecindy/cindy",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "7,844",
        "forks": "922",
        "starsToday": "740",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +740★ 首登！7,844★。开源、开箱即用的 AI Agent，口号是「想到，就能做到」。不强调可配置，强调的是装完就能用。",
        "problems": [
            "<strong>开源 Agent 配置成本高：</strong>装完还要接模型、写提示词、配工具，折腾半天。",
            "<strong>闭源产品不可改：</strong>想接自己的系统，接口不开放。",
            "<strong>试用门槛高：</strong>不知道好不好用，先要花一天搭环境。"
        ],
        "usage": [
            "按 README 一键部署（TypeScript 项目）。",
            "默认配置直接跑通一个任务，确认可用。",
            "再按需接入自己的模型与工具。"
        ],
        "insights": [
            "<strong>「开箱即用」在开源 Agent 里是个空位：</strong>这一年的开源 agent 大多面向愿意折腾的人，默认体验差。它把这个空位当成卖点，赌的是不想配置的大多数。",
            "<strong>首登 7,844 星：</strong>体量不小，说明它已经积累了一段时间。这类项目真正的考验是默认配置能不能兑现承诺，而不是功能列表有多长。",
            "<strong>本质是开源在补「最后一公里」：</strong>代码开放不等于能用。把默认路径做好，比多十个可选项更能决定一个开源项目能不能被普通人用起来。"
        ],
        "tags": ["ai-agent", "open-source", "typescript", "out-of-the-box", "assistant"]
    },
    {
        "rank": 11,
        "owner": "ruvnet",
        "name": "RuView",
        "fullName": "ruvnet / RuView",
        "org": "ruvnet",
        "url": "https://github.com/ruvnet/RuView",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "100,588",
        "forks": "13,128",
        "starsToday": "415",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +415★ 首登即 10.06万★！把普通 WiFi 信号变成实时空间智能：感知人的位置、监测生命体征、判断有没有人在场，全程不需要一个摄像头像素。",
        "problems": [
            "<strong>摄像头方案有隐私硬伤：</strong>装在卧室、卫生间这类空间，视频本身就让人不适。",
            "<strong>暗光与遮挡失效：</strong>摄像头在夜里、在墙后基本没用。",
            "<strong>硬件成本高：</strong>专用雷达传感器要单独布线采购。"
        ],
        "usage": [
            "按 README 安装（Rust 实现）。",
            "用现有 WiFi 设备采集信道状态信息。",
            "跑模型输出位置、在场状态与呼吸心率等指标。"
        ],
        "insights": [
            "<strong>十多万星的首登：</strong>这个体量说明项目在圈内已经积累很久。WiFi 感知不是新方向，但把它做成开源可跑的实现，门槛一下子降了。",
            "<strong>它的价值在「没有画面」：</strong>同样能知道屋里有没有人、呼吸是否正常，却不产生可回放的影像。对养老、独居监护这类场景，这是能不能装进卧室的分界线。",
            "<strong>本质是感知正在绕开摄像头：</strong>当所有设备都在抢视觉入口，用已有的无线电波做感知，等于把家里最普通的路由器变成了传感器。"
        ],
        "tags": ["wifi-sensing", "rust", "privacy", "spatial", "iot"]
    },
    {
        "rank": 12,
        "owner": "expo",
        "name": "skills",
        "fullName": "expo / skills",
        "org": "Expo",
        "url": "https://github.com/expo/skills",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "3,375",
        "forks": "217",
        "starsToday": "212",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +212★ 首登！3,375★。Expo 官方的 AI agent 技能合集，用来处理 Expo 项目和 Expo Application Services 的构建、发布等流程。平台方开始把自家工具链写成技能。",
        "problems": [
            "<strong>移动端构建流程碎：</strong>证书、签名、打包、分发，每一步都容易卡住。",
            "<strong>Agent 不懂平台细节：</strong>通用技能给出的命令经常过时。",
            "<strong>文档是给人读的：</strong>写给人看的步骤，模型照着执行容易漏。"
        ],
        "usage": [
            "把技能目录接入支持 Agent Skills 的编码工具。",
            "在 Expo 项目里让 agent 执行构建、发布相关任务。",
            "遇到平台特有问题时，优先用官方技能里的步骤。"
        ],
        "insights": [
            "<strong>又一家平台方下场写技能：</strong>这一年已经有 Anthropic 的插件目录、Google 的 Android 技能仓库，现在轮到 Expo。平台把自己的知识做成 agent 能执行的形式，正在变成标配动作。",
            "<strong>它的价值在「不过时」：</strong>社区技能最大的问题是跟不上版本，官方维护的技能天然解决了这一点。这类仓库的竞争点不是功能多，是准确。",
            "<strong>本质是文档的读者换了一半：</strong>过去平台写文档给人看，现在还要写给模型执行。同一份知识两种读者，后者的份额在变大。"
        ],
        "tags": ["expo", "agent-skills", "mobile", "shell", "developer-tools"]
    },
    {
        "rank": 13,
        "owner": "xiaolai",
        "name": "the-craft-of-selfteaching",
        "fullName": "xiaolai / the-craft-of-selfteaching",
        "org": "xiaolai",
        "url": "https://github.com/xiaolai/the-craft-of-selfteaching",
        "lang": "Jupyter Notebook",
        "langClass": "py",
        "stars": "18,297",
        "forks": "17,866",
        "starsToday": "143",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +143★ 首登！1.83万★，但 fork 数是 1.79 万，几乎一比一。李笑来的《自学是门手艺》，一本用 Jupyter Notebook 写的自学方法书。在 AI 能把答案直接给你的年份，它讲的是怎么自己找答案。",
        "problems": [
            "<strong>答案变便宜了，方向没变便宜：</strong>搜索和问答都能秒回，但不知道学什么、怎么排顺序。",
            "<strong>教程要么太浅要么太长：</strong>跟着做完还是不会自己解决问题。",
            "<strong>学习没有反馈：</strong>错了没人指出，容易在错误路径上重复。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/xiaolai/the-craft-of-selfteaching.git</code></pre>",
            "用 Jupyter 打开，边读边跑代码。",
            "按书里的方法给自己设定练习与检查点。"
        ],
        "insights": [
            "<strong>fork 数接近 star 数：</strong>这个比例很反常。多数项目 star 远多于 fork，说明大家只是收藏；这本书被大量 fork，意味着真的有人下载下来跟着做。",
            "<strong>它出现在 AI 榜单上的时机很微妙：</strong>这一年所有人都在问「还需要学吗」。它的回答是：需要，但学的对象变了，从记知识变成设计学习路径。",
            "<strong>本质是自学能力在 AI 时代被重新定价：</strong>答案免费之后，值钱的是提出问题和判断答案对不对。这两件事都没法外包给模型。"
        ],
        "tags": ["self-teaching", "jupyter", "learning", "book", "methodology"]
    },
    {
        "rank": 14,
        "owner": "macro-inc",
        "name": "macro",
        "fullName": "macro-inc / macro",
        "org": "Macro Inc",
        "url": "https://github.com/macro-inc/macro",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "5,201",
        "forks": "507",
        "starsToday": "106",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +106★！5,201★ 第2次登榜（8 月中 2,589★，两个多月翻倍）。面向团队的统一工作区：邮件、聊天、文档、任务、agent、通话、CRM 全部 @ 互链，共享同一份 AI 记忆。",
        "problems": [
            "<strong>工具切成七八块：</strong>邮件、文档、任务、CRM 各一个系统，信息在不同地方断掉。",
            "<strong>Agent 只能看见一个工具：</strong>接进聊天就看不到邮件，接进 CRM 就看不到文档。",
            "<strong>记忆不共享：</strong>每个工具里的助手都要重新认识你一次。"
        ],
        "usage": [
            "按 README 自托管，或用云版本。",
            "把邮件、文档、任务导入同一个工作区，用 @ 建立关联。",
            "让 agent 基于共享记忆跨模块回答问题、推进任务。"
        ],
        "insights": [
            "<strong>两个多月从 2,589 翻到 5,201：</strong>涨幅不快，但对一个「全家桶」产品来说已经不容易。整合类工具最难的是让人愿意搬数据。",
            "<strong>「共享 AI 记忆」是它和 Notion、Slack 的分界：</strong>过去的协作工具共享的是文档，它共享的是上下文。agent 能不能跨模块干活，取决于这一点。",
            "<strong>本质是软件套件在按 agent 的需要重组：</strong>人用工具时能自己搬运信息，agent 不能。把邮件、任务、文档焊在一起，首先是为了让模型看得全。"
        ],
        "tags": ["workspace", "collaboration", "rust", "ai-memory", "crm"]
    }
]

# 按日增降序规整编号（平铺渲染，全部新面孔）
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

today_projects = sorted(today_projects, key=lambda p: -_today(p))
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels for the real gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = f'{gap_days}天前'
    elif label == '昨天':
        day['label'] = f'{gap_days+1}天前'
    elif label == '前天':
        day['label'] = f'{gap_days+2}天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + gap_days}天前'

new_day = {
    "date": "2026-10-28",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-28'
data['topic'] = '🔥 <strong>榜首不是 AI，真正的竞争变成了「别像 AI 做的」</strong> —— hmjz100/LinkSwift（+3,209★）拿下日增第一，一个支持八大网盘的直链下载工具，和 AI 没有任何关系；HKUDS/DeepTutor（+2,376★）首登 4.73万★，港大实验室把「终身个性化辅导」做成了产品。真正的 AI 主线在它们后面：Nutlope/hallmark（+2,109★）4.00万★，给 Claude Code、Cursor、Codex 的反 AI-slop 设计技能，三个多月涨了近四倍；pbakaus/impeccable（+1,471★）9.14万★，把设计词汇表交给编码 agent，用 polish、bolder、critique、audit 直接调风格；elayadesign/ai-design-skills（+1,395★）空描述首登 1.06万★；JetBrains/thinkrail（+1,075★）首登，一家做了二十年重型 IDE 的公司，开始卖「轻」和「随你变」。四个项目同一天在榜，指向同一件事：生成不再稀缺之后，稀缺的是看起来不像 AI 做的。另外 obra/superpowers（+1,096★）第19次登榜，突破三十万星；nightly-labs/openbot（+1,053★）做本地优先的 AI 队友办公室；togg53192-cmd/jailbreaks（+1,478★）纯文本越狱合集首登，说明模型的边界仍在靠外部社区测绘；ruvnet/RuView（+415★）10.06万★，用普通 WiFi 信号做空间感知和生命体征监测，不产生一个像素。今日主线：当所有人都能生成，判断力和审美成了唯一的分界线。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
assert nf <= 6 or st == 0, f"栏位超限: 新面孔 {nf} / 连登 {st}"
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★ count={p['count']}")
