#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-08 (2-day gap from 8/6)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 8)
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
        "stars": "6,910",
        "forks": "564",
        "starsToday": "2,293",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +2,293★！6.9K★ 首日爆发！自我改进的 RLM Agent——为编码工作流和长时自主任务设计，Agent 能自己进化。",
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
            "<strong>2,293★ 首日爆发：</strong>自我改进 Agent 是社区等待已久的品类——「Agent 能自己进化」直击痛点。",
            "<strong>RLM 是下一代 Agent 方向：</strong>从 LLM 到 RLM（强化学习模型）——Agent 不只「会回答」，还要「会学习」。",
            "<strong>Prime Intellect 的分布式野心：</strong>做分布式训练的公司下场做 Agent——从训练到应用的完整闭环。"
        ],
        "tags": ["rlm", "self-improving", "agent", "reinforcement-learning", "coding-agent"]
    },
    {
        "rank": 2,
        "owner": "mattpocock",
        "name": "skills",
        "fullName": "mattpocock / skills",
        "org": "mattpocock",
        "url": "https://github.com/mattpocock/skills",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "209,042",
        "forks": "18,054",
        "starsToday": "2,152",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +2,152★！209K★ 连续两天登榜！「真正的工程师技能」——Matt Pocock 的 .agents 目录，TypeScript 工程师的 Agent 技能圣经。",
        "problems": [
            "<strong>Agent 技能质量参差：</strong>社区技能良莠不齐，工程师需要可信来源。",
            "<strong>TypeScript 工程实践缺失：</strong>主流编码 Agent 缺少 TypeScript 领域的最佳实践技能。",
            "<strong>个人权威背书稀缺：</strong>开发者需要一个真正懂工程的作者开箱即用的技能库。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/mattpocock/skills.git</code></pre>",
            "复制需要的技能到你的 .agents 目录。",
            "支持 Claude Code、Codex、Cursor 等编码 Agent。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+1,695★ → +2,152★ 热度不减——个人权威技能库持续领跑。",
            "<strong>209K★ 的号召力：</strong>两天涨近 4K★——「真实工程师在用」的定位依然是最强卖点。",
            "<strong>技能经济个人品牌化：</strong>从 addyosmani 到 mattpocock，顶级工程师正在成为 Agent 技能的第一供应商。"
        ],
        "tags": ["skills", "typescript", "agent-skills", "mattpocock", "developer-tools"]
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
        "stars": "84,010",
        "forks": "8,976",
        "starsToday": "1,131",
        "count": 6,
        "description": "🔥 亮点 —— 今日 +1,131★！84K★ 第六次登榜！Google Chrome 团队技术负责人开源的工程级 Agent 技能库。",
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
            "<strong>第六次登榜：</strong>从 5/17 至今持续上榜——84K★ 的工程级技能库是持久型基础设施。",
            "<strong>Google Chrome 工程总监出手：</strong>addyosmani 的技能就是 Web 工程领域的最权威指南。",
            "<strong>技能生态三分天下：</strong>个人权威（mattpocock）× 工程实战（agent-skills）× 框架方法论（superpowers）。"
        ],
        "tags": ["agent-skills", "google-chrome", "web-engineering", "claude-code", "developer-tools"]
    },
    {
        "rank": 4,
        "owner": "cloudflare",
        "name": "computer",
        "fullName": "cloudflare / computer",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/computer",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "5,927",
        "forks": "298",
        "starsToday": "872",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +872★！5.9K★ 连续两天登榜！给 Agent 一台电脑——Cloudflare 官方让 AI Agent 拥有完整计算机操作能力。",
        "problems": [
            "<strong>Agent 没有「手」：</strong>AI Agent 能读能写文件，但无法操作浏览器、点击界面、运行完整应用。",
            "<strong>云上操作环境稀缺：</strong>给 Agent 提供真实电脑环境的基础设施不成熟。",
            "<strong>安全隔离难保证：</strong>Agent 操作真实系统风险高，需要受控的沙箱环境。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cloudflare/computer.git</code></pre>",
            "部署到 Cloudflare Workers：<pre><code>wrangler deploy</code></pre>",
            "配置 Agent 连接电脑环境即可使用。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+2,690★ → +872★——「给 Agent 一台电脑」的热度持续。",
            "<strong>Agent 操作系统的战争：</strong>从 OpenAI Operator 到 Claude Computer Use，再到 Cloudflare 开源——谁给 Agent 最好的「手」就赢。",
            "<strong>5.9K★ 两天涨 1.5K：</strong>Cloudflare 正在把「Agent 基础设施」做成自己的新增长曲线。"
        ],
        "tags": ["cloudflare", "agent", "computer-use", "cloud", "infrastructure"]
    },
    {
        "rank": 5,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "268,836",
        "forks": "24,004",
        "starsToday": "782",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +782★！269K★ 连续两天登榜！Agentic Skills 框架 + 软件开发方法论集大成者，技能像 npm 包一样安装卸载。",
        "problems": [
            "<strong>Agent 技能碎片化：</strong>社区技能散落各处，缺乏统一发现和安装机制。",
            "<strong>开发方法论缺失：</strong>AI 编码 Agent 能力强但缺乏配套工作流指导。",
            "<strong>跨平台兼容难题：</strong>Claude Code、Codex、Cursor 各有格式，互不兼容。"
        ],
        "usage": [
            "安装 CLI：<pre><code>npm install -g superpowers</code></pre>",
            "搜索技能：<pre><code>superpowers search \"test generator\"</code></pre>",
            "安装技能：<pre><code>superpowers install writing-plans</code></pre>"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>+858★ → +782★——269K★ 的 Agent 技能分发基础设施持续霸榜。",
            "<strong>技能即代码再确认：</strong>像 npm 包一样管理 Agent 技能——生态化管理是 Agent 平台的护城河。",
            "<strong>方法论 + 技能的复合价值：</strong>工具 + 思想的组合才是完整产品。"
        ],
        "tags": ["agent-framework", "skills", "developer-tools", "cli", "agent-ecosystem"]
    },
    {
        "rank": 6,
        "owner": "goauthentik",
        "name": "authentik",
        "fullName": "goauthentik / authentik",
        "org": "goauthentik",
        "url": "https://github.com/goauthentik/authentik",
        "lang": "Python",
        "langClass": "py",
        "stars": "23,673",
        "forks": "1,814",
        "starsToday": "530",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +530★！23.7K★ 连续登榜！开源身份认证粘合剂——SSO、MFA、LDAP 一体化，Agent 时代的身份基础设施。",
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
            "<strong>23.7K★ 身份基建热：</strong>Agent 大规模落地后，身份认证成为刚需——authentik 站在了风口。",
            "<strong>开源 IAM 的崛起：</strong>从 Okta 垄断到开源替代——身份管理正在经历与数据库相同的开源化进程。",
            "<strong>Agent 身份是新战场：</strong>AI Agent 需要可审计、可撤销的身份——传统 IAM 厂商还没反应过来。"
        ],
        "tags": ["authentication", "sso", "identity", "iam", "security"]
    },
    {
        "rank": 7,
        "owner": "denoland",
        "name": "celld",
        "fullName": "denoland / celld",
        "org": "Deno",
        "url": "https://github.com/denoland/celld",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "2,264",
        "forks": "65",
        "starsToday": "516",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +516★！2.3K★ Deno 官方出品！自托管分布式 Durable Objects——Rust 编写，让状态持久化像呼吸一样简单。",
        "problems": [
            "<strong>分布式状态管理难：</strong>跨节点共享状态、持久化、恢复是分布式系统的老大难。",
            "<strong>Durable Objects 被云厂商锁定：</strong>Cloudflare DO 好用但只能在 Cloudflare 上跑。",
            "<strong>自托管方案缺失：</strong>想在自己的基础设施上获得 DO 能力，没有成熟选择。"
        ],
        "usage": [
            "安装：<pre><code>cargo install celld</code></pre>",
            "启动集群：<pre><code>celld start</code></pre>",
            "定义 Durable Object 并在应用中使用。"
        ],
        "insights": [
            "<strong>Deno 官方入局：</strong>celld 把 Cloudflare Durable Objects 的能力自托管化——分布式状态管理迎来开源标准。",
            "<strong>Rust + 分布式基建：</strong>性能敏感的基础设施全面 Rust 化——Deno 也在强化自己的底层能力。",
            "<strong>2.3K★ 高增速：</strong>Agent 长时任务需要持久状态——DO 是 Agent 基础设施的重要拼图。"
        ],
        "tags": ["durable-objects", "deno", "distributed-systems", "rust", "state-management"]
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
    "date": "2026-08-08",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-08'
data['topic'] = '🔥 <strong>Prime Agent 自我改进 RLM 首日爆发 + Matt Pocock 技能两天连涨 + Agent Skills 第六次 + Cloudflare Computer 持续 + Superpowers 连登 + Authentik 身份基建 + Deno Durable Objects</strong> —— PrimeIntellect-ai/prime-agent（+2,293★）6.9K★ 首日即爆！自我改进的 RLM Agent——Agent 能自己进化。mattpocock/skills（+2,152★）209K★ 连续两天登榜两天涨 4K★。addyosmani/agent-skills（+1,131★）84K★ 第六次登榜，Google Chrome 工程总监权威技能。cloudflare/computer（+872★）5.9K★ 给 Agent 一台电脑持续升温。obra/superpowers（+782★）269K★ 连续登榜，技能分发基础设施。goauthentik/authentik（+530★）23.7K★ Agent 时代身份认证基建。denoland/celld（+516★）2.3K★ Deno 官方分布式 Durable Objects。自我改进 × 技能生态 × 电脑操作 × 身份基建 × 分布式状态——Agent 基础设施竞争进入深水区。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
