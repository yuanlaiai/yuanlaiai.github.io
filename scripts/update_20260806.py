#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-08-06 (7-day gap from 7/30)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 8, 6)
gap_days = (today - last).days  # 7
shift = gap_days + 1  # 8
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

today_projects = [
    {
        "rank": 1,
        "owner": "cloudflare",
        "name": "computer",
        "fullName": "cloudflare / computer",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/computer",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "4,451",
        "forks": "216",
        "starsToday": "2,690",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +2,690★！4.5K★ Cloudflare 官方出品！给 Agent 一台电脑——让 AI Agent 拥有完整计算机操作能力的云端方案。",
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
            "<strong>Cloudflare 入局 Agent 基础设施：</strong>给 Agent 一台电脑——这是从「Agent 会写代码」到「Agent 会操作电脑」的关键一跃。",
            "<strong>2,690★ 单日爆发：</strong>首日即爆——开发者苦「Agent 没有手」久矣，云端电脑是刚需。",
            "<strong>Agent 操作系统的战争：</strong>从 OpenAI Operator 到 Claude Computer Use，再到 Cloudflare 开源——谁给 Agent 最好的「手」，谁就掌握下一代入口。"
        ],
        "tags": ["cloudflare", "agent", "computer-use", "cloud", "infrastructure"]
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
        "stars": "206,223",
        "forks": "17,810",
        "starsToday": "1,695",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,695★！206K★ 重磅回归！「真正的工程师技能」——来自 Matt Pocock 的 .agents 目录，TypeScript 工程师的 Agent 技能圣经。",
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
            "<strong>206K★ 回归榜单：</strong>上次 7/14 登榜后回归——个人权威技能库的持久魅力。",
            "<strong>「真实工程师」定位：</strong>不是理论教程，是 Matt Pocock 自己每天都在用的技能——实战是最高标准。",
            "<strong>技能经济个人品牌化：</strong>从 addyosmani 到 mattpocock，顶级工程师正在成为 Agent 技能的第一供应商。"
        ],
        "tags": ["skills", "typescript", "agent-skills", "mattpocock", "developer-tools"]
    },
    {
        "rank": 3,
        "owner": "firecrawl",
        "name": "pdf-inspector",
        "fullName": "firecrawl / pdf-inspector",
        "org": "Firecrawl",
        "url": "https://github.com/firecrawl/pdf-inspector",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "12,091",
        "forks": "809",
        "starsToday": "1,194",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,194★！12.1K★ Rust 编写的 PDF 检查库——快速分类、文本提取，智能识别扫描版 vs 文本版 PDF。",
        "problems": [
            "<strong>PDF 处理性能差：</strong>现有 PDF 解析库慢且内存占用高。",
            "<strong>扫描版识别难：</strong>无法自动区分扫描版和文本版 PDF，路由决策困难。",
            "<strong>文档智能预处理缺失：</strong>RAG 和文档管线需要前置的分类判断。"
        ],
        "usage": [
            "安装：<pre><code>cargo add pdf-inspector</code></pre>",
            "检查 PDF：<pre><code>pdf-inspector inspect file.pdf</code></pre>",
            "集成到文档管线：自动判断是否需要 OCR 处理。"
        ],
        "insights": [
            "<strong>12.1K★ 的 RAG 基建热：</strong>PDF 是 RAG 最大的数据源——谁把 PDF 处理做得又快又准，谁就赢在文档智能的起点。",
            "<strong>Rust 在文档处理崛起：</strong>性能敏感场景全面转向 Rust——扫描版检测这种 IO 密集型任务尤其受益。",
            "<strong>Firecrawl 生态扩张：</strong>从网页抓取到 PDF 检查——文档智能基础设施正在被系统性补齐。"
        ],
        "tags": ["pdf", "rust", "rag", "document-processing", "firecrawl"]
    },
    {
        "rank": 4,
        "owner": "TencentCloud",
        "name": "TencentDB-Agent-Memory",
        "fullName": "TencentCloud / TencentDB-Agent-Memory",
        "org": "腾讯云",
        "url": "https://github.com/TencentCloud/TencentDB-Agent-Memory",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "15,881",
        "forks": "1,427",
        "starsToday": "1,053",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +1,053★！15.9K★ 腾讯云开源！团队级 AI Agent 记忆中枢——对话、文档、代码转成四种可复用记忆资产，跨 Agent 跨框架共享。",
        "problems": [
            "<strong>Agent 记忆碎片化：</strong>每个 Agent 的对话、技能、知识互相隔离，无法团队共享。",
            "<strong>知识资产难沉淀：</strong>对话和文档里的经验无法转化为可复用的结构化记忆。",
            "<strong>跨框架兼容困难：</strong>不同 Agent 框架的记忆格式不互通。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git</code></pre>",
            "接入数据库：配置 TencentDB 连接。",
            "四种记忆资产：Chat Memory / Skill / LLM-Wiki / Code-Graph 自动沉淀。"
        ],
        "insights": [
            "<strong>15.9K★ 腾讯云开源重磅：</strong>国内云厂商开始下场做 Agent 基础设施——记忆中枢是下一个竞争高地。",
            "<strong>团队级记忆是空白：</strong>个人记忆工具很多，团队级共享记忆是全新品类——Agent 协作的组织级基础设施。",
            "<strong>四种资产的划分：</strong>对话记忆 + 技能 + 知识库 + 代码图谱——几乎覆盖了 Agent 的全部认知资产。"
        ],
        "tags": ["agent-memory", "tencent-cloud", "team-collaboration", "llm-wiki", "code-graph"]
    },
    {
        "rank": 5,
        "owner": "esengine",
        "name": "DeepSeek-Reasonix",
        "fullName": "esengine / DeepSeek-Reasonix",
        "org": "esengine",
        "url": "https://github.com/esengine/DeepSeek-Reasonix",
        "lang": "Go",
        "langClass": "go",
        "stars": "32,152",
        "forks": "2,078",
        "starsToday": "894",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +894★！32.2K★ DeepSeek 原生终端编码 Agent！围绕前缀缓存稳定性设计——挂机不塌，Go 编写。",
        "problems": [
            "<strong>编码 Agent 成本高：</strong>Claude Code/Codex 订阅贵，token 消耗大。",
            "<strong>前缀缓存不稳定：</strong>大多数 Agent 工具的前缀缓存命中率低，重复计费。",
            "<strong>缺少 DeepSeek 原生方案：</strong>没有为 DeepSeek 模型深度优化的编码 Agent。"
        ],
        "usage": [
            "安装：<pre><code>go install github.com/esengine/DeepSeek-Reasonix@latest</code></pre>",
            "配置 DeepSeek API Key 后启动。",
            "在终端中直接对话式编程。"
        ],
        "insights": [
            "<strong>32.2K★ DeepSeek 生态爆发：</strong>V4 Flash 发布后，DeepSeek 原生工具链全线起飞——模型强了，工具就跟着繁荣。",
            "<strong>前缀缓存稳定性是卖点：</strong>「leave it running」——为挂机场景设计的架构，省 token 就是省钱。",
            "<strong>Go 写 Agent 的新趋势：</strong>单二进制 + 高性能 + 内存安全——Go 正在成为 Agent 基础设施的新选择。"
        ],
        "tags": ["deepseek", "coding-agent", "go", "terminal", "prefix-cache"]
    },
    {
        "rank": 6,
        "owner": "obra",
        "name": "superpowers",
        "fullName": "obra / superpowers",
        "org": "obra",
        "url": "https://github.com/obra/superpowers",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "267,837",
        "forks": "23,932",
        "starsToday": "858",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +858★！268K★ 重磅回归！Agentic Skills 框架 + 软件开发方法论集大成者，技能像 npm 包一样安装卸载。",
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
            "<strong>268K★ 第 13 次登榜：</strong>从 5 月至今持续霸榜——superpowers 已是 Agent 技能分发的标准基础设施。",
            "<strong>技能即代码再确认：</strong>像 npm 包一样管理 Agent 技能——生态化管理是 Agent 平台的护城河。",
            "<strong>方法论 + 技能的复合价值：</strong>不只是技能库，还包含软件开发方法论——工具 + 思想的组合才是完整产品。"
        ],
        "tags": ["agent-framework", "skills", "developer-tools", "cli", "agent-ecosystem"]
    },
    {
        "rank": 7,
        "owner": "huangruiteng",
        "name": "loopx",
        "fullName": "huangruiteng / loopx",
        "org": "huangruiteng",
        "url": "https://github.com/huangruiteng/loopx",
        "lang": "Python",
        "langClass": "py",
        "stars": "2,654",
        "forks": "195",
        "starsToday": "854",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +854★！2.7K★ 轻量循环工程状态内核——面向长运行 AI Agent 团队，跨 Codex/Claude Code 的 Agent-loop 状态管理。",
        "problems": [
            "<strong>长运行 Agent 状态丢失：</strong>Agent 跑几小时后上下文丢失、目标漂移、无法恢复。",
            "<strong>Agent 团队协作无状态：</strong>多个 Agent 协作时缺少共享的进度和交接机制。",
            "<strong>配额管理缺失：</strong>长运行 Agent 无法感知 API 配额自动休眠。"
        ],
        "usage": [
            "安装：<pre><code>pip install loopx</code></pre>",
            "初始化：<pre><code>loopx init</code></pre>",
            "运行 Agent 团队：<pre><code>loopx run --agents 3</code></pre>"
        ],
        "insights": [
            "<strong>2.7K★ 的高增速：</strong>854★ 单日——长运行 Agent 的状态管理是刚需中的刚需。",
            "<strong>「循环工程」新概念：</strong>Agent-loop 状态内核——把 Agent 从一次性任务变成可持续运行的团队。",
            "<strong>配额感知自动唤醒：</strong>这是工程化思维——让 Agent 知道自己有多少预算、什么时候该停。"
        ],
        "tags": ["agent-loop", "state-management", "long-running", "agent-team", "python"]
    }
]

# Shift labels for 7-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = f'{shift-1}天前'  # 7天前
    elif label == '昨天':
        day['label'] = f'{shift}天前'  # 8天前
    elif label == '前天':
        day['label'] = f'{shift+1}天前'  # 9天前
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + shift}天前'

# Insert new day
new_day = {
    "date": "2026-08-06",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-08-06'
data['topic'] = '🔥 <strong>Cloudflare 给 Agent 一台电脑 + Matt Pocock 技能回归 + PDF 检查库爆发 + 腾讯云 Agent 记忆中枢 + DeepSeek 原生 Agent + Superpowers 第13次 + LoopX 循环工程</strong> —— cloudflare/computer（+2,690★）4.5K★ 首日即爆！给 AI Agent 一台电脑，从「会写代码」到「会操作电脑」的关键一跃。mattpocock/skills（+1,695★）206K★ 重磅回归——真实工程师的 Agent 技能圣经。firecrawl/pdf-inspector（+1,194★）12.1K★ Rust PDF 检查库，RAG 基建热。TencentCloud/TencentDB-Agent-Memory（+1,053★）15.9K★ 腾讯云开源团队级 Agent 记忆中枢。esengine/DeepSeek-Reasonix（+894★）32.2K★ DeepSeek 原生编码 Agent，V4 Flash 生态起飞。obra/superpowers（+858★）268K★ 第13次登榜——Agent 技能分发基础设施。huangruiteng/loopx（+854★）2.7K★ 长运行 Agent 状态内核。电脑操作 × 技能生态 × PDF 基建 × 记忆中枢 × DeepSeek 生态 × 循环工程——Agent 基础设施全面开花。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
