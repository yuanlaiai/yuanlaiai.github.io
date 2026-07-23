#!/usr/bin/env python3
"""Update GitHub trending data for 2026-07-06"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 7, 6)
gap_days = (today - last).days
shift = gap_days + 1  # 3
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

def find_latest_count(data, project_name):
    for day in data['days']:
        for proj in day['projects']:
            if proj['name'] == project_name:
                return proj['count']
    return 0

today_projects = [
    {
        "rank": 1,
        "owner": "Zackriya-Solutions",
        "name": "meetily",
        "fullName": "Zackriya-Solutions / meetily",
        "org": "Zackriya Solutions",
        "url": "https://github.com/Zackriya-Solutions/meetily",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "18,577",
        "forks": "1,897",
        "starsToday": "2,493",
        "count": 1,
        "description": "\U0001f525 亮点 —— 今日 +2,493\u2605！18.6K\u2605 本地优先 AI 会议助手！4x Parakeet/Whisper 实时转录 + Ollama 总结，100% 本地运行。",
        "problems": [
            "<strong>会议记录隐私危机：</strong>云端会议工具录音上传到第三方，敏感内容存在泄露风险。",
            "<strong>实时转录延迟高：</strong>大多数会议助手依赖云 API，网络延迟影响实时体验。",
            "<strong>本地部署门槛高：</strong>自建本地会议系统需要复杂的配置和硬件支持。"
        ],
        "usage": [
            "下载安装：<pre><code>brew install meetily</code></pre>或从 GitHub Releases 下载。",
            "启动：<pre><code>meetily</code></pre>自动监听系统音频。",
            "查看转录：打开浏览器访问 <pre><code>http://localhost:5371</code></pre>"
        ],
        "insights": [
            "<strong>本地 AI 会议助手爆发：</strong>多日连续登榜 +2,493\u2605 创新高——隐私 + 本地 AI = 刚需组合。",
            "<strong>Rust + AI 双引擎：</strong>用 Rust 写的 Whisper 转录 4x 加速，证明本地推理也能有云端级别的性能。",
            "<strong>Ollama 生态受益者：</strong>接入 Ollama 做本地总结，不依赖任何云 API——隐私敏感企业的最佳入门方案。"
        ],
        "tags": ["meeting-assistant", "whisper", "rust", "privacy", "ollama"]
    },
    {
        "rank": 2,
        "owner": "Leonxlnx",
        "name": "taste-skill",
        "fullName": "Leonxlnx / taste-skill",
        "org": "Leonxlnx",
        "url": "https://github.com/Leonxlnx/taste-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "58,441",
        "forks": "3,986",
        "starsToday": "1,453",
        "count": find_latest_count(data, 'taste-skill') + 1,
        "description": "\U0001f525 亮点 —— 今日 +1,453\u2605！58.4K\u2605 四次登榜！给 AI 装上「审美」——阻止生成无聊 AI 味的技能。",
        "problems": [
            "<strong>AI 输出千篇一律：</strong>大模型生成的内容越来越同质化，「AI 味」让人一眼就能识别。",
            "<strong>缺乏美学判断：</strong>LLM 写文案/做设计时，不知道什么是好的审美，什么是有品味的。",
            "<strong>品牌一致性难保障：</strong>生成内容与品牌调性脱节，需要大量人工后处理。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/Leonxlnx/taste-skill.git</code></pre>",
            "加载 SKILL.md 到 AI 助手，即可获得品味增强。",
            "支持 Claude Code、Cursor、Codex 等主流编码 Agent。"
        ],
        "insights": [
            "<strong>58K\u2605 四次登榜：</strong>从 5/26 首登以来持续增长——「反 AI 味」是真正的开发者刚需。",
            "<strong>审美即生产力：</strong>AI 生成内容最大的瓶颈不是能力，是「有没有品味」——taste-skill 切中了核心痛点。",
            "<strong>Agent 技能的品类化：</strong>继「省钱技能」（caveman）之后，「审美技能」成了第二个垂直品类——技能经济正在细分。"
        ],
        "tags": ["ai-quality", "taste", "anti-slop", "agent-skill", "design"]
    },
    {
        "rank": 3,
        "owner": "asgeirtj",
        "name": "system_prompts_leaks",
        "fullName": "asgeirtj / system_prompts_leaks",
        "org": "asgeirtj",
        "url": "https://github.com/asgeirtj/system_prompts_leaks",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "50,885",
        "forks": "8,298",
        "starsToday": "1,386",
        "count": 1,
        "description": "\U0001f525 亮点 —— 今日 +1,386\u2605！50.9K\u2605 AI 行业最高机密公开！提取各大厂商的系统提示词——Anthropic、OpenAI、Google、xAI 全收录。",
        "problems": [
            "<strong>系统提示词是黑盒：</strong>AI 模型的行为规则被锁在厂商的 API 里，开发者无从了解内部机制。",
            "<strong>提示词工程缺乏参考：</strong>社区写 Prompt 全靠猜测，缺少真实世界顶级模型的系统提示作为标杆。",
            "<strong>安全透明度不足：</strong>被删改的提示词说明什么？厂商的安全策略和内容过滤规则需要阳光。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/asgeirtj/system_prompts_leaks.git</code></pre>",
            "浏览分类：<pre><code>ls */</code></pre>查看按厂商分类的提示词目录。",
            "学习 Claude Fable 5、GPT 5.5 Thinking、Gemini 3.5 等顶级模型的系统提示设计。"
        ],
        "insights": [
            "<strong>50K\u2605 的背后是好奇心：</strong>AI 用户对「模型背后怎么想的」有巨大好奇心——系统提示词成了 AI 时代的新考古学。",
            "<strong>提示词透明化趋势：</strong>Claude Code、Codex、Cursor 等开源了系统提示，但闭源模型仍被社区反向提取。",
            "<strong>安全博弈永不停歇：</strong>每次更新 Prompt 后社区都在对比差异——这是一场厂商和社区之间的猫鼠游戏。"
        ],
        "tags": ["system-prompts", "prompt-engineering", "ai-transparency", "reverse-engineering", "llm"]
    },
    {
        "rank": 4,
        "owner": "addyosmani",
        "name": "agent-skills",
        "fullName": "addyosmani / agent-skills",
        "org": "Google Chrome",
        "url": "https://github.com/addyosmani/agent-skills",
        "lang": "Shell",
        "langClass": "sh",
        "stars": "70,389",
        "forks": "7,628",
        "starsToday": "1,114",
        "count": find_latest_count(data, 'agent-skills') + 1,
        "description": "\U0001f525 亮点 —— 今日 +1,114\u2605！70.4K\u2605 三次登榜！Google Chrome 团队技术负责人开源的工程级 Agent 技能库。",
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
            "<strong>Google Chrome 负责人出手：</strong>addyosmani 是 Google Chrome 工程总监，他的技能就是 Web 工程领域的最权威指南。",
            "<strong>70K\u2605 的号召力：</strong>从 6/11 首登到 7/6 第三次登榜，持续增长——开发者迫切需要一个权威 Agent 技能参考。",
            "<strong>技能生态分化：</strong>个人权威（mattpocock/skills）vs 社区共建（agency-agents）vs 工程实战（agent-skills）——三种模式并行繁荣。"
        ],
        "tags": ["agent-skills", "google-chrome", "web-engineering", "claude-code", "developer-tools"]
    },
    {
        "rank": 5,
        "owner": "openai",
        "name": "codex-plugin-cc",
        "fullName": "openai / codex-plugin-cc",
        "org": "OpenAI",
        "url": "https://github.com/openai/codex-plugin-cc",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "26,069",
        "forks": "1,564",
        "starsToday": "910",
        "count": 1,
        "description": "\U0001f525 亮点 —— 今日 +910\u2605！26.1K\u2605 OpenAI 官方出品！在 Claude Code 里用 Codex 审查代码、委派任务——跨 Agent 协作！",
        "problems": [
            "<strong>Agent 能力各有千秋：</strong>Claude Code 擅长长上下文推理，Codex 擅长代码审查，但无法互相调用。",
            "<strong>工作流割裂：</strong>开发者需要在不同编码 Agent 之间手动切换，中断创作流。",
            "<strong>缺少官方互操作方案：</strong>社区虽然做了各种整合，但缺少 OpenAI 官方支持。"
        ],
        "usage": [
            "安装：<pre><code>claude add openai/codex-plugin-cc</code></pre>",
            "在 Claude Code 中运行：<pre><code>/codex review</code></pre>委派 Codex 审查当前代码。",
            "批量审查：<pre><code>/codex review src/</code></pre>对整个目录进行 Codex 安全扫描。"
        ],
        "insights": [
            "<strong>跨 Agent 协作里程碑：</strong>OpenAI 官方为 Claude Code 做插件——竞品之间互操作，这才是真正的 AI 生态。",
            "<strong>26K\u2605 的首日爆发：</strong>上线即爆，开发者一直在等这样的官方方案。",
            "<strong>Codex 的新定位：</strong>从独立编码 Agent 变成「Claude Code 的审查引擎」——Agent 协作才是未来。"
        ],
        "tags": ["openai", "codex", "claude-code", "code-review", "agent-interop"]
    }
]

# Shift labels (shift=3 for 2-day gap)
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '前天'  # shift-1 = 2天前, but shift=3 so 2+1=前天
    elif label == '昨天':
        day['label'] = f'{shift+1}天前'  # 4天前
    elif label == '前天':
        day['label'] = f'{shift+2}天前'  # 5天前
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + shift}天前'

# Insert new day
new_day = {
    "date": "2026-07-06",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}

days.insert(0, new_day)
data['lastUpdated'] = '2026-07-06'
data['topic'] = '\U0001f525 <strong>隐私会议 AI 爆发 + 审美技能四次登榜 + 系统提示词透明运动 + Chrome 权威技能 + OpenAI 跨 Agent 互操作</strong> —— Zackriya-Solutions/meetily（+2,493\u2605）本地 AI 会议助手爆发式增长。Leonxlnx/taste-skill（+1,453\u2605）58K\u2605 四次登榜，「反 AI 味」是开发者核心痛点。asgeirtj/system_prompts_leaks（+1,386\u2605）50K\u2605 系统提示词透明化运动席卷社区。addyosmani/agent-skills（+1,114\u2605）Google Chrome 工程总监出手，70K\u2605 权威技能。openai/codex-plugin-cc（+910\u2605）OpenAI 为 Claude Code 做插件——跨 Agent 互操作时代来临。隐私、品味、透明、权威、协作——五个不同维度的 AI 趋势同日爆发。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:6]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
