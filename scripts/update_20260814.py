#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-14 (1-day gap from 8/13)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 14)
gap_days = (today - last).days  # 1
shift = gap_days + 1  # 2
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
        "stars": "14,434",
        "forks": "862",
        "starsToday": "4,475",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +4,475★！14.4K★ 连续两天登榜！29 种编辑级图表设计给 Claude Code——自包含 HTML + SVG，反 Mermaid-slop 两天涨 1.4 万星。",
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
            "<strong>连续两天登榜爆发：</strong>+2,855★ → +4,475★ 两天涨 1.4 万星——「反 Mermaid-slop」是现象级需求。",
            "<strong>编辑级图表是蓝海：</strong>把专业设计标准注入 Agent 输出——设计类 Agent 技能持续走红。",
            "<strong>审美革命的下一站：</strong>继文本/图片后，图表成为 AI 内容「去 AI 味」的新战场。"
        ],
        "tags": ["diagram", "claude-code", "design", "svg", "html"]
    },
    {
        "rank": 2,
        "owner": "macro-inc",
        "name": "macro",
        "fullName": "macro-inc / macro",
        "org": "Macro Inc",
        "url": "https://github.com/macro-inc/macro",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "2,589",
        "forks": "276",
        "starsToday": "1,239",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,239★！2.6K★ Rust 编写的团队统一工作区——邮件、聊天、文档、任务、Agent、通话、CRM 全打通，@ 链接 + 共享 AI 记忆。",
        "problems": [
            "<strong>团队工具碎片化：</strong>邮件、聊天、文档、任务、CRM 分散在不同应用。",
            "<strong>Agent 与工作流割裂：</strong>AI Agent 无法访问团队的全部上下文。",
            "<strong>共享记忆缺失：</strong>团队知识散落各处，无法被 Agent 高效利用。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/macro-inc/macro.git</code></pre>",
            "启动：<pre><code>cargo run</code></pre>",
            "@ 链接打通各类工具，配置共享 AI 记忆。"
        ],
        "insights": [
            "<strong>1,239★ 单日爆发：</strong>「统一工作区 + AI 记忆」——团队协作工具的新范式正在形成。",
            "<strong>Rust 写协作软件：</strong>性能敏感的前端基建用 Rust——新一代协作工具的技术选择。",
            "<strong>Agent 时代的 Slack 之争：</strong>当 Agent 成为团队一员，工作区需要重新设计——macro 抢占了这个生态位。"
        ],
        "tags": ["workspace", "rust", "team-collaboration", "ai-memory", "agents"]
    },
    {
        "rank": 3,
        "owner": "msitarzewski",
        "name": "agency-agents",
        "fullName": "msitarzewski / agency-agents",
        "org": "msitarzewski",
        "url": "https://github.com/msitarzewski/agency-agents",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "145,178",
        "forks": "23,482",
        "starsToday": "778",
        "count": 8,
        "description": "🔥 亮点 —— 今日 +778★！145.2K★ 第八次登榜！社区最大 AI Agent 专业技能库——每个 Agent 都是专属专家，技能生态网络效应持续。",
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
            "<strong>第八次登榜：</strong>从 6 月至今持续霸榜——145.2K★ 社区共建技能库网络效应强大。",
            "<strong>Agent 技能生态成熟化：</strong>从「技能库」到「AI 代理机构」——技能生态正在产品化。",
            "<strong>SKILL.md 标准化：</strong>从建议格式演变为事实标准——技能分发的基础设施已成型。"
        ],
        "tags": ["ai-agent", "skills", "agent-framework", "productivity", "automation"]
    },
    {
        "rank": 4,
        "owner": "cactus-compute",
        "name": "needle",
        "fullName": "cactus-compute / needle",
        "org": "Cactus Compute",
        "url": "https://github.com/cactus-compute/needle",
        "lang": "Python",
        "langClass": "py",
        "stars": "4,940",
        "forks": "333",
        "starsToday": "769",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +769★！4.9K★ 14MB 基础模型——专为手机、可穿戴、智能家居和机器人等微型设备设计！",
        "problems": [
            "<strong>边缘设备无法跑大模型：</strong>手机、手表、智能家居内存和算力有限。",
            "<strong>云端推理隐私风险：</strong>小型设备依赖云端 AI，敏感数据外传。",
            "<strong>端侧 AI 生态空白：</strong>缺少为微型设备优化的基础模型。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/cactus-compute/needle.git</code></pre>",
            "安装：<pre><code>pip install needle</code></pre>",
            "部署到手机/手表/智能家居/机器人。"
        ],
        "insights": [
            "<strong>14MB 的极限压缩：</strong>基础模型从 GB 级压缩到 14MB——边缘 AI 的「最小可行智能」。",
            "<strong>端侧 AI 爆发前夜：</strong>手机、穿戴、智能家居都需要本地智能——needle 押注微型设备赛道。",
            "<strong>隐私是驱动力：</strong>数据不出设备——端侧推理是隐私保护的终极方案。"
        ],
        "tags": ["edge-ai", "tiny-model", "embedded", "privacy", "on-device"]
    },
    {
        "rank": 5,
        "owner": "semantica-agi",
        "name": "semantica",
        "fullName": "semantica-agi / semantica",
        "org": "Semantica AGI",
        "url": "https://github.com/semantica-agi/semantica",
        "lang": "Python",
        "langClass": "py",
        "stars": "6,625",
        "forks": "697",
        "starsToday": "713",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +713★！6.6K★ 连续两天登榜！图原生基础设施——为上下文和可问责 AI 系统而生，Graph-Native 架构让 AI 可解释可追溯。",
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
            "<strong>连续两天登榜：</strong>+845★ → +713★——图原生可问责 AI 基建需求稳定。",
            "<strong>监管推动：</strong>欧盟 AI Act 等法规要求可解释、可追溯——图结构是答案。",
            "<strong>Context 层竞争：</strong>继 RAG 之后，「上下文基础设施」成为新战场。"
        ],
        "tags": ["graph-database", "ai-infrastructure", "context", "accountability", "rag"]
    },
    {
        "rank": 6,
        "owner": "NVIDIA-NeMo",
        "name": "Switchyard",
        "fullName": "NVIDIA-NeMo / Switchyard",
        "org": "NVIDIA NeMo",
        "url": "https://github.com/NVIDIA-NeMo/Switchyard",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "1,204",
        "forks": "108",
        "starsToday": "408",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +408★！1.2K★ 连续两天登榜！NVIDIA 官方 LLM 路由——跨模型跨提供商流量调度，原生兼容 OpenAI/Anthropic API。",
        "problems": [
            "<strong>多模型路由复杂：</strong>不同模型、不同提供商切换需要改代码。",
            "<strong>成本优化困难：</strong>无法按任务自动选择性价比最高的模型。",
            "<strong>基准测试碎片化：</strong>缺少统一的多模型对比框架。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/NVIDIA-NeMo/Switchyard.git</code></pre>",
            "构建：<pre><code>cargo build --release</code></pre>",
            "配置路由策略：按任务/成本/性能自动选择模型。"
        ],
        "insights": [
            "<strong>连续两天登榜：</strong>NVIDIA 官方入局 LLM 路由——模型路由是 Agent 时代的「网络交换机」。",
            "<strong>兼容性是关键：</strong>原生 OpenAI/Anthropic API 兼容——开发者零改动接入。",
            "<strong>成本优化是卖点：</strong>多模型路由 + 基准对比 = 自动选择性价比最优解。"
        ],
        "tags": ["nvidia", "llm-routing", "rust", "cost-optimization", "api-gateway"]
    },
    {
        "rank": 7,
        "owner": "unslothai",
        "name": "unsloth",
        "fullName": "unslothai / unsloth",
        "org": "Unsloth AI",
        "url": "https://github.com/unslothai/unsloth",
        "lang": "Python",
        "langClass": "py",
        "stars": "71,044",
        "forks": "6,406",
        "starsToday": "328",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +328★！71K★ 本地训练/运行 LLM 和扩散模型的 UI——支持 Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX 等。",
        "problems": [
            "<strong>本地微调门槛高：</strong>LLM 训练需要复杂的命令行和配置。",
            "<strong>模型生态碎片化：</strong>不同模型需要不同的工具链。",
            "<strong>GPU 利用率低：</strong>本地训练缺少性能优化。"
        ],
        "usage": [
            "安装：<pre><code>pip install unsloth</code></pre>",
            "启动 UI：<pre><code>unsloth ui</code></pre>",
            "选择模型开始训练或运行。"
        ],
        "insights": [
            "<strong>71K★ 本地 AI 主力工具：</strong>训练/推理一体的本地 UI——开源社区微调的事实标准。",
            "<strong>中国模型全家桶支持：</strong>Qwen3.8、Kimi K3、DeepSeek-V4——中国开源模型的传播基础设施。",
            "<strong>本地 AI 加速普及：</strong>GUI 化让微调从极客走向普通开发者。"
        ],
        "tags": ["fine-tuning", "local-llm", "ui", "training", "open-source"]
    }
]

# Shift labels for 1-day gap
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
        day['label'] = f'{num + 2}天前'

# Insert new day
new_day = {
    "date": "2026-08-14",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-14'
data['topic'] = '🔥 <strong>图表设计两天涨 1.4 万星 + Macro 统一工作区爆发 + Agency Agents 第八次 + Needle 14MB 微型模型 + Semantica 连登 + NVIDIA Switchyard 连登 + Unsloth 本地训练</strong> —— cathrynlavery/diagram-design（+4,475★）14.4K★ 连续两天登榜两天涨 1.4 万星！反 Mermaid-slop 现象级需求。macro-inc/macro（+1,239★）2.6K★ Rust 团队统一工作区 + AI 记忆。msitarzewski/agency-agents（+778★）145.2K★ 第八次登榜。cactus-compute/needle（+769★）4.9K★ 14MB 微型基础模型，端侧 AI 爆发前夜。semantica-agi/semantica（+713★）6.6K★ 连续两天图原生基建。NVIDIA-NeMo/Switchyard（+408★）1.2K★ 连续两天 LLM 路由。unslothai/unsloth（+328★）71K★ 本地训练 UI。设计技能 × 统一工作区 × 微型模型 × 图原生基建 × LLM 路由 × 本地训练——Agent 基础设施全面进入深水区。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
