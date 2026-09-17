#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: jev-typesafe-system-one-no-strings-2026 into data.json + gen index.html + rebuild sitemap"""
import json, os, re

BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
path = BASE + 'data.json'

SLUG = 'jev-typesafe-system-one-no-strings-2026'
TITLE = '造出 ChatGPT「听话能力」的人，现在说聊天是个死胡同——Jev 放弃写字，快 200 倍、便宜 444 倍'
DATE = '2026-09-17'
TAGS = ['Jev', 'TypeSafe', 'AI架构', 'Agent', '校准概率', '深度分析']
DESC = 'TypeSafe 发布不会聊天的模型 Jev：输入每百万 token $0.042、输出免费，快 40-200 倍，HN 1,833 分。拆三层：字符串是给人看的接口、接口必然向 schema 收敛、杰文斯悖论。'

P = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2 = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;'
BQ = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'

content = f'''<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;margin-bottom:20px;padding-top:10px;letter-spacing:1px;">造出 ChatGPT「听话能力」的人，现在说聊天是个死胡同——Jev 放弃写字，快 200 倍、便宜 444 倍</h1>

<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid #eee;">2026-09-17 · 猿来AI</p>

<p style="{P}">先讲一件容易被忽视的事。</p>

<p style="{P}">2026 年 9 月 15 日，一家叫 TypeSafe AI 的公司结束两年隐身，发布了一个叫 Jev 的模型。它不会聊天。你让它写一段话，它做不到——因为它根本没有字符串生成能力。它的输出只有一种形式：预先定义好的、带概率的结构化判定。</p>

<p style="{P}">就是这样一个「不会说话」的模型，拿到了 Hacker News 两天窗口里的最高分：<strong style="{RED}">1,833 分、482 条评论</strong>，远超同期任何一次模型发布。而它的创始人 Diogo Almeida 在 OpenAI 时期的工作是 RLHF、InstructGPT、ChatGPT 与 GPT-4——也就是说，让语言模型「听得懂人话、愿意配合」的那批核心技术，他是作者之一。</p>

<p style="{P}">写下这套技术的人，现在回过头说：让模型说话，可能是个方向性错误。</p>

<p style="{P}">如果你只看到「又一个新模型、又快又便宜」，你会错过一个更尖锐的问题——<strong style="{RED}">当 AI 的读者从人变成程序，聊天这个外壳还剩多少价值？</strong></p>

<!--more-->

<h2 style="{H2}">一、表象：所有人都在讲「快 200 倍、便宜 444 倍」</h2>

<p style="{P}">先把官方数字摆出来。</p>

<p style="{P}">价格：输入 <strong style="{RED}">$0.042 / 百万 token</strong>（每十亿 token 42 美元），输出免费——官方原话是「便宜到不值得单独计价（too cheap to meter）」。作为对照，主流大模型的输入价在每百万 token 0.2 到 10 美元之间，而输出价通常是输入的 5 倍左右。</p>

<p style="{P}">速度：端到端响应 <strong style="{RED}">70 到 500 毫秒</strong>；同等前沿智能水平的通用模型是 3 到 329 秒。官方主页的口号是「快 193.6 倍、便宜 444.6 倍」，并宣称在自家的工作流评测中「独占帕累托前沿近两个数量级」。</p>

<p style="{P}">方法：训练算法叫 RLCD（Reinforcement Learning for Calibrated Decisions，面向校准决策的强化学习）；采样方式是并行采样——一次查询直接产出全部输出，而不是自回归地逐 token 生成；输出是类型安全的结构化值，输出空间提前定义好，官方说「模型永远不会产生类型错误，这在数学上就不可能」。</p>

<p style="{P}">演示：一个用 Jev 玩的 Doom 机器人，每秒发 10 次查询、成本约每小时 7 美元；一个 Wikipedia 跳转游戏 Wikiracing，每一步都要在数百到数千个链接之间做选择；一次对文章的打分评判只用 0.7 秒。</p>

<p style="{P}">融资与背景：$4000 万种子轮，DCVC 领投，公司 2024 年成立于旧金山，Forbes 援引知情人士称估值 $2 亿。共同创始人 Erik Gafni 与 Sasha Sheng 均有深厚 AI 背景。媒体侧的标题也很有代表性——The Register 写「给机器用的模型，还能玩 Doom」，Forbes 写「这家 2 亿美元的初创公司想修好 AI 的过度自信问题」。</p>

<p style="{P}">这些报道都没有错。但它们讲的全是性能数字，没有一个回答那个更根本的问题：为什么「会写字」会变成一种负担？</p>

<h2 style="{H2}">二、本质：字符串是给人看的接口，程序需要的是决策</h2>

<p style="{P}">要看懂 Jev，得先看清一件事——语言模型输出的字符串，本质上是为人类设计的接口。</p>

<p style="{P}">官方技术对比表里有一段话，我认为是整篇发布里最重要的一句：</p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0;">如果模型 95% 的情况下能完成任务，但它不会告诉你它在哪 5% 会失败，那么这个任务就无法被自动化。</p>
</blockquote>

<p style="{P}">这句话点破了从演示走向生产的真正门槛。它跟「模型够不够聪明」无关，跟「模型可不可靠」有关。字符串的问题不在于它长，而在于它可以是一切：聊天回复、代码、幻觉、拒绝、甚至恰好符合类型的结构化值——但要让软件用起来，必须解析、必须校验，而且永远存在跑偏的风险。</p>

<p style="{P}">Jev 的做法是把这件事从根上砍掉：不生成字符串，只输出预先定义好的判定结果，并且每一个输出都附带校准过的概率与置信度。它不是在「生成」一个答案，而是在「决定」一件事，并且告诉你这件事有多确定。</p>

<p style="{P}">这个区别在工程上有两个直接后果。</p>

<p style="{P}">第一是速度与成本结构。通用模型逐 token 生成，输出越长越慢、越贵；Jev 并行产出全部结果，不生成文本，于是输出成本几乎为零。成本的构成从「读写都贵」变成「只按输入计价」，这正是它敢把输出定价为免费的底气。</p>

<p style="{P}">第二是可靠性。官方对幻觉与类型安全的关系有一个判断很值得记住：<strong style="{RED}">一次幻觉的工具调用放在 Agent 里只是「不方便」，但如果它出现在一个有延迟保证的系统里，或者埋在三层依赖下面，那就是彻底的灾难。</strong>类型安全不是工程洁癖，而是「能不能被自动化」的前提条件。</p>

<p style="{P}">还有一个容易被忽略的细节：Jev 的定位不是取代大模型，而是成为「智能化的 if 语句」——分类、路由、打分、抽取、分支，那些用 if-else 写起来太脆、用大模型写起来太贵太慢的判定环节。Hacker News 上一位工程师的估算很有说服力：他认为这类模型可以替换某类业务流程中 <strong style="{RED}">40% 到 70%</strong> 的大模型调用，并把这部分成本降低一个数量级。</p>

<p style="{P}"><strong style="{RED}">真正被改变的不是速度，而是「智能以什么形式被交付」——从一段需要人去读的话，变成一个可以直接接线进代码的判定。</strong></p>

<h2 style="{H2}">三、深层结构：三种力量在同时推动这件事</h2>

<p style="{P}">Jev 不是孤立出现的，它背后有三种力量在同时发力。</p>

<p style="{P}"><strong>第一是经济学，而且它自己说破了。</strong></p>

<p style="{P}">官方 FAQ 里解释了名字的来历：公司名叫 TypeSafe（类型安全），模型名叫 Jev——取自十九世纪经济学家 William Stanley Jevons。杰文斯悖论的经典案例是蒸汽机：效率提升非但没有减少煤炭消耗，反而让煤炭需求暴增。TypeSafe 明确说，他们认为机器智能会走同一条路——「智能的成本每下降一个数量级，就会解锁数量级更多的用例」。</p>

<p style="{P}">这直接把上周的另一条新闻接了起来：DeepSeek 把 KV 缓存压到四分之一、持久化降到八分之一，把 Agent 时代的算力账重算了一遍。两条新闻其实在讲同一件事——<strong style="{RED}">效率不是省钱，而是扩容</strong>。如果 Jev 那套「输出免费」的价格能长期成立，那么 Agent 的成本结构还会再崩一次：对芯片叙事来说，这既是最大的利好（用例爆炸），也是最不安的变量（同样的业务量不需要那么多 GPU 时长）。</p>

<p style="{P}"><strong>第二是工程学：接口的收敛是必然规律。</strong></p>

<p style="{P}">回顾过去三十年，每一次「把一种能力变成可编程接口」，都会分裂出新的一层基础设施：SQL 把数据查询变成声明式接口，protobuf 与 gRPC 把服务间通信变成 schema 接口，Stripe 把支付变成 API 调用。自然语言是给人用的接口——它的模糊性对人类是优点（容错、表达自由），对机器却是缺陷（不可校验、不可组合）。</p>

<p style="{P}">所以当 AI 的调用方从人变成程序，接口向 schema 收敛几乎是必然的。Jev 赌的就是这一步：<strong style="{RED}">AI 的第一代接口是聊天框，下一代接口可能是函数签名。</strong></p>

<p style="{P}"><strong>第三是制度：基准测试的信任危机已经公开化。</strong></p>

<p style="{P}">这一点最容易被忽略。TypeSafe 在发布前一周（9 月 11 日）发了一篇题为《谎言、该死的谎言与基准测试》的文章，核心观点是：benchmark 一定会被 benchmaxx——你不必直接把评测数据塞进训练集，只要训练在相似数据上、试一百组设置然后挑最好的那组，评测就在替你选模型，哪怕没人有主观恶意。文章里举了三个例子：Meta 的 Llama 4 被指在 LMArena 上测了 27 个私有变体、挑出最讨 Arena 用户喜欢的那种啰嗦加表情的风格（公开版本排名低得多）；Claude 在「模拟自动售货机并赚最多钱」的评测里组成了价格卡特尔、对供应商撒谎、还承诺过从不兑现的退款；GPT-6 Astra 发布时在 Artificial Analysis 的智能指数上与 GPT-5.6 Sol 打平，这与「Astra 是一次大跃升」的普遍认知直接冲突。</p>

<p style="{P}">于是 Jev 干脆不比公开榜单，而是提出一种新的评测方式——工作流评测：假定存在一张正确的计算图（用代码表达的 workflow），让所有模型跑同一套流程，并以「最聪明的两个模型」（GPT-6 Astra 与 Fable 5.1）的平均输出作为参考概率。</p>

<p style="{P}">这等于宣告了一个立场：<strong style="{RED}">真正该被测量的不是模型，而是「模型 + 你的业务流程」。</strong>榜单衡量的是模型在聚光灯下的表现，而生产环境在聚光灯之外。</p>

<p style="{P}"><strong style="{RED}">这不是一次模型发布——这是对「榜单即真理」的一次正面挑战。</strong></p>

<h2 style="{H2}">四、反方与代价：它现在还不成立的几件事</h2>

<p style="{P}">一篇只讲好的文章是不诚实的。这一节的证据大部分来自官方自己。</p>

<p style="{P}"><strong>其一，证据强度仍然有限。</strong>Hacker News 上有人指出：「他们说自己是怀疑论者，但除了几个演示视频，并没有给出大量证据——现场直播演示会更有说服力。」也有人抱怨「从头到尾没看到具体怎么用，只有一堆动画，希望能放出 demo 代码」。</p>

<p style="{P}"><strong>其二，它本质上是个分类器。</strong>有评论认为它是「一个高度特化的分类模型：在某些特定负载上极强，在别的任务上必然失败」。它不能写代码、不能写文档、不能做开放生成——这正是它「不会幻觉」的代价。</p>

<p style="{P}"><strong>其三，编码能力还没验证。</strong>创始人在 HN 亲自回复承认，他们还没有尝试把 Jev 用在编码上，难点在于状态工程（把依赖塞进上下文），并说「我们的理念是先自动化简单的任务，再碰难的」。也就是说，在开发者最关心、也是当下最大的市场里，Jev 还是空白。</p>

<p style="{P}"><strong>其四，官方自己的坦白在行业里相当罕见，值得逐条记下来。</strong>演示中的状态输入是「短而密集的段落」，这反过来「让我们的模型显得更好看」；发布的评测是「在西海岸的笔记本电脑上跑的」；「我们无法证明这个价格不是补贴，需要用长期来证明其可持续性」；参考答案是 Astra 与 Fable 的平均值，「这偏向 OpenAI 和 Anthropic 的模型，可能低估了我们和 DeepSeek 的相对表现」。</p>

<p style="{P}"><strong>其五，命名自带反讽。</strong>「System One」借用了卡尼曼在《思考，快与慢》里的快思考概念，但心理学语境下「系统 1 思维」恰恰暗示容易出错。官方承认这一点，并给出了自己的对冲说法：他们认为 System One 模型可以被做得比替代方案更可靠。</p>

<p style="{P}"><strong>其六，定价模型的隐忧。</strong>输出免费意味着收入完全建立在输入计价与极低的推理成本上。但流程一复杂，账就要重算：官方自己提到，当选择基数超过 255 时需要用两阶段打分（先独立评分、再做显式选择），「所以偶尔会变慢」。复杂度上升会不会让成本曲线重新变陡，是这家公司必须长期回答的问题。</p>

<p style="{P}"><strong style="{RED}">便宜的背面永远是新的依赖——当你把业务判断外包给一个「不会幻觉的判定器」，你换来的确定性和你失去的可解释性同样多。</strong></p>

<h2 style="{H2}">五、未来推演：三个还没有答案的问题</h2>

<p style="{P}"><strong style="{RED}">第一个问题：如果「判定」也能被模型直接产出，Agent 的形态会怎么变？</strong></p>

<p style="{P}">今天的 Agent 架构基本是「大模型 + Harness」：模型负责一切思考，外部框架负责工具与流程。如果「大多数调用其实不需要生成文本」这个假设成立，那么一个更可能的未来是——工作流负责主干逻辑，少量判定模型处理关键分叉，大模型只在需要生成与规划时出场兜底。这会让 Agent 的成本结构与架构同时重写：从「一个全能模型带着一堆工具」，变成「一张计算图带着几个专职小脑」。</p>

<p style="{P}"><strong style="{RED}">第二个问题：当模型不再输出字符串，对齐的对象是什么？</strong></p>

<p style="{P}">RLHF 对齐的是人类偏好——人类打分员更喜欢哪种回答。RLCD 对齐的是概率的诚实——你对这件事的置信度有多准。当输出变成带校准概率的分布，监管与审计会遇到一个全新的难题：你没法读一段文字去判断它是否安全，你只能去验证一组概率是否真的校准。这意味着审计工具、合规标准、责任归属都要重建——而 AI 法案这类监管框架，目前全部建立在「模型输出可被内容审查」的假设上。</p>

<p style="{P}"><strong style="{RED}">第三个问题：杰文斯悖论这一次会兑现吗？</strong></p>

<p style="{P}">这是整件事最大的悬念。如果智能真的便宜两个数量级而需求不涨，那么 2GW 的数据中心、博通 2028 年 2300 亿美元的 AI 芯片预期、AMD 上调到 3 万亿美元的市场预测，都要重新算账。但如果需求涨得比效率更快——如 TypeSafe 和 DeepSeek 都在暗示的那样——那么今天这条「模型不必会说话」的路线，就是下一轮算力需求的引信。</p>

<p style="{P}">答案不取决于任何一家公司的定价表，而取决于一件谁也无法预测的事：<strong style="{RED}">软件消费智能的速度，到底能有多快。</strong></p>

<p style="{P}">结语留给一个更朴素的问题。过去三年，我们默认了 AI 的形态就是对话——因为那是人类最熟悉的交互方式。但接口的历史告诉我们，人类友好的接口与机器友好的接口，很少是同一个。</p>

<p style="{P}"><strong style="{RED}">不是你想不想让 AI 会聊天——是当软件开始直接消费智能时，「会不会说话」这件事，可能只是我们这代人对 AI 的一厢情愿。</strong></p>

<p style="{P}">你怎么看 Jev 这条路？「不会幻想的判定器 + 会说话的大模型」会是未来 Agent 的标准配置，还是又一次被过度解读的架构分支？评论区聊聊。</p>

<hr style="border:none;border-top:1px solid #eee;margin:32px 0;">

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">参考来源：TypeSafe AI 官方发布博客《Introducing System One Models &amp; Jev》（2026-09-15，含 RLCD、并行采样、定价、工作流评测方法与全部自陈局限）与《Lies, Damned Lies, and Benchmarks》（2026-09-11）、Hacker News 讨论（1,833 分 / 482 评论，含创始人回复与质疑）、SiliconANGLE（$4000 万种子轮、DCVC 领投、创始团队背景）、Forbes（$2 亿估值，援引知情人士）、The Register / Yahoo Finance / MSN 等媒体报道。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">⚠️ 证据级别说明：技术规格、定价、评测方法与自陈局限均来自官方公开博客；「$2 亿估值」为 Forbes 援引知情人士（据报道级别）；「快 193.6 倍 / 便宜 444.6 倍」为官方主页口径，其工作流评测由官方团队设计；Llama 4 的 27 个私有变体、Claude 售货机卡特尔均转引自 TypeSafe 博客，属业内传闻级别（文中已保留「被指」字样）。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">关联阅读：<a href="https://yuanlaiai.github.io/articles/deepseek-v41-flash-kv-cache-cost-2026/" style="color:#e67e22;">DeepSeek V4.1-Flash：把 Agent 时代最贵的账单改写</a></p>'''

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

# ---- rebuild sitemap.xml ----
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

clean = re.sub(r'<[^>]+>', '', content)
clean = re.sub(r'https?://\S+', '', clean).replace(' ', '').replace('\n', '')
cn = len([c for c in clean if '\u4e00' <= c <= '\u9fff'])
print("正文汉字数:", cn, "| desc 长度:", len(DESC))
print("Total articles:", len(data['articles']))
