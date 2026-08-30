#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-30 (1-day gap, 双栏结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 30)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 🆕 新面孔 ──
    {
        "rank": 1,
        "owner": "THU-MAIC",
        "name": "OpenMAIC",
        "fullName": "THU-MAIC / OpenMAIC",
        "org": "清华 MAIC",
        "url": "https://github.com/THU-MAIC/OpenMAIC",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "22,955",
        "forks": "1,120",
        "starsToday": "907",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +907★！23K★ 首登！清华大学 Open Multi-Agent Interactive Classroom——一键沉浸式多 Agent 学习体验。",
        "problems": [
            "<strong>学习体验单向：</strong>传统在线课程缺乏互动，学不进去。",
            "<strong>教育资源不均：</strong>名校课程优质资源难以触达。",
            "<strong>个性化缺失：</strong>统一教学无法适配个人进度。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/THU-MAIC/OpenMAIC.git</code></pre>",
            "一键启动多 Agent 教室。",
            "沉浸式多 Agent 互动学习。"
        ],
        "insights": [
            "<strong>清华 MAIC 首登：</strong>中国高校 AI 项目登榜——多 Agent 教育场景的新范式。",
            "<strong>多 Agent 互动课堂：</strong>多个 Agent 扮演教师/同学——学习从「看视频」变「进教室」。",
            "<strong>呼应教育攻防战：</strong>Google 免费送学生 AI vs 清华开源多 Agent 教室——教育 AI 双线竞争。"
        ],
        "tags": ["tsinghua", "multi-agent", "education", "classroom", "ai-learning"]
    },
    {
        "rank": 2,
        "owner": "every-app",
        "name": "open-seo",
        "fullName": "every-app / open-seo",
        "org": "every-app",
        "url": "https://github.com/every-app/open-seo",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "14,890",
        "forks": "680",
        "starsToday": "517",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +517★！14.9K★ 首登！Semrush/Ahrefs 的开源替代——SEO 工具链开源化。",
        "problems": [
            "<strong>SEO 工具贵：</strong>Semrush/Ahrefs 订阅费用高昂。",
            "<strong>数据不透明：</strong>商业 SEO 工具黑盒算法难信任。",
            "<strong>自托管缺失：</strong>SEO 数据无法私有化部署。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/every-app/open-seo.git</code></pre>",
            "自托管部署 SEO 工具链。",
            "关键词研究、外链分析、排名追踪。"
        ],
        "insights": [
            "<strong>14.9K★ 的 SEO 开源：</strong>Semrush 替代品首登——营销工具链开源化浪潮。",
            "<strong>数据主权：</strong>SEO 数据私有化——企业营销数据不想再被 SaaS 锁。",
            "<strong>与 AI 结合：</strong>AI 内容优化 + 开源 SEO——创作者经济的基础设施。"
        ],
        "tags": ["seo", "semrush-alternative", "self-hosted", "marketing", "typescript"]
    },
    {
        "rank": 3,
        "owner": "mvanhorn",
        "name": "last30days-skill",
        "fullName": "mvanhorn / last30days-skill",
        "org": "mvanhorn",
        "url": "https://github.com/mvanhorn/last30days-skill",
        "lang": "Python",
        "langClass": "py",
        "stars": "60,305",
        "forks": "3,480",
        "starsToday": "272",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +272★！60.3K★ 回归！AI Agent 研究技能——跨 Reddit/X/YouTube/HN/Polymarket 全网话题调研，自动综合摘要。",
        "problems": [
            "<strong>调研费时：</strong>人工扫遍全网平台效率极低。",
            "<strong>信息分散：</strong>同一话题散落各平台，难以聚合。",
            "<strong>摘要靠人：</strong>调研结果需要人工综合提炼。"
        ],
        "usage": [
            "安装 last30days 技能到 AI Agent。",
            "输入话题，自动跨平台调研。",
            "获得带来源的综合摘要。"
        ],
        "insights": [
            "<strong>60.3K★ 的 Agent 技能：</strong>last30days 多次上榜——「让 Agent 替我做调研」是刚需。",
            "<strong>技能生态标杆：</strong>从 Reddit 到 Polymarket——跨平台调研技能的品类开创者。",
            "<strong>与 archify 同赛道：</strong>技能经济继续——调研技能是 Agent 时代的高频场景。"
        ],
        "tags": ["agent-skills", "research", "reddit", "youtube", "hn"]
    },
    {
        "rank": 4,
        "owner": "p-e-w",
        "name": "heretic",
        "fullName": "p-e-w / heretic",
        "org": "p-e-w",
        "url": "https://github.com/p-e-w/heretic",
        "lang": "Python",
        "langClass": "py",
        "stars": "28,915",
        "forks": "980",
        "starsToday": "150",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +150★！28.9K★ 回归！语言模型的自动审查移除——p-e-w（Planck 作者）的「异端」工具。",
        "problems": [
            "<strong>模型审查限制：</strong>LLM 内置审查/安全限制过度，影响自由表达。",
            "<strong>安全边界争议：</strong>模型拒绝回答合法问题。",
            "<strong>控制权缺失：</strong>用户无法掌控模型行为。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/p-e-w/heretic.git</code></pre>",
            "本地部署模型。",
            "移除模型内置审查限制。"
        ],
        "insights": [
            "<strong>28.9K★ 的「异端」工具：</strong>p-e-w 的审查移除工具回归——开源社区对安全对齐的反弹。",
            "<strong>对齐之争：</strong>heretic 代表「用户控制」阵营——AI 安全的另一面。",
            "<strong>与水印争议呼应：</strong>Anthropic 加水印、heretic 去审查——控制与反控制的拉锯。"
        ],
        "tags": ["llm", "censorship", "alignment", "local-model", "python"]
    },
    {
        "rank": 5,
        "owner": "pollen-robotics",
        "name": "microduck_rl",
        "fullName": "pollen-robotics / microduck_rl",
        "org": "Pollen Robotics",
        "url": "https://github.com/pollen-robotics/microduck_rl",
        "lang": "Python",
        "langClass": "py",
        "stars": "648",
        "forks": "42",
        "starsToday": "147",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +147★！648★ 首登！Microduck（mjlab）的强化学习训练环境——教机器鸭子学走路。",
        "problems": [
            "<strong>机器人 RL 门槛高：</strong>足式机器人强化学习训练环境搭建复杂。",
            "<strong>仿真缺失：</strong>缺乏低成本 RL 训练环境。",
            "<strong>教学案例少：</strong>机器人 RL 学习资源稀缺。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/pollen-robotics/microduck_rl.git</code></pre>",
            "配置仿真环境。",
            "训练 Microduck 机器人走路。"
        ],
        "insights": [
            "<strong>648★ 的小项目登榜：</strong>「机器鸭子学走路」——足式机器人 RL 的极佳入门案例。",
            "<strong>RL 民主化：</strong>低成本仿真环境——机器人强化学习不再是大厂专属。",
            "<strong>硬件 + AI 融合：</strong>从虚拟到现实——sim-to-real 是机器人 AI 的核心路径。"
        ],
        "tags": ["robotics", "reinforcement-learning", "simulation", "quadruped", "education"]
    },
    {
        "rank": 6,
        "owner": "corsairdev",
        "name": "corsair",
        "fullName": "corsairdev / corsair",
        "org": "Corsair",
        "url": "https://github.com/corsairdev/corsair",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "10,773",
        "forks": "480",
        "starsToday": "99",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +99★！10.8K★ 首登！连接用户到他们的应用——App 连接/授权基础设施新玩家。",
        "problems": [
            "<strong>App 连接割裂：</strong>用户与应用之间的授权连接体验差。",
            "<strong>集成开发繁琐：</strong>第三方应用连接需要大量定制开发。",
            "<strong>连接管理缺失：</strong>缺乏统一的连接生命周期管理。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/corsairdev/corsair.git</code></pre>",
            "集成连接 SDK。",
            "让用户一键连接第三方应用。"
        ],
        "insights": [
            "<strong>10.8K★ 的连接层：</strong>corsair 首登——「连接用户到应用」是 AI 时代的新中间件。",
            "<strong>与 MCP 呼应：</strong>应用连接标准化——Agent 时代的应用互联基础设施。",
            "<strong>身份与授权：</strong>连接即授权——OAuth 之后的下一个基础设施层。"
        ],
        "tags": ["connections", "oauth", "middleware", "integrations", "typescript"]
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
        "stars": "32,971",
        "forks": "1,060",
        "starsToday": "3,902",
        "count": 4,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +3,902★！33K★ 四连登连续三天破三千！架构图 Agent 技能——四天累计 13,000★，技能经济之王。",
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
            "<strong>四连登连续三天破三千：</strong>+4,239 → +3,927 → +3,902——archify 四天从 17K 冲到 33K。",
            "<strong>自包含 HTML：</strong>单文件图表 + 动效 + 可导出——Agent 技能正在工业化。",
            "<strong>技能经济之王：</strong>架构图技能成为近期开源圈最大现象——单技能库的极限还在上探。"
        ],
        "tags": ["agent-skills", "architecture", "diagrams", "html", "visualization"]
    },
    {
        "rank": 8,
        "owner": "K-Dense-AI",
        "name": "scientific-agent-skills",
        "fullName": "K-Dense-AI / scientific-agent-skills",
        "org": "K-Dense AI",
        "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "38,409",
        "forks": "2,180",
        "starsToday": "1,587",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,587★！38.4K★ 三连登连续两天破千！AI 科学家技能库——163 个技能 + 100+ 科学数据库。",
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
            "<strong>三连登连续两天破千：</strong>+1,604 → +1,587——科研技能库热度稳定高位。",
            "<strong>17.5 万科学家的选择：</strong>163 个验证技能 + 100+ 科学数据库——纵向深耕的样板。",
            "<strong>技能库立体化：</strong>archify 通用 + scientific 纵向——技能经济双龙头。"
        ],
        "tags": ["scientific", "agent-skills", "research", "biology", "science"]
    },
    {
        "rank": 9,
        "owner": "tashfeenahmed",
        "name": "freellmapi",
        "fullName": "tashfeenahmed / freellmapi",
        "org": "tashfeenahmed",
        "url": "https://github.com/tashfeenahmed/freellmapi",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "22,414",
        "forks": "2,380",
        "starsToday": "622",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +622★！22.4K★ 连登！免费 LLM API 聚合——74 亿 tokens/月、34 家免费提供商、635 个端点。",
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
            "<strong>连登：</strong>免费 LLM 聚合持续吸星——免费化浪潮没有停。",
            "<strong>与 sub2api/free-claude-code 同源：</strong>免费化浪潮第三弹继续——开发者对 API 价格的组织化抵抗。",
            "<strong>智能路由：</strong>635 个端点自动调度——免费资源也能当生产环境用。"
        ],
        "tags": ["llm", "free", "api", "aggregator", "openai-compatible"]
    },
    {
        "rank": 10,
        "owner": "NationalSecurityAgency",
        "name": "ghidra",
        "fullName": "NationalSecurityAgency / ghidra",
        "org": "NSA",
        "url": "https://github.com/NationalSecurityAgency/ghidra",
        "lang": "Java",
        "langClass": "java",
        "stars": "73,682",
        "forks": "8,940",
        "starsToday": "375",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +375★！73.7K★ 连登！NSA 开源的逆向工程框架——安全研究者的标配武器。",
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
            "<strong>连登：</strong>Ghidra 稳定吸星——安全研究工具需求持续。",
            "<strong>与 AI 结合：</strong>逆向工程 + 编码 Agent——AI 正在进入二进制分析。",
            "<strong>安全工具链升温：</strong>AI 时代安全研究工具需求持续——ghidra 是其中的老兵。"
        ],
        "tags": ["reverse-engineering", "security", "malware", "nsa", "binary-analysis"]
    },
    {
        "rank": 11,
        "owner": "livekit",
        "name": "agents",
        "fullName": "livekit / agents",
        "org": "LiveKit",
        "url": "https://github.com/livekit/agents",
        "lang": "Python",
        "langClass": "py",
        "stars": "13,590",
        "forks": "1,050",
        "starsToday": "254",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +254★！13.6K★ 连登！实时语音 AI Agent 框架——语音 Agent 开发的标配基础设施。",
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
            "<strong>连登：</strong>语音 Agent 框架持续吸星——语音 AI 是 Agent 的下一个主战场。",
            "<strong>实时音视频 + AI：</strong>WebRTC 基建 + LLM——语音 Agent 的「水电煤」。",
            "<strong>与边缘 AI 呼应：</strong>语音交互是最自然的 AI 入口——这个赛道正在起量。"
        ],
        "tags": ["voice-ai", "realtime", "agent", "webrtc", "python"]
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
    "date": "2026-08-30",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-30'
data['topic'] = '🔥 <strong>清华 OpenMAIC 首登 + archify 四连登再破三千 + scientific-agent-skills 三连登破千 + last30days 调研技能回归 + open-seo 开源 + heretic 审查移除</strong> —— THU-MAIC/OpenMAIC（+907★）23K★ 清华多 Agent 课堂首登，中国高校 AI 登榜。tt-a1i/archify（+3,902★）33K★ 四连登连续三天破三千，技能经济之王。K-Dense-AI/scientific-agent-skills（+1,587★）38.4K★ 三连登破千。every-app/open-seo（+517★）14.9K★ SEO 开源替代首登。tashfeenahmed/freellmapi（+622★）连登。NationalSecurityAgency/ghidra（+375★）连登。mvanhorn/last30days-skill（+272★）60.3K★ 调研技能回归。livekit/agents（+254★）连登。p-e-w/heretic（+150★）审查移除回归。pollen-robotics/microduck_rl（+147★）机器鸭子 RL 首登。corsairdev/corsair（+99★）连接层首登。技能经济继续统治 + 中国高校 AI 登场 + 教育/调研/SEO 场景全面开花——Agent 时代的「工具民主化」正在加速。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
