#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-13 (3-day gap from 8/10)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 13)
gap_days = (today - last).days  # 3
shift = gap_days + 1  # 4
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

today_projects = [
    {
        "rank": 1,
        "owner": "cathrynlavery",
        "name": "diagram-design",
        "fullName": "cathrynlavery / diagram-design",
        "org": "cathrynlavery",
        "url": "https://github.com/cathrynlavery/diagram-design",
        "lang": "HTML",
        "langClass": "html",
        "stars": "10,277",
        "forks": "668",
        "starsToday": "2,855",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +2,855★！10.3K★ 首日爆发！29 种编辑级图表设计供 Claude Code 使用——自包含 HTML + SVG，无阴影、无 Mermaid 味。",
        "problems": [
            "<strong>AI 图表千篇一律：</strong>Mermaid 生成的图表模板感强，缺乏设计感。",
            "<strong>图表设计门槛高：</strong>编辑级图表需要专业设计技能，普通开发者做不出来。",
            "<strong>缺少可直接用的图表库：</strong>想让 Claude 生成高质量图表，但没有设计规范可循。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cathrynlavery/diagram-design.git</code></pre>",
            "按类型加载图表设计到 Claude Code。",
            "生成自包含 HTML + SVG 图表，无需额外依赖。"
        ],
        "insights": [
            "<strong>2,855★ 首日爆发：</strong>「反 Mermaid-slop」直击开发者痛点——AI 生成内容的审美革命延伸到图表领域。",
            "<strong>29 种编辑级类型：</strong>不是简单的流程图，而是编辑级图表设计——把专业设计标准注入 Agent 输出。",
            "<strong>设计规范即技能：</strong>继 taste-skill/impeccable 之后，设计类 Agent 技能持续走红——审美是 AI 的下一个战场。"
        ],
        "tags": ["diagram", "claude-code", "design", "svg", "html"]
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
        "stars": "144,550",
        "forks": "23,418",
        "starsToday": "1,873",
        "count": 7,
        "description": "🔥 亮点 —— 今日 +1,873★！144.6K★ 第七次登榜！社区最大 AI Agent 专业技能库——从前端魔法师到 Reddit 社区忍者，每个 Agent 都是专属专家。",
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
            "<strong>第七次登榜：</strong>从 6 月至今持续霸榜——144.6K★ 社区共建技能库网络效应强大。",
            "<strong>Agent 技能生态成熟化：</strong>从「技能库」到「AI 代理机构」——技能生态正在产品化。",
            "<strong>SKILL.md 标准化：</strong>从建议格式演变为事实标准——技能分发的基础设施已成型。"
        ],
        "tags": ["ai-agent", "skills", "agent-framework", "productivity", "automation"]
    },
    {
        "rank": 3,
        "owner": "stablyai",
        "name": "orca",
        "fullName": "stablyai / orca",
        "org": "Stably AI",
        "url": "https://github.com/stablyai/orca",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "43,839",
        "forks": "3,054",
        "starsToday": "1,235",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,235★！43.8K★ Orca——并行 Agent 舰队开发环境！用你自己的订阅跑任意编码 Agent，桌面/移动/VPS 全支持。",
        "problems": [
            "<strong>多 Agent 并行管理难：</strong>同时跑多个编码 Agent 缺少统一的管理界面。",
            "<strong>订阅碎片化：</strong>每个 Agent 工具要单独订阅，成本高且分散。",
            "<strong>跨设备工作流割裂：</strong>桌面、移动、服务器之间的 Agent 工作流无法同步。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g orca</code></pre>",
            "启动：<pre><code>orca</code></pre>",
            "接入你自己的 Agent 订阅并管理并行任务。"
        ],
        "insights": [
            "<strong>43.8K★ 的 Agent 舰队概念：</strong>「并行 Agent 舰队」——把多个编码 Agent 组织成可管理的工作流，是 Agent 规模化使用的新范式。",
            "<strong>自带订阅模式：</strong>不锁生态——运行任何编码 Agent 用自己的订阅，把选择权还给开发者。",
            "<strong>跨设备覆盖：</strong>桌面/移动/VPS——Agent 开发环境从单机走向全端。"
        ],
        "tags": ["agent-ide", "parallel-agents", "developer-tools", "typescript", "workflow"]
    },
    {
        "rank": 4,
        "owner": "semantica-agi",
        "name": "semantica",
        "fullName": "semantica-agi / semantica",
        "org": "Semantica AGI",
        "url": "https://github.com/semantica-agi/semantica",
        "lang": "Python",
        "langClass": "py",
        "stars": "5,699",
        "forks": "623",
        "starsToday": "845",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +845★！5.7K★ 图原生基础设施——为上下文和可问责 AI 系统而生，Graph-Native 架构让 AI 可解释可追溯。",
        "problems": [
            "<strong>AI 上下文黑盒：</strong>大模型的上下文处理不透明，难以审计和追责。",
            "<strong>图数据结构缺失：</strong>传统向量检索缺乏关系理解，复杂知识场景表现差。",
            "<strong>可问责 AI 基建空白：</strong>缺少让 AI 决策可解释、可追溯的基础设施。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/semantica-agi/semantica.git</code></pre>",
            "安装：<pre><code>pip install semantica</code></pre>",
            "接入图数据库构建可问责 AI 上下文层。"
        ],
        "insights": [
            "<strong>图原生 AI 基建升温：</strong>从向量检索到图结构——「可问责 AI」需要关系型上下文，图数据库是答案。",
            "<strong>5.7K★ 的合规需求：</strong>欧盟 AI Act 等监管推动——可解释、可追溯成为 AI 系统刚需。",
            "<strong>Context 层竞争：</strong>继 RAG 之后，「上下文基础设施」成为新战场——semantica 押注图原生路线。"
        ],
        "tags": ["graph-database", "ai-infrastructure", "context", "accountability", "rag"]
    },
    {
        "rank": 5,
        "owner": "paperclipai",
        "name": "paperclip",
        "fullName": "paperclipai / paperclip",
        "org": "Paperclip AI",
        "url": "https://github.com/paperclipai/paperclip",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "77,715",
        "forks": "14,299",
        "starsToday": "571",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +571★！77.7K★ 开源 Agent 管理应用——管理工作中所有 Agent 的「主力工具」。",
        "problems": [
            "<strong>Agent 数量失控：</strong>团队里的 Agent 越来越多，缺少统一管理入口。",
            "<strong>Agent 工作流混乱：</strong>每个 Agent 的任务、状态、产出分散各处。",
            "<strong>缺少协作基础设施：</strong>Agent 之间、人机之间缺少统一的协作平台。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/paperclipai/paperclip.git</code></pre>",
            "部署：<pre><code>docker compose up</code></pre>",
            "在界面中统一管理团队 Agent。"
        ],
        "insights": [
            "<strong>77.7K★ 的「Agent 管理器」定位：</strong>当 Agent 成为团队标配，「管理 Agent 的 Agent 平台」就是下一个 Slack——paperclip 抢占了这个生态位。",
            "<strong>开源企业工具崛起：</strong>14K 分叉——企业对 Agent 治理的需求已经在爆发。",
            "<strong>AgentOps 赛道成形：</strong>从开发到运维到治理——Agent 全生命周期管理成为独立品类。"
        ],
        "tags": ["agent-management", "agentops", "team-collaboration", "typescript", "enterprise"]
    },
    {
        "rank": 6,
        "owner": "hugohe3",
        "name": "ppt-master",
        "fullName": "hugohe3 / ppt-master",
        "org": "hugohe3",
        "url": "https://github.com/hugohe3/ppt-master",
        "lang": "Python",
        "langClass": "py",
        "stars": "45,543",
        "forks": "3,713",
        "starsToday": "476",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +476★！45.5K★ AI 生成原生 PowerPoint——真正的原生形状、过渡、动画，数据图表、音频旁白，支持自定义模板。",
        "problems": [
            "<strong>AI 幻灯片质量差：</strong>大多数 AI 生成 PPT 只是文字堆砌，没有真正的设计。",
            "<strong>缺乏原生动画：</strong>生成结果没有原生形状、过渡和动画，无法直接使用。",
            "<strong>数据图表能力弱：</strong>AI 无法生成数据支撑的图表和表格。"
        ],
        "usage": [
            "安装：<pre><code>pip install ppt-master</code></pre>",
            "生成：<pre><code>ppt-master generate --topic \"AI 趋势\"</code></pre>",
            "自定义模板：传入你自己的 .pptx 模板。"
        ],
        "insights": [
            "<strong>45.5K★ 的办公自动化刚需：</strong>PPT 是职场最高频的文档——「真正能用」的 AI 幻灯片工具需求巨大。",
            "<strong>原生格式是分水岭：</strong>不是输出图片而是原生 PPTX——带形状、动画、图表的成品才能进职场。",
            "<strong>AI 办公套件前夜：</strong>从文档到 PPT 到表格——AI 正在逐个攻占办公软件的高地。"
        ],
        "tags": ["powerpoint", "ai-office", "presentation", "python", "automation"]
    },
    {
        "rank": 7,
        "owner": "NVIDIA-NeMo",
        "name": "Switchyard",
        "fullName": "NVIDIA-NeMo / Switchyard",
        "org": "NVIDIA NeMo",
        "url": "https://github.com/NVIDIA-NeMo/Switchyard",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "814",
        "forks": "85",
        "starsToday": "421",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +421★！814★ NVIDIA NeMo 官方出品——Rust 编写的推理基础设施，为 AI Agent 服务的性能调度。",
        "problems": [
            "<strong>Agent 推理性能瓶颈：</strong>多 Agent 并发推理时 GPU 利用率低、调度效率差。",
            "<strong>推理基础设施碎片化：</strong>缺少统一的高性能推理调度层。",
            "<strong>Rust 生态缺位：</strong>AI 基础设施大多用 Python，性能敏感层缺少 Rust 方案。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/NVIDIA-NeMo/Switchyard.git</code></pre>",
            "构建：<pre><code>cargo build --release</code></pre>",
            "接入推理集群配置调度策略。"
        ],
        "insights": [
            "<strong>NVIDIA 官方入局推理调度：</strong>NeMo 团队做 Rust 推理基础设施——从训练到推理，NVIDIA 在补全 Agent 时代的能力拼图。",
            "<strong>Rust 接管性能敏感层：</strong>推理调度这种 IO/并发密集场景——Rust 是正确选择。",
            "<strong>Agent 规模化的基建竞赛：</strong>多 Agent 并发推理的调度优化，是下一个算力瓶颈。"
        ],
        "tags": ["nvidia", "inference", "rust", "agent-infrastructure", "scheduling"]
    }
]

# Shift labels for 3-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = f'{shift-1}天前'  # 3天前
    elif label == '昨天':
        day['label'] = f'{shift}天前'  # 4天前
    elif label == '前天':
        day['label'] = f'{shift+1}天前'  # 5天前
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + shift}天前'

# Insert new day
new_day = {
    "date": "2026-08-13",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-13'
data['topic'] = '🔥 <strong>图表设计技能首日爆发 + Agency Agents 第七次 + Orca 并行 Agent 舰队 + Semantica 图原生 AI + Paperclip Agent 管理 + PPT Master 办公自动化 + NVIDIA Switchyard</strong> —— cathrynlavery/diagram-design（+2,855★）10.3K★ 首日即爆！29 种编辑级图表设计给 Claude Code，反 Mermaid-slop。msitarzewski/agency-agents（+1,873★）144.6K★ 第七次登榜。stablyai/orca（+1,235★）43.8K★ 并行 Agent 舰队开发环境。semantica-agi/semantica（+845★）5.7K★ 图原生可问责 AI 基建。paperclipai/paperclip（+571★）77.7K★ 开源 Agent 管理平台。hugohe3/ppt-master（+476★）45.5K★ AI 生成原生 PPT。NVIDIA-NeMo/Switchyard（+421★）814★ NVIDIA Rust 推理调度。设计技能 × Agent 舰队 × 图原生基建 × Agent 管理 × 办公自动化 × 推理调度——Agent 基础设施进入精细化阶段。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
