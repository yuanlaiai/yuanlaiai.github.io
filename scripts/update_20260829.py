#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-29 (1-day gap, 双栏结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 29)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 🆕 新面孔 ──
    {
        "rank": 1,
        "owner": "tailscale",
        "name": "tailcat",
        "fullName": "tailscale / tailcat",
        "org": "Tailscale",
        "url": "https://github.com/tailscale/tailcat",
        "lang": "Go",
        "langClass": "go",
        "stars": "3,136",
        "forks": "68",
        "starsToday": "790",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +790★！3.1K★ 首登！像 netcat 一样，但走 Tailscale 数据面——不需要控制面的 P2P 网络瑞士军刀。",
        "problems": [
            "<strong>内网穿透复杂：</strong>netcat 等工具无法穿透 NAT 和防火墙。",
            "<strong>VPN 配置繁琐：</strong>传统组网需要控制面协调，配置复杂。",
            "<strong>P2P 工具缺失：</strong>缺少开箱即用的安全点对点连接工具。"
        ],
        "usage": [
            "安装：<pre><code>go install tailscale.com/cmd/tailcat@latest</code></pre>",
            "连接：<pre><code>tailcat <peer> <port></code></pre>",
            "在 Tailscale 网络内像 netcat 一样传输数据。"
        ],
        "insights": [
            "<strong>3.1K★ 首登：</strong>Tailscale 官方的 netcat 替代品——P2P 网络工具需求旺盛。",
            "<strong>去掉控制面：</strong>直接用数据面建连——去中心化网络工具的极简主义。",
            "<strong>基础设施玩家下场：</strong>Tailscale 补上最后一块拼图——安全组网从「配置」变「默认」。"
        ],
        "tags": ["tailscale", "netcat", "p2p", "networking", "go"]
    },
    {
        "rank": 2,
        "owner": "tashfeenahmed",
        "name": "freellmapi",
        "fullName": "tashfeenahmed / freellmapi",
        "org": "tashfeenahmed",
        "url": "https://github.com/tashfeenahmed/freellmapi",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "21,971",
        "forks": "2,340",
        "starsToday": "612",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +612★！22K★ 首登！免费 LLM API 聚合——74 亿 tokens/月、34 家免费提供商、635 个端点，统一 /v1 入口。",
        "problems": [
            "<strong>免费 LLM 分散：</strong>各家免费模型散落不同平台，管理困难。",
            "<strong>API 不兼容：</strong>不同提供商 API 格式各异，切换成本高。",
            "<strong>免费额度难追踪：</strong>多平台免费额度各自为政。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/tashfeenahmed/freellmapi.git</code></pre>",
            "配置免费提供商密钥。",
            "用统一 /v1 端点调用所有免费模型。"
        ],
        "insights": [
            "<strong>22K★ 的免费聚合：</strong>74 亿 tokens/月——免费 LLM 的「中央交换机」首登。",
            "<strong>与 sub2api/free-claude-code 同源：</strong>免费化浪潮第三弹——开发者对 API 价格的抵抗全面组织化。",
            "<strong>智能路由：</strong>635 个端点自动调度——免费资源也能当生产环境用。"
        ],
        "tags": ["llm", "free", "api", "aggregator", "openai-compatible"]
    },
    {
        "rank": 3,
        "owner": "NationalSecurityAgency",
        "name": "ghidra",
        "fullName": "NationalSecurityAgency / ghidra",
        "org": "NSA",
        "url": "https://github.com/NationalSecurityAgency/ghidra",
        "lang": "Java",
        "langClass": "java",
        "stars": "73,517",
        "forks": "8,920",
        "starsToday": "375",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +375★！73.5K★ 首登！NSA 开源的逆向工程框架——安全研究者的标配武器。",
        "problems": [
            "<strong>逆向工具贵：</strong>IDA Pro 等商业逆向工具价格高昂。",
            "<strong>二进制分析门槛：</strong>恶意软件分析需要专业工具链。",
            "<strong>漏洞研究难：</strong>缺乏开源的高质量逆向框架。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/NationalSecurityAgency/ghidra.git</code></pre>",
            "启动 Ghidra 分析二进制文件。",
            "用反编译/调试功能研究恶意软件。"
        ],
        "insights": [
            "<strong>73.5K★ 的 NSA 开源：</strong>Ghidra 首登——政府级工具开源是安全研究的里程碑。",
            "<strong>与 AI 结合：</strong>逆向工程 + 编码 Agent——AI 正在进入二进制分析。",
            "<strong>安全工具链升温：</strong>AI 时代安全研究工具需求持续——ghidra 是其中的老兵。"
        ],
        "tags": ["reverse-engineering", "security", "malware", "nsa", "binary-analysis"]
    },
    {
        "rank": 4,
        "owner": "cursor",
        "name": "plugins",
        "fullName": "cursor / plugins",
        "org": "Cursor",
        "url": "https://github.com/cursor/plugins",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "6,087",
        "forks": "300",
        "starsToday": "257",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +257★！6.1K★ 隔日回归！Cursor 插件规范 + 官方插件库——编码 IDE 的生态主导权之争。",
        "problems": [
            "<strong>插件生态混乱：</strong>Cursor 插件缺少统一规范。",
            "<strong>官方插件分散：</strong>功能插件各自独立，体验割裂。",
            "<strong>生态标准缺位：</strong>第三方插件质量参差。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cursor/plugins.git</code></pre>",
            "查看插件规范与官方插件。",
            "按规范开发或安装 Cursor 插件。"
        ],
        "insights": [
            "<strong>隔日回归 6.1K★：</strong>5/28 → 8/23 → 8/29——Cursor 插件生态持续吸星。",
            "<strong>插件规范即话语权：</strong>Cursor 定义插件标准——生态主导权之争从 IDE 延伸到插件层。",
            "<strong>编码 Agent 生态战：</strong>Anthropic 插件双仓库、Cursor 插件规范、OpenAI CLI——三方混战。"
        ],
        "tags": ["cursor", "plugins", "ide", "ecosystem", "typescript"]
    },
    {
        "rank": 5,
        "owner": "livekit",
        "name": "agents",
        "fullName": "livekit / agents",
        "org": "LiveKit",
        "url": "https://github.com/livekit/agents",
        "lang": "Python",
        "langClass": "py",
        "stars": "13,473",
        "forks": "1,040",
        "starsToday": "256",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +256★！13.5K★ 首登！实时语音 AI Agent 框架——语音 Agent 开发的标配基础设施。",
        "problems": [
            "<strong>语音 Agent 门槛高：</strong>实时语音交互涉及 ASR/TTS/网络传输全链路。",
            "<strong>实时通信复杂：</strong>低延迟语音传输需要专业 WebRTC 支持。",
            "<strong>多模态编排难：</strong>语音 Agent 需要音频+模型+工具协同。"
        ],
        "usage": [
            "安装：<pre><code>pip install livekit-agents</code></pre>",
            "构建实时语音 Agent。",
            "接入 ASR/TTS 与 LLM 完成对话。"
        ],
        "insights": [
            "<strong>13.5K★ 的语音 Agent 框架：</strong>livekit 首登——语音 AI 是 Agent 的下一个主战场。",
            "<strong>实时音视频 + AI：</strong>WebRTC 基建 + LLM——语音 Agent 的「水电煤」。",
            "<strong>与边缘 AI 呼应：</strong>语音交互是最自然的 AI 入口——这个赛道正在起量。"
        ],
        "tags": ["voice-ai", "realtime", "agent", "webrtc", "python"]
    },
    {
        "rank": 6,
        "owner": "ChromeDevTools",
        "name": "chrome-devtools-mcp",
        "fullName": "ChromeDevTools / chrome-devtools-mcp",
        "org": "Chrome DevTools",
        "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "50,084",
        "forks": "2,120",
        "starsToday": "215",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +215★！50.1K★ 隔日回归！Chrome DevTools 官方 MCP——给编码 Agent 装上浏览器调试能力。",
        "problems": [
            "<strong>Agent 调试网页难：</strong>编码 Agent 无法操作浏览器 DevTools。",
            "<strong>前端调试自动化缺位：</strong>Agent 写完前端无法自测。",
            "<strong>MCP 生态缺官方工具：</strong>浏览器调试类 MCP 服务器质量参差。"
        ],
        "usage": [
            "配置 MCP 服务器指向 chrome-devtools-mcp。",
            "让编码 Agent 打开浏览器调试。",
            "Agent 自动检查 DOM、控制台、网络请求。"
        ],
        "insights": [
            "<strong>50.1K★ 官方 MCP：</strong>Chrome 官方下场给 Agent 做调试工具——MCP 生态的里程碑。",
            "<strong>Agent 全栈闭环：</strong>写代码 + 调试浏览器——编码 Agent 从「写」到「验」。",
            "<strong>5/21 后回归：</strong>官方工具 + Agent 浪潮——浏览器调试自动化成为标配。"
        ],
        "tags": ["chrome", "mcp", "devtools", "coding-agent", "debugging"]
    },
    # ── 🔥 连登追踪 ──
    {
        "rank": 7,
        "owner": "tt-a1i",
        "name": "archify",
        "fullName": "tt-a1i / archify",
        "org": "tt-a1i",
        "url": "https://github.com/tt-a1i/archify",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "29,580",
        "forks": "980",
        "starsToday": "3,927",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +3,927★！29.6K★ 三连登再破三千！架构图 Agent 技能——三天累计 9,100★，技能经济的神话继续。",
        "problems": [
            "<strong>架构图绘制费时：</strong>手动画架构图/流程图耗时且难维护。",
            "<strong>图表工具割裂：</strong>不同图表类型要用不同工具。",
            "<strong>可验证性缺失：</strong>图与实际代码/架构脱节。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/tt-a1i/archify.git</code></pre>",
            "加载 SKILL.md 到 AI 助手。",
            "让 Agent 生成自包含 HTML 架构图。"
        ],
        "insights": [
            "<strong>三连登累计 9,100★：</strong>+1,002 → +4,239 → +3,927——架构图技能成为技能经济最大赢家。",
            "<strong>自包含 HTML：</strong>单文件图表 + 动效 + 可导出——Agent 技能正在工业化。",
            "<strong>技能经济现象级：</strong>archify 三天从 17K 冲到 29.6K——单技能库的极限在哪里。"
        ],
        "tags": ["agent-skills", "architecture", "diagrams", "html", "visualization"]
    },
    {
        "rank": 8,
        "owner": "bilawalsidhu",
        "name": "gods-eye-view",
        "fullName": "bilawalsidhu / gods-eye-view",
        "org": "bilawalsidhu",
        "url": "https://github.com/bilawalsidhu/gods-eye-view",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "11,953",
        "forks": "680",
        "starsToday": "1,870",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,870★！12K★ 连登！浏览器间谍卫星模拟器——真实数据 3D 地球空间情报，两天累计近四千星。",
        "problems": [
            "<strong>空间情报门槛高：</strong>卫星数据可视化需要专业 GIS 工具。",
            "<strong>3D 地球渲染复杂：</strong>真实感地球可视化开发成本极高。",
            "<strong>数据封闭：</strong>卫星数据被商业公司垄断，普通人接触不到。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/bilawalsidhu/gods-eye-view.git</code></pre>",
            "本地启动浏览器 3D 地球。",
            "接入真实卫星数据源浏览空间情报。"
        ],
        "insights": [
            "<strong>连登两天累计近四千：</strong>+1,984 → +1,870——「上帝视角」热度持续。",
            "<strong>开源空间情报：</strong>真实卫星数据 + 浏览器渲染——空间情报民主化。",
            "<strong>个人开发者杰作：</strong>bilawal 的浏览器卫星项目——个人开发者也能引爆现象级。"
        ],
        "tags": ["spatial-intelligence", "satellite", "3d-globe", "visualization", "open-source"]
    },
    {
        "rank": 9,
        "owner": "K-Dense-AI",
        "name": "scientific-agent-skills",
        "fullName": "K-Dense-AI / scientific-agent-skills",
        "org": "K-Dense AI",
        "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "37,409",
        "forks": "2,140",
        "starsToday": "1,604",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,604★！37.4K★ 连登破千！把任何 AI Agent 变成 AI 科学家——163 个技能 + 100+ 科学数据库。",
        "problems": [
            "<strong>科研工具链复杂：</strong>科学家做数据分析需要大量编程技能。",
            "<strong>领域知识门槛：</strong>生物学/化学等领域的专业分析需要领域技能。",
            "<strong>Agent 不懂科学：</strong>通用 Agent 缺乏科研工作流支持。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/K-Dense-AI/scientific-agent-skills.git</code></pre>",
            "加载科研技能到 AI Agent。",
            "让 Agent 辅助生物学/化学等科研工作。"
        ],
        "insights": [
            "<strong>单日破千：</strong>+498 → +1,604——科研技能库热度翻三倍，AI 科学家进入主流。",
            "<strong>17.5 万科学家的选择：</strong>163 个验证技能 + 100+ 科学数据库——纵向深耕的样板。",
            "<strong>技能库立体化：</strong>横向通用库 + 纵向科学库——Agent 技能生态完整成型。"
        ],
        "tags": ["scientific", "agent-skills", "research", "biology", "science"]
    },
    {
        "rank": 10,
        "owner": "freestylefly",
        "name": "awesome-gpt-image-2",
        "fullName": "freestylefly / awesome-gpt-image-2",
        "org": "freestylefly",
        "url": "https://github.com/freestylefly/awesome-gpt-image-2",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "24,789",
        "forks": "1,960",
        "starsToday": "767",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +767★！24.8K★ 五连登！GPT-Image2 提示词引擎——五天累计 12,000+★，提示词工程的传奇继续。",
        "problems": [
            "<strong>图片提示词玄学：</strong>GPT 图片生成效果不稳定，提示词靠猜。",
            "<strong>优秀案例难沉淀：</strong>社区好提示词分散，无法系统复用。",
            "<strong>工程化缺失：</strong>图片生成缺乏模板化、版本化管理。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/freestylefly/awesome-gpt-image-2.git</code></pre>",
            "浏览 530+ 逆向工程案例。",
            "套用 20+ 工业级模板生成图片。"
        ],
        "insights": [
            "<strong>五连登累计 12,000+★：</strong>+2,442 → +1,698 → +4,044 → +2,096 → +767——提示词工程持续霸榜五天。",
            "<strong>Prompt as Code 全球验证：</strong>中文开发者把提示词做成模板库——图片生成工程化被全球采纳。",
            "<strong>提示词经济成型：</strong>案例逆向 + 模板复用——提示词正在变成可交易的知识资产。"
        ],
        "tags": ["gpt-image", "prompt-engineering", "templates", "ai-image", "awesome-list"]
    },
    {
        "rank": 11,
        "owner": "anthropics",
        "name": "claude-plugins-official",
        "fullName": "anthropics / claude-plugins-official",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/claude-plugins-official",
        "lang": "Python",
        "langClass": "py",
        "stars": "35,225",
        "forks": "1,300",
        "starsToday": "356",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +356★！35.2K★ 四连登！Anthropic 官方管理的高质量 Claude Code 插件目录——插件生态的「官方认证」。",
        "problems": [
            "<strong>插件质量无保障：</strong>第三方插件良莠不齐，安全风险高。",
            "<strong>官方插件难发现：</strong>高质量插件缺少官方认证渠道。",
            "<strong>生态信任缺失：</strong>开发者不敢随意安装社区插件。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/anthropics/claude-plugins-official.git</code></pre>",
            "浏览 Anthropic 官方认证插件。",
            "安装高质量 Claude Code 插件。"
        ],
        "insights": [
            "<strong>四连登：</strong>+55 → +307 → +292 → +356——官方插件目录稳定吸星。",
            "<strong>官方 + 社区双轨：</strong>official（认证）+ community（投稿）——插件生态标准分层。",
            "<strong>生态战争升级：</strong>Anthropic 插件市场、Cursor 插件规范、OpenAI CLI——编码 Agent 生态全面开打。"
        ],
        "tags": ["anthropic", "claude", "plugins", "official", "ecosystem"]
    },
    {
        "rank": 12,
        "owner": "JetBrains",
        "name": "go-modern-guidelines",
        "fullName": "JetBrains / go-modern-guidelines",
        "org": "JetBrains",
        "url": "https://github.com/JetBrains/go-modern-guidelines",
        "lang": "Go",
        "langClass": "go",
        "stars": "2,754",
        "forks": "120",
        "starsToday": "294",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +294★！2.8K★ 连登！JetBrains 官方 Go 指南——专门帮 AI 编码 Agent 写现代 Go。",
        "problems": [
            "<strong>AI 写 Go 不规范：</strong>LLM 生成的 Go 代码常过时、不符合现代实践。",
            "<strong>官方指南分散：</strong>Go 最佳实践散落各处，无权威汇总。",
            "<strong>Agent 需要喂养：</strong>编码 Agent 需要高质量的领域指南作为上下文。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/JetBrains/go-modern-guidelines.git</code></pre>",
            "把指南喂给 AI 编码 Agent。",
            "让 Agent 按现代 Go 实践写代码。"
        ],
        "insights": [
            "<strong>连登两天：</strong>+300 → +294——「给 AI 看的指南」需求稳定。",
            "<strong>JetBrains 下场喂 Agent：</strong>官方出「给 AI 看的指南」——IDE 厂商拥抱 Agent 时代。",
            "<strong>指南即训练数据：</strong>高质量领域指南成为 Agent 上下文的关键资产。"
        ],
        "tags": ["jetbrains", "go", "guidelines", "ai-coding", "agent"]
    }
]

# Shift labels for 1-day gap (accurate offset: +1)
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '昨天'
    elif label == '昨天':
        day['label'] = '前天'
    elif label == '前天':
        day['label'] = '3天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + 1}天前'

# Insert new day
new_day = {
    "date": "2026-08-29",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-29'
data['topic'] = '🔥 <strong>archify 三连登再破三千 + gods-eye-view 转连登破千 + scientific-agent-skills 单日破千 + awesome-gpt-image-2 五连登 + 免费聚合第三弹 + NSA Ghidra 回归 + Tailscale P2P 新工具</strong> —— tt-a1i/archify（+3,927★）29.6K★ 三连登累计九千星，技能经济最大赢家。bilawalsidhu/gods-eye-view（+1,870★）12K★ 连登破千，卫星模拟器持续爆火。K-Dense-AI/scientific-agent-skills（+1,604★）37.4K★ 单日破千，AI 科学家进入主流。freestylefly/awesome-gpt-image-2（+767★）24.8K★ 五连登累计破万二。tailscale/tailcat（+790★）3.1K★ P2P 网络工具首登。tashfeenahmed/freellmapi（+612★）22K★ 免费 LLM 聚合首登。NationalSecurityAgency/ghidra（+375★）73.5K★ NSA 逆向框架回归。anthropics/claude-plugins-official（+356★）四连登。JetBrains/go-modern-guidelines（+294★）连登。cursor/plugins（+257★）回归。livekit/agents（+256★）语音 Agent 框架首登。ChromeDevTools/chrome-devtools-mcp（+215★）50K★ 官方 MCP 回归。技能经济五连霸 + 免费浪潮第三弹 + 官方生态齐下场——开源世界的新秩序正在成型。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
