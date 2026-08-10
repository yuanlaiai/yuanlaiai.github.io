#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-10 (2-day gap from 8/8)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 10)
gap_days = (today - last).days  # 2
shift = gap_days + 1  # 3
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

today_projects = [
    {
        "rank": 1,
        "owner": "PrimeIntellect-ai",
        "name": "prime-agent",
        "fullName": "PrimeIntellect-ai / prime-agent",
        "org": "Prime Intellect AI",
        "url": "https://github.com/PrimeIntellect-ai/prime-agent",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "11,856",
        "forks": "1,205",
        "starsToday": "2,356",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +2,356★！11.9K★ 连续三天登榜！自我改进的 RLM Agent——编码工作流和长时自主任务，四天涨近 1.2 万星。",
        "problems": [
            "<strong>Agent 不会自我改进：</strong>传统 Agent 每次任务都是从头开始，无法从经验中学习。",
            "<strong>长时任务容易跑偏：</strong>长时间自主运行时 Agent 会迷失目标，缺乏自我校正机制。",
            "<strong>RLM 训练门槛高：</strong>强化学习模型（RLM）训练复杂，普通开发者难以触达。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/PrimeIntellect-ai/prime-agent.git</code></pre>",
            "启动 Agent：<pre><code>npm install && npm run agent</code></pre>",
            "配置任务：在 config 中定义编码工作流和自主任务。"
        ],
        "insights": [
            "<strong>连续三天登榜爆发：</strong>+2,293★ → +2,356★，四天从 0 涨到 11.9K★——自我改进 Agent 是社区最热品类。",
            "<strong>RLM 是下一代 Agent 方向：</strong>从 LLM 到 RLM——Agent 不只「会回答」，还要「会学习」。",
            "<strong>Prime Intellect 的分布式野心：</strong>做分布式训练的公司下场做 Agent——从训练到应用的完整闭环。"
        ],
        "tags": ["rlm", "self-improving", "agent", "reinforcement-learning", "coding-agent"]
    },
    {
        "rank": 2,
        "owner": "msitarzewski",
        "name": "agency-agents",
        "fullName": "msitarzewski / agency-agents",
        "org": "msitarzewski",
        "url": "https://github.com/msitarzewski/agency-agents",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "141,101",
        "forks": "23,028",
        "starsToday": "858",
        "count": 6,
        "description": "🔥 亮点 —— 今日 +858★！141K★ 第六次登榜！社区最大 AI Agent 专业技能库——从前端魔法师到 Reddit 社区忍者，每个 Agent 都有专属技能。",
        "problems": [
            "<strong>Agent 能力碎片化：</strong>每个编码助手各有一套技能体系，跨平台迁移成本高。",
            "<strong>技能复用率低：</strong>每次新项目都要重新调教 Agent 角色和提示词。",
            "<strong>缺乏质量标准：</strong>社区 Agent 配置良莠不齐，没有统一评审机制。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/msitarzewski/agency-agents.git</code></pre>",
            "浏览全部分类：<pre><code>ls */SKILL.md | sort</code></pre>",
            "按需加载对应目录的 SKILL.md 到 AI 助手即可使用。"
        ],
        "insights": [
            "<strong>第六次登榜：</strong>从 6 月至今持续霸榜——141K★ 的社区共建技能库网络效应强大。",
            "<strong>Agent 技能生态成熟化：</strong>从「技能库」到「AI 代理机构」——每个 Agent 有性格、流程和交付物，技能生态正在产品化。",
            "<strong>SKILL.md 标准化：</strong>从建议格式演变为事实标准——技能分发的基础设施已成型。"
        ],
        "tags": ["ai-agent", "skills", "agent-framework", "productivity", "automation"]
    },
    {
        "rank": 3,
        "owner": "addyosmani",
        "name": "agent-skills",
        "fullName": "addyosmani / agent-skills",
        "org": "Google Chrome",
        "url": "https://github.com/addyosmani/agent-skills",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "85,320",
        "forks": "9,180",
        "starsToday": "680",
        "count": 7,
        "description": "🔥 亮点 —— 今日 +680★！85.3K★ 第七次登榜！Google Chrome 团队技术负责人开源的工程级 Agent 技能库。",
        "problems": [
            "<strong>工程师不知道怎么用 Agent：</strong>AI Agent 能力很强，但实际工程场景中缺乏可靠的技能配置参考。",
            "<strong>主流框架技能更新慢：</strong>React、TypeScript、Webpack 等框架的最佳实践在 Agent 技能领域还是空白。",
            "<strong>缺乏权威来源认可：</strong>社区 Agent 技能水平不一，开发者需要来自一线大牛的信誉背书。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/addyosmani/agent-skills.git</code></pre>",
            "按项目复制对应 SKILL.md 到你的 .claude 或项目目录。",
            "支持 Claude Code、Codex、Cursor 等编码 Agent。"
        ],
        "insights": [
            "<strong>第七次登榜：</strong>从 5 月至今持续上榜——85.3K★ 工程级技能库是持久型基础设施。",
            "<strong>Google Chrome 工程总监出手：</strong>addyosmani 的技能就是 Web 工程领域的最权威指南。",
            "<strong>技能生态三分天下：</strong>个人权威（mattpocock）× 工程实战（agent-skills）× 框架方法论（superpowers）。"
        ],
        "tags": ["agent-skills", "google-chrome", "web-engineering", "claude-code", "developer-tools"]
    },
    {
        "rank": 4,
        "owner": "google",
        "name": "skills",
        "fullName": "google / skills",
        "org": "Google",
        "url": "https://github.com/google/skills",
        "lang": "Python",
        "langClass": "py",
        "stars": "17,376",
        "forks": "1,400",
        "starsToday": "528",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +528★！17.4K★ Google 官方 Agent Skills——Google 产品和技术的官方技能集，开发者开箱即用。",
        "problems": [
            "<strong>Google 生态技能缺失：</strong>开发者想让 Agent 操作 Google 产品但缺少官方技能。",
            "<strong>第三方技能不可信：</strong>社区技能质量不一，涉及 Google API 时更需官方背书。",
            "<strong>跨产品技能碎片化：</strong>Sheets、Gmail、Drive 等各自为战，缺少统一技能库。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/google/skills.git</code></pre>",
            "浏览技能目录：<pre><code>ls skills/</code></pre>",
            "按需复制技能到 Agent 配置目录使用。"
        ],
        "insights": [
            "<strong>Google 官方下场：</strong>继 addyosmani 个人技能库后，Google 官方也发布 Agent Skills——技能生态的「国家队」入场了。",
            "<strong>17.4K★ 高增速：</strong>官方背书 + 生态需求——Google 系开发者终于有权威技能来源。",
            "<strong>技能经济进入大厂时代：</strong>从个人（mattpocock）到工程总监（addyosmani）到官方（google/skills）——技能分发正在被巨头瓜分。"
        ],
        "tags": ["google", "agent-skills", "skills", "developer-tools", "official"]
    },
    {
        "rank": 5,
        "owner": "goauthentik",
        "name": "authentik",
        "fullName": "goauthentik / authentik",
        "org": "goauthentik",
        "url": "https://github.com/goauthentik/authentik",
        "lang": "Python",
        "langClass": "py",
        "stars": "24,373",
        "forks": "1,862",
        "starsToday": "310",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +310★！24.4K★ 连续两天登榜！开源身份认证粘合剂——SSO、MFA、LDAP 一体化，Agent 时代的身份基础设施。",
        "problems": [
            "<strong>身份系统碎片化：</strong>企业内 SSO、MFA、LDAP、OAuth 各管各的，维护成本高。",
            "<strong>商业 IAM 太贵：</strong>Okta/Azure AD 价格高昂，中小团队难以承受。",
            "<strong>Agent 身份认证缺失：</strong>AI Agent 需要自己的身份和权限体系，传统 IAM 不适用。"
        ],
        "usage": [
            "Docker 部署：<pre><code>docker compose up -d</code></pre>",
            "访问管理界面：<pre><code>http://localhost:9000</code></pre>",
            "配置应用接入 SSO/MFA。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>24.4K★——Agent 大规模落地后身份认证成为刚需，authentik 站在风口。",
            "<strong>开源 IAM 的崛起：</strong>从 Okta 垄断到开源替代——身份管理正在经历数据库行业的开源化进程。",
            "<strong>Agent 身份是新战场：</strong>AI Agent 需要可审计、可撤销的身份——传统 IAM 厂商还没反应过来。"
        ],
        "tags": ["authentication", "sso", "identity", "iam", "security"]
    },
    {
        "rank": 6,
        "owner": "ZhuLinsen",
        "name": "daily_stock_analysis",
        "fullName": "ZhuLinsen / daily_stock_analysis",
        "org": "ZhuLinsen",
        "url": "https://github.com/ZhuLinsen/daily_stock_analysis",
        "lang": "Python",
        "langClass": "py",
        "stars": "61,442",
        "forks": "52,081",
        "starsToday": "306",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +306★！61.4K★ 第三次登榜！LLM 驱动的多市场股票智能分析——多源行情、实时新闻、决策看板、自动推送，零成本定时运行。",
        "problems": [
            "<strong>散户信息不对称：</strong>机构有专业工具和投研团队，散户靠碎片化信息做决策。",
            "<strong>股票分析耗时：</strong>多市场行情、新闻、财报都要手动跟踪，无法及时响应。",
            "<strong>AI 分析成本高：</strong>商业量化工具昂贵，个人投资者难以负担。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/ZhuLinsen/daily_stock_analysis.git</code></pre>",
            "配置行情源和通知渠道。",
            "定时运行：支持 GitHub Actions 零成本定时任务。"
        ],
        "insights": [
            "<strong>第三次登榜：</strong>从 6 月至今——61.4K★ 的 LLM 炒股系统热度稳定，个人量化是长期需求。",
            "<strong>52K 分叉的奇观：</strong>分叉数惊人——「抄作业」式使用说明散户对 AI 分析结果的高需求。",
            "<strong>AI 金融民主化：</strong>零成本定时运行 + LLM 分析——散户也能拥有机构级的信息处理能力。"
        ],
        "tags": ["stock-analysis", "llm", "finance", "quantitative", "automation"]
    },
    {
        "rank": 7,
        "owner": "Comfy-Org",
        "name": "ComfyUI",
        "fullName": "Comfy-Org / ComfyUI",
        "org": "Comfy Org",
        "url": "https://github.com/Comfy-Org/ComfyUI",
        "lang": "Python",
        "langClass": "py",
        "stars": "125,778",
        "forks": "14,864",
        "starsToday": "365",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +365★！125.8K★ 登榜回归！最强大的模块化扩散模型 GUI——图/节点界面的 AI 图像生成工作流标准。",
        "problems": [
            "<strong>图像生成工作流复杂：</strong>多模型组合、参数调优、节点连线学习成本高。",
            "<strong>GUI 与后端割裂：</strong>多数工具界面和 API 分离，自动化集成困难。",
            "<strong>生态碎片化：</strong>不同扩散模型各有界面，缺少统一工作流平台。"
        ],
        "usage": [
            "安装：<pre><code>git clone https://github.com/Comfy-Org/ComfyUI.git && cd ComfyUI && pip install -r requirements.txt</code></pre>",
            "启动：<pre><code>python main.py</code></pre>",
            "浏览器访问 <pre><code>http://127.0.0.1:8188</code></pre> 开始节点式工作流。"
        ],
        "insights": [
            "<strong>125.8K★ 图像生成基石：</strong>节点式工作流标准——ComfyUI 是扩散模型生态的「操作系统」。",
            "<strong>登榜回归：</strong>图像生成工具链持续迭代——AI 绘画依然是最活跃的创作赛道。",
            "<strong>图/节点界面的胜利：</strong>可视化工作流让复杂 AI 管线人人可用——从实验室到生产环境。"
        ],
        "tags": ["comfyui", "diffusion", "image-generation", "workflow", "ai-art"]
    }
]

# Shift labels for 2-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '前天'  # shift-1 = 2天前 = 前天
    elif label == '昨天':
        day['label'] = f'{shift}天前'  # 3天前
    elif label == '前天':
        day['label'] = f'{shift+1}天前'  # 4天前
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + shift}天前'

# Insert new day
new_day = {
    "date": "2026-08-10",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-10'
data['topic'] = '🔥 <strong>Prime Agent 三天狂涨 12K + Agency Agents 第六次 + Agent Skills 第七次 + Google 官方技能入场 + Authentik 连登 + 股票分析回归 + ComfyUI 回归</strong> —— PrimeIntellect-ai/prime-agent（+2,356★）11.9K★ 连续三天登榜四天涨 12K——自我改进 RLM Agent 是本季最热。msitarzewski/agency-agents（+858★）141K★ 第六次登榜，社区技能库网络效应。addyosmani/agent-skills（+680★）85.3K★ 第七次登榜。google/skills（+528★）17.4K★ Google 官方 Agent 技能入场——技能经济进入大厂时代。goauthentik/authentik（+310★）24.4K★ 连续两天，Agent 身份基建。ZhuLinsen/daily_stock_analysis（+306★）61.4K★ 第三次登榜 LLM 炒股。Comfy-Org/ComfyUI（+365★）125.8K★ 图像生成基石回归。自我改进 × 技能生态 × 身份基建 × AI 金融 × 图像生成——Agent 基础设施全面开花。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
