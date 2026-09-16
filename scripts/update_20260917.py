#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-09-17 (7-day gap, 无昨日榜→平铺结构)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 9, 17)
gap_days = (today - last).days  # 7
print(f"Last: {last}, Today: {today}, Gap: {gap_days}")

today_projects = [
    # ── 全部为新面孔（7天gap无昨日榜，含回归项目，触发平铺渲染）──
    {
        "rank": 1,
        "owner": "alibaba",
        "name": "open-code-review",
        "fullName": "alibaba / open-code-review",
        "org": "Alibaba",
        "url": "https://github.com/alibaba/open-code-review",
        "lang": "Go",
        "langClass": "go",
        "stars": "31,699",
        "forks": "2,251",
        "starsToday": "3,215",
        "count": 2,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +3,215★ 冲上日榜第一！31.7K★ 二次登榜，较 7 月底首登时翻倍还多！阿里官方开源的代码审查工具——确定性管线 + LLM Agent 混合架构，行级精确评论，内置 NPE / 线程安全 / XSS / SQL 注入规则集。",
        "problems": [
            "<strong>代码审查堵在人工环节：</strong>大厂每天几千个 PR，Reviewer 不够用，关键改动排到最后。",
            "<strong>纯 LLM 评审不可靠：</strong>幻觉、漏报、评论位置漂移，工程师不敢信。",
            "<strong>规则与模型两张皮：</strong>静态检查工具查不出语义问题，模型又抓不住确定的硬性缺陷。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/alibaba/open-code-review.git</code></pre>",
            "接入仓库与 CI，配置规则集与模型端点（兼容 OpenAI / Anthropic 协议）。",
            "在 PR 上直接获得行级评论与修复建议。"
        ],
        "insights": [
            "<strong>二次登榜即翻倍：</strong>7-28 首登 14,772★ → 今天 31,699★，一个半月翻倍——「确定性管线 + LLM」这种不性感的混合架构，反而比纯 Agent 更能落地。",
            "<strong>大厂自用工具的开源化：</strong>描述里那句「在阿里规模上久经考验」才是真正的卖点——它卖的是被几万个 PR 打磨过的规则集，而不是又一个 Agent 框架。",
            "<strong>本质是审查权的重新分配：</strong>当机审能覆盖确定的缺陷类型，人类 Reviewer 的时间就被挤向架构判断——代码质量的门槛正在从「谁看得多」变成「谁的规则库更全」。"
        ],
        "tags": ["code-review", "agent", "go", "alibaba", "static-analysis"]
    },
    {
        "rank": 2,
        "owner": "JustVugg",
        "name": "colibri",
        "fullName": "JustVugg / colibri",
        "org": "JustVugg",
        "url": "https://github.com/JustVugg/colibri",
        "lang": "C",
        "langClass": "c",
        "stars": "34,994",
        "forks": "3,672",
        "starsToday": "1,532",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,532★！35.0K★ 首登！纯 C、零依赖的推理引擎——把存储、内存、显存当成单一推理层级，在消费级硬件上跑 744B 到 2.8 万亿参数的 MoE 模型，专家权重直接从磁盘流式加载。",
        "problems": [
            "<strong>大模型与硬件断层：</strong>前沿 MoE 动辄千亿到万亿参数，个人设备根本装不下。",
            "<strong>显存是硬天花板：</strong>现有推理引擎默认模型必须完整驻留 VRAM 或 RAM。",
            "<strong>部署链条沉重：</strong>跑一个开源模型要装一整套 Python 生态与 CUDA 依赖。"
        ],
        "usage": [
            "下载发行版：<pre><code>https://github.com/JustVugg/colibri/releases</code></pre>",
            "把模型权重按层级放好，磁盘上的专家按需流式加载。",
            "已支持 GLM-5.2/5.3（744B）、GLM-5.3-Flash（321B 带视觉）、Inkling（975B）、Kimi K3 等九个家族。"
        ],
        "insights": [
            "<strong>纯 C 是刻意的减法：</strong>零引擎依赖意味着任何机器都能编译——它不跟推理框架比功能，只在「能不能跑起来」这件事上碾压。",
            "<strong>把内存层级当架构：</strong>磁盘当专家仓库、RAM 当缓存、VRAM 当热区，本质是把操作系统的虚拟内存思路搬到模型推理——这也是 DeepSeek 那套 KV 压缩的同一条思路。",
            "<strong>本质是「模型所有权」的普及：</strong>当 2.8T 模型能在消费级设备上跑起来，算力租用的必要性就被削弱——地缘与合规压力下，这条路线会越来越重要。"
        ],
        "tags": ["moe", "inference", "local-llm", "c", "streaming"]
    },
    {
        "rank": 3,
        "owner": "cloudflare",
        "name": "security-audit-skill",
        "fullName": "cloudflare / security-audit-skill",
        "org": "Cloudflare",
        "url": "https://github.com/cloudflare/security-audit-skill",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "7,054",
        "forks": "414",
        "starsToday": "1,249",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,249★！Cloudflare 官方开源的安全审计技能——把编码 Agent 变成审计员，六阶段流程（侦察→覆盖驱动狩猎→候选验证→结构化输出→独立记录核验→中立报告），是 Cloudflare 全网漏洞发现系统的源头版本。",
        "problems": [
            "<strong>安全审计靠人不靠流程：</strong>漏掉的攻击面没有账本，谁查过、谁没查过全凭记忆。",
            "<strong>模型报告不可信：</strong>Agent 报出的漏洞缺少独立验证，误报与幻觉并存。",
            "<strong>审计无法复现：</strong>缺少机器可读的产出，无法在团队间交接与比对。"
        ],
        "usage": [
            "把技能装进 Claude Code / Codex 等 Agent 的 skills 目录。",
            "让 Agent 按六阶段跑一遍：产出 architecture.md 与 coverage-ledger.json。",
            "每个候选漏洞交给独立的验证 Agent 去「证伪」，只留可确认项。"
        ],
        "insights": [
            "<strong>官方亲述的「源头版本」：</strong>README 明确说这是 Cloudflare 漏洞发现 harness 的起点——企业把内部系统的雏形开源出来当标准，是 2026 年最有效的技术品牌动作。",
            "<strong>关键设计是「让另一个 Agent 去证伪」：</strong>把审计的信任问题转化为交叉验证问题——单模型自证永远不可靠，隔离的验证者才是安全 Agent 的必需品。",
            "<strong>本质是把审计从能力变成流程：</strong>安全行业的稀缺从来不是聪明人，而是「不遗漏」的制度——覆盖账本（coverage ledger）就是这个制度在 Agent 时代的形态。"
        ],
        "tags": ["security", "agent-skills", "audit", "cloudflare", "javascript"]
    },
    {
        "rank": 4,
        "owner": "Tencent",
        "name": "WeKnora",
        "fullName": "Tencent / WeKnora",
        "org": "Tencent",
        "url": "https://github.com/Tencent/WeKnora",
        "lang": "Go",
        "langClass": "go",
        "stars": "25,235",
        "forks": "3,470",
        "starsToday": "1,201",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,201★！25.2K★ 首登！腾讯开源的 LLM 知识平台——把原始文档变成可查询的 RAG、自主推理 Agent，最后长成一个自维护的 Wiki，已配套官网、微信对话开放平台与 Chrome 扩展。",
        "problems": [
            "<strong>企业文档沉睡：</strong>PDF、Word、会议记录堆在网盘里，没人能问出答案。",
            "<strong>RAG 做完就烂：</strong>知识库上线后无人维护，几周就过期失真。",
            "<strong>知识不闭环：</strong>问答结果无法沉淀回知识库，同一个问题要反复检索。"
        ],
        "usage": [
            "部署：<pre><code>git clone https://github.com/Tencent/WeKnora.git</code></pre>",
            "导入原始文档，自动构建 RAG 索引与推理 Agent。",
            "开启自维护 Wiki：把新的问答结论写回知识库。"
        ],
        "insights": [
            "<strong>「自维护 Wiki」是最值得看的一步：</strong>它把 RAG 从「一次性检索」推进到「持续累积」——知识库不再是索引，而是会自己长大的文档。",
            "<strong>腾讯的落地路径：</strong>官网 + 微信对话开放平台 + Chrome 扩展 + Agent 技能四件套同时给出——国内大厂的 AI 开源开始直接对接自己的流量入口。",
            "<strong>本质是知识资产的所有权回归：</strong>当 RAG 能自己维护，企业内部的知识就不再依赖少数专家的记忆——这是组织记忆第一次可以被工程化保存。"
        ],
        "tags": ["rag", "knowledge-base", "agent", "go", "tencent"]
    },
    {
        "rank": 5,
        "owner": "abue-ammar",
        "name": "tinycast",
        "fullName": "abue-ammar / tinycast",
        "org": "abue-ammar",
        "url": "https://github.com/abue-ammar/tinycast",
        "lang": "Swift",
        "langClass": "swift",
        "stars": "5,555",
        "forks": "264",
        "starsToday": "1,136",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,136★！5.5K★ 首登！全原生 macOS 启动器：一个热键覆盖全天所有常用动作，启动、剪贴板历史、窗口操作全在一个框里，内存占用控制在 100MB 以下。",
        "problems": [
            "<strong>启动器越做越重：</strong>Electron 系工具箱动辄占用几百 MB 内存。",
            "<strong>功能分散在多个 App：</strong>剪贴板、启动、窗口管理各装一个，热键互相打架。",
            "<strong>原生体验被牺牲：</strong>跨平台框架下的动效与输入手感总差一口气。"
        ],
        "usage": [
            "下载安装：<pre><code>https://github.com/abue-ammar/tinycast/releases/latest</code></pre>",
            "一个热键唤起，输入即搜：应用、文件、剪贴板历史。",
            "在设置里把常用动作绑成快捷指令。"
        ],
        "insights": [
            "<strong>「100MB 以下」被写进 README 第一行：</strong>这是反 AI 时代的宣言——当所有软件都在往用户机器里塞模型和进程，轻量本身成了稀缺体验。",
            "<strong>Swift 6 + macOS 26+：</strong>完全押注苹果最新的原生栈，放弃了跨平台市场换取手感与性能——小工具的差异化正在从功能转向「被感知的质感」。",
            "<strong>本质是本地软件的复兴：</strong>云端功能越强，用户越在意那些必须瞬时响应的东西——启动器、剪贴板、窗口操作永远不会去云端，这类需求是原生开发最后的护城河。"
        ],
        "tags": ["macos", "swift", "launcher", "native", "productivity"]
    },
    {
        "rank": 6,
        "owner": "NationalSecurityAgency",
        "name": "ghidra",
        "fullName": "NationalSecurityAgency / ghidra",
        "org": "NSA",
        "url": "https://github.com/NationalSecurityAgency/ghidra",
        "lang": "Java",
        "langClass": "java",
        "stars": "77,740",
        "forks": "8,593",
        "starsToday": "1,059",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,059★！77.7K★ 时隔 18 天第三次登榜！NSA 开源的逆向工程框架——反汇编、反编译、脚本化分析，安全研究绕不开的基础设施。",
        "problems": [
            "<strong>逆向工具昂贵：</strong>商业反编译器许可费每年数千到上万美元。",
            "<strong>二进制世界黑箱：</strong>没有源码就无法审计漏洞与后门。",
            "<strong>分析无法协作：</strong>缺少可脚本化、可版本化的团队分析流程。"
        ],
        "usage": [
            "下载发行版：<pre><code>https://github.com/NationalSecurityAgency/ghidra/releases</code></pre>",
            "导入二进制文件，自动反汇编与反编译。",
            "用 Python / Java 脚本批量做特征扫描与漏洞定位。"
        ],
        "insights": [
            "<strong>第三次登榜且仍在加速：</strong>8-29 首登 73,517★ → 8-30 二登 73,682★ → 今天 77,740★，三周净增 4.2K★——AI 生成代码越多，能看懂二进制的人越值钱。",
            "<strong>与今天的 AI 安全技能同台：</strong>Cloudflare 的审计技能守源代码，Ghidra 守二进制——AI 时代的攻防正在两个战场同时扩容。",
            "<strong>本质是透明度对闭源的反制：</strong>当供应链攻击成为常态，能把闭源组件拆开看清楚的组织才有安全底线——这解释了一个 2019 年的政府工具为什么持续吸星。"
        ],
        "tags": ["reverse-engineering", "security", "ghidra", "java", "binary-analysis"]
    },
    {
        "rank": 7,
        "owner": "affaan-m",
        "name": "ECC",
        "fullName": "affaan-m / ECC",
        "org": "affaan-m",
        "url": "https://github.com/affaan-m/ECC",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "260,221",
        "forks": "38,948",
        "starsToday": "1,046",
        "count": 7,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,046★！260K★ 第七次上榜！Agent Harness 性能优化系统——技能、直觉、记忆、安全与研究优先的开发流程，跨 Claude Code / Codex / Opencode / Cursor 通用。",
        "problems": [
            "<strong>Agent 效率不可控：</strong>同一任务不同跑法成本差几倍，却没有优化层。",
            "<strong>记忆与技能割裂：</strong>技能库、记忆、直觉分散在不同配置里互相打架。",
            "<strong>安全边界模糊：</strong>Agent 拿到越大的行动权限，越缺少配套约束。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/affaan-m/ECC.git</code></pre>",
            "接入 Claude Code / Codex / Opencode / Cursor。",
            "启用技能、记忆与安全策略，统一管理 Agent 行为。"
        ],
        "insights": [
            "<strong>九天内再涨 6.4K★：</strong>9-8 是 253,809★，今天 260,221★——榜单间隙期照样净增，热度不依赖曝光。",
            "<strong>跨 Harness 通用是关键卖点：</strong>在 Agent 工具碎片化的当下，「一个优化层兼容所有编码 Agent」比押注单一平台更有生命线。",
            "<strong>本质是 Agent 的运维层：</strong>模型、Harness、技能各自迭代得飞快，中间必然长出一层做协调与约束——谁占住这一层，谁就掌握了 Agent 的「操作系统」。"
        ],
        "tags": ["agent", "harness", "optimization", "memory", "javascript"]
    },
    {
        "rank": 8,
        "owner": "alphaXiv",
        "name": "OpenResearch",
        "fullName": "alphaXiv / OpenResearch",
        "org": "alphaXiv",
        "url": "https://github.com/alphaXiv/OpenResearch",
        "lang": "Rust",
        "langClass": "rs",
        "stars": "4,370",
        "forks": "271",
        "starsToday": "1,036",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +1,036★！首登！把 Claude Code、Codex、OpenCode、Cursor 变成研究 Agent 的本地工作台——读文献、提假设、跑实验、产出研究工件，本地优先，带 macOS 客户端。",
        "problems": [
            "<strong>科研流程断裂：</strong>文献、笔记、实验代码、结果散落在十几个工具里。",
            "<strong>编码 Agent 不会做研究：</strong>它们擅长写代码，不懂假设检验与文献综述。",
            "<strong>云端科研工具的数据顾虑：</strong>未发表的想法不敢放进第三方服务。"
        ],
        "usage": [
            "下载桌面版：<pre><code>https://github.com/alphaXiv/OpenResearch/releases/latest</code></pre>",
            "接入已有的编码 Agent（Claude Code / Codex / OpenCode / Cursor）。",
            "按「文献 → 假设 → 实验 → 工件」流程让 Agent 自主推进。"
        ],
        "insights": [
            "<strong>alphaXiv 的延伸：</strong>从「论文讨论社区」走向「研究工作台」——它掌握了研究者的入口（读论文），再往上游接住执行环节，路径非常清晰。",
            "<strong>本地优先的科研工具：</strong>未发表的想法是学者最敏感的资产，本地部署不是加分项而是准入门槛。",
            "<strong>本质是科研的成本结构被改写：</strong>当文献综述与实验脚手架由 Agent 承担，研究者的稀缺能力会从「执行力」转向「提问的品味」——这也是学术评价体系迟早要面对的问题。"
        ],
        "tags": ["research", "agent", "rust", "local-first", "science"]
    },
    {
        "rank": 9,
        "owner": "ever-co",
        "name": "ever-gauzy",
        "fullName": "ever-co / ever-gauzy",
        "org": "Ever Co",
        "url": "https://github.com/ever-co/ever-gauzy",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "7,284",
        "forks": "1,086",
        "starsToday": "771",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +771★！首登！开源商业管理平台（ERP / CRM / HRM / 招聘 / 项目管理）——把财务、销售、人力、工时、库存塞进一套可自托管系统，直接对标中小企业的 SaaS 年费账单。",
        "problems": [
            "<strong>SaaS 年费堆积：</strong>CRM、HR、工时、开票各订阅一个，成本随人头线性上涨。",
            "<strong>数据割裂：</strong>客户、项目、工时、账单分散在不同平台，报表要手工拼。",
            "<strong>自托管门槛高：</strong>开源 ERP 通常难部署、难维护，中小企业用不起。"
        ],
        "usage": [
            "克隆部署：<pre><code>git clone https://github.com/ever-co/ever-gauzy.git</code></pre>",
            "按模块启用：会计、开票、CRM、HRM、招聘、项目管理。",
            "自托管数据，按需对接支付与邮件服务。"
        ],
        "insights": [
            "<strong>非 AI 项目的上榜信号：</strong>在 AI 项目霸榜的环境里，一个 2019 年建的 ERP 还能日增 771★——说明「用开源砍掉 SaaS 订阅」依然是企业最硬的刚需。",
            "<strong>一体化是它的护城河：</strong>单点开源工具（只做 CRM 或只做开票）拼不成系统，而企业真正付费买的是「数据在一处」这件事。",
            "<strong>本质是 SaaS 定价权的转移：</strong>当开源能覆盖 80% 的通用管理流程，剩下的 20% 溢价必须来自行业深度——通用 SaaS 的日子会越来越难过。"
        ],
        "tags": ["erp", "crm", "typescript", "self-hosted", "business"]
    },
    {
        "rank": 10,
        "owner": "addyosmani",
        "name": "agent-skills",
        "fullName": "addyosmani / agent-skills",
        "org": "Addy Osmani",
        "url": "https://github.com/addyosmani/agent-skills",
        "lang": "JavaScript",
        "langClass": "js",
        "stars": "95,413",
        "forks": "10,109",
        "starsToday": "656",
        "count": 8,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +656★！95.4K★ 第八次上榜，较 8 月中已涨 10K★！Addy Osmani 出品的生产级工程技能集——把「什么样的代码算合格」写成 Agent 能执行的规则，适配 Claude Code / Codex / Cursor / Antigravity。",
        "problems": [
            "<strong>Agent 代码质量靠运气：</strong>同一需求不同轮次产出质量浮动巨大。",
            "<strong>资深经验无法传递：</strong>团队里高工的判断标准留在脑子里，Agent 学不到。",
            "<strong>技能生态碎片化：</strong>各家 Agent 的规则格式不统一，知识难以迁移。"
        ],
        "usage": [
            "安装：<pre><code>npx skills add addyosmani/agent-skills</code></pre>",
            "接入 Claude Code / Codex / Cursor 等 harness。",
            "按技能逐个启用：从测试、重构到性能与可访问性。"
        ],
        "insights": [
            "<strong>第八次登榜：</strong>8-10 时 85,320★，今天 95,413★——六周涨 10K★，「生产级技能」的稀缺性没有下降。",
            "<strong>作者信用即内容质量：</strong>Addy Osmani 在 Web 性能领域二十年的声誉，直接转换为技能库的分发优势——Agent 时代，署名比参数更能决定采用率。",
            "<strong>本质是工程标准的固化：</strong>技能越普及，团队间的代码质量基线就被拉得越高——这对行业是把双刃剑，标准统一也意味着审美的趋同。"
        ],
        "tags": ["agent-skills", "engineering", "quality", "javascript", "claude-code"]
    },
    {
        "rank": 11,
        "owner": "Lakr233",
        "name": "vphone-cli",
        "fullName": "Lakr233 / vphone-cli",
        "org": "Lakr233",
        "url": "https://github.com/Lakr233/vphone-cli",
        "lang": "Swift",
        "langClass": "swift",
        "stars": "13,321",
        "forks": "1,586",
        "starsToday": "444",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +444★！13.3K★ 首登！用 Apple 的 Virtualization.framework 在 Mac 上启动一台「虚拟 iPhone」——借用 PCC 研究 VM 的基础设施，作者是中文开发者。",
        "problems": [
            "<strong>iOS 测试依赖真机：</strong>自动化测试与安全研究要挂一堆实体设备。",
            "<strong>模拟器不够真：</strong>Xcode 模拟器跑的不是完整 iOS 系统，很多底层行为无法复现。",
            "<strong>研究环境难搭：</strong>想研究 iOS 内核与系统服务，缺一个可控的虚拟设备。"
        ],
        "usage": [
            "安装：<pre><code>brew install zqxwce/tap/vphone-cli</code></pre>",
            "准备 Apple Silicon 主机、macOS 15+ 与 iOS SDK。",
            "启动虚拟设备，接入测试或分析流程。"
        ],
        "insights": [
            "<strong>借来的基础设施：</strong>它直接复用 Apple 为私有云计算（PCC）搭的研究 VM 能力——把厂商的内部工具链从缝隙里挖出来，是独立开发者最擅长的打法。",
            "<strong>需要放宽 SIP 与 AMFI：</strong>README 明说要允许私有 PV=3 entitlement 的未签名二进制——门槛高，但正因为高，才没人抢着做。",
            "<strong>本质是硬件壁垒的软件化：</strong>当一台 iPhone 能变成 Mac 上的一个进程，围绕封闭硬件建立的测试与安全产业，就要重算一遍成本账。"
        ],
        "tags": ["ios", "virtualization", "swift", "macos", "reverse-engineering"]
    },
    {
        "rank": 12,
        "owner": "jamiepine",
        "name": "voicebox",
        "fullName": "jamiepine / voicebox",
        "org": "jamiepine",
        "url": "https://github.com/jamiepine/voicebox",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "54,345",
        "forks": "6,785",
        "starsToday": "409",
        "count": 3,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +409★！54.3K★ 第三次上榜，较首登涨 21K★！开源 AI 语音工作室——克隆音色、生成语音、在任意 App 里语音输入，整套语音 I/O 栈跑在本地，基于 Qwen3-TTS 与 MLX/CUDA 加速。",
        "problems": [
            "<strong>语音合成是订阅制：</strong>主流 TTS 服务按字计费，长期使用成本不可控。",
            "<strong>音色与隐私风险：</strong>把声音样本交给云端服务，等于交出生物特征。",
            "<strong>工作流割裂：</strong>克隆、生成、听写分散在不同工具里，无法串联。"
        ],
        "usage": [
            "下载安装：<pre><code>https://github.com/jamiepine/voicebox/releases</code></pre>",
            "本地克隆音色并生成语音（支持 MLX 与 CUDA 加速）。",
            "开启全局听写，把语音输入进任意应用。"
        ],
        "insights": [
            "<strong>32.9K → 44.1K → 54.3K：</strong>三次登榜一次比一次高，说明「本地语音栈」是持续放大的需求，不是短期热点。",
            "<strong>Qwen3-TTS 成为事实开源基座：</strong>国产开源语音模型被海外开发者直接集成为产品核心——中国模型在语音这条垂直赛道上的影响力，比大模型榜单更实在。",
            "<strong>本质是生物特征的所有权问题：</strong>声音是身份的一部分，把它交给云端等于永久授权——本地语音栈的流行，是用户对「生物特征不出设备」这条底线的一次集体表态。"
        ],
        "tags": ["tts", "voice-cloning", "qwen", "local-first", "typescript"]
    },
    {
        "rank": 13,
        "owner": "SnailSploit",
        "name": "Claude-Red",
        "fullName": "SnailSploit / Claude-Red",
        "org": "SnailSploit",
        "url": "https://github.com/SnailSploit/Claude-Red",
        "lang": "Python",
        "langClass": "py",
        "stars": "5,751",
        "forks": "739",
        "starsToday": "383",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +383★！首登！进攻性安全技能库——把结构化 SKILL.md 喂给 Claude，让它变成具备专家方法论的红队操作员：从 SQL 注入到 shellcode 编写，从 EDR 绕过到 ADCS 滥用。",
        "problems": [
            "<strong>渗透测试知识门槛高：</strong>攻击面众多、工具链复杂，没五年经验不敢上手。",
            "<strong>红队方法论不可复用：</strong>每次项目都从头摸索，知识留在个人身上。",
            "<strong>通用模型不懂攻防细节：</strong>缺少具体攻击面的边缘情况与提权路径。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/SnailSploit/Claude-Red.git</code></pre>",
            "把需要的技能目录放进 Claude 的 skills 路径。",
            "按对话触发按需加载，只在使用时消耗上下文。"
        ],
        "insights": [
            "<strong>技能框架既是能力也是清单：</strong>按攻击面整理的 SKILL.md 目录，本质上是一份公开的「现代攻击手册」——它同时服务红队和防御者。",
            "<strong>与 Cloudflare 审计技能同日登榜：</strong>一个做防守审计、一个做进攻方法论，共用同一套 Agent 技能机制——攻防双方在同一个抽象层上军备竞赛，这在安全史上还是第一次。",
            "<strong>本质是双用途困境：</strong>让模型更懂攻击细节，等于同时降低了攻防两端的门槛——安全社区必须回答一个老问题：知识公开到什么程度是净收益。"
        ],
        "tags": ["red-team", "security", "claude-skills", "offensive", "python"]
    },
    {
        "rank": 14,
        "owner": "multimodal-art-projection",
        "name": "YuE",
        "fullName": "multimodal-art-projection / YuE",
        "org": "M-A-P",
        "url": "https://github.com/multimodal-art-projection/YuE",
        "lang": "Python",
        "langClass": "py",
        "stars": "9,350",
        "forks": "1,007",
        "starsToday": "370",
        "count": 1,
        "badge": "新面孔",
        "description": "🔥 亮点 —— 今日 +370★！首登！YuE2 开源音乐生成模型——把「符号作曲」与「音频生成」统一在一个框架里，支持零样本翻唱与 Agent 化音乐编辑，由港科大、NYU、斯坦福等机构联合研发。",
        "problems": [
            "<strong>音乐生成不可控：</strong>端到端音频模型生成的东西无法按谱改动。",
            "<strong>没有编辑能力：</strong>想改一个乐句就得重新生成整首。",
            "<strong>翻唱依赖训练：</strong>换音色通常要针对性微调，成本极高。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/multimodal-art-projection/YuE.git</code></pre>",
            "从 HuggingFace 下载 YuE2-3B 权重（3B 规模）。",
            "用符号规划生成结构，再渲染成音频；支持零样本翻唱与 Agent 编辑。"
        ],
        "insights": [
            "<strong>「符号 + 音频」是本轮的关键词：</strong>先决定乐谱结构再生成声音，等于把可控性还给创作者——这与视频领域「先分镜后渲染」是同一条工程思路。",
            "<strong>3B 规模做前沿音乐：</strong>在动辄千亿的语言模型时代，音乐生成用 3B 就能达到前沿——垂直领域的参数效率，远高于通用模型竞赛。",
            "<strong>本质是创作门槛的再分配：</strong>当结构可编程、音色可零样本迁移，音乐行业稀缺的将不再是演奏与编曲的劳力，而是「决定做什么」的品味与版权谈判能力。"
        ],
        "tags": ["music-generation", "audio", "open-source", "multimodal", "python"]
    }
]

# Shift labels for 7-day gap (accurate offset: +7)
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

# Insert new day
new_day = {
    "date": "2026-09-17",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-09-17'
data['topic'] = '🔥 <strong>阿里 open-code-review 日增 3215★登顶 + Cloudflare 官方安全审计技能 + 腾讯 WeKnora 知识平台 + colibri 纯 C 跑 2.8T 模型 + ECC 七登 / agent-skills 八登</strong> —— alibaba/open-code-review（+3,215★）31.7K★ 翻倍回归，确定性管线 + LLM 混合架构。JustVugg/colibri（+1,532★）35.0K★ 首登，纯 C 零依赖在消费级硬件跑万亿参数 MoE。cloudflare/security-audit-skill（+1,249★）官方六阶段审计技能首登。Tencent/WeKnora（+1,201★）腾讯 LLM 知识平台首登。abue-ammar/tinycast（+1,136★）100MB 以下的原生 macOS 启动器首登。NationalSecurityAgency/ghidra（+1,059★）77.7K★ 三登。affaan-m/ECC（+1,046★）260K★ 七登。alphaXiv/OpenResearch（+1,036★）研究 Agent 工作台首登。ever-co/ever-gauzy（+771★）开源 ERP 首登。addyosmani/agent-skills（+656★）95.4K★ 八登。Lakr233/vphone-cli（+444★）虚拟 iPhone 首登。jamiepine/voicebox（+409★）54.3K★ 三登。SnailSploit/Claude-Red（+383★）红队技能库首登。multimodal-art-projection/YuE（+370★）YuE2 音乐生成首登。时隔 7 天回归更新——今日榜单的三条明线：机构级玩家（阿里 / 腾讯 / Cloudflare / NSA）把 Agent 工具链当基础设施开源；技能与安全成为新战场（审计技能与红队技能同台）；本地与边缘推理继续下沉（纯 C 跑万亿模型、本地语音栈、虚拟 iPhone）——「Agent 的第二战场」不是更聪明的模型，而是审计、科研、安全、语音这些具体工位。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:5]]}")

# Verify badge present on every project
assert all(p.get('badge') in ('新面孔', '连登') for p in days[0]['projects']), "badge missing!"

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  [{p.get('badge','')}] #{p['rank']} {p['name']}: +{p['starsToday']}★ count={p['count']}")
