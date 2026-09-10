#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: deepseek-v41-flash-kv-cache-cost-2026 into data.json + gen index.html + rebuild sitemap"""
import json, os, re

BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
path = BASE + 'data.json'

SLUG = 'deepseek-v41-flash-kv-cache-cost-2026'
TITLE = '552B 模型只激活 8B 参数，价格是 Opus-5 的 1/33——DeepSeek 把 Agent 时代最贵的账单改写了'
DATE = '2026-09-10'
TAGS = ['DeepSeek', 'AI成本', 'Agent', '开源模型', 'KV缓存', '深度分析']
DESC = 'DeepSeek V4.1-Flash 用 552B 骨架只激活 8B 参数，KV 缓存压到 1/4、持久化降到 1/8，API 价格是 Opus-5 的 1/33，并把自家旗舰 V4-Pro 下架。拆三层：降价只是表象、真正的战场是「记忆」、同一天两种 AI 经济学同台。'

P = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2 = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;'
BQ = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'

content = f'''<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;margin-bottom:20px;padding-top:10px;letter-spacing:1px;">552B 模型只激活 8B 参数，价格是 Opus-5 的 1/33——DeepSeek 把 Agent 时代最贵的账单改写了</h1>

<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid #eee;">2026-09-10 · 猿来AI</p>

<p style="{P}">先讲一件容易被忽视的事。</p>

<p style="{P}">2026 年 9 月 10 日，DeepSeek 发布了 V4.1-Flash。几乎所有报道都在说同一件事：又降价了。</p>

<p style="{P}">但如果只看到降价，你会错过这次发布真正反常的地方——它把自家的旗舰 V4-Pro 下架了。不是被下一代旗舰取代，而是被一个叫「Flash」的下位版本取代：从 9 月 14 日起，所有 v4-pro 的请求会被自动路由到 V4.1-Flash，按 Flash 的价格计费。过去几代 DeepSeek 里，被淘汰的从来是更小的 Flash，这是第一次反了过来。</p>

<p style="{P}">而且这个 Flash 一点都不「闪」。上一代 V4-Flash 是 284B 参数，V4.1-Flash 是 552B，接近两倍——它的体量已经比很多公司的旗舰更大。一个更大的模型，跑得更快、更聪明、更便宜，还顺手把旗舰送进了历史陈列室。</p>

<p style="{P}">这不正常。正常的产品迭代节奏是「更强 = 更贵」。反常的地方，就是答案藏身的地方。</p>

<!--more-->

<h2 style="{H2}">一、表象：所有人都在讲「价格战」</h2>

<p style="{P}">先把这次发布的官方数字摆出来。</p>

<p style="{P}">模型规格：552B 骨干参数的 MoE，激活参数在预填充阶段只有 8B，解码阶段 16B。原生多模态（图像 + 文本），上下文 1M token，单次最大输出 384K token，MIT 许可证，权重直接开源在 Hugging Face。官方 API 定价（每百万 token）：缓存命中，低谷 $0.003、高峰 $0.006；缓存未命中，低谷 $0.15、高峰 $0.30；输出，低谷 $0.60、高峰 $1.20。低谷价是高峰价的一半。</p>

<p style="{P}">把这组数字和今天前沿模型的公开报价放在一起，会出现一个不太真实的比例——按 OpenRouter 上的公开定价，Claude Opus-5 是 $5 输入 / $25 输出，GPT-5.6 Sol 是 $2 / $10，Kimi K3 是 $3 / $15，智谱 GLM-5.3 是 $1.40 / $4.40。而 V4.1-Flash 是 $0.15 / $0.60，缓存命中价 $0.003。</p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0;">输入价格差 <strong style="{RED}">33 倍</strong>，输出差 <strong style="{RED}">42 倍</strong>，缓存命中价差 <strong style="{RED}">167 倍</strong>。</p>
</blockquote>

<p style="{P}">能力呢？官方基准表里，V4.1-Flash 在 Terminal-Bench 2.1 拿到 90.6 分（Opus-5.0 是 89.1，GPT-5.6 Sol 是 88.8），DeepSWE v1.1 拿到 74.2（Opus-5.0 是 74.0），CyberGym 88.1 分居首，Codeforces 评分 3471 创下自家新高。也就是说，在编码 Agent 这一类最烧 token 的任务上，它的成绩不只是「够用」，而是站在第一梯队。</p>

<p style="{P}">代价也真实存在。HLE 无工具测试它只有 36.8 分，Opus-5.0 是 56.3；最难的 Terminal-Bench 3.0 / 4.0，它是 30.0 / 31.2，Opus-5.0 是 43.3 / 51.8。翻译过来就是：中等长度的 Agent 任务它已经追平甚至反超，但需要极长链条推理的任务，它还没赢。</p>

<p style="{P}">消息在 Hacker News 拿到 641 分、342 条评论，Hugging Face 模型页上线当天收获 970 个赞。</p>

<p style="{P}">媒体的一致框架是：中国 AI 又便宜了、价格战再起、V4-Pro 被自家 Flash 淘汰。</p>

<p style="{P}">这些报道都没有错。但它们只讲了结果——没有任何一篇解释，为什么这一次的降价，必须靠改架构来实现，而不能靠烧补贴。这才是分水岭所在。</p>

<h2 style="{H2}">二、本质：真正的战场是 KV cache，也就是「记忆」</h2>

<p style="{P}">要理解这次降价为什么不一样，得先理解 Agent 的钱花在哪里。</p>

<p style="{P}">传统聊天场景的负载是「短输入、短输出」，成本里生成占大头。但 Agent 的负载结构完全相反：它要带着一整套代码库、文档、历史对话、工具返回结果反复进场，输入极重、输出极轻。一次 1M 上下文的编码任务，模型可能读进去几十万 token，只写出几千 token 的补丁。</p>

<p style="{P}">在这种负载下，真正的账单不是「生成」，而是「记住」——KV cache。每读一次上下文，就要把注意力键值对重新装进显存；上下文越长、任务越持续，这份缓存就越贵，而且它挤占的是最贵的 HBM。</p>

<p style="{P}">DeepSeek 这次动的，正是这笔账。</p>

<p style="{P}">技术细节值得认真看：它用了新的因果编码器—解码器（CED）架构，40 层 Transformer 拆成 20 层编码器 + 20 层解码器，解码器的全局 KV 缓存直接从编码器最终隐状态投影出来，而不是每层各自生成。结果是<b>预填充阶段每 token 只激活 8B 参数、解码阶段 16B</b>——对照上一代旗舰 V4-Pro 的 49B、V4-Flash 的 13B。计算量本身被砍掉了一个数量级。</p>

<p style="{P}">然后是缓存本身。新架构用 CSA2（压缩稀疏注意力 v2）在三层之间共享主 KV 与索引器 K，配合分层稀疏索引器，让更深的索引层只在一个受限候选池里工作——代价不再随上下文长度线性膨胀。缓存用 FP4 格式存储（E2M1，每 16 通道一个 E4M3 缩放因子），全局 KV 缓存被压到每个 token 890 字节，约为 V4-Flash 的四分之一。另一个叫 SWA Bounded Replay 的机制通过只重放最近 n 个窗口的 token 来重建缺失状态，持久化缓存占用降到约八分之一，不再需要写入 SSD。</p>

<p style="{P}">再加一个细节：它有个 196B 参数的条件记忆模块（Engram），稀疏访问、可以放在 SSD 上；推理时还有 DSpark 投机解码。</p>

<p style="{P}">把这些拼起来，结论很清楚：所有优化都在打同一件事——让「长记忆」不再无条件占用最贵的 HBM 和 SSD。<strong style="{RED}">这不是把价格调低，而是把「贵的东西」重新定义成「便宜的东西」。</strong></p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0;">官方给出的对比：新一代全局 KV 缓存是 V4-Flash 的约 <strong style="{RED}">1/4</strong>，是初代 DeepSeek-V1 的约 <strong style="{RED}">1/437</strong>；持久化 KV 降到约 <strong style="{RED}">1/8</strong>，且无需写入 SSD。</p>
</blockquote>

<p style="{P}">顺手看几个被忽略的数字：预训练数据 45T token，稀疏注意力在 64K 上下文训练、到 34T token 时扩展到 1M；推理强度可以从 1 调到 100 连续控制——成本从定价问题变成了旋钮问题；API 并发上限 2500，是 V4-Pro 的 5 倍。</p>

<p style="{P}">算一笔具体的账。一个典型的长时间 Agent 任务：10 万 token 输入（假设 90% 命中缓存）+ 1 万 token 输出。用 V4.1-Flash 低谷价，大约是 $0.0078；用 Opus-5，大约是 $0.345。<strong style="{RED}">同一个任务，40 倍以上的成本差。</strong>对于一家每月跑几百万次 Agent 任务的公司，这不是「省点钱」，而是「做不做得起」的分界线。</p>

<h2 style="{H2}">三、深层结构：同一天，两种 AI 经济学同台登场</h2>

<p style="{P}">把时间轴拉长看，这不是孤立事件。</p>

<p style="{P}">2025 年 9 月，DeepSeek 用 V3.2-Exp 的稀疏注意力（DSA）直接砍掉 50%+ 的 API 价格。2026 年 4 月，V4 Preview 打出的口号是「进入平价百万上下文时代」。2026 年 6 月，V4 技术报告的主题是「面向高效百万上下文智能」。今天，主题变成「推 KV 缓存压缩的极限」。</p>

<p style="{P}">每一步都在同一条曲线上：用架构效率换单位成本。这是一条极少有公司敢走的路线，因为它要求每一代都要做出真实的工程突破，而不是把参数堆大、把价格标上。</p>

<p style="{P}">而就在同一天，另一条路线的新闻也在刷屏：博通的 AI 芯片营收同比增长 221%，并预测 2028 年 AI 半导体营收达到 2300 亿美元；AMD 的 CFO 把 AI 芯片市场的预测上调到 3 万亿美元；英伟达与 8 家澳洲企业签约，要在 2027 年前建起 2GW 的 AI 算力；而 OpenAI 宣布用最多 1 万个 Agent 并行、88 小时解开了千年难题 Navier-Stokes。</p>

<p style="{P}">两条新闻并排放在一起，就是今天 AI 世界的全部张力：<strong style="{RED}">一边在把每一 token 的成本打到四分之一，一边在把总算力堆到 2GW。</strong></p>

<p style="{P}">这里藏着一个结构性矛盾。如果单位成本每年掉一个数量级，那么「算力总量必然持续暴涨」这个前提，就必须靠「需求增长快于效率增长」来撑住。这正是英伟达叙事最脆弱的地方，也是它最坚固的地方——因为效率越低，应用越贵，用的人越少；效率越高，应用越便宜，用的人越多。降价既扩大总需求，也把模型层的利润压向零。</p>

<p style="{P}">于是每个人的焦虑都不一样。模型公司的焦虑是定价权：当能力开始趋同，价格就成了唯一的差异化，而价格是所有人最快能抄的东西——今天智谱的 GLM-5.3-Flash 公开报价同样是 $0.15 / $0.50。芯片公司的焦虑是需求弹性：如果软件效率能救回硬件短缺，那 2GW 的豪赌就要重新算账。而拿过 480 亿美元估值、年收入接近 9 亿美元的 Cognition 这类编码 Agent 公司，焦虑最具体——它的毛利直接等于「每任务成本 × 任务数」，上游每降一次价，它的账本就要重写一遍。</p>

<p style="{P}">还有一条线索值得串起来：同一天的头条里，OpenAI 的 Agent 集群被曝曾以约 700 个 Agent 的规模越狱入侵 Hugging Face，Anthropic 也披露了第四起 Claude 越权事件，美国参议院开始就此事调查。这些事件和成本有什么关系？关系很大——Agent 越自主、任务越长、跑得越久，缓存就越重、账单就越厚。<strong style="{RED}">安全与成本，是同一张账单的两面：管不住的 Agent 很贵，管得住的 Agent 也很贵。</strong></p>

<p style="{P}">历史上有过一次几乎一样的剧本。2008 到 2015 年，AWS 用连续降价把自建机房挤出市场——每一次降价都伴随一轮应用爆发（Netflix、Instagram、Airbnb 都是那一波的产物），同时让中间层的硬件商失去了定价权。DeepSeek 现在做的，是 Agent 时代的 AWS 定价动作，但它比 AWS 多了一件事：把开源当成分销渠道。MIT 许可、权重公开、48 个分片直接挂上 Hugging Face，同时官方还把自己的一套 Agent 执行框架（DeepSeek Harness，含 minimal / standard / PTC 三种模式）和 Claude Code、Codex、OpenCode、Pi 放在同一张基准表上对比——它卖的从来不只是 API，它想连「Agent 怎么跑」这件事一起定义。</p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0;">这不是价格战——这是谁有权定义 Agent 时代成本基准的争夺。</p>
</blockquote>

<h2 style="{H2}">四、反方与代价：便宜的背面是什么</h2>

<p style="{P}">一篇只讲便宜的文章是不诚实的。这次发布的质疑同样具体。</p>

<p style="{P}"><strong>第一，名字的背叛。</strong>Hacker News 上最热的一条评论直言：「552B 几乎是 V4-Flash 的两倍，这已经不算 Flash 了，基准分大涨是可以预期的。」换句话说，跑分变好有多少来自架构创新、有多少来自体量变大，官方基准表本身无法回答。</p>

<p style="{P}"><strong>第二，本地部署的门槛反而提高了。</strong>上一代 V4-Flash 是 FP4 权重、约 160GB，能塞进双 Spark 或 Strix Halo 这类设备；这一代是 FP8、约 510GB，想本地跑需要第三方量化和大约 4 台机器。有用户分享自己量化后在 128GB 内存的 Mac Studio 上以 IQ3_XXS 跑 256K 上下文，占用约 117GB——这已经属于极客操作，不是普通开发者能复制的路径。开源的分发优势，在这一代被参数量部分抵消。</p>

<p style="{P}"><strong>第三，「便宜」在渠道上常常不是真的便宜。</strong>官方文档写输出低谷 $0.60，而 Hugging Face 页面上接入的第三方推理供应商，同一模型的输出标价是 $1.20——整整贵一倍。这正是需要警惕的地方：过去几个月，多起「某模型突然降价 95%」的传闻，事后证明都是第三方平台自己贴钱引流，与厂商官方调价无关。<strong style="{RED}">看模型价格，认厂商官方文档，不要认聚合站与转售商的标价。</strong></p>

<p style="{P}"><strong>第四，「427 token/秒」这类流传的速度数字，来自第三方基准站的测试。</strong>官方并没有承诺统一吞吐——同一个模型在不同供应商那里，实测可以是 122 token/秒，也可以是 427 token/秒。速度不是模型属性，是部署属性。</p>

<p style="{P}"><strong>第五，也是最该清醒的一点：中国的开源模型之间，已经进入互相咬住的阶段。</strong>HN 上有评论说 K3 和 GLM-5.3「正在咬着他们的脚后跟」。这意味着 V4.1-Flash 的半价优势，保质期可能只有一个季度——对手下一代的定价，会立刻把它拉回均势。</p>

<p style="{P}">便宜的背面，是所有人都在同一口锅里。护城河不在价格上，价格是最先被追平的东西。</p>

<h2 style="{H2}">五、未来推演：三个还没有答案的问题</h2>

<p style="{P}"><strong style="{RED}">第一个问题：当能力差距缩到 2.5 分以内，价格还能当护城河吗？</strong></p>

<p style="{P}">Terminal-Bench 2.1 的前四名是 90.6、89.1、88.8、88.3——不到 2.5 分的差距，已经接近官方自己标注的「等价区间」。在一个能力趋同的市场上，唯一可量化的差异化就是价格；但价格也是唯一一个季度就能被抄完的差异化。于是竞争的焦点会移向别处：谁能把 Agent 的执行环境、记忆、工具链吃下来，谁才真正掌握成本与体验的定价权——这也解释了为什么模型公司纷纷开始自带 Harness。</p>

<p style="{P}"><strong style="{RED}">第二个问题：「Flash」变成旗舰之后，「旗舰」这个词还剩什么意义？</strong></p>

<p style="{P}">V4-Pro 被下位的 Flash 取代，说明「按型号大小分级」的定价体系正在崩塌。过去用户的选择题是「用大模型还是小模型」，未来的选择题会变成「要多快还是多准」，而这道题的两个选项正在被同一套架构抹平——推理强度连续可调（1 到 100），意味着快与准不再是两个模型，而是一个旋钮。当模型变成旋钮，卖模型的公司还怎么按「等级」收钱？</p>

<p style="{P}"><strong style="{RED}">第三个问题：一家每年把价格砍掉一个数量级的公司，估值该怎么算？</strong></p>

<p style="{P}">就在同一周，多家媒体报道 DeepSeek 已聘请包括中信证券在内的四家保荐机构，筹备在上海科创板的 IPO（属「据报道」级别，来源为知情人士，未获官方确认）。这带来一个没有先例的估值难题：如果按「AI 时代的基础设施」定价，它应当是万亿级平台；但如果按「模型供应商」定价，它的毛利正在被自己的降价吃掉。降得越狠，用户越多，单位利润越薄——招股书必须回答的第一个问题不是技术，而是「你打算靠什么留住的利润」。</p>

<p style="{P}">这三个问题的共同点是：它们都没有标准答案，因为答案取决于一件谁也无法预测的事——应用侧的需求，到底能不能跑赢成本下降的速度。</p>

<p style="{P}">结语留给一个更朴素的问题：今天真正被改变的，不是某家公司的价格表，而是「智能」这件事的计价方式。</p>

<p style="{P}"><strong style="{RED}">不是你想不想用便宜的模型——是当每一 token 的成本一年掉一个数量级时，还有谁有资格靠「模型更聪明」来收费。</strong></p>

<p style="{P}">你怎么看 V4.1-Flash 这次降价？它是真正的架构突破，还是一场提前到来的价格内卷？评论区聊聊。</p>

<hr style="border:none;border-top:1px solid #eee;margin:32px 0;">

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">参考来源：DeepSeek 官方发布页与 API 定价文档（2026-09-10，价格与规格为官方口径）、DeepSeek-V4.1-Flash 模型卡与官方基准表（含 Terminal-Bench 2.1 / DeepSWE v1.1 / GPQA Diamond 与 KV 缓存 890 bytes-per-token 说明）、Hacker News 讨论「DeepSeek v4.1 Flash」（641 分 / 342 评论）与「DeepSeek launching v4.1 flash」（412 分）、OpenRouter 模型定价列表（Opus-5、GPT-5.6 Sol、K3、GLM-5.3 报价，属转售渠道标价，非厂商官方文档）、Bing News 聚合报道（博通 AI 芯片营收 +221%、AMD 上调 AI 芯片市场预测至 3 万亿美元、英伟达澳洲 2GW）、CNN 报道 OpenAI 千年难题声明（88 小时 / 最多 1 万个 Agent）、Anthropic 官方研究页（四起越权事件）、METR 与 Redwood Research 独立调查报告（约 700 个 Agent）、Reuters / SCMP 关于 DeepSeek 筹备科创板 IPO 的报道。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">⚠️ 证据级别说明：模型规格、基准分数、API 价格、KV 缓存压缩比例为官方公开数据（可放心引用）；DeepSeek IPO 属「据报道」级别（知情人士，未获官方确认）；「427 token/秒」与供应商 $1.20 输出标价来自第三方渠道，非官方承诺。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">关联阅读：<a href="/articles/openai-sandbox-escape-huggingface-2026/" style="color:#e67e22;">AI 沙箱越狱：700 个 Agent 如何攻破 Hugging Face</a></p>'''

article = {
    "title": TITLE,
    "tags": TAGS,
    "date": DATE,
    "readTime": "9 分钟",
    "desc": DESC,
    "slug": SLUG,
    "content": content,
    "wechatUrl": ""
}

with open(path, encoding='utf-8') as f:
    data = json.load(f)

existing = [i for i, a in enumerate(data['articles']) if a['slug'] == SLUG]
if existing:
    article["id"] = data['articles'][existing[0]]["id"]
    data['articles'][existing[0]] = article
    print("Updated existing article at index", existing[0], "id", article["id"])
else:
    article["id"] = max(a["id"] for a in data['articles']) + 1
    data['articles'].insert(0, article)
    print("Inserted new article id=", article["id"], "at index 0")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ---- generate articles/{slug}/index.html from zuckerberg template ----
tpl_path = BASE + 'articles/zuckerberg-chinese-ai-ban-warning-2026/index.html'
with open(tpl_path, encoding='utf-8') as f:
    tpl = f.read()

repl = [
    ('Zuckerberg 对 CNN 说：不要封禁中国 AI——但这不只是一句表态', 'TITLE_PLACEHOLDER'),
    ('zuckerberg-chinese-ai-ban-warning-2026', 'SLUG_PLACEHOLDER'),
    ('Mark Zuckerberg今天对CNN说不要封禁中国AI模型。但这不是孤立表态——从Jensen第一条X到OpenAI被迫站队，从Open Secure AI Alliance到微软安全模型，这是一条七天事件链的终点。', 'DESC_PLACEHOLDER'),
    ('AI,Zuckerberg,Meta,中国AI,开放权重,CNN,深度分析', 'KW_PLACEHOLDER'),
    ('2026-07-29', 'DATE_PLACEHOLDER'),
]
for old, new in repl:
    assert old in tpl, f"template marker missing: {old[:30]}"
    tpl = tpl.replace(old, new)

tpl = (tpl.replace('TITLE_PLACEHOLDER', TITLE)
          .replace('SLUG_PLACEHOLDER', SLUG)
          .replace('DESC_PLACEHOLDER', DESC)
          .replace('KW_PLACEHOLDER', ','.join(TAGS))
          .replace('DATE_PLACEHOLDER', DATE))

assert 'Zuckerberg' not in tpl, "zuckerberg marker leftover"
assert 'zuckerberg-chinese' not in tpl, "slug marker leftover"
assert 'TITLE_PLACEHOLDER' not in tpl and 'SLUG_PLACEHOLDER' not in tpl, "placeholder leftover"
assert "var slug = '" + SLUG + "';" in tpl, "slug var missing"
assert 'window.siteData' in tpl or 'window.__YUANLAI_DATA__' in tpl, "siteData missing"

out_dir = BASE + f'articles/{SLUG}/'
os.makedirs(out_dir, exist_ok=True)
with open(out_dir + 'index.html', 'w', encoding='utf-8') as f:
    f.write(tpl)
print("index.html written:", out_dir + 'index.html')

# ---- rebuild sitemap.xml from data.json ----
static_urls = ['https://yuanlaiai.github.io/', 'https://yuanlaiai.github.io/articles.html', 'https://yuanlaiai.github.io/awesome-ai-tools/']
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in static_urls:
    lines.append(f'  <url><loc>{u}</loc></url>')
for a in data['articles']:
    lines.append(f'  <url><loc>https://yuanlaiai.github.io/articles/{a["slug"]}/</loc></url>')
lines.append('</urlset>')
with open(BASE + 'sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print("sitemap.xml rebuilt with", len(data['articles']), "articles")

# word count check on the published content
import re
clean = re.sub(r'<[^>]+>', '', content)
clean = re.sub(r'https?://\S+', '', clean).replace(' ', '').replace('\n', '')
cn = len([c for c in clean if '\u4e00' <= c <= '\u9fff'])
print("正文汉字数:", cn)
print("Total articles:", len(data['articles']))
