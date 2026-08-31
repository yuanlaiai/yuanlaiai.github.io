#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-31 (1-day gap, 双栏结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 31)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 🆕 新面孔 ──
    {
        "rank": 1,
        "owner": "zhaoxuya520",
        "name": "reverse-skill",
        "fullName": "zhaoxuya520 / reverse-skill",
        "org": "zhaoxuya520",
        "url": "https://github.com/zhaoxuya520/reverse-skill",
        "lang": "PowerShell",
        "langClass": "powershell",
        "stars": "32,729",
        "forks": "4,417",
        "starsToday": "1,439",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,439★！32.7K★ 首登！逆向/渗透/安全技能路由包——AI 自动路由 + 按需自举工具链 + 自动进化经验库，支持 Claude Code/Cursor/Cline。",
        "problems": [
            "<strong>安全工具链碎片化：</strong>逆向与渗透工具分散，选型成本高。",
            "<strong>流程依赖人工：</strong>渗透测试步骤繁琐，专家经验难沉淀。",
            "<strong>知识库不进化：</strong>安全经验无法随项目自动积累。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/zhaoxuya520/reverse-skill.git</code></pre>",
            "加载 SKILL 到 Claude Code / Cursor / Cline。",
            "输入目标，AI 自动路由到对应安全工具链。"
        ],
        "insights": [
            "<strong>32.7K★ 首登：</strong>中文安全技能包登榜——逆向/渗透的 Agent 化正在发生。",
            "<strong>自动路由 + 自举工具链：</strong>技能包不只有指令，还能按需拉起工具——Agent 技能从「文档」变「引擎」。",
            "<strong>与 ghidra 同赛道：</strong>安全工具链持续升温——AI 时代的攻防两端都在被 Agent 重构。"
        ],
        "tags": ["security", "reverse-engineering", "penetration-testing", "agent-skills", "powershell"]
    },
    {
        "rank": 2,
        "owner": "k1tbyte",
        "name": "Wand-Enhancer",
        "fullName": "k1tbyte / Wand-Enhancer",
        "org": "k1tbyte",
        "url": "https://github.com/k1tbyte/Wand-Enhancer",
        "lang": "C#",
        "langClass": "cs",
        "stars": "23,148",
        "forks": "59,160",
        "starsToday": "718",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +718★！23.1K★ 首登！WeMod（Wand）应用的 UX 与互操作增强扩展——游戏修改器生态的高级玩法。",
        "problems": [
            "<strong>游戏修改器体验糙：</strong>WeMod 默认界面功能受限。",
            "<strong>互操作缺失：</strong>修改器难以与其他工具联动。",
            "<strong>高级功能门槛：</strong>深度定制需要自己写扩展。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/k1tbyte/Wand-Enhancer.git</code></pre>",
            "安装扩展到 Wand/WeMod 应用。",
            "启用增强的 UX 与互操作功能。"
        ],
        "insights": [
            "<strong>23.1K★ 首登：</strong>游戏修改器生态的扩展层登榜——59K fork 说明社区改造热情极高。",
            "<strong>扩展经济：</strong>连游戏修改器都在做「增强层」——平台 + 插件的模式无处不在。",
            "<strong>非 AI 项目也上榜：</strong>榜单覆盖全品类——游戏工具社区同样活跃。"
        ],
        "tags": ["gaming", "wemod", "extension", "modding", "csharp"]
    },
    {
        "rank": 3,
        "owner": "handsomestWei",
        "name": "patent-disclosure-skill",
        "fullName": "handsomestWei / patent-disclosure-skill",
        "org": "handsomestWei",
        "url": "https://github.com/handsomestWei/patent-disclosure-skill",
        "lang": "Python",
        "langClass": "py",
        "stars": "6,106",
        "forks": "724",
        "starsToday": "571",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +571★！6.1K★ 首登！中国专利技能——专利点挖掘与交底书编写（发明/实用/外观），通俗解读专利、嗅探政策动向、辅助审查答复。",
        "problems": [
            "<strong>专利写作门槛高：</strong>交底书格式专业，工程师不熟悉。",
            "<strong>技术点挖掘难：</strong>不知道哪些创新点值得申请专利。",
            "<strong>审查答复复杂：</strong>审查意见答复需要专业话术。"
        ],
        "usage": [
            "加载专利技能到 AI Agent。",
            "输入技术方案，自动挖掘专利点。",
            "生成交底书 / 辅助审查答复。"
        ],
        "insights": [
            "<strong>6.1K★ 首登：</strong>中国专利技能登榜——知识产权 AI 化是合规刚需。",
            "<strong>垂直场景技能：</strong>专利写作这类高门槛专业场景——正是 Agent 技能的最佳落点。",
            "<strong>中文技能出海信号：</strong>中文安全/专利技能接连上榜——中文 Agent 技能生态正在成型。"
        ],
        "tags": ["patent", "intellectual-property", "agent-skills", "china", "legal"]
    },
    {
        "rank": 4,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "244,965",
        "forks": "37,013",
        "starsToday": "490",
        "count": 5,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +490★！245K★ 时隔一月回归！Agent Harness 性能优化系统——技能/直觉/记忆/安全 + research-first 开发，横跨 Claude Code/Codex/Opencode/Cursor。",
        "problems": [
            "<strong>Agent 性能瓶颈：</strong>Harness 层低效拖慢整个 Agent 工作流。",
            "<strong>记忆与技能管理乱：</strong>技能/直觉/记忆缺乏统一调度。",
            "<strong>安全缺失：</strong>Agent 自主执行缺少权限边界。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/affaan-m/ECC.git</code></pre>",
            "接入 Claude Code / Codex / Opencode。",
            "启用性能优化与安全策略。"
        ],
        "insights": [
            "<strong>245K★ 巨无霸回归：</strong>7 月底 236K★ 后沉寂一月，今天重新登榜——Agent 基础设施需求没有退潮。",
            "<strong>research-first 开发：</strong>强调先研究后写码——与主流 Agent 工作流方法论合流。",
            "<strong>技能经济常青：</strong>ECC 与 archify/scientific-agent-skills 同台——Harness 优化是技能经济的底层生意。"
        ],
        "tags": ["agent", "harness", "performance", "optimization", "javascript"]
    },
    {
        "rank": 5,
        "owner": "jingyaogong",
        "name": "minimind",
        "fullName": "jingyaogong / minimind",
        "org": "jingyaogong",
        "url": "https://github.com/jingyaogong/minimind",
        "lang": "Python",
        "langClass": "py",
        "stars": "55,787",
        "forks": "7,292",
        "starsToday": "472",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +472★！55.8K★ 首登！2 小时从零训练 64M 参数 LLM——把大模型训练讲明白的中文教学项目。",
        "problems": [
            "<strong>LLM 训练门槛高：</strong>预训练流程复杂，初学者无从下手。",
            "<strong>教学资源割裂：</strong>数据/代码/理论分散在不同教程。",
            "<strong>硬件要求吓人：</strong>以为训练大模型必须多卡集群。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/jingyaogong/minimind.git</code></pre>",
            "按教程准备数据集。",
            "单卡 2 小时跑完 64M 参数训练。"
        ],
        "insights": [
            "<strong>55.8K★ 首登：</strong>中文教学项目登榜——「从零训练 LLM」是永恒的求知刚需。",
            "<strong>小模型教学法：</strong>64M 参数讲清预训练全流程——以小见大是 AI 教育的最佳路径。",
            "<strong>民主化叙事：</strong>从 minimind 到 microduck_rl——「小成本玩转 AI」是当下最强的社区情绪。"
        ],
        "tags": ["llm", "training", "education", "from-scratch", "python"]
    },
    {
        "rank": 6,
        "owner": "kaifcodec",
        "name": "user-scanner",
        "fullName": "kaifcodec / user-scanner",
        "org": "kaifcodec",
        "url": "https://github.com/kaifcodec/user-scanner",
        "lang": "Python",
        "langClass": "py",
        "stars": "3,977",
        "forks": "439",
        "starsToday": "462",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +462★！4K★ 首登！Email/Username 二合一 OSINT 套件——465+ 扫描向量（175+ email / 290+ username）深挖数字足迹。",
        "problems": [
            "<strong>OSINT 工具分散：</strong>邮箱与用户名调查需要多个工具拼接。",
            "<strong>信息收集费时：</strong>手动搜索效率极低。",
            "<strong>深度挖掘难：</strong>难以从单一标识符挖出完整数字足迹。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/kaifcodec/user-scanner.git</code></pre>",
            "输入 Email 或 Username。",
            "自动跑 465+ 扫描向量生成报告。"
        ],
        "insights": [
            "<strong>4K★ 首登：</strong>OSINT 工具登榜——安全研究需求在 Agent 时代被放大。",
            "<strong>465+ 向量自动化：</strong>把侦查工作向量化、脚本化——安全工具正在工业化。",
            "<strong>隐私的另一面：</strong>OSINT 越强，数字足迹暴露越深——攻防一体的伦理张力。"
        ],
        "tags": ["osint", "security", "email", "username", "recon"]
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
        "stars": "37,042",
        "forks": "2,377",
        "starsToday": "3,993",
        "count": 5,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +3,993★！37K★ 五连登！架构图 Agent 技能——五天累计 19,000★，自包含 HTML 图表 + 动效 + 可导出，技能经济之王继续狂飙。",
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
            "<strong>五连登连续四天破三千：</strong>+1,002 → +4,239 → +3,927 → +3,902 → +3,993——archify 五天从 17.8K 冲到 37K。",
            "<strong>单日 +3,993 新高：</strong>热度不但没衰减还在加速——架构图是开发者最高频的 Agent 场景。",
            "<strong>技能经济天花板还在上探：</strong>37K★ 的「一个技能」——Agent 技能正在成为独立的软件品类。"
        ],
        "tags": ["agent-skills", "architecture", "diagrams", "html", "visualization"]
    },
    {
        "rank": 8,
        "owner": "THU-MAIC",
        "name": "OpenMAIC",
        "fullName": "THU-MAIC / OpenMAIC",
        "org": "清华 MAIC",
        "url": "https://github.com/THU-MAIC/OpenMAIC",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "25,873",
        "forks": "4,658",
        "starsToday": "2,819",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +2,819★！25.9K★ 二连登！清华大学 Open Multi-Agent Interactive Classroom——一键沉浸式多 Agent 学习体验，单日增速翻三倍。",
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
            "<strong>二连登爆发：</strong>+907 → +2,819——清华项目第二天直接翻三倍，25.9K★ 破 25K。",
            "<strong>教育 AI 主战场：</strong>多 Agent 课堂 vs Google 免费送学生 AI——教育场景的竞争白热化。",
            "<strong>中国高校 AI 输出：</strong>清华项目连续两日霸榜——中国高校开源力量持续登场。"
        ],
        "tags": ["tsinghua", "multi-agent", "education", "classroom", "ai-learning"]
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
        "stars": "40,390",
        "forks": "3,742",
        "starsToday": "1,968",
        "count": 6,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +1,968★！40.4K★ 六连登单日新高！AI 科学家技能库——165 个验证技能 + 100+ 科学数据库，19 万科学家在用，破 40K★。",
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
            "<strong>六连登单日新高：</strong>+130 → +498 → +1,604 → +1,587 → +1,968——今天破了 40K★ 大关。",
            "<strong>19 万科学家背书：</strong>165 个技能 + 100+ 数据库——纵向深耕的样板还在加厚。",
            "<strong>与 archify 双龙头：</strong>通用架构图 + 垂直科研——技能经济两条腿都在狂奔。"
        ],
        "tags": ["scientific", "agent-skills", "research", "biology", "science"]
    },
    {
        "rank": 10,
        "owner": "every-app",
        "name": "open-seo",
        "fullName": "every-app / open-seo",
        "org": "every-app",
        "url": "https://github.com/every-app/open-seo",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "15,512",
        "forks": "1,862",
        "starsToday": "608",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +608★！15.5K★ 二连登！Semrush/Ahrefs 的开源替代——SEO 工具链开源化持续吸星。",
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
            "<strong>二连登：</strong>+517 → +608——SEO 开源替代热度稳步上扬。",
            "<strong>营销数据主权：</strong>企业不想再被 SaaS 锁死——自托管营销工具是长期趋势。",
            "<strong>与 AI 结合：</strong>AI 内容优化 + 开源 SEO——创作者经济基础设施成型。"
        ],
        "tags": ["seo", "semrush-alternative", "self-hosted", "marketing", "typescript"]
    },
    {
        "rank": 11,
        "owner": "p-e-w",
        "name": "heretic",
        "fullName": "p-e-w / heretic",
        "org": "p-e-w",
        "url": "https://github.com/p-e-w/heretic",
        "lang": "Python",
        "langClass": "py",
        "stars": "29,454",
        "forks": "3,227",
        "starsToday": "536",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +536★！29.5K★ 二连登！语言模型的自动审查移除——p-e-w（Planck 作者）的「异端」工具，单日增速翻三倍。",
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
            "<strong>二连登加速：</strong>+150 → +536——「去审查」话题热度突然放大。",
            "<strong>对齐之争再起：</strong>heretic 代表「用户控制」阵营——AI 安全的另一面持续被讨论。",
            "<strong>控制与反控制：</strong>Anthropic 加水印、heretic 去审查——这场拉锯远未结束。"
        ],
        "tags": ["llm", "censorship", "alignment", "local-model", "python"]
    },
    {
        "rank": 12,
        "owner": "pollen-robotics",
        "name": "microduck_rl",
        "fullName": "pollen-robotics / microduck_rl",
        "org": "Pollen Robotics",
        "url": "https://github.com/pollen-robotics/microduck_rl",
        "lang": "Python",
        "langClass": "py",
        "stars": "1,044",
        "forks": "179",
        "starsToday": "384",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 今日 +384★！1,044★ 二连登破千！Microduck（mjlab）的强化学习训练环境——教机器鸭子学走路，小项目两天翻倍。",
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
            "<strong>二连登破千：</strong>+147 → +384——1,044★ 翻倍式增长，「机器鸭子」出圈。",
            "<strong>RL 民主化：</strong>低成本仿真环境——机器人强化学习不再是大厂专属。",
            "<strong>sim-to-real 路径：</strong>从虚拟到现实——机器人 AI 的核心方法论被小项目验证。"
        ],
        "tags": ["robotics", "reinforcement-learning", "simulation", "quadruped", "education"]
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
    "date": "2026-08-31",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-31'
data['topic'] = '🔥 <strong>archify 五连登单日 +3,993 再创新高 + OpenMAIC 二连登翻三倍 + scientific-agent-skills 六连登破 40K + reverse-skill/专利技能/ECC 回归 + minimind 教学登榜</strong> —— tt-a1i/archify（+3,993★）37K★ 五连登，五天累计 19K★ 技能经济之王。THU-MAIC/OpenMAIC（+2,819★）25.9K★ 清华多 Agent 课堂二连登翻三倍。K-Dense-AI/scientific-agent-skills（+1,968★）40.4K★ 六连登破 40K。zhaoxuya520/reverse-skill（+1,439★）32.7K★ 中文安全技能路由包首登。every-app/open-seo（+608★）二连登。handsomestWei/patent-disclosure-skill（+571★）中国专利技能首登。p-e-w/heretic（+536★）二连登加速。affaan-m/ECC（+490★）245K★ 时隔一月回归。jingyaogong/minimind（+472★）55.8K★ 从零训练 LLM 教学首登。kaifcodec/user-scanner（+462★）OSINT 首登。pollen-robotics/microduck_rl（+384★）破千二连登。技能经济持续统治 + 中文技能生态（安全/专利）密集登场 + 中国高校与教学项目同步升温——「Agent 技能」正在成为开源世界最大的新增量。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
