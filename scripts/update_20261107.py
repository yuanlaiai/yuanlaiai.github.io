#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新 GitHub 榜单 2026-11-07（距上次更新 2 天，flat day：全部新面孔）"""
import json
from datetime import datetime

DATA = "/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json"
TODAY = "2026-11-07"

LANGCLASS = {
    "Python": "py", "TypeScript": "ts", "JavaScript": "js", "Shell": "sh",
    "Rust": "rs", "C": "c", "C++": "cpp", "HTML": "html", "CSS": "css",
    "Markdown": "md", "Go": "go", "C#": "cs", "Java": "java",
    "Kotlin": "kotlin", "Dart": "dart", "TeX": "tex", "Swift": "swift",
    "Zig": "zig",
}

P = []


def add(owner, name, lang, stars, forks, starsToday, description,
        problems, usage, insights, tags):
    P.append({
        "owner": owner,
        "name": name,
        "fullName": "%s / %s" % (owner, name),
        "org": owner,
        "url": "https://github.com/%s/%s" % (owner, name),
        "lang": lang,
        "langClass": LANGCLASS.get(lang, lang.lower()),
        "stars": stars,
        "forks": forks,
        "starsToday": starsToday,
        "badge": "新面孔",
        "description": description,
        "problems": problems,
        "usage": usage,
        "insights": insights,
        "tags": tags,
    })


add("cloudflare", "security-audit-skill", "JavaScript", "64,961", "4,213", "2,088",
    "🔥 亮点 —— 今日 +2,088★ 第一，6.5万★，第 7 次上榜。Cloudflare 开源的安全审计技能：六阶段跑完侦察、覆盖式挖掘、候选验证、结构化输出和独立复核，把 agent 变成审计员。",
    [
        "<strong>agent 审代码靠瞎猜：</strong>读一遍就报告「可能有注入」，说不出覆盖到哪、漏了哪。",
        "<strong>误报淹没人：</strong>找十个问题九个是假的，工程师干脆不看报告。",
        "<strong>审计过程不可复核：</strong>结论从哪来、谁验证的，事后没人能追溯。",
    ],
    [
        "把技能装进 Claude Code 等 agent 的 skills 目录。",
        "第一阶段先产 architecture.md 和 coverage-ledger.json，把信任边界和覆盖范围写清。",
        "每个候选漏洞交给全新的验证 agent 去证伪，通过的结构化写入 findings.json 并按 schema 校验，最后再做一次独立复核。",
    ],
    [
        "<strong>两个月从 1.75 万★ 涨到 6.5 万★：</strong>安全审计是全公司都在等 agent 接手的活，需求比工具迭代快得多。",
        "<strong>它的核心设计是「证伪」而不是「发现」：</strong>每个候选都交给一个想去推翻它的 agent，误报率就是这么压下来的。",
        "<strong>Cloudflare 先写博客再开源技能：</strong>大厂把自己的内部方法做成技能发出来，既拿声誉也定标准。",
    ],
    ["security", "audit", "skills", "agents", "cloudflare"])

add("milind-soni", "OpenMausBot", "TypeScript", "16,354", "2,320", "1,986",
    "🔥 亮点 —— +1,986★，1.64万★，第 2 次上榜。Grok Bot 的开源替代：侧边栏每个 bot 都是本地跑的 Claude 或 Codex，各有性格、模型、云电脑和接好的应用，像联系人一样指挥。",
    [
        "<strong>官方 bot 锁在自己生态里：</strong>模型、记忆、能连的应用都由厂商决定。",
        "<strong>一套人格应付所有事：</strong>写代码、查资料、盯邮件需要不同工作方式。",
        "<strong>长任务看不见过程：</strong>扔一句话进去，中间做了什么你无从判断。",
    ],
    [
        "从 openmausbot.com 下 macOS/Windows/Ubuntu 客户端。",
        "给每个 bot 配模型（本地 Claude 或 Codex）和人格，各自接自己的应用。",
        "重要操作弹审批，执行过程在聊天窗口里直接可见。",
    ],
    [
        "<strong>六天前 9,662★，今天 1.64万★：</strong>官方 bot 产品把好奇心拉起来，开源替代接住了这批人。",
        "<strong>底层是本地 Claude/Codex，说明上层不掌握模型：</strong>这类产品的竞争力全在编排和界面。",
        "<strong>「agent 当联系人」是交互上的迁移：</strong>人从操作者变成管理者，这个转变比模型升级更能改变日常。",
    ],
    ["ai-agent", "electron", "local-first", "chat", "typescript"])

add("NVIDIA", "auto-ontology", "Python", "9,601", "772", "1,322",
    "🔥 亮点 —— +1,322★，9,601★，第 2 次上榜。NVIDIA 的语义层框架：把企业元数据编成知识图谱，告诉 agent 每个指标怎么定义、数字从哪来、能不能拿来算。",
    [
        "<strong>agent 查数快但不敢用：</strong>问一句营收，它给一个数，你没法确认这个口径和财务是不是同一个。",
        "<strong>同名指标到处不一致：</strong>BI、数仓、业务表格各一套定义。",
        "<strong>生成的 SQL 没有验收：</strong>结果对不对没人校验。",
    ],
    [
        "克隆仓库，<code>cp .env.example .env</code> 填 build.nvidia.com 申请到的 key。",
        "用 Docker Compose 接 Wide World Importers 示例库跑通。",
        "通过 MCP、CLI 或 API 接入自己的 agent，生成查询时对着认证定义校验并返回来源。",
    ],
    [
        "<strong>两天从 6,456★ 到 9,601★：</strong>企业场景的付费意愿比消费级工具强，热度虽然不高但落得实。",
        "<strong>它只做约束，不做生成：</strong>在所有人都往上堆能力的时候，NVIDIA 卖的是「这个数字能不能信」。",
        "<strong>每次纠错回写本体：</strong>用得越久越准，这是数据资产唯一能复利的地方。",
    ],
    ["ontology", "text-to-sql", "semantic-layer", "mcp", "nvidia"])

add("mattpocock", "skills", "Shell", "317,258", "26,548", "1,111",
    "🔥 亮点 —— +1,111★，31.73万★，第 14 次上榜。日常工程技能集，小而可组合、鼓励改成自己的，明确反对把流程收走的框架。",
    [
        "<strong>流程框架替你握方向盘：</strong>出问题连从哪查都不知道。",
        "<strong>大而全的规范比代码慢：</strong>文档写一堆，最后没人读。",
        "<strong>绑死某个 agent 等于自废武功：</strong>模型换代，写法全废。",
    ],
    [
        "按 README 的 30 秒流程装成 plugin。",
        "从一个小技能开始，按自己习惯改。",
        "技能就是 markdown，换任何模型都能读。",
    ],
    [
        "<strong>14 次上榜，几乎每次日增都在千星以上：</strong>这个仓库已经变成技能生态的默认入口之一。",
        "<strong>它的立场和 GitHub 官方 spec-kit 正好相反：</strong>一个要规范流程，一个坚决不碰，两边都在涨，说明用户分层已经很明显。",
        "<strong>30 万★ 的资产是判断力：</strong>代码可以生成，判断不行。",
    ],
    ["skills", "engineering", "typescript", "workflow", "composable"])

add("google", "skills", "Python", "23,104", "1,940", "449",
    "🔥 亮点 —— +449★，2.31万★，第 3 次上榜。Google 官方的 Agent Skills 仓库，覆盖 Google Cloud 等自家产品，一条 <code>npx skills add</code> 装上。",
    [
        "<strong>云服务知识和 agent 隔着层：</strong>文档写得全，但 agent 不知道什么时候该用哪条命令。",
        "<strong>技能格式不统一：</strong>装一个能用的技能，先读半天结构说明。",
        "<strong>认证权限区域容易配错：</strong>错一个参数卡半天。",
    ],
    [
        "<code>npx skills add google/skills</code>，按提示选技能和目标 agent。",
        "选项目级或全局安装，后续用 <code>npx skills update</code> 更新。",
        "从认证授权那组开始装，再接云资源操作。",
    ],
    [
        "<strong>两天前刚上过榜，今天又回来：</strong>官方技能库不是一次性曝光，而是持续被搜索安装的常客。",
        "<strong>云厂商把文档改写成技能：</strong>这是最便宜的生态投入，写一次，所有 agent 都能读。",
        "<strong>它的对手是自家 CLI：</strong>装技能和让人读文档，抢的是同一批操作。",
    ],
    ["skills", "google-cloud", "agents", "cli", "standards"])

add("anthropics", "skills", "Python", "188,398", "22,220", "386",
    "🔥 亮点 —— +386★，18.84万★，第 3 次上榜。Anthropic 官方的技能示例库：从画图、做音乐到测试 Web 应用、生成 MCP server，配套 agentskills.io 标准。",
    [
        "<strong>官方文档只讲概念：</strong>技能到底能干什么，得自己一个个试。",
        "<strong>社区技能质量参差：</strong>没有基准，装十个不如自己写一个。",
        "<strong>格式各家不一致：</strong>Claude、Cursor、Codex 的技能目录结构各有一套。",
    ],
    [
        "克隆仓库，按技能目录结构放进本地 skills 路径。",
        "用 <code>/plugin</code> 安装，或直接复制某个技能去改。",
        "重点参考 MCP server 生成、Web 应用测试几个样例。",
    ],
    [
        "<strong>和 Cloudflare、Google 的官方技能库同天在榜：</strong>三家的技能库同时出现在 13 个位置里，标准之争已经摆在台面上。",
        "<strong>示例库的价值是降低第一次尝试的门槛：</strong>用户学技能的第一站通常就是这里。",
        "<strong>谁定义格式，谁就定义能力的边界：</strong>技能能调用什么工具，取决于厂商把哪些接口写进标准。",
    ],
    ["skills", "anthropic", "examples", "mcp", "standard"])

add("jamiepine", "voicebox", "Python", "59,872", "7,512", "318",
    "🔥 亮点 —— +318★，5.99万★ 首登。开源的 AI 语音工作室：一个应用里可切换 8 个 TTS 引擎，能克隆音色、按情绪和语气标记生成，还能全局听写和语音转写。",
    [
        "<strong>语音工具各管一段：</strong>克隆一个工具、合成一个工具、听写又一个工具，音色对不上。",
        "<strong>换引擎等于换工作流：</strong>想试新模型，先重学一套接口和参数。",
        "<strong>云服务按秒计费：</strong>做长音频或批量生成，账单涨得比进度快。",
    ],
    [
        "从 Releases 下对应平台的安装包。",
        "按任务切引擎：多语言克隆用 Qwen3-TTS，轻量高速用 LuxTTS，23 种语言用 Chatterbox Multilingual。",
        "用 Stories Editor 拼长音频，生成的版本可回退，配音稿和音色分开管理。",
    ],
    [
        "<strong>八个引擎并列是可用的关键：</strong>没有哪个 TTS 在所有场景都最好，能随手切换比押注一家实际。",
        "<strong>它把「语音 I/O」当成一整套做：</strong>合成、听写、转写在同一个应用里，音色才能贯穿始终。",
        "<strong>本地跑全栈对创作者最实在：</strong>长音频和批量生成按秒计费的模式撑不住，一次性买断的机器可以。",
    ],
    ["tts", "voice-clone", "dictation", "local-first", "audio"])

add("microsoft", "VibeVoice", "Python", "56,616", "6,375", "237",
    "🔥 亮点 —— +237★，5.66万★，第 3 次上榜。微软开源语音栈：TTS 之外有流式 ASR，能边听边转写「谁说了什么」，还有压到 CPU 的 BitNet 版本。",
    [
        "<strong>会议转写分不清谁在说：</strong>整段文字没有说话人，纪要等于白做。",
        "<strong>语音模型离不开显卡：</strong>想本地或边缘跑，先得有张卡。",
        "<strong>长音频一段段切：</strong>切碎丢上下文，拼起来前后不接。",
    ],
    [
        "从 Hugging Face 的 microsoft/vibevoice 集合下权重。",
        "TTS 用 Colab 示例跑通，ASR 用官方 playground 试「谁说了什么」。",
        "边缘场景用 VibeASR.cpp 的 BitNet 版本，纯 CPU 推理。",
    ],
    [
        "<strong>半个月第三次上榜：</strong>语音这类基础能力的复访率比工具高，因为它一直在被集成。",
        "<strong>压到 CPU 才是分水岭：</strong>语音入口要常驻，常驻的东西不能占着显卡。",
        "<strong>TTS 和 ASR 一起开源：</strong>两端都在自己手里，才有资格谈标准。",
    ],
    ["voice", "tts", "asr", "microsoft", "edge"])

add("meta", "astryx", "TypeScript", "14,177", "1,171", "198",
    "🔥 亮点 —— +198★，1.42万★ 首登。Meta 开源的 React 设计系统，基于 React 19 和 StyleX，明确按「人和身边的 agent 一起做界面」来设计，目前 Beta。",
    [
        "<strong>agent 写界面不懂设计系统：</strong>生成一堆样式内联的组件，和现有规范对不上。",
        "<strong>组件库对机器不友好：</strong>文档给人看，agent 读不出「什么场景该用哪个组件」。",
        "<strong>改主题要动代码：</strong>品牌换色时逐个文件改，一致性靠人盯。",
    ],
    [
        "用 <code>npm i @astryxdesign/core</code> 装上，按文档接进现有 React 项目。",
        "先用 Storybook 看组件形态，再决定怎么覆盖主题。",
        "让 agent 读组件文档和约束，生成时按规范选组件而不是自己拼样式。",
    ],
    [
        "<strong>设计系统第一次把 agent 列为目标用户：</strong>它是给「写代码的不是人」这个场景重新整理组件边界。",
        "<strong>Beta 就开源，Meta 在抢标准：</strong>设计系统的价值在生态规模，越早开放越容易被当成默认。",
        "<strong>React 19 加 StyleX 是明确取舍：</strong>它赌编译期样式能同时满足人和机器对一致性的要求。",
    ],
    ["design-system", "react", "stylex", "meta", "components"])

add("ranxianglei", "billion-context", "TypeScript", "4,435", "359", "185",
    "🔥 亮点 —— +185★，4,435★ 首登。一个上下文压缩代理：把 agent 的 base URL 指过来，历史对话被压成分层摘要，可按需解压，号称省 5 倍 token，能撑月级长会话。",
    [
        "<strong>长会话必定撞墙：</strong>越接近上下文窗口上限，模型表现越差，最后直接崩。",
        "<strong>宿主自带的摘要不可逆：</strong>压完细节就没了，需要回头查原文时找不回来。",
        "<strong>压缩破坏缓存：</strong>前缀一变，prefix cache 全失效，省下的 token 又赔回去。",
    ],
    [
        "<code>npm install -g billion-context</code>，用 <code>bili claude</code> 之类的启动器指向你的 agent。",
        "代理注入 compress、decompress、search_context、acp_status 四个工具，由模型自己决定何时压缩。",
        "被折叠的区间留在历史里保持摘要状态，需要细节时再解压回来。",
    ],
    [
        "<strong>「增量、可逆、缓存友好」三个词定义了它和宿主自带摘要的区别：</strong>可逆是最难也最有用的一条。",
        "<strong>支持近二十种 harness，包括 Hermes：</strong>做在代理层而不是插件层，一次适配就全通，这是协议位置的杠杆。",
        "<strong>省 token 只是表象：</strong>真正解决的是「一个项目跑一星期」这件事，会话不该因为窗口满而重启。",
    ],
    ["context", "compression", "proxy", "tokens", "coding-agent"])

add("vercel-labs", "agent-browser", "Rust", "46,469", "3,186", "180",
    "🔥 亮点 —— +180★，4.65万★ 首登。Vercel Labs 给 agent 用的浏览器自动化 CLI：打开页面、读成无障碍树、在 shell 里对元素直接操作。",
    [
        "<strong>agent 读网页靠截图：</strong>烧 token 还不准，长页面直接被截断。",
        "<strong>Playwright 脚本要人写：</strong>agent 想自己操作浏览器，得先学一套测试框架。",
        "<strong>页面结构变了就找不到元素：</strong>选择器一崩，整条流程中断。",
    ],
    [
        "npm 装上 CLI，直接 <code>agent-browser open</code> 一个地址。",
        "用无障碍树读页面，元素带引用，操作时按引用点。",
        "在 agent 里把这几个命令当工具调，形成「读、点、再读」的循环。",
    ],
    [
        "<strong>它和 agent-desktop 是同一个思路的两种边界：</strong>一个管浏览器，一个管操作系统，都用无障碍树代替像素。",
        "<strong>Vercel 一周内两个项目上榜：</strong>它们在赌 agent 的行动能力是下一个入口。",
        "<strong>以 CLI 形式发布而不是 SDK：</strong>因为 CLI 能被任何 agent 直接调用，不用适配各家框架。",
    ],
    ["browser", "automation", "cli", "rust", "accessibility"])

add("Usagi-org", "ai-goofish-monitor", "Python", "18,285", "3,014", "146",
    "🔥 亮点 —— +146★，1.83万★，第 2 次上榜。Playwright 加多模态模型的闲鱼监控：自然语言建任务，按价格、区域、包邮筛选，命中推飞书、企业微信、Bark 或 Telegram。",
    [
        "<strong>好价商品活不过几分钟：</strong>等你刷到，已经被拍下。",
        "<strong>筛选条件太粗：</strong>平台只能按关键词和价格，看不出成色和猫腻。",
        "<strong>多账号易被风控：</strong>手动切号换 IP，效率极低。",
    ],
    [
        "克隆仓库，<code>cp .env.example .env</code> 填配置，<code>docker compose up -d</code>。",
        "打开 Web 界面用自然语言建任务，配 AI 评分标准。",
        "绑通知渠道，配 Cron 定时跑，多账号和代理池轮换。",
    ],
    [
        "<strong>隔一天又上榜：</strong>这类工具的热度不看技术，看某个品类最近有没有行情。",
        "<strong>多模态模型在二手场景才显出价值：</strong>判断成色、识别图片里的坑，关键词匹配做不到。",
        "<strong>账号池和代理轮换说明对抗成本：</strong>平台风控和工具一直在互相升级，这类项目天然短命。",
    ],
    ["ecommerce", "monitoring", "multimodal", "playwright", "china"])

add("dsx-ai-factory", "nvke", "Go", "381", "78", "125",
    "🔥 亮点 —— +125★，381★ 首登。NVIDIA Kubernetes Engine：给 GPU 裸金属机器装一个管理面，让平台团队像卖云一样给自己的客户开 K8s 集群。",
    [
        "<strong>GPU 机器各自为政：</strong>一堆裸金属服务器，调度、隔离、分租全靠手工。",
        "<strong>自建托管 K8s 太重：</strong>控制面、etcd、节点池都要自己搭。",
        "<strong>算力卖不上价：</strong>没有多租户和配额，只能整机出租。",
    ],
    [
        "按文档在管理节点上装 NVKE 管理面。",
        "为每个租户创建独立的 workload 集群，各自带控制面、etcd 和节点池。",
        "客户用自己的 kubectl 访问集群，平台侧只管管理面和配额。",
    ],
    [
        "<strong>星星很少但位置关键：</strong>它解决的是算力怎么像水电一样分租出去，这决定了 GPU 云的成本结构。",
        "<strong>明确标注 Preview：</strong>NVIDIA 在试探自建云这条路，买不买单取决于中小规模机房。",
        "<strong>裸金属托管 K8s 是边缘算力的基建：</strong>推理下沉之后，机房会从超大规模变成很多中小节点。",
    ],
    ["kubernetes", "gpu", "infra", "nvidia", "bare-metal"])

TOPIC = ("🔥 <strong>今日主题：技能库开始有厂牌。</strong>"
         "Cloudflare 的安全审计技能一天涨 2,088★，Google 和 Anthropic 的官方技能库同时在榜，"
         "加上 Matt Pocock 的个人技能集，13 个位置里 4 个是 skills 仓库。"
         "它们干的是同一件事：把「怎么做」写成 markdown 发给 agent。"
         "另一条线是语音，voicebox 一个应用里塞了 8 个 TTS 引擎，VibeVoice 半个月第三次上榜。"
         "真正的变化不在技能数量，在于厂商开始用技能库抢标准："
         "谁能定义技能怎么写、能调什么，谁就定义了 agent 的能力边界。")

with open(DATA, encoding="utf-8") as fh:
    data = json.load(fh)

prior = {}
for day in data["days"]:
    for p in day["projects"]:
        k = (p.get("owner"), p.get("name"))
        prior[k] = max(prior.get(k, 0), p.get("count") or 0)

P.sort(key=lambda p: -int(p["starsToday"].replace(",", "")))
for i, p in enumerate(P, 1):
    p["rank"] = i
    p["count"] = 1 + prior.get((p["owner"], p["name"]), 0)

new_day = {"date": TODAY, "label": "今天", "icon": "", "projects": P}

today = datetime.strptime(TODAY, "%Y-%m-%d")
for day in data["days"]:
    d = (today - datetime.strptime(day["date"], "%Y-%m-%d")).days
    if d <= 0:
        day["label"] = "今天"
    elif d == 1:
        day["label"] = "昨天"
    elif d == 2:
        day["label"] = "前天"
    else:
        day["label"] = "%d天前" % d

data["days"].insert(0, new_day)
data["lastUpdated"] = TODAY
data["topic"] = TOPIC

assert all(p.get("badge") in ("新面孔", "连登") for p in data["days"][0]["projects"])
assert len(data["days"]) == 96, len(data["days"])

with open(DATA, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)

print("写入完成：%s，%d 个项目，总天数 %d" % (TODAY, len(P), len(data["days"])))
for p in P:
    print("  %2d. %-38s +%-6s %8s★ count=%d" % (
        p["rank"], p["fullName"], p["starsToday"], p["stars"], p["count"]))
