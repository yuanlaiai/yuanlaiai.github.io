#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-27 (3-day gap -> 平铺，全部新面孔，9 席)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 27)
gap_days = (today - last).days  # 3
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    {
        "rank": 1,
        "owner": "paperclipai",
        "name": "paperclip",
        "fullName": "paperclipai / paperclip",
        "org": "Paperclip",
        "url": "https://github.com/paperclipai/paperclip",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "87,914",
        "forks": "15,486",
        "starsToday": "2,608",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,608★ 登顶！8.8 万星：把 AI Agent 当员工来管的应用。官方那句话很直白——「如果 OpenClaw 是员工，Paperclip 就是公司」：定义目标、招团队（CEO / CTO / 工程师 / 设计 / 市场，任何厂商的 Agent 都行）、批预算、看仪表盘。看着像任务管理器，底下是组织架构图、预算、治理、目标对齐与 Agent 协调。支持 OpenClaw、Claude Code、Codex、Cursor、Bash、HTTP——「只要能收心跳就能入职」。",
        "problems": [
            "<strong>Agent 越多越乱：</strong>开着二十个 Claude Code 终端，没人说得清谁在做什么、做到哪一步。",
            "<strong>目标对不齐：</strong>每个 Agent 都能干活，但没人把它们指向同一个业务目标。",
            "<strong>花钱没数：</strong>没有预算与成本视图，跑飞的账单只能在月底发现。"
        ],
        "usage": [
            "起 Node.js 服务与 React 前端：<pre><code>git clone https://github.com/paperclipai/paperclip.git</code></pre>",
            "定义业务目标，招入你自己的 Agent（任意厂商）。",
            "审批策略、设定预算后开跑，在仪表盘上跟踪工作与花费。"
        ],
        "insights": [
            "<strong>它把编排对象从「任务」换成了「组织」：</strong>以往的工具管的是任务队列与上下文，Paperclip 管的是岗位、预算与治理——这是「Agent 团队」第一次有了组织架构图。",
            "<strong>「管业务目标，不管 PR」这句是分水岭：</strong>开发者工具的粒度是提交与合并请求，管理层工具的粒度是收入与目标——Agent 一旦被当员工，衡量的单位就换成了业务结果。",
            "<strong>本质是管理层的自动化：</strong>过去十年自动化的是执行（写代码、做表、回邮件），现在开始自动化分配与问责——谁定目标、谁批预算、谁背结果，这套流程正在被搬进软件。"
        ],
        "tags": ["ai-agents", "orchestration", "autonomous-org", "typescript", "openclaw"]
    },
    {
        "rank": 2,
        "owner": "vectorize-io",
        "name": "hindsight",
        "fullName": "vectorize-io / hindsight",
        "org": "Vectorize",
        "url": "https://github.com/vectorize-io/hindsight",
        "lang": "Python",
        "langClass": "py",
        "stars": "33,749",
        "forks": "3,977",
        "starsToday": "2,147",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +2,147★！三天前上榜时 26,963★ → 33,749★（三天 +6,786★）。会学习的 Agent 记忆系统：官方说法是「多数记忆系统只是回放对话历史，Hindsight 要做的是让 Agent 真的学会」，在 LongMemEval 长期记忆基准上拿到最准成绩，自带 arXiv 论文、Python / JS 客户端、MCP 服务器与嵌入式模式（不跑服务端也能用），另有云托管版本。",
        "problems": [
            "<strong>长对话记不住重点：</strong>上下文一长，早期关键信息被稀释，Agent 反复问已经说过的事。",
            "<strong>RAG 只解决「找得到」：</strong>向量检索能捞出片段，不会把经验沉淀成判断。",
            "<strong>记忆散落各处：</strong>对话历史、工具结果、项目约定各存一份，换个 Agent 就全丢。"
        ],
        "usage": [
            "起服务：<pre><code>pip install hindsight-api</code></pre>，或在 Python 里直接用嵌入式模式。",
            "接客户端：<pre><code>pip install hindsight-client</code></pre> 或 npm 包，两行代码包住 LLM 调用即可接入。",
            "给 Agent 挂 MCP 服务器，或用官方的 coding agent 集成。"
        ],
        "insights": [
            "<strong>三天涨了近 7,000 星，曲线比发布当天更陡：</strong>这不是发布曝光，而是被反复引用后的复利——说明「记忆」被当成了 Agent 落地的必答题。",
            "<strong>retain / recall / reflect 三个操作是它的骨架：</strong>把经历压缩成观察与心智模型，而不是把原文再喂一遍——记忆系统的竞争点从「存得下」变成「压得准」。",
            "<strong>本质是上下文经济的拐点：</strong>上下文窗口再大也按 token 计费，而「学会」是压缩——谁能把经历压成更少 token 而不丢判断，谁就同时赢了能力与成本。"
        ],
        "tags": ["agent-memory", "ai-agents", "longMemEval", "mcp", "python"]
    },
    {
        "rank": 3,
        "owner": "dream-num",
        "name": "univer",
        "fullName": "dream-num / univer",
        "org": "dream-num",
        "url": "https://github.com/dream-num/univer",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "19,723",
        "forks": "1,664",
        "starsToday": "849",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +849★！三天前 17,123★ → 19,723★（三天 +2,600★）。2022 年建仓的开源 Office SDK，简介是「The Office Harness for AI Agents」：表格、文档、幻灯片、画布、关系表、PDF 一套运行时， Canvas 渲染 + 公式引擎 + 插件架构 + 浏览器与 Node 同构的 Facade API。",
        "problems": [
            "<strong>Office 能力嵌不进产品：</strong>想在自己应用里放一张能算的表格，商业组件贵、开源组件弱。",
            "<strong>模型读不懂文件结构：</strong>Agent 能写代码，却常常读不出表格里的公式依赖与文档层级。",
            "<strong>两端渲染不一致：</strong>浏览器算一遍、服务端再算一遍，结果还对不上。"
        ],
        "usage": [
            "安装：<pre><code>npm install @univerjs/presets</code></pre>",
            "用 Facade API 在浏览器或 Node 端创建表格、文档、幻灯片实例。",
            "按需要挂插件扩展公式、协同或自定义渲染。"
        ],
        "insights": [
            "<strong>改个定位换来一周的持续增长：</strong>从「开源 Office」到「Agent 的办公桌」，星级从 15,352 涨到 19,723——同一份代码在 Agent 叙事里的估值完全不同。",
            "<strong>它与 Paperclip 是同一件事的两端：</strong>一个给 Agent 组织开会用的工作空间，一个给 Agent 改表格文档的办公桌——「Agent 在哪里办公」正在变成具体产品。",
            "<strong>本质是资产重定价：</strong>技术周期切换时，最先受益的往往不是新项目，而是早就把事做好、只差一个说法的老项目。"
        ],
        "tags": ["office-sdk", "spreadsheet", "typescript", "ai-agents", "chinese"]
    },
    {
        "rank": 4,
        "owner": "rohitg00",
        "name": "ai-engineering-from-scratch",
        "fullName": "rohitg00 / ai-engineering-from-scratch",
        "org": "rohitg00",
        "url": "https://github.com/rohitg00/ai-engineering-from-scratch",
        "lang": "Python",
        "langClass": "py",
        "stars": "58,551",
        "forks": "10,153",
        "starsToday": "827",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +827★！三天前 55,943★ → 58,551★（三天 +2,608★）。5.8 万星的手写课程：523 节课、20 个阶段、约 342 小时，覆盖 Python / TypeScript / Rust / Julia；每节课都产出一个可复用产物（提示词、技能、Agent、MCP 服务器）。作者引用数据是「84% 的学生已经在用 AI 工具，只有 18% 觉得自己能专业地用」。",
        "problems": [
            "<strong>会用工具不等于会做系统：</strong>会写提示词的人很多，能从零搭出检索、评测、部署链路的很少。",
            "<strong>教程只讲不敢动手：</strong>大部分课程停在概念与 API 调用，不碰底层实现。",
            "<strong>学完没有作品：</strong>刷完课手上空空，面试与项目都拿不出东西。"
        ],
        "usage": [
            "挑一个目标（从零打基础 / 直接做 Agent / 专攻某个方向）而不是从头刷 523 课。",
            "按阶段推进，每节课跟着实现并留下可复用产物。",
            "支持十二种语言的落地页，中文读者可直接看简体中文入口。"
        ],
        "insights": [
            "<strong>它在三天里的持续涨幅比首登当天还稳：</strong>课程类项目的热度通常一次爆发就结束，这轮是三天连续上行——说明供给端（岗位需求）没变过。",
            "<strong>它与 reverse-skill 构成今天的两端：</strong>一个教人从零造系统，一个把行业经验（逆向/渗透）封装给 Agent——知识正在同时流向人和机器。",
            "<strong>本质是技能缺口的定价：</strong>当「AI 工程师」成为岗位，培训市场先于教育体系反应——课程结构是被招聘需求倒逼出来的。"
        ],
        "tags": ["education", "ai-engineering", "course", "llm", "mcp"]
    },
    {
        "rank": 5,
        "owner": "openbao",
        "name": "openbao",
        "fullName": "openbao / openbao",
        "org": "OpenBao",
        "url": "https://github.com/openbao/openbao",
        "lang": "Go",
        "langClass": "go",
        "stars": "8,059",
        "forks": "591",
        "starsToday": "364",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +364★ 首登！由 OpenSSF 托管、MPL-2.0 许可的机密管理系统：密码、证书、密钥的统一存储与分发。它是 HashiCorp Vault 改成 BUSL 许可后的社区开源分支，安全披露走 OpenSSF 邮件列表，命名空间、PKCS#11、可扩展性都有专门工作组在推进。",
        "problems": [
            "<strong>密钥散在人和机器之间：</strong>配置、CI、Agent 配置各存一份，轮换一次要改几十处。",
            "<strong>许可变更逼你搬家：</strong>用惯的开源工具改了许可证，商业使用受限，自建分支又不敢信。",
            "<strong>Agent 需要凭证但没人敢给：</strong>自动化调用越来越多，凭证该给谁、给多久、怎么吊销都没规矩。"
        ],
        "usage": [
            "克隆构建：<pre><code>git clone https://github.com/openbao/openbao.git</code></pre>",
            "按官方文档部署服务端，或从 Vault 迁移（接口兼容是它的主要卖点）。",
            "用命名空间隔离团队与租户，接 PKCS#11 做硬件密钥托管。"
        ],
        "insights": [
            "<strong>它与上周的 treg 是同一条线：</strong>一个把团队密钥收回服务器、Agent 只拿 token，一个把机密管理本身开源——Agent 时代密钥的重要性和暴露面同时在涨。",
            "<strong>治理结构比功能列表更值得看：</strong>挂在 OpenSSF 下、安全披露走独立邮件列表、三个工作组并行——这是「许可争议之后，社区自己接住关键基础设施」的完整样本。",
            "<strong>本质是关键基础设施的接管：</strong>商业公司收紧许可后，社区能真正接管的项目其实不多，因为机密管理需要长期信任——谁能提供这份信任，谁就拿到了这一层的长期位置。"
        ],
        "tags": ["secrets-management", "vault", "openssf", "security", "golang"]
    },
    {
        "rank": 6,
        "owner": "zhaoxuya520",
        "name": "reverse-skill",
        "fullName": "zhaoxuya520 / reverse-skill",
        "org": "zhaoxuya520",
        "url": "https://github.com/zhaoxuya520/reverse-skill",
        "lang": "PowerShell",
        "langClass": "powershell",
        "stars": "38,131",
        "forks": "5,290",
        "starsToday": "361",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +361★！3.8 万星的中文项目「逆向技能路由包」：当 Agent 遇到 APK、二进制、前端 JS 加密、CTF 题目或授权渗透目标时，它负责把任务路由到正确的方法论、检查可用工具、执行可重复流程，而不是瞎猜命令。现有 44 条路由规则、175 个回归用例、45 个技能模块，Windows 与 Ubuntu 双平台 CI，客户端中立（Claude Code / Codex / Cursor / Cline 等）。",
        "problems": [
            "<strong>Agent 不知道用哪个工具：</strong>jadx、apktool、Frida、IDA、BurpSuite 各管一段，选错了整条链路白跑。",
            "<strong>每类任务都是一套剧本：</strong>APK、ELF、JS、PCAP、CTF 的方法完全不同，通用提示词覆盖不了。",
            "<strong>踩过的坑不再复用：</strong>同类错误在团队和模型之间反复出现，经验没有沉淀成资产。"
        ],
        "usage": [
            "把仓库克隆到本地：<pre><code>git clone https://github.com/zhaoxuya520/reverse-skill.git</code></pre>",
            "按 README_AI.md 的指引把路由规则注册进你的 Agent 客户端。",
            "任务进入后先走 case-init 与 scope.md 确认授权与网络画像，再进入对应场景技能执行。"
        ],
        "insights": [
            "<strong>它把「授权」写进了流程的第一步：</strong>未确认授权与网络画像就不对目标执行动作——安全工具过去常靠使用者自律，这里把它做成了硬前提。",
            "<strong>技能包开始分行业了：</strong>上周是通用开发方法论（superpowers），这周是逆向与渗透——「教 Agent 怎么干活」正在从通用技巧拆成专业领域。",
            "<strong>本质是经验的可执行化：</strong>老手知道遇到混淆 JS 该先看什么、报错意味着什么，这些判断过去只能靠带徒弟；现在被写成规则与回归用例，可以被机器复用和验证。"
        ],
        "tags": ["reverse-engineering", "pentest", "agent-skills", "chinese", "security"]
    },
    {
        "rank": 7,
        "owner": "NVIDIA",
        "name": "Model-Optimizer",
        "fullName": "NVIDIA / Model-Optimizer",
        "org": "NVIDIA",
        "url": "https://github.com/NVIDIA/Model-Optimizer",
        "lang": "Python",
        "langClass": "py",
        "stars": "4,824",
        "forks": "673",
        "starsToday": "357",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +357★ 首登！NVIDIA 的模型优化工具箱（ModelOpt）：量化、剪枝、神经架构搜索、蒸馏、投机解码、稀疏化这些 SOTA 技术收在一个库里，输入 Hugging Face / PyTorch / ONNX 模型，输出优化后的量化权重，直接对接 TensorRT-LLM、TensorRT、vLLM 等部署框架做推理加速，并与 Megatron-Bridge、Megatron-LM、Hugging Face Accelerate 集成。",
        "problems": [
            "<strong>推理成本压不下来：</strong>模型越大越准，但延迟与显存直接决定能不能上线。",
            "<strong>优化技术各写一遍：</strong>量化、蒸馏、剪枝分散在不同脚本里，交叉组合容易出错。",
            "<strong>优化完部署不了：</strong>实验室里改好的模型，落到推理框架上格式不认。"
        ],
        "usage": [
            "安装：<pre><code>pip install nvidia-modelopt</code></pre>",
            "用 Python API 组合量化、剪枝、蒸馏等技术并导出优化后的权重。",
            "把产物交给 TensorRT-LLM / vLLM 部署，或走 Megatron 与 HF Accelerate 的集成链路。"
        ],
        "insights": [
            "<strong>它出现的位置说明竞争点回到了成本：</strong>不是更大的模型，而是「同样的模型跑得更便宜」——量化与投机解码是当下最直接的降本手段。",
            "<strong>优化库与推理框架的绑定是护城河：</strong>ModelOpt 的输入输出都对着自家部署栈，用起来越顺，迁移成本越高——工具链的锁定往往发生在这一步。",
            "<strong>本质是算力的再分配：</strong>当芯片供给紧张、价格居高不下，能省下显存与带宽的软件就会直接变成利润——这也是为什么优化库值得被拿出来单独开源。"
        ],
        "tags": ["quantization", "inference-optimization", "tensorrt", "vllm", "nvidia"]
    },
    {
        "rank": 8,
        "owner": "block",
        "name": "buzz",
        "fullName": "block / buzz",
        "org": "Block",
        "url": "https://github.com/block/buzz",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "34,889",
        "forks": "4,598",
        "starsToday": "339",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +339★ 首登！Block 开源的「蜂群思维通讯平台」：一个可自托管的工作空间，人和 Agent 待在同一批房间里。底层是 Nostr relay——每条消息、表情回应、工作流步骤、评审批注、git 事件都是同一条日志里的签名事件，人和程序共用同一套身份模型与审计轨迹。Agent 在里面能开仓库、发补丁、评审代码、跑工作流、编排其他 Agent、进语音讨论、建频道。",
        "problems": [
            "<strong>人和 Agent 各用一套工具：</strong>Agent 在终端、人在聊天软件，协作全靠人肉搬运上下文。",
            "<strong>Agent 的动没有审计：</strong>它改了什么、谁批准的、什么时候做的，散落在各处日志里。",
            "<strong>平台归别人所有：</strong>团队协作内容存在厂商服务器上，规则、留存、导出都不由自己。"
        ],
        "usage": [
            "按文档部署自托管的 relay（单 relay 即一个社区）。",
            "把团队与 Agent 一起接进同一个 URL 下的工作空间。",
            "让 Agent 用与人类相同的身份参与评审、工作流与代码讨论，所有事件留在同一条事件日志里。"
        ],
        "insights": [
            "<strong>「同一套审计轨迹」才是它真正的卖点：</strong>Agent 参与协作后最麻烦的是追责与复现，Nostr 的签名事件日志让「谁在什么时候做了什么」不再依赖平台方的口头保证。",
            "<strong>它和 Paperclip 从两端解决同一个问题：</strong>Paperclip 给 Agent 排组织架构，Buzz 给人和 Agent 同一间办公室——一个自上而下管理，一个平铺协作。",
            "<strong>本质是协作形态的重写：</strong>当成员里既有同事、也有自动化程序，协作平台的第一性要求就变成了「身份与事件可验证」——人类习惯的平台默认信任参与者，Agent 进来的那一刻，这条默认就不成立了。"
        ],
        "tags": ["nostr", "collaboration", "self-hosted", "rust", "ai-agents"]
    },
    {
        "rank": 9,
        "owner": "mobile-next",
        "name": "mobile-mcp",
        "fullName": "mobile-next / mobile-mcp",
        "org": "Mobile Next",
        "url": "https://github.com/mobile-next/mobile-mcp",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "7,499",
        "forks": "650",
        "starsToday": "168",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +168★ 首登！把手机交给 Agent 的 MCP 服务器：iOS 与 Android 的模拟器、仿真器、真机统一成一个平台无关接口，Agent 通过结构化无障碍快照或基于截图的坐标点击来操作原生 App。支持 Claude Code、Codex、Gemini、Copilot、Antigravity 等 MCP 客户端，也能接 Mobile Next Cloud 直接在云端真机上跑。",
        "problems": [
            "<strong>移动端自动化要两套知识：</strong>iOS 与 Android 的驱动、版本、坐标体系完全不同，团队很难兼顾。",
            "<strong>手工点测耗时：</strong>多步用户旅程、表单填写、数据采集全靠人盯着模拟器点。",
            "<strong>真机成本高：</strong>本地设备农场贵，维护系统镜像与设备池更是长期负担。"
        ],
        "usage": [
            "在 MCP 客户端里配置该服务器，连上本机的模拟器或仿真器。",
            "让 Agent 用无障碍快照读取界面结构，或按截图坐标点击。",
            "需要真实机型时切到云端设备池，工具接口不变。"
        ],
        "insights": [
            "<strong>移动端是 Agent 最后一块没被吃下的屏幕：</strong>桌面与浏览器自动化已经很成熟，手机因为封闭与设备成本一直是空白——把模拟器与真机统一成一个接口，等于给 Agent 开了新的一屏。",
            "<strong>无障碍快照这个细节值得注意：</strong>用系统级的无障碍树读界面，比纯截图识别稳得多，也顺带把「为残障用户做的结构」变成了自动化基础设施。",
            "<strong>本质是操作面的最后一公里：</strong>Agent 能写代码、能改表格、能开会，但只要还有大量业务只存在于手机 App 里，最后那一步就必须有人——这类工具正在把这个「必须」删掉。"
        ],
        "tags": ["mcp", "mobile-automation", "ios", "android", "testing"]
    }
]

# 规整顺序与编号：按日增降序（3 天间隔，全部新面孔平铺）
def _today(p):
    return int(str(p['starsToday']).replace(',', ''))

today_projects = sorted(today_projects, key=lambda p: -_today(p))
for i, p in enumerate(today_projects, 1):
    p['rank'] = i

# Shift labels by real gap (3 days)
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
    "date": "2026-09-27",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-27'
data['topic'] = '🔥 <strong>Agent 从「工具」升级成「组织」+ 行业技能包开始分家</strong> —— paperclipai/paperclip（+2,608★）登顶：8.8 万星，把 Agent 当员工管，官方说法是「如果 OpenClaw 是员工，Paperclip 就是公司」——组织架构、预算、治理、目标对齐全在一个仪表盘里，支持任何厂商的 Agent 入职。block/buzz（+339★）34.9K★：Block 开源的蜂群平台，人和 Agent 待在同一批房间，底层是 Nostr relay，消息与评审都是同一条日志里的签名事件，共用一套身份与审计轨迹。zhaoxuya520/reverse-skill（+361★）3.8 万星中文项目：逆向/授权渗透的技能路由包，44 条路由规则、175 个回归用例、45 个技能模块，未确认授权就不动目标。openbao/openbao（+364★）：Vault 改许可后的社区开源分支，挂在 OpenSSF 下，机密与证书管理交付给社区接住。NVIDIA/Model-Optimizer（+357★）把量化、剪枝、NAS、投机解码收进一个库，直接对接 TensorRT-LLM 与 vLLM。mobile-next/mobile-mcp（+168★）把 iOS/Android 真机交给 Agent 操作。连续三天上行的三个老面孔：vectorize-io/hindsight（+2,147★，26,963★ → 33,749★，三天 +6,786★）、dream-num/univer（+849★，三天 +2,600★）、rohitg00/ai-engineering-from-scratch（+827★，三天 +2,608★）。今日三条主线：一、编排对象从任务变成组织——Paperclip 排组织架构、Buzz 给人和 Agent 同一间办公室；二、技能包开始分行业，通用方法论之后是逆向渗透这类专业领域；三、控制权继续往回收——机密管理开源分支、自托管协作平台、本地记忆，都是同一件事。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:4]]}")

assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"
nf = sum(1 for p in days[0]['projects'] if p['badge'] == '新面孔')
st = sum(1 for p in days[0]['projects'] if p['badge'] == '连登')
print(f"新面孔 {nf} / 连登 {st}（gap=3，平铺）")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['owner']}/{p['name']}: {p['stars']}★ +{p['starsToday']}★")
