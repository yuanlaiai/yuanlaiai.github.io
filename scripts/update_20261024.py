#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-10-24 (3-day gap, 无昨日榜→平铺结构, 8 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 10, 24)
gap_days = (today - last).days  # 3
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（3天gap无昨日榜，含回归项目，触发平铺渲染），按日增降序 ──
    {
        "rank": 1,
        "owner": "cloudflare",
        "name": "security-audit-skill",
        "fullName": "cloudflare / security-audit-skill",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "42,837",
        "forks": "2,672",
        "starsToday": "2,716",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,716★ 再创日增新高，连续两次上榜！4.28万★（三天前 3.52万★，一周前 1.75万★）。Cloudflare 出的编码 agent 技能：多阶段安全审计，每个结论都要独立验证，输出机器可读的结果。",
        "problems": [
            "<strong>AI 写的代码没人验：</strong>生成速度快了十倍，安全评审还停在人工抽样。",
            "<strong>审计结论不可信：</strong>模型说「这里可能有注入」，没有证据链，工程师只能重查一遍。",
            "<strong>报告不能进流水线：</strong>自然语言写一堆，CI 读不了，也就没法卡住合并。"
        ],
        "usage": [
            "把技能装进支持 Agent Skills 的编码工具（Claude Code、Cursor、Codex 等）。",
            "在提交前或 CI 里触发多阶段审计，让每个发现都附上可验证的证据。",
            "读取机器可读的结果，接进流水线做阻断或分级处理。"
        ],
        "insights": [
            "<strong>一周从 1.75 万涨到 4.28 万：</strong>这不是自然增长的速度。当一类工具在几天内翻两倍多，通常意味着某个环节的预算被迫提前了，安全审计就是这种「不做不行」的支出。",
            "<strong>日增还能创新高，说明需求没有一次性释放完：</strong>第5次上榜时 +1,997，今天 +2,716。同一批人不会连续加购，更可能是新的团队在陆续接入。",
            "<strong>本质是验证成本成了 AI 编码的真瓶颈：</strong>写得快这件事已经解决了，确认写得对没有。谁把这部分自动化，谁就拿走了下一段最刚性的预算。"
        ],
        "tags": ["security", "agent-skill", "audit", "javascript", "devsecops"]
    },
    {
        "rank": 2,
        "owner": "NVIDIA",
        "name": "OpenShell",
        "fullName": "NVIDIA / OpenShell",
        "org": "NVIDIA",
        "url": "https://github.com/NVIDIA/OpenShell",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "19,060",
        "forks": "1,901",
        "starsToday": "1,119",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,119★！1.91万★ 第2次登榜（9 月底首登时 9,975★，一个月接近翻倍）。英伟达给自主 agent 造的安全私有运行时：你在策略里声明每个 agent 能碰什么，它靠内核级拦截加形式化验证来执行——策略变更生效前，先算清它会放行什么。",
        "problems": [
            "<strong>给 Agent 权限就是给风险：</strong>能读文件、装包、调 API 才能干活，但每一步都可能碰到不该碰的东西。",
            "<strong>策略写完不知道放行了什么：</strong>权限规则越叠越多，没人算过组合起来到底允许了哪些操作。",
            "<strong>应用层拦不住：</strong>过滤器可以绕过，容器隔离又挡不住合法的系统调用。"
        ],
        "usage": [
            "安装：<pre><code>pip install openshell</code></pre>（Apache-2.0，文档在 docs.nvidia.com/openshell）",
            "用策略声明每个 Agent 能访问的文件、系统调用与网络范围。",
            "策略变更先走形式化验证，确认放行范围后再应用；Agent 各自跑在隔离沙箱里。"
        ],
        "insights": [
            "<strong>一个月从 9,975 涨到 19,060：</strong>首登时它更像一条新闻，这次是实打实的安装量在推。厂商工具能走完这个曲线，说明企业的 agent 试点进入「要上生产、得先圈起来」的阶段。",
            "<strong>它和今天另外两个安全项目构成完整三层：</strong>cloudflare 做审计（事后查）、Claude-Red 做红队（事前攻）、OpenShell 做运行时（事中拦）。防守、进攻、隔离，同一天凑齐。",
            "<strong>本质是安全从倡议变成了可安装的组件：</strong>过去两年行业反复呼吁「要管住 agent」，今年的回答是一堆能 pip 安装、能写进 CI 的东西。话术退场，配置登场。"
        ],
        "tags": ["agent-runtime", "sandbox", "security", "rust", "nvidia"]
    },
    {
        "rank": 3,
        "owner": "php",
        "name": "php-src",
        "fullName": "php / php-src",
        "org": "PHP",
        "url": "https://github.com/php/php-src",
        "lang": "C",
        "langClass": "c",
        "stars": "41,622",
        "forks": "8,372",
        "starsToday": "716",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +716★ 首次登榜！4.16万★。PHP 解释器本体，一个 1995 年活到现在、撑起大半互联网的老项目。它出现在一张 AI 榜单上，本身就是今天最值得说的事。",
        "problems": [
            "<strong>老语言被默认当成遗留：</strong>新项目不选它，但存量系统还得靠它跑十年。",
            "<strong>性能与类型系统长期被诟病：</strong>每次版本升级都要在兼容和现代化之间找平衡。",
            "<strong>维护者比用户少得多：</strong>用的人多，愿意读 C 源码的人少。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/php/php-src.git</code></pre>",
            "按 README 用 C 工具链编译，或直接看各版本的 release 说明。",
            "关注 RFC 与变更日志，评估升级对现有项目的影响。"
        ],
        "insights": [
            "<strong>它挤进榜单，说明今天的热点很薄：</strong>全天只有 8 个席位，日增 716 就能排第三。榜单变短，往往是注意力从「新东西」转向「在跑的东西」。",
            "<strong>存量系统的重量开始回到视野：</strong>这一年所有人都在谈 agent 能写多少代码，却很少有人问这些代码最终跑在哪里。答案是大量仍在 PHP、Java 这类老栈上。",
            "<strong>本质是 AI 改造的对象是存量，不是空白：</strong>新写的代码只是增量，行业里 90% 的逻辑早就写完了。谁能安全地动这些老代码，谁才真的改变了生产。"
        ],
        "tags": ["php", "interpreter", "c", "legacy", "infrastructure"]
    },
    {
        "rank": 4,
        "owner": "anthropics",
        "name": "knowledge-work-plugins",
        "fullName": "anthropics / knowledge-work-plugins",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/knowledge-work-plugins",
        "lang": "Python",
        "langClass": "py",
        "stars": "32,458",
        "forks": "3,587",
        "starsToday": "635",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +635★！3.25万★ 第6次登榜（10 月 11 日 2.88万★，两周涨 3,628）。Anthropic 官方开源、面向知识工作者的插件库，主要装在 Claude Cowork 里用。方向很明确：把 Claude 从「陪你聊天」变成「在你的日常工作里干活」。",
        "problems": [
            "<strong>知识工作散落在工具里：</strong>邮件、文档、表格、会议纪要，Agent 一样都够不着。",
            "<strong>插件格式没标准：</strong>各家 Agent 的插件互不兼容，写一个只能给一个平台用。",
            "<strong>企业想用又不敢用：</strong>缺官方背书的插件，安全与合规没有底，落地时推不动。"
        ],
        "usage": [
            "从仓库取出需要的插件，装进 Claude Cowork。",
            "按具体场景（文档处理、研究、协作）挑对应插件。",
            "官方维护，跟 Claude 的版本一起更新。"
        ],
        "insights": [
            "<strong>第6次登榜，是少数横跨三个月的常客：</strong>它没有爆发过，但一直没掉队。官方插件库的价值不在热度，在于「默认就在那里」。",
            "<strong>今天它和一个安全审计技能同榜：</strong>一个把 agent 推进日常工作，一个把 agent 的产出管住。企业采购时这两样通常一起出现，前者负责说服老板，后者负责说服法务。",
            "<strong>本质是入口之争已经从模型转到插件目录：</strong>谁定义插件长什么样，谁就决定用户在哪儿调 agent。这条线不会上头条，但会决定最后谁收钱。"
        ],
        "tags": ["plugins", "anthropic", "knowledge-work", "claude", "productivity"]
    },
    {
        "rank": 5,
        "owner": "Renhuai123",
        "name": "ziwei-doushu",
        "fullName": "Renhuai123 / ziwei-doushu",
        "org": "Renhuai123",
        "url": "https://github.com/Renhuai123/ziwei-doushu",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "7,146",
        "forks": "1,457",
        "starsToday": "546",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +546★ 首登！7,146★。紫微斗数的开源排盘引擎：基于倪海厦《天纪》体系，包含完整排盘算法、四化系统、格局知识库和古籍原文数据。在一张被 agent 和安全工具占满的榜单上，它显得很突兀。",
        "problems": [
            "<strong>命理工具多为黑箱：</strong>排盘规则散在书里和口传里，各家说法还不一致。",
            "<strong>古籍是扫描件：</strong>原文难检索，术语与算法对不上号。",
            "<strong>排盘软件不开放：</strong>想按自己的理解改规则，改不动。"
        ],
        "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/Renhuai123/ziwei-doushu.git</code></pre>",
            "按 README 安装（TypeScript 项目），输入出生信息排盘。",
            "查阅内置的格局知识库与古籍原文，按四化系统推演。"
        ],
        "insights": [
            "<strong>它上榜的方式很现代：</strong>把口传的规则写成算法，把古籍整理成可检索的数据集，把判断依据挂成知识库。这套动作和技术文档的工程化没有区别。",
            "<strong>7,146 星不算多，但它说明一件事：</strong>榜单不只服务「用 AI 干活的人」，也服务「想在自己关心的领域里获得确定性的人」。命理是最古老的那类确定性需求。",
            "<strong>本质是知识工程正在往下沉：</strong>过去只有金融、医疗这类领域值得建知识库，现在连命理都在被结构化。工具的门槛降下来之后，被整理的领域会越来越多。"
        ],
        "tags": ["ziwei", "divination", "typescript", "knowledge-base", "open-source"]
    },
    {
        "rank": 6,
        "owner": "SnailSploit",
        "name": "Claude-Red",
        "fullName": "SnailSploit / Claude-Red",
        "org": "SnailSploit",
        "url": "https://github.com/SnailSploit/Claude-Red",
        "lang": "Python",
        "langClass": "py",
        "stars": "8,732",
        "forks": "1,119",
        "starsToday": "226",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +226★！8,732★ 第2次登榜（9 月中 5,751★，一个月涨了 52%）。面向 Claude 技能体系的进攻性安全技能库：每个技能都是一份结构化的 SKILL.md，把红队流程拆成模型能直接执行的步骤。",
        "problems": [
            "<strong>红队流程靠人记：</strong>侦察、枚举、提权、横向，步骤多且依赖经验。",
            "<strong>知识和工具脱节：</strong>方法论写在书里，命令散在笔记里。",
            "<strong>新人上手慢：</strong>没有标准化流程，练手成本高。"
        ],
        "usage": [
            "把技能目录装进支持 Claude 技能体系的工具。",
            "按目标阶段选择侦察、枚举或利用类技能。",
            "让 agent 按 SKILL.md 的步骤执行，并保留每一步的原始输出。"
        ],
        "insights": [
            "<strong>它和 cloudflare 的审计技能是一对：</strong>一个从防守侧验证，一个从进攻侧试探。同一天在榜说明企业开始两头都补，而不是只买一个「AI 安全」的标签。",
            "<strong>一个月涨 52%：</strong>安全技能库的增长通常滞后于攻防事件。它稳步上涨，说明用的人在做常规演练，而不是被某次事故临时推起来。",
            "<strong>本质是攻防知识在变成可执行的资产：</strong>过去红队的能力长在人身上，人走了能力就走了。写成技能之后，能力留在仓库里。"
        ],
        "tags": ["red-team", "security", "agent-skill", "python", "offensive-security"]
    },
    {
        "rank": 7,
        "owner": "OpenBMB",
        "name": "VoxCPM",
        "fullName": "OpenBMB / VoxCPM",
        "org": "清华 OpenBMB",
        "url": "https://github.com/OpenBMB/VoxCPM",
        "lang": "Python",
        "langClass": "py",
        "stars": "40,452",
        "forks": "4,596",
        "starsToday": "150",
        "count": 6,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +150★！4.05万★ 第6次登榜（6 月中 3.04万★，四个月涨了一万）。清华 OpenBMB 的 VoxCPM2：不用 tokenizer 的 TTS，支持多语言语音生成、音色设计和接近真人的克隆。",
        "problems": [
            "<strong>传统 TTS 链路太长：</strong>文本转 token、token 转声学特征、再转波形，每一步都会丢信息。",
            "<strong>多语言音色不统一：</strong>换一种语言，音色和韵律就变了。",
            "<strong>克隆不够像：</strong>少量样本克隆出来的声音，情绪和停顿经常不对。"
        ],
        "usage": [
            "按 README 安装（Python 项目，建议有 GPU）。",
            "用少量样本做音色设计或克隆。",
            "输入文本生成多语言语音，导出音频接进自己的流程。"
        ],
        "insights": [
            "<strong>第6次登榜，跨度四个月：</strong>语音模型的榜单寿命通常很短，能反复回来，说明它在被持续用于实际生产，而不只是被下载试听。",
            "<strong>「无 tokenizer」是它和主流方案的分界：</strong>少一层离散化，少一次信息损失。这类架构选择不会出现在宣传语里，但会体现在克隆的相似度上。",
            "<strong>本质是语音这条线正在被本地化重做：</strong>从 VoiceStudio 到 VoxCPM，本地跑、多语言、少量样本克隆，三个需求指向同一件事：声音要留在自己手里。"
        ],
        "tags": ["tts", "speech", "multilingual", "python", "voice-cloning"]
    },
    {
        "rank": 8,
        "owner": "nodejs",
        "name": "node",
        "fullName": "nodejs / node",
        "org": "Node.js",
        "url": "https://github.com/nodejs/node",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "123,025",
        "forks": "39,845",
        "starsToday": "66",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +66★ 首次登榜！12.30万★。Node.js 运行时本体。日增只有两位数，它挤进榜单靠的是今天只有 8 个席位——另一个老基础设施和它一起回来了。",
        "problems": [
            "<strong>运行时升级牵一发动全身：</strong>依赖树一动，整个项目都要回归测试。",
            "<strong>异步与内存问题难查：</strong>回调、Promise、事件循环，出问题时栈信息帮不上忙。",
            "<strong>生态碎片化：</strong>包管理器、构建工具、模块格式各有一套说法。"
        ],
        "usage": [
            "从官网或版本管理器安装 LTS 版本。",
            "用 npm / pnpm 管理依赖，锁版本后再升级。",
            "关注 release 说明里的破坏性变更，按计划迁移。"
        ],
        "insights": [
            "<strong>日增 66 星也能进榜：</strong>这句话本身就是今天的信息。榜单从常见的 12 到 13 条缩到 8 条，说明当天没有真正的新故事，注意力退回到「一直在跑的东西」上。",
            "<strong>它和 php-src 同一天出现不是巧合：</strong>两个老运行时一起回榜，通常对应同一件事——有一批新项目在起，或者有版本更新在推。它不需要热度，只需要被用到。",
            "<strong>本质是 AI 应用的下一层永远是老基础设施：</strong>再新的 agent，最后也要跑在某个运行时上。热点的寿命以周计，运行时的寿命以十年计。"
        ],
        "tags": ["nodejs", "runtime", "javascript", "infrastructure", "open-source"]
    }
]

# 按日增降序规整编号（平铺渲染，全部新面孔）
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

today_projects = sorted(today_projects, key=lambda p: -_today(p))
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels for the real gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = f'{gap_days}天前'
    elif label == '昨天':
        day['label'] = f'{gap_days+1}天前'
    elif label == '前天':
        day['label'] = f'{gap_days+2}天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + gap_days}天前'

new_day = {
    "date": "2026-10-24",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-10-24'
data['topic'] = '🔥 <strong>Agent 安全凑齐三层：审计、红队、运行时</strong> —— cloudflare/security-audit-skill（+2,716★）第6次登榜，日增再创新高，4.28万★，一周前才 1.75万★，多阶段审计、结论独立验证、机器可读；SnailSploit/Claude-Red（+226★）第2次，面向 Claude 技能体系的进攻性安全技能库，一个月涨 52%；NVIDIA/OpenShell（+1,119★）第2次，1.91万★，比首登时接近翻倍，给自主 agent 的安全私有运行时，靠内核拦截加形式化验证执行策略。三件东西分别是事后查、事前攻、事中拦，同一天在榜。anthropics/knowledge-work-plugins（+635★）第6次，横跨三个月的常客。老基础设施也回来了：php/php-src（+716★）首登，nodejs/node（+66★）首登——榜单今天只有 8 个席位，日增 66 星都能排进末位，说明注意力从新故事退回到在跑的系统。两个意外：OpenBMB/VoxCPM（+150★）第6次，无 tokenizer 的多语言 TTS，四个月涨一万星；Renhuai123/ziwei-doushu（+546★）首登，基于倪海厦《天纪》体系的紫微斗数开源排盘引擎，把口传规则写成算法、把古籍整理成可检索数据集。今日主线：安全从倡议变成可安装的组件，而热点变薄的时候，地基重新显形。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
assert nf <= 6 or st == 0, f"栏位超限: 新面孔 {nf} / 连登 {st}"
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★ count={p['count']}")
