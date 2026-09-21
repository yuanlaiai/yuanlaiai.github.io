#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-21 (1-day gap, 双栏：新面孔 6 + 连登 4)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 21)
gap_days = (today - last).days  # 1
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ══ 新面孔（未出现在 09-20 榜上）══
    {
        "rank": 1,
        "owner": "Open-Dev-Society",
        "name": "OpenStock",
        "fullName": "Open-Dev-Society / OpenStock",
        "org": "Open Dev Society",
        "url": "https://github.com/Open-Dev-Society/OpenStock",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "17,344",
        "forks": "2,190",
        "starsToday": "843",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +843★（16,496★ → 17,344★）！开源版行情平台——实时价格、个性化提醒、公司洞察，「为所有人而建，永远免费」。",
        "problems": [
            "<strong>行情被订阅锁死：</strong>实时报价与提醒动辄每月几十上百美元。",
            "<strong>免费工具功能残缺：</strong>要么延迟严重，要么广告不断。",
            "<strong>数据无法自留：</strong>关注列表与提醒都留在别人服务器上。"
        ],
        "usage": [
            "克隆部署：<pre><code>git clone https://github.com/Open-Dev-Society/OpenStock.git</code></pre>",
            "配置行情数据源与自选股。",
            "设置价格与事件提醒，长期数据留在自己的数据库。"
        ],
        "insights": [
            "<strong>连登且日增反超首登：</strong>昨天 +752★、今天 +843★——教学型开源项目的热度没有衰减，说明它踩中的是「数据订阅制」这个真痛点。",
            "<strong>与 NOMAD 同日上榜构成一条线：</strong>一个是金融数据自持，一个是知识库离线自持——「把关键数据搬回自己硬盘」今天占了两个席位。",
            "<strong>本质是订阅制的裂缝：</strong>当开源能复制「数据展示 + 提醒」这类表层功能，付费平台的溢价只能靠更低延迟与合规资质撑着。"
        ],
        "tags": ["stock-market", "open-source", "self-hosted", "typescript", "education"]
    },
    {
        "rank": 2,
        "owner": "ruanyf",
        "name": "weekly",
        "fullName": "ruanyf / weekly",
        "org": "阮一峰",
        "url": "https://github.com/ruanyf/weekly",
        "lang": "Markdown",
        "langClass": "md",
        "stars": "103,819",
        "forks": "5,850",
        "starsToday": "621",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +621★！103.8K★ 首登！阮一峰的《科技爱好者周刊》——每周五发布，记录值得分享的科技内容，已连载到第 413 期（最新一期标题：「再见了，React Native」）。",
        "problems": [
            "<strong>信息噪音太大：</strong>每天刷不完的资讯，真正值得看的被淹没。",
            "<strong>中文技术资讯缺乏筛选：</strong>英文源一手、中文源多是二手转译。",
            "<strong>好内容难沉淀：</strong>读完就忘，没有系统归档。"
        ],
        "usage": [
            "阅读最新一期：<pre><code>https://github.com/ruanyf/weekly</code></pre>",
            "投稿或浏览历史：issue 区按周归档，可检索 413 期。",
            "顺带看《谁在招人》招聘帖（免费发布岗位）。"
        ],
        "insights": [
            "<strong>十万里程碑式的「非 AI 项目」：</strong>在 AI 项目霸榜的环境里，一份持续八年、每周五准时更新的中文技术周刊拿到 10.3 万星——说明「可靠的筛选」本身就是最稀缺的产品。",
            "<strong>413 期意味着什么：</strong>按每周一期算，这是超过八年的稳定输出。在一个平均项目寿命不到两年的生态里，持续性比爆发力更罕见。",
            "<strong>本质是人类编辑的价值证明：</strong>在人人可以用模型自动生成摘要的时代，一个由人手工挑选、有品味、有偏见、敢取舍的周刊反而更值钱——信息过载的解药从来不是更多信息，而是可信的删减。"
        ],
        "tags": ["newsletter", "chinese", "curation", "markdown", "weekly"]
    },
    {
        "rank": 3,
        "owner": "trycua",
        "name": "cua",
        "fullName": "trycua / cua",
        "org": "Cua",
        "url": "https://github.com/trycua/cua",
        "lang": "HTML",
        "langClass": "html",
        "stars": "25,516",
        "forks": "1,760",
        "starsToday": "609",
        "count": 2,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +609★（24,914★ → 25,516★）！「给 AI Agent 一台能用的电脑」——开源桌面自动化驱动、隔离云桌面、本地 macOS 虚拟机、专职决策模型与评测基准。",
        "problems": [
            "<strong>Agent 没有身体：</strong>模型能思考，但没有可安全操作的执行环境。",
            "<strong>在真机上操作危险：</strong>一次误操作可能不可逆。",
            "<strong>跨系统难统一：</strong>macOS / Linux / Windows 各一套方案。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/trycua/cua.git</code></pre>",
            "在本地 macOS 虚拟机或隔离云桌面里运行 Agent。",
            "接上基准评估 computer-use 能力，或做训练数据生成。"
        ],
        "insights": [
            "<strong>连登且热度居高：</strong>两天合计新增超过 1,600★，是本周「给 Agent 造身体」这条线里最稳的项目。",
            "<strong>与 agent-native、Codex-X 同日上榜：</strong>一个给 Agent 环境、一个给构建框架、一个给管理界面——Agent 的工具链正在从「模型侧」全面转向「工程侧」。",
            "<strong>本质是可丢弃的执行权：</strong>Agent 越能干，越需要能随时重装的活动范围——提供沙箱的人，掌握着 Agent 落地最上层的闸门。"
        ],
        "tags": ["computer-use", "agent", "virtualization", "sandbox", "benchmark"]
    },
    {
        "rank": 4,
        "owner": "BuilderIO",
        "name": "agent-native",
        "fullName": "BuilderIO / agent-native",
        "org": "Builder.io",
        "url": "https://github.com/BuilderIO/agent-native",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "5,637",
        "forks": "327",
        "starsToday": "607",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +607★ 首登！Builder.io 的「agent 原生应用」框架——不再把 Agent 当成应用里的一个功能，而是假设 Agent 就是应用的运行时，让 React 应用与 Agent 共享同一套状态。",
        "problems": [
            "<strong>Agent 是后加的补丁：</strong>现有应用把 AI 当插件塞进去，状态与权限处处打架。",
            "<strong>前后端割裂：</strong>Agent 想要的数据在前端，能改的数据在后端。",
            "<strong>没有协作范式：</strong>人和 Agent 同时操作同一个界面时，谁改了什么无从追溯。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/BuilderIO/agent-native.git</code></pre>",
            "用 React 编写界面，把状态暴露给 Agent。",
            "让人与 Agent 在同一份状态上协作，操作可追溯。"
        ],
        "insights": [
            "<strong>「agent-native」这个词本身就是路线宣言：</strong>如同当年 mobile-first、cloud-native 一样，它主张的不是「支持 Agent」，而是「以 Agent 为前提重新设计」——Builder.io 把赌注押在了应用架构的代际更替上。",
            "<strong>与 vercel-labs/json-render（前天上榜）正面竞争：</strong>Vercel 选择用组件白名单约束模型生成界面，Builder.io 选择让 Agent 直接持有应用状态——两条路线今天在同一张榜单上对撞。",
            "<strong>本质是前端框架的又一次重写：</strong>jQuery → React → 服务端渲染 → Agent 原生。每一次范式迁移的赢家，都是第一个假设「新常态已经发生」的框架。"
        ],
        "tags": ["agent-native", "react", "framework", "typescript", "frontend"]
    },
    {
        "rank": 5,
        "owner": "coder",
        "name": "coder",
        "fullName": "coder / coder",
        "org": "Coder",
        "url": "https://github.com/coder/coder",
        "lang": "Go",
        "langClass": "go",
        "stars": "16,286",
        "forks": "1,178",
        "starsToday": "461",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第三天，今日 +461★（15,345★ → 15,842★ → 16,286★）！自托管云开发环境——给开发者和他们的 AI Agent 提供安全、隔离、可复制的远程工作空间。",
        "problems": [
            "<strong>Agent 在本地跑危险：</strong>执行命令、装依赖等于交出密钥。",
            "<strong>环境不一致：</strong>「在我机器上能跑」被 Agent 放大。",
            "<strong>云端环境不自主：</strong>SaaS 方案托管源码与密钥。"
        ],
        "usage": [
            "自托管部署：<pre><code>https://coder.com/docs/install</code></pre>",
            "用模板定义开发环境与权限边界。",
            "让开发者与 AI Agent 在同一套受控环境里协作。"
        ],
        "insights": [
            "<strong>三天连登、日增稳定：</strong>与 cua 一起把「Agent 执行环境」变成了本周的常驻主题。",
            "<strong>与 financial-services（同榜）形成对照：</strong>一个是通用的隔离环境，一个是垂直行业的成套 Agent——基础设施与行业方案正在同时成熟。",
            "<strong>本质是权限模型的迁移：</strong>环境的第一用户从人变成 Agent 后，审计日志、成本归因与最小权限原则都要重做。"
        ],
        "tags": ["dev-environment", "self-hosted", "agent", "go", "remote"]
    },
    {
        "rank": 6,
        "owner": "anthropics",
        "name": "financial-services",
        "fullName": "anthropics / financial-services",
        "org": "Anthropic",
        "url": "https://github.com/anthropics/financial-services",
        "lang": "Python",
        "langClass": "py",
        "stars": "35,649",
        "forks": "5,270",
        "starsToday": "425",
        "count": 3,
        "badge": "连登",
        "description": "🔥 亮点 —— 连登第二天，今日 +425★（35,220★ → 35,649★）！Anthropic 官方的「Claude for Financial Services」——投行、股票研究、私募、财富管理的参考 Agent、技能与数据连接器，插件与 Managed Agents API 双形态交付。",
        "problems": [
            "<strong>金融场景不能瞎试：</strong>备忘录、估值模型有严格格式与合规要求。",
            "<strong>通用助手不懂行业流程：</strong>数据源、模板、审阅链路都是行业特有。",
            "<strong>自建成本高：</strong>提示词到连接器都要自己攒，且难验证。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/anthropics/financial-services.git</code></pre>",
            "装成 Claude Cowork 插件，或走 Managed Agents API 接入自己的流程引擎。",
            "按角色启用：投行、股票研究、私募、财富管理。"
        ],
        "insights": [
            "<strong>连续两天在榜且日增上行：</strong>昨天 +236★、今天 +425★——热度还在爬，说明「模型公司直接交付行业方案」的范式正在被开发者接受。",
            "<strong>与 agent-native 同榜：</strong>一边是通用框架（怎么构建 Agent 应用），一边是行业成品（金融怎么落地）——两端同时被推。",
            "<strong>本质是交付形态的选择权：</strong>同一套内容既能装成插件、也能走 API，等于把「跑在哪」交给客户决定——这是模型公司对咨询与集成商的正面挤压。"
        ],
        "tags": ["financial-services", "agents", "claude", "anthropic", "industry"]
    },
    # ══ 新面孔（续，按日增排序并入新面孔组）══
    {
        "rank": 7,
        "owner": "Crosstalk-Solutions",
        "name": "project-nomad",
        "fullName": "Crosstalk-Solutions / project-nomad",
        "org": "Crosstalk Solutions",
        "url": "https://github.com/Crosstalk-Solutions/project-nomad",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "37,624",
        "forks": "2,412",
        "starsToday": "360",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +360★！37.6K★ 首登！一台「永远不会下线」的知识服务器——维基百科、数千本书、课程与地图全部离线打包，可选配本地 AI，跑在你自己拥有的硬件上，不需要互联网。",
        "problems": [
            "<strong>知识依赖网络：</strong>断网、限网、涨价，都会让「查资料」变成奢侈品。",
            "<strong>云服务随时改规则：</strong>平台关停或条款变更，你的资料就没了。",
            "<strong>灾难与偏远场景无解：</strong>灾区、船上是知识服务的真空。"
        ],
        "usage": [
            "克隆部署：<pre><code>git clone https://github.com/Crosstalk-Solutions/project-nomad.git</code></pre>",
            "一次导入离线知识包（维基、书籍、课程、地图）。",
            "可选接入本地 AI 做检索与问答。"
        ],
        "insights": [
            "<strong>「离线优先」在 AI 时代反而更热：</strong>当模型与数据都在云端，能脱离网络运转的知识基础设施成了稀缺品——它与榜单上的 hister、rustfs、customers 自托管线是同一个母题。",
            "<strong>37.6K★ 的体量说明需求真实：</strong>这不是极客玩具，而是教育、救援、船上/野外工作者的实际工具。",
            "<strong>本质是知识的「主权备份」：</strong>文明级别的知识过去被托管在少数平台上，本地化打包等于给人类知识做一份离线副本——AI 越集中，这种分散就越有价值。"
        ],
        "tags": ["offline-first", "knowledge", "self-hosted", "education", "local-ai"]
    },
    {
        "rank": 8,
        "owner": "zhouxiaoka",
        "name": "autoclip",
        "fullName": "zhouxiaoka / autoclip",
        "org": "zhouxiaoka",
        "url": "https://github.com/zhouxiaoka/autoclip",
        "lang": "Python",
        "langClass": "py",
        "stars": "8,043",
        "forks": "1,021",
        "starsToday": "395",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +395★！8.0K★ 首登！中文项目 AutoClip：AI 视频智能切片系统——支持 YouTube / B 站视频下载、自动切片、智能合集生成，面向二创场景的一站式高光提取工具。",
        "problems": [
            "<strong>长视频剪不完：</strong>一场直播、一期播客要人工听完整段才能找出亮点。",
            "<strong>二创效率低：</strong>切片、起标题、做合集全是重复劳动。",
            "<strong>工具链割裂：</strong>下载、转码、切片、封面各用一个软件。"
        ],
        "usage": [
            "克隆部署：<pre><code>git clone https://github.com/zhouxiaoka/autoclip.git</code></pre>",
            "输入视频链接（YouTube / B 站）自动下载。",
            "AI 提取高光并切片，自动生成合集与标题。"
        ],
        "insights": [
            "<strong>中文开发者的实用主义：</strong>它解决的不是「AI 能做什么」，而是「二创团队每天要做什么」——这类工具在中文开源里出现频率明显更高。",
            "<strong>与 ruanyf/weekly 一起构成今天的中文主线：</strong>加上 Codex-X，今天 6 个新面孔里有 3 个来自中国开发者。",
            "<strong>本质是内容再生产的工业化：</strong>当原视频产量爆炸，真正的价值转移到「把内容重新切分并找到受众」这一层——剪辑师的工作内容正在从操作软件变成定义标准。"
        ],
        "tags": ["video-editing", "ai-video", "chinese", "python", "content-creation"]
    },
    {
        "rank": 9,
        "owner": "cloudflare",
        "name": "quiche",
        "fullName": "cloudflare / quiche",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/quiche",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "12,187",
        "forks": "1,087",
        "starsToday": "242",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +242★！12.2K★ 首登！Cloudflare 的 QUIC / HTTP/3 实现——用 Rust 写的高性能传输协议库，是 Cloudflare 边缘网络跑 HTTP/3 的底座，2018 年建仓的老基建今天被重新发现。",
        "problems": [
            "<strong>老协议瓶颈：</strong>TCP + TLS 的握手延迟在弱网下尤其明显。",
            "<strong>自研传输层太难：</strong>QUIC 状态机复杂，从零实现风险极高。",
            "<strong>语言选择纠结：</strong>C/C++ 有内存风险，高级语言又不够快。"
        ],
        "usage": [
            "作为库引入：<pre><code>cargo add quiche</code></pre>",
            "用低层 API 处理 QUIC 包与连接状态。",
            "自行提供 socket 与事件循环（或参考 Cloudflare 的示例）。"
        ],
        "insights": [
            "<strong>老基建被重新发现：</strong>2018 年建仓、常年低调的基础库突然登上趋势榜，通常意味着某个下游生态（如新一代 agent 通信或边缘运行时）开始大量依赖它。",
            "<strong>与 Cloudflare 的审计技能形成组合：</strong>同一家公司三天前靠安全技能霸榜，今天靠传输协议库上榜——「攻防 + 基建」的双线存在感。",
            "<strong>本质是 AI 时代被忽视的延迟战场：</strong>模型推理再快，网络握手与拥塞控制仍在决定端到端体验——这类项目的价值会随实时 Agent 的普及被重新定价。"
        ],
        "tags": ["quic", "http3", "rust", "networking", "cloudflare"]
    },
    {
        "rank": 10,
        "owner": "yynxxxxx",
        "name": "Codex-X",
        "fullName": "yynxxxxx / Codex-X",
        "org": "yynxxxxx",
        "url": "https://github.com/yynxxxxx/Codex-X",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "3,607",
        "forks": "198",
        "starsToday": "210",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +210★ 首登！中文项目 Codex-X：OpenAI Codex 桌面端 / CLI 的可视化管理工具——Provider 与 API 切换、会话同步、提示词注入、Skills / MCP 管理、TOML 配置全部搬进图形界面。",
        "problems": [
            "<strong>配置文件手改易错：</strong>TOML 里改错一个字段，Agent 行为就变了。",
            "<strong>多供应商切换麻烦：</strong>换 API 要手改环境变量与配置。",
            "<strong>会话与技能散落：</strong>历史会话、Skills、MCP 没有统一入口。"
        ],
        "usage": [
            "克隆构建：<pre><code>git clone https://github.com/yynxxxxx/Codex-X.git</code></pre>",
            "在图形界面里配置 Provider / API、Skills 与 MCP。",
            "用会话同步与提示词模板管理多项目工作流。"
        ],
        "insights": [
            "<strong>「给官方工具做外壳」是一门正经生意：</strong>Codex CLI 本身足够强，但配置体验是命令行的——中文开发者把这个缝隙做成了桌面应用，说明了工具链体验的缺口有多真实。",
            "<strong>与 Claude Code 的 AGENTS.md 争议遥相呼应：</strong>当配置文件成为竞争核心，围绕「配置怎么管」的第三方工具必然出现——这是标准之争的下游产业。",
            "<strong>本质是配置权的回收：</strong>谁掌握配置界面，谁就掌握了用户实际使用的模型与技能组合——界面即分发渠道。"
        ],
        "tags": ["codex", "developer-tools", "chinese", "rust", "tauri"]
    }
]

# 规整顺序与编号：新面孔在前（按日增降序），连登在后 —— 与 app.js 双栏渲染顺序一致
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

new_faces = sorted([p for p in today_projects if p['badge'] == '新面孔'], key=_today, )
new_faces = sorted(new_faces, key=lambda p: -_today(p))
streaks = sorted([p for p in today_projects if p['badge'] == '连登'], key=lambda p: -_today(p))
today_projects = new_faces + streaks
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels for 1-day gap (accurate offset: +1)
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
    "date": "2026-09-21",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-21'
data['topic'] = '🔥 <strong>阮一峰《科技爱好者周刊》10.3 万星登榜 + 中文项目一天占三席（周刊 / AutoClip / Codex-X）+ 离线知识服务器 NOMAD 3.7 万星 + Agent 原生应用框架 agent-native + Cloudflare QUIC 实现回归</strong> —— Open-Dev-Society/OpenStock（+843★）连登两日热度上行。ruanyf/weekly（+621★）103.8K★ 首登，连载 413 期。trycua/cua（+609★）给 Agent 造可丢弃的电脑连登。BuilderIO/agent-native（+607★）agent 原生应用框架首登。coder/coder（+461★）隔离开发环境三连登。anthropics/financial-services（+425★）35.6K★ 连登。Crosstalk-Solutions/project-nomad（+360★）37.6K★ 离线知识服务器首登。zhouxiaoka/autoclip（+395★）AI 视频切片首登。cloudflare/quiche（+242★）QUIC/HTTP3 实现回归。yynxxxxx/Codex-X（+210★）Codex 可视化管理首登。今日两条明线：一、中文开发者一天拿下 6 个新面孔中的 3 席（十年周刊、二创切片、官方工具外壳），都是「把成熟能力做成可用产品」的实用主义路线；二、自持与离线成为母题——NOMAD 把维基与书籍装进本地硬盘、OpenStock 把行情数据收回自己服务器、cua 与 coder 给 Agent 划出可丢弃的活动范围，数据与执行权正在同时从云端撤回本地。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:5]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
print(f"新面孔 {nf} / 连登 {st}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
