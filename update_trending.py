#!/usr/bin/env python3
import json

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

today = {
    "date": "2026-07-03",
    "label": "今天",
    "icon": "",
    "projects": [
        {
            "rank": 1,
            "owner": "msitarzewski",
            "name": "agency-agents",
            "fullName": "msitarzewski / agency-agents",
            "org": "msitarzewski",
            "url": "https://github.com/msitarzewski/agency-agents",
            "lang": "Shell",
            "langClass": "sh",
            "stars": "125,474",
            "forks": "20,359",
            "starsToday": "3,032",
            "count": 5,
            "description": "🔥 亮点 —— 今日 +3,032★！125K★ 连续5次登榜破纪录！社区最大 AI Agent 专业技能库，SKILL.md 标准已成 Agent 技能分发的基石。",
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
                "<strong>连续5次登榜创纪录：</strong>从 6/12 → 6/29 → 6/30 → 7/2 → 7/3，agency-agents 五连击！+3,032★ 单日新高。",
                "<strong>125K★ 的价值：</strong>这不是一夜爆红，而是持续积累——社区共建的 Agent 技能库正在形成网络效应。",
                "<strong>SKILL.md 标准化：</strong>从 Anthropic 官方到社区，SKILL.md 正从「建议格式」演变为「事实标准」。"
            ],
            "tags": ["ai-agent", "skills", "agent-framework", "productivity", "automation"]
        },
        {
            "rank": 2,
            "owner": "usestrix",
            "name": "strix",
            "fullName": "usestrix / strix",
            "org": "usestrix",
            "url": "https://github.com/usestrix/strix",
            "lang": "Python",
            "langClass": "py",
            "stars": "32,190",
            "forks": "3,375",
            "starsToday": "2,137",
            "count": 2,
            "description": "🔥 亮点 —— 今日 +2,137★！32K★ 二次登榜。开源 AI 渗透测试工具，自动发现和修复应用安全漏洞，CI/CD 集成。",
            "problems": [
                "<strong>安全测试门槛高：</strong>传统渗透测试需要专业技能和大量手动操作。",
                "<strong>漏洞发现周期长：</strong>从扫描到验证到修复流程缓慢。",
                "<strong>安全工具碎片化：</strong>不同扫描器各有专长，需要多种工具组合。"
            ],
            "usage": [
                "安装：<pre><code>pip install strix</code></pre>",
                "扫描：<pre><code>strix scan https://your-app.com</code></pre>",
                "CI 集成：<pre><code>strix ci --fail-on critical</code></pre> 阻断高危漏洞。"
            ],
            "insights": [
                "<strong>二次登榜热度翻倍：</strong>7/2 +1,195★ → 7/3 +2,137★，strix 热度不降反升，AI 安全赛道正在加速。",
                "<strong>红蓝对抗 AI 化：</strong>攻防双方都在用 AI——安全测试也不例外。",
                "<strong>安全左移的实践：</strong>CI/CD 集成让 strix 不只是扫描器，而是开发流程中的安全检查点。"
            ],
            "tags": ["security", "penetration-testing", "ai-agent", "devsecops", "vulnerability"]
        },
        {
            "rank": 3,
            "owner": "JuliusBrussee",
            "name": "caveman",
            "fullName": "JuliusBrussee / caveman",
            "org": "JuliusBrussee",
            "url": "https://github.com/JuliusBrussee/caveman",
            "lang": "JavaScript",
            "langClass": "js",
            "stars": "80,903",
            "forks": "4,531",
            "starsToday": "926",
            "count": 1,
            "description": "🔥 亮点 —— 今日 +926★！80K★ 病毒式传播！Claude Code 野人语技能——「为什么要用很多 token，当少数 token 就行」砍掉 65% Token。",
            "problems": [
                "<strong>API 开销高昂：</strong>编码 Agent 的 Token 消耗是最大成本，尤其是重复上下文。",
                "<strong>提示词过于啰嗦：</strong>Agent 回复中大量客套话和冗余描述浪费 Token。",
                "<strong>成本限制了 Agent 的规模化使用：</strong>Token 费用让高频度 Agent 交互难以承受。"
            ],
            "usage": [
                "安装到 Claude Code：<pre><code>claude add skills JuliusBrussee/caveman</code></pre>",
                "激活后 Agent 自动切换「野人语」模式，输出极度精简。",
                "安装到任何支持 SKILL.md 的编码助手（Codex、Cursor 等）均适用。"
            ],
            "insights": [
                "<strong>病毒式传播的密码：</strong>80K★ 的爆发说明了 Token 成本焦虑的普遍性——开发者苦 API 费用久矣。",
                "<strong>「野人语」不是玩笑是策略：</strong>砍掉 65% Token 意味着省 65% 成本，这不是段子，是降本增效的硬需求。",
                "<strong>Token 优化赛道：</strong>从 Headroom 的 Token 压缩引擎到 caveman 的野人语，省钱才是第一生产力。"
            ],
            "tags": ["token-saving", "claude-code", "skill", "cost-optimization", "fun-tool"]
        },
        {
            "rank": 4,
            "owner": "obra",
            "name": "superpowers",
            "fullName": "obra / superpowers",
            "org": "obra",
            "url": "https://github.com/obra/superpowers",
            "lang": "Shell",
            "langClass": "sh",
            "stars": "244,410",
            "forks": "21,680",
            "starsToday": "897",
            "count": 12,
            "description": "🔥 亮点 —— 今日 +897★！244K★ 第12次登榜。Agentic Skills 框架 + 软件开发方法论的集大成者，技能可像 npm 包一样安装卸载。",
            "problems": [
                "<strong>Agent 技能碎片化：</strong>社区 Agent 技能散落各处，缺乏统一发现和安装机制。",
                "<strong>开发方法论缺失：</strong>AI 编码 Agent 能力很强，但缺乏配套工作流指导。",
                "<strong>跨平台兼容难题：</strong>Claude Code、Codex、Cursor 等平台各有格式，互不兼容。"
            ],
            "usage": [
                "安装 CLI：<pre><code>npm install -g superpowers</code></pre>",
                "搜索技能：<pre><code>superpowers search \"test generator\"</code></pre>",
                "安装技能：<pre><code>superpowers install writing-plans</code></pre> 自动配置到当前编辑器。"
            ],
            "insights": [
                "<strong>第12次登榜 = 持久型基础设施：</strong>从 5月至今几乎每周登榜，superpowers 已是 Agent 技能分发的标准基础设施。",
                "<strong>技能即代码：</strong>像 npm 包一样安装卸载 Agent 技能——生态化的技能管理是 Agent 平台的下一个战场。",
                "<strong>跨平台能力是护城河：</strong>同时支持 Claude、Codex、Cursor、Kimi、OpenCode 等平台，兼容性本身就是壁垒。"
            ],
            "tags": ["agent-framework", "skills", "developer-tools", "cli", "agent-ecosystem"]
        },
        {
            "rank": 5,
            "owner": "santifer",
            "name": "career-ops",
            "fullName": "santifer / career-ops",
            "org": "santifer",
            "url": "https://github.com/santifer/career-ops",
            "lang": "JavaScript",
            "langClass": "js",
            "stars": "57,813",
            "forks": "11,389",
            "starsToday": "372",
            "count": 2,
            "description": "🔥 亮点 —— 今日 +372★！57K★ 二次上榜的 AI 求职系统。14 种技能模式、Go 仪表盘 + PDF 简历生成，全方位求职自动化。",
            "problems": [
                "<strong>求职过程繁琐：</strong>投简历、跟进展、准备面试、谈薪资——每个环节都需要大量精力。",
                "<strong>简历千篇一律：</strong>针对不同公司定制简历费时费力，容易因此错过机会。",
                "<strong>面试准备缺乏针对性：</strong>不知道目标公司会问什么，准备方向容易跑偏。"
            ],
            "usage": [
                "克隆：<pre><code>git clone https://github.com/santifer/career-ops.git && cd career-ops</code></pre>",
                "分析目标岗位：<pre><code>career-ops analyze --job-url https://linkedin.com/jobs/xxx</code></pre>",
                "生成定制简历：<pre><code>career-ops resume --job-analysis output.json</code></pre>"
            ],
            "insights": [
                "<strong>AI + 求职的实用主义：</strong>57K★ 说明找工作是开发者最痛的场景之一——AI Agent 正是解决信息不对称的利器。",
                "<strong>14 种技能模式 = 全链路覆盖：</strong>从简历优化到模拟面试到薪资谈判，career-ops 覆盖了求职全流程。",
                "<strong>二次上榜验证需求：</strong>6/10 首次上榜后今天再次回归，求职自动化不是一次性需求而是持续痛点。"
            ],
            "tags": ["job-search", "career", "ai-agent", "resume", "automation"]
        }
    ]
}

# 1-day gap, normal shift
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '昨天'
    elif label == '昨天':
        day['label'] = '前天'
    elif label == '前天':
        day['label'] = '4天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + 2}天前'

days.insert(0, today)
data['lastUpdated'] = '2026-07-03'
data['topic'] = '🔥 <strong>Agent 技能五连霸 + AI 安全翻倍 + 野人语 Token 省钱 + Superpowers 第12次 + AI 求职实用主义</strong> —— msitarzewski/agency-agents（+3,032★）连续5次登榜创纪录，单日 +3K★ 新高。usestrix/strix（+2,137★）二次登榜热度翻倍，AI+安全赛道爆发。JuliusBrussee/caveman（+926★）80K★ 野人语 Token 节省技能病毒式传播，省钱才是第一生产力。obra/superpowers（+897★）第12次登榜，Agent 技能分发基础设施。santifer/career-ops（+372★）二次上榜 AI 求职系统，开发者最痛的场景就是最好的 AI 落地场景。Agent 技能生态、AI 安全、Token 优化、求职自动化——AI Agent 正从炫技走向省钱和实用。'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('data.json updated successfully!')
print(f'Total days: {len(data["days"])}')
print(f'New day date: {data["days"][0]["date"]}')
for p in data['days'][0]['projects']:
    print(f'  {p["name"]}: count={p["count"]} starsToday={p["starsToday"]}')
