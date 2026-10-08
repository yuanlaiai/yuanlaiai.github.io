#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-09 (10-day gap, 无昨日榜→平铺结构, 9 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 9)
gap_days = (today - last).days  # 10
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（10天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "morluto",
        "name": "rea",
        "fullName": "morluto / rea",
        "org": "morluto",
        "url": "https://github.com/morluto/rea",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "24,875",
        "forks": "2,763",
        "starsToday": "7,744",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +7,744★ 全场日增第一！2.49万★ 首登！用 Agent 做逆向工程：从应用行为一路下探到原生二进制。它把「看懂一个黑盒程序」拆成 Agent 能一步步执行的流程——先看它怎么跑、再拆它怎么实现。TypeScript 实现，和同榜的 raddebugger 同一天上榜。",
        "problems": [
            "<strong>逆向工程门槛极高：</strong>拆一个二进制要懂反汇编、调试器、调用约定，能上手的人本来就少。",
            "<strong>工具链割裂：</strong>行为观察、网络抓包、二进制分析分散在不同工具里，各自的结论很难串成一条线。",
            "<strong>黑盒只会越来越多：</strong>闭源 App、混淆代码、逻辑后移到服务端，纯静态分析看不到全貌。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/morluto/rea.git</code></pre>",
            "指向目标应用或二进制，让 Agent 从行为层开始观察，再逐层下探到实现层。",
            "产出结构化的逆向结论，可交给后续的自动化流程使用。"
        ],
        "insights": [
            "<strong>逆向这个老领域被重做了一遍：</strong>它解决的已经不是「能不能拆」，而是「不懂汇编的人能不能拆」——把专业技能的准入线往下拉，是这一波 Agent 工具的共同动作。",
            "<strong>它和 raddebugger 构成今天的一组对照：</strong>一个让 AI 替你理解程序，一个仍坚持把人训练成更好的调试者。两条路线同一天登榜，说明「看懂软件」的需求已经大到能同时养活两种解法。",
            "<strong>本质是理解软件的成本在被重估：</strong>当写代码越来越便宜，读懂别人写的代码越来越贵——逆向工具的火，是代码存量的火。"
        ],
        "tags": ["reverse-engineering", "ai-agent", "typescript", "binary-analysis", "developer-tools"]
    },
    {
        "rank": 2,
        "owner": "boykopovar",
        "name": "AnyPS5",
        "fullName": "boykopovar / AnyPS5",
        "org": "boykopovar",
        "url": "https://github.com/boykopovar/AnyPS5",
        "lang": "C++",
        "langClass": "cpp",
        "stars": "15,234",
        "forks": "1,206",
        "starsToday": "4,640",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +4,640★ 日增第二！1.52万★ 首登！把 PS5 的可执行文件自动移植到 Linux 和 Windows。主机二进制被锁在定制系统和专有运行时里，这个项目想做的事是把它「翻译」成通用平台能跑的代码。C++ 实现，和 rea、raddebugger 同一天上榜。",
        "problems": [
            "<strong>主机程序被平台锁死：</strong>PS5 跑在定制 FreeBSD 加专有运行时上，换平台几乎等于从零重写。",
            "<strong>手动移植成本吓人：</strong>系统调用、图形 API、内存模型处处不一样，一个项目几个月起步。",
            "<strong>整机模拟太慢：</strong>模拟器能跑但性能损耗大，不如把二进制转换成目标平台的原生代码。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/boykopovar/AnyPS5.git</code></pre>",
            "准备目标平台的构建环境（Linux / Windows），按文档编译工具本身。",
            "输入 PS5 可执行文件，得到可在目标平台运行的程序；实际支持范围要看 README 的兼容清单。"
        ],
        "insights": [
            "<strong>它落在一个敏感地带：</strong>主机二进制移植天然踩在版权与厂商政策的边缘，热度能起来，但能不能长期存在取决于法律而不是技术——追捧它的人应该先看清这一点。",
            "<strong>和 rea 同榜不是巧合：</strong>今天榜单冒出一整片二进制层面的工具，指向同一件事——AI 能写新代码之后，人类反而更在意「已有的代码怎么理解、怎么复用」。",
            "<strong>本质是把锁死的价值重新释放：</strong>主机靠封闭生态卖硬件，移植工具在拆这道墙——它服务的是「我买过的软件为什么不能在别的机器上跑」这个长期怨气。"
        ],
        "tags": ["ps5", "porting", "binary-translation", "cpp", "homebrew"]
    },
    {
        "rank": 3,
        "owner": "storytold",
        "name": "artcraft",
        "fullName": "storytold / artcraft",
        "org": "storytold",
        "url": "https://github.com/storytold/artcraft",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "7,648",
        "forks": "1,053",
        "starsToday": "2,510",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,510★ 日增第三！7,648★ 首登！一个用 Rust 写的创作引擎，作者给它的定位是 intentional crafting engine（刻意、有意图的创作引擎），面向艺术家、设计师和电影人。它把重点放在「创作过程可控」，而不是「一句话生成」。",
        "problems": [
            "<strong>生成式工具让人失控：</strong>输入提示词出一张图，构图、细节、风格都不可精确控制，改一处动全身。",
            "<strong>创作意图没有落点：</strong>从草图到成品之间缺一层工具，现有的要么太底层（三维软件），要么太黑箱（文生图）。",
            "<strong>多工种工具不通：</strong>艺术家、设计师、导演各自用一套软件，资产在图与模型之间来回丢。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/storytold/artcraft.git</code></pre>",
            "用 Rust 工具链构建：<pre><code>cargo build --release</code></pre>",
            "按文档导入资产、搭建场景，导出给后续制作流程使用。"
        ],
        "insights": [
            "<strong>「intentional」是今天最值钱的一个词：</strong>生成式 AI 把出图成本压到接近零之后，一批工具开始反着做——不卖「一句话生成」，卖「每一步都可控」。当生成变成免费，可控就变成稀缺。",
            "<strong>它和 diagram-design 是同一种情绪的两副面孔：</strong>一个要「不靠提示词的随机图」，一个要「不靠 Mermaid 的丑图」——今天上榜的创作者工具，投的都是同一张票。",
            "<strong>本质是创意工具在分路线：</strong>效率派押 AI 生成，掌控派押精确工具，ArtCraft 选后者——它赌的是专业创作者不会把最终控制权交出去。"
        ],
        "tags": ["creative-tools", "rust", "art", "design", "rendering"]
    },
    {
        "rank": 4,
        "owner": "mattpocock",
        "name": "skills",
        "fullName": "mattpocock / skills",
        "org": "mattpocock",
        "url": "https://github.com/mattpocock/skills",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "280,973",
        "forks": "23,551",
        "starsToday": "1,770",
        "count": 9,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,770★！28.1万★ 第9次登榜（两个月前 20.9万★）。Matt Pocock 把自己 .agents 目录里的技能直接开源出来，仓库说明只有一句：给真正的工程师用的技能。TypeScript 圈最有影响力的教育者之一，把个人 Agent 工作流原样交出。",
        "problems": [
            "<strong>Agent 技能全靠自己攒：</strong>每个人从零写自己的提示词和技能，重复造轮子，还造得不好。",
            "<strong>公开技能良莠不齐：</strong>大部分是演示品，看着漂亮，真干活时用不上。",
            "<strong>不知道信谁的：</strong>技能满天飞，缺一个能判断「这套靠不靠谱」的可信来源。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/mattpocock/skills.git</code></pre>",
            "把需要的技能目录拷进你自己的 .agents / skills 目录。",
            "在 Claude Code、Codex 等支持技能的工具里直接调用。"
        ],
        "insights": [
            "<strong>第9次登榜，是榜单上最持久的项目之一：</strong>从 5 月的 7.6 万星涨到今天的 28 万星，半年翻近四倍。技能库这个品类已经固化下来，不再是尝鲜。",
            "<strong>卖点是署名，不是功能：</strong>描述里那句「straight from my .agents directory」（直接来自我的 .agents 目录）才是关键——技能不缺，缺的是「这个人写的」。",
            "<strong>本质是 Agent 生态在走开源的老路：</strong>从个人配置变成公开技能库，很像十几年前 dotfiles 流行的那一阵——工具越强，个人配置越会变成一种可分享、可 star 的资产。"
        ],
        "tags": ["agent-skills", "shell", "dotfiles", "developer-tools", "ai-agent"]
    },
    {
        "rank": 5,
        "owner": "cathrynlavery",
        "name": "diagram-design",
        "fullName": "cathrynlavery / diagram-design",
        "org": "cathrynlavery",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "lang": "HTML",
        "langClass": "html",
        "stars": "46,211",
        "forks": "2,942",
        "starsToday": "1,163",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,163★！4.62万★ 第6次登榜（19天前 3.73万★）。给编码 Agent 用的图表设计技能：42 种图表类型，输出自包含的 HTML 加 SVG。仓库说明里两句狠话——不要阴影，不要 Mermaid 那种糊弄——矛头直接对准「能用就行」的自动生成图。",
        "problems": [
            "<strong>Agent 默认产出的图见不得人：</strong>流程图千篇一律、配色难看，放进正式文档一眼就露怯。",
            "<strong>样式改不动：</strong>想调一个图表的配色或排版，只能改提示词碰运气，试十次不一定对一次。",
            "<strong>导出不自由：</strong>很多图表依赖渲染服务，想嵌进自己的文档或网页得绕一大圈。"
        ],
        "usage": [
            "把技能装进 Claude Code / Codex / GitHub Copilot / Factory Droid / Pi。",
            "用自然语言说清图表需求，从 42 种类型里选一种。",
            "得到自包含的 HTML 加 SVG，可直接嵌进文档或网页，不依赖外部渲染。"
        ],
        "insights": [
            "<strong>第6次登榜、隔了19天又回来：</strong>说明它已经从「试用的新玩具」变成很多人工作流里的固定件——回到榜单是习惯，不是新闻。",
            "<strong>「No Mermaid slop」是一句定位宣言：</strong>在 Agent 什么都能生成的时代，「生成得好看且可控」本身成了生意。它卖的其实不是功能，是审美。",
            "<strong>兼容名单越来越长：</strong>Claude Code、Codex、Copilot、Factory Droid、Pi 一个不落——技能一旦标准化，作者就得同时伺候所有 Agent 平台，这是继浏览器兼容之后开发者的第二次多端适配负担。"
        ],
        "tags": ["diagram", "svg", "agent-skill", "design", "documentation"]
    },
    {
        "rank": 6,
        "owner": "thedotmack",
        "name": "claude-mem",
        "fullName": "thedotmack / claude-mem",
        "org": "TheDotMack",
        "url": "https://github.com/thedotmack/claude-mem",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "98,388",
        "forks": "8,631",
        "starsToday": "662",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +662★！9.84万★ 第2次登榜（上次是 5 月，7.86万★）。给所有 Agent 装长期记忆：会话里发生的每件事全部记下，用 AI 压缩成结构化记忆，下次会话自动把相关的塞回上下文。兼容名单一路排到 Claude Code、Codex、Gemini、Hermes、Copilot、OpenCode。",
        "problems": [
            "<strong>每次对话都从零开始：</strong>Agent 记不住上个会话的偏好、决定和踩过的坑。",
            "<strong>用户被迫当搬运工：</strong>每开一轮新对话，都要手动把背景信息再粘一遍。",
            "<strong>记忆被平台锁住：</strong>各家自带的记忆互不通用，换个工具就断档。"
        ],
        "usage": [
            "按 README 安装（TypeScript 项目，支持多个 Agent 平台）。",
            "让它接管会话记录，AI 自动压缩成可检索的记忆条目。",
            "新会话开始时，相关记忆自动注入上下文，不用再手动喂。"
        ],
        "insights": [
            "<strong>两次登榜之间涨了 2 万星：</strong>冷启动型的工具很少能有这种走势，说明「记不住」是 Agent 使用里最痛的一根刺。",
            "<strong>兼容名单本身就是一份路线图：</strong>从 Claude Code 到 Hermes、OpenCode，一个第三方中间件把七种 Agent 全接上——记忆层正在变成独立于具体模型的公共设施。",
            "<strong>本质是上下文主权之争：</strong>模型厂商希望记忆留在自家平台，第三方希望记忆变成可随身携带的资产——谁掌握记忆，谁就掌握了用户换工具时的黏性。"
        ],
        "tags": ["memory", "context", "ai-agent", "typescript", "cross-platform"]
    },
    {
        "rank": 7,
        "owner": "liquidslr",
        "name": "system-design-notes",
        "fullName": "liquidslr / system-design-notes",
        "org": "liquidslr",
        "url": "https://github.com/liquidslr/system-design-notes",
        "lang": "",
        "langClass": "",
        "stars": "24,552",
        "forks": "4,594",
        "starsToday": "398",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +398★！2.46万★ 第2次登榜（19天前 1.85万★）。Alex Xu《系统设计面试》的浓缩笔记：把一本面试书拆成可以在 GitHub 上检索的仓库。没有代码，全是知识点，19 天涨了 6,000 星。",
        "problems": [
            "<strong>系统设计知识太散：</strong>缓存、分片、一致性、限流，每个话题都能写一本书，资料天南地北。",
            "<strong>书查起来慢：</strong>纸质书和 PDF 没法全文检索，想找一个概念得来回翻。",
            "<strong>读完成本高：</strong>完整啃一本系统设计书要几十个小时，大多数人半途就放下了。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/liquidslr/system-design-notes.git</code></pre>",
            "按主题（缓存、消息队列、一致性等）快速查阅。",
            "面试前把它当复习清单过一遍，对照原书补细节。"
        ],
        "insights": [
            "<strong>19 天涨 6,000 星：</strong>一个没有代码、纯笔记的仓库能持续涨星，说明「高密度的知识整理」本身就是稀缺品——不是没人知道这些知识，是没人替你把它们压成能读的样子。",
            "<strong>它和 raddebugger、AnyPS5 排在同一张榜上：</strong>一边是最硬核的二进制工具，一边是一份读书笔记——GitHub 榜单早就不区分「代码」和「知识」了。",
            "<strong>本质是知识载体在搬家：</strong>从出版的纸质书到可检索、可 star、可 fork 的仓库，连面试复习都被版本化管理了。"
        ],
        "tags": ["system-design", "interview", "notes", "backend", "learning"]
    },
    {
        "rank": 8,
        "owner": "anthropics",
        "name": "knowledge-work-plugins",
        "fullName": "anthropics / knowledge-work-plugins",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/knowledge-work-plugins",
        "lang": "Python",
        "langClass": "py",
        "stars": "27,475",
        "forks": "3,191",
        "starsToday": "309",
        "count": 4,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +309★！2.75万★ 第4次登榜（10天前 2.49万★）。Anthropic 官方开源、面向知识工作者的插件库，主要装在 Claude Cowork 里用。方向很清楚：把 Claude 从「陪你聊天」变成「在你的日常工作里替你干活」。",
        "problems": [
            "<strong>知识工作散落在工具里：</strong>邮件、文档、表格、会议纪要，Agent 一样都够不着。",
            "<strong>插件格式没标准：</strong>各家 Agent 的插件互不兼容，写一个只能给一个平台用。",
            "<strong>企业想用又不敢用：</strong>缺官方背书的插件，安全与合规没有底，落地时推不动。"
        ],
        "usage": [
            "从仓库取出需要的插件，装进 Claude Cowork。",
            "按具体场景（文档处理、研究、协作）挑对应插件。",
            "官方维护，跟 Claude 的版本一起更新。"
        ],
        "insights": [
            "<strong>第4次登榜、10 天涨 2,500 星：</strong>官方插件库的走势比个人项目稳得多，这是生态在成熟的信号——厂商开始下场定义「插件长什么样」。",
            "<strong>关键词是 Cowork，不是 Code：</strong>Anthropic 的注意力正从「给开发者的编码」扩到「给知识工作者的日常」——后者人群大得多，也是和 OpenAI 正面撞上的战场。",
            "<strong>本质是 Agent 的入口之争：</strong>谁定了插件格式，谁就定了用户在哪儿调用 Agent。插件库是平台把触角伸进别人日常工作流的方式。"
        ],
        "tags": ["plugins", "anthropic", "knowledge-work", "claude", "productivity"]
    },
    {
        "rank": 9,
        "owner": "EpicGames",
        "name": "raddebugger",
        "fullName": "EpicGames / raddebugger",
        "org": "Epic Games",
        "url": "https://github.com/EpicGames/raddebugger",
        "lang": "C",
        "langClass": "c",
        "stars": "8,088",
        "forks": "391",
        "starsToday": "283",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +283★ 首登！8,088★。Epic Games 开源的原生图形化调试器：用户态、多进程，纯 C 实现。在 AI 批量生成代码的当下，它解决的是最反潮流的问题——程序出了事，怎么看清一堆进程到底在干什么。",
        "problems": [
            "<strong>现代调试器又重又慢：</strong>IDE 自带的调试器在一堆进程里卡顿，看不了全局状态。",
            "<strong>多进程难调：</strong>服务、渲染、插件各跑各的，断点很难跨进程跟着走。",
            "<strong>老牌工具停在过去：</strong>WinDbg、GDB 功能强，但界面和体验把新人挡在门外。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/EpicGames/raddebugger.git</code></pre>",
            "用仓库自带的构建脚本编译（以 Windows 平台为主，需要 C 工具链）。",
            "附加到目标进程，做跨进程断点、内存与线程观察。"
        ],
        "insights": [
            "<strong>Epic 开源自家调试器这件事值得记一笔：</strong>游戏引擎公司把内部工具放出来，赌的是开发者生态而不是卖软件——引擎战争的战场已经挪到了工具链。",
            "<strong>它和 rea 同一天上榜：</strong>一个用 AI 替你看懂程序，一个把你武装成更强的调试者。两条路都通向同一个结论：软件越复杂，「看懂它」越值钱。",
            "<strong>本质是 AI 时代稀缺能力在倒转：</strong>写代码变便宜之后，读代码、定位问题、理解系统成了最贵的能力——所以调试器这种「老工具」会被重新翻出来，摆到榜单上。"
        ],
        "tags": ["debugger", "c", "windows", "epic-games", "developer-tools"]
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
    "date": "2026-10-09",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-09'
data['topic'] = '🔥 <strong>Agent 的记忆与技能层正在固化 + 逆向工程被 Agent 重做 + 可控创作与硬核工具同日回归</strong> —— morluto/rea（+7,744★）单日拿下全场第一，Agent 驱动的逆向工程从应用行为一路下探到原生二进制，和 Epic 开源的 raddebugger（+283★）同日上榜：一个让 AI 替你拆黑盒，一个仍坚持把人武装成更好的调试者。boykopovar/AnyPS5（+4,640★）把 PS5 可执行文件自动移植到 Linux / Windows，落在主机生态最敏感的地带。Agent 技能与记忆继续霸榜：mattpocock/skills（+1,770★）28万星第9次、cathrynlavery/diagram-design（+1,163★）第6次、thedotmack/claude-mem（+662★）第2次，兼容名单都拉到了七个以上 Agent 平台。创作工具在用脚投票：storytold/artcraft（+2,510★）的 intentional crafting engine 与 diagram-design 的「No Mermaid slop」，投的都是「可控」而不是「生成」。知识资产也在版本化：liquidslr/system-design-notes（+398★）2.46万星、anthropics/knowledge-work-plugins（+309★）第4次。今日三条主线：一、Agent 的记忆与技能正从个人配置变成可分享的资产，跨平台兼容成了默认要求；二、逆向与调试工具集体爆发，软件越复杂，看懂它的能力越稀缺；三、创作者用工具投票，可控性正在取代生成能力成为卖点。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★ count={p['count']}")
