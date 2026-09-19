#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: agent-code-review-rework-tax-2026 into data.json + gen index.html + rebuild sitemap"""
import json, os, re

BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
path = BASE + 'data.json'

SLUG = 'agent-code-review-rework-tax-2026'
TITLE = 'AI 写的代码评分更高，生产事故却更多——当「验收」成为新瓶颈，给 Agent 立规矩就是最值钱的生意'
DATE = '2026-09-19'
TAGS = ['AI编程', '代码审查', '返工税', 'Cloudflare', 'Agent', '深度分析']
DESC = 'AI 让写代码变便宜，却让「确认代码能用」变贵：Cloudflare 审计技能三天翻倍、阿里 code-review 四连登，而 AI 代码评审分更高、生产事故更多。'

P = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2 = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;'
BQ = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'

content = f'''<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;margin-bottom:20px;padding-top:10px;letter-spacing:1px;">AI 写的代码评分更高，生产事故却更多——当「验收」成为新瓶颈，给 Agent 立规矩就是最值钱的生意</h1>

<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid #eee;">2026-09-19 · 猿来AI</p>

<p style="{P}">先讲一件容易被忽视的事。</p>

<p style="{P}">2026 年 9 月 17 日到 19 日，GitHub 趋势榜的榜首连续三天被两个「审查代码」的项目占着：Cloudflare 的安全审计技能三天从 7,054 星涨到 14,072 星，两天翻一倍；阿里的代码审查工具四连登，从 7 月底的 14,772 星涨到 36,828 星。同期还有一个做「规格驱动开发」的项目以 69,420 星首次上榜。</p>

<p style="{P}">它们都不是模型，不谈智能，只谈规矩——而且都在讲同一件事：<strong style="{RED}">别让 AI 直接写代码，先立规矩，再有门禁。</strong></p>

<p style="{P}">与此同时出现了一份更反直觉的报告。New Relic 在其 AI 相关发布中指出：AI 生成的代码在评审环节得分更高，但引发的生产事故在上升。翻译成人话就是：<strong style="{RED}">检查流程说「没问题」的代码，到线上出事了。</strong></p>

<p style="{P}">如果你只看到「AI 编程工具又火了」，你就会错过这条真正重要的分界线——AI 让写代码变便宜了，但让「确认代码能用」变贵了。</p>

<!--more-->

<h2 style="{H2}">一、表象：史上最强的代码生成能力，撞上了最快的评审队列</h2>

<p style="{P}">先看 AI 写代码这一侧有多猛。</p>

<p style="{P}">BairesDev 的调查显示，把一半以上代码交给 AI 写、而且是直接采用的开发者比例，一年内从 <strong style="{RED}">12% 涨到 42%</strong>；微软的研究发现 AI 编码 Agent 让团队提交的 PR 数量提升了 <strong style="{RED}">24%</strong>；Black Duck 的调研说 AI 编码在企业里的采用率已达 <strong style="{RED}">97%</strong>。三条曲线指向同一个结论：代码产量正在指数级增长。</p>

<p style="{P}">问题出在另一边。Cloudflare 在官方博客里给了一段很诚实的自述：在他们内部项目里，<strong style="{RED}">合并请求等待首次评审的中位时间常常以小时计</strong>——一个 MR 排在队列里，评审人终于切过来看 diff，留下几条变量命名的吹毛求疵，作者回应，循环再来一遍。</p>

<p style="{P}">他们当然试过 AI。而且路径和大多数人一样：先试现成的 AI 代码审查工具——结论是「很多工具其实相当不错，甚至可以配置」，但对 Cloudflare 这个规模的组织来说灵活性不够；于是退到第二方案：把 git diff 塞进一个半成品的提示词里，让大模型找 bug。结果「噪音和你想的一模一样」——满屏含糊的建议、<strong style="{RED}">幻觉出来的语法错误</strong>，以及对一个<strong style="{RED}">已经有错误处理的函数</strong>建议「考虑加上错误处理」。</p>

<p style="{P}">而市场已经给这件事定了价。AI 代码审查平台 CodeRabbit 以 <strong style="{RED}">15 亿美元估值</strong>完成 <strong style="{RED}">1.43 亿美元</strong> C 轮，官方叙事是帮公司「驾驭 AI 生成代码的爆炸」，收入一年增长超过 5 倍。</p>

<p style="{P}">再回到成本这一侧。Tech.co 对 300 家中小企业负责人和 C 层的调查给出了一个精确的数字：<strong style="{RED}">每使用 AI 一小时，平均有 16 分钟被用来审阅、修改和核实 AI 的产出——相当于「省下来的时间」里的 26% 被返工吃掉。</strong>按时薪 40 美元计算，等于每小时损失 10.55 美元。他们把这称作「AI 返工税」（AI rework tax）。</p>

<p style="{P}">这些报道和数字都没有错。但都停留在「效率高低」的层面，没有一个回答那个更难的问题：为什么模型越强，围绕它的检查反而越贵？</p>

<h2 style="{H2}">二、本质：瓶颈从「生产」转移到了「验收」</h2>

<p style="{P}">答案藏在一条老掉牙的经济学里：<strong style="{RED}">当某个环节的边际成本趋零，瓶颈必然转移到它的下游。</strong></p>

<p style="{P}">写代码的成本正在趋零。一个 Agent 可以在几分钟内产出一个功能、一套测试、一份重构方案。但「这段代码能不能上线」这个判断，仍然需要有人——或者有东西——去看懂它、验证它、并且为结论负责。而产出速度上去了，判断速度没变，于是所有压力都堆到了验收环节。</p>

<p style="{P}">Cloudflare 描述的那个队列，就是这条规律最朴素的样子：写代码的人（现在是 AI）变多了，评审的人还是那些。</p>

<p style="{P}">关键点在于，返工并不只是浪费。Tech.co 的调查里有一个格外反直觉的发现：<strong style="{RED}">花更多时间返工的公司，整体生产率提升反而更高</strong>；而那些几乎不返工的群体，恰恰是收益最低的。这说明返工本质上是一种必要投资——它不是「AI 不行」，而是「AI 需要被验收」。</p>

<p style="{P}">问题在于，目前这笔投资是<strong style="{RED}">被动、零散、无法复用</strong>的：每个人凭个人经验去核对，同样的错误在十个团队里重复十遍。</p>

<p style="{P}">于是我们就看到了这三天霸榜的三个项目，它们其实是同一件事的三个时间点：</p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0 0 8px;">事前 · <strong style="{RED}">OpenSpec</strong>（规格驱动开发，69.4K★）——先让 AI 把「要做什么」写成规格，你确认之后才允许动手，把最贵的返工成本挪到最便宜的一步。</p>
<p style="font-size:15px;line-height:1.8;margin:0 0 8px;">事中 · <strong style="{RED}">agent-skills</strong>（96.5K★）——把资深工程师的工作流固化成六个阶段：定义 → 规划 → 构建 → 验证 → 评审 → 发布，每个阶段都有质量门禁。</p>
<p style="font-size:15px;line-height:1.8;margin:0;">事后 · <strong style="{RED}">阿里 code-review</strong>（36.8K★）与 <strong style="{RED}">Cloudflare 安全审计技能</strong>（14.1K★）——用确定性规则加 Agent 混合的方式做行级审查与六阶段安全审计。</p>
</blockquote>

<p style="{P}">再加上 AWS 推出的规格驱动 IDE Kiro、GitHub 的 Spec Kit——大厂和创业公司同时扑向同一块地方：<strong style="{RED}">不是让 AI 写出更多代码，而是让 AI 的产出可以被验证。</strong></p>

<p style="{P}">真正被改变的，是「什么能力最值钱」：AI 时代最贵的能力不是写代码，而是判断代码能不能过。</p>

<h2 style="{H2}">三、深层结构：三种力量在同时推动这场「验收军备竞赛」</h2>

<p style="{P}"><strong>第一是经济学：验收产能成了新的稀缺资源。</strong></p>

<p style="{P}">这不是 IT 行业独有的剧本。制造业经历过一次几乎一模一样的转折：当装配线让产量暴涨，工匠自检就失效了，于是「独立质检部门」和「统计过程控制」成为独立学科，质量不再由生产者自己说了算。软件行业也走过两步——CI/CD 让自动化测试独立成工具链，云时代让可观测性从日志升级成一个产业（Datadog、Splunk 都是那个转折的产物）。</p>

<p style="{P}">现在轮到「AI 产出的验收」。CodeRabbit 的 15 亿美元估值、Cloudflare 与阿里的开源方法论，都是这条新产业链的早期定价。</p>

<p style="{P}"><strong>第二是工程学：为什么「多智能体 + 协调者」正在成为标准架构。</strong></p>

<p style="{P}">Cloudflare 的方案很值得抄作业：当工程师提交合并请求时，不是一个模型给出一个长回答，而是<strong style="{RED}">最多七个专职评审员分头行动</strong>——安全、性能、代码质量、文档、发布管理、合规各有其人，再由一个<strong style="{RED}">协调 Agent</strong>负责去重、判断问题的真实严重程度，最后只发出一条结构化的评审评论。这套系统已经跑过了数万个合并请求，会批准干净的代码、拦截真正的严重问题。</p>

<p style="{P}">阿里的思路异曲同工：确定性管线负责规则能覆盖的硬缺陷（空指针、线程安全、XSS、SQL 注入），LLM Agent 负责语义层面的问题。</p>

<p style="{P}">两者的共同点是把「评审」拆成可验证的环节，而不是让一个大模型一次性给结论。这与上周 TypeSafe 发布 Jev 时讲的道理完全一致——让模型输出带校准概率的判定，而不是一段需要人去解读的文字。方向是同一个：<strong style="{RED}">把判断变成可验证的结构化事实。</strong></p>

<p style="{P}"><strong>第三是制度：当评审本身失效，信任链条就空转了。</strong></p>

<p style="{P}">这才是最值得警惕的部分。New Relic 那份观察里最刺眼的一句是：AI 生成的代码在评审里得分更高，生产事故却在增加。</p>

<p style="{P}">为什么会这样？因为评审制度的设计前提是「人写的代码需要另一个懂行的人来判断是否可信」。而在新的工作流里，代码由 AI 写、评审也由 AI 做——如果两边同源，就会出现系统性的共同盲区：它们对同一类错误同样视而不见，而评审打出的高分反而给了团队虚假的安全感。Cloudflare 那句「幻觉出来的语法错误」正是这类盲区的直观证据。</p>

<p style="{P}">于是审计与合规必须重建。这也能解释为什么同期监管讨论异常密集：参议院在调查 Agent 越狱事件、Anthropic 在指控竞争对手蒸馏、各国在收紧数据出境。当写代码和查代码都交给机器，「谁为这行代码负责」就从一个技术问题变成了法律问题——而这正是企业采购时最保守、最舍得花钱的地方。</p>

<p style="{P}"><strong style="{RED}">这不是工具潮——这是验收产能的军备竞赛。</strong></p>

<h2 style="{H2}">四、反方与代价：给 AI 立规矩的生意，也有它的软肋</h2>

<p style="{P}">一篇只讲趋势的文章是不诚实的。这场「规矩生意」至少有四道裂缝。</p>

<p style="{P}"><strong>其一，成本和噪音可能比想象中大。</strong>Hacker News 上有一篇「我取消了 AI 代码审查订阅，自己写了个免费的本地版」的帖子（23 分、32 条评论），讨论的核心正是价值与价格的错配。Cloudflare 自述的「满屏含糊建议」也说明：<strong style="{RED}">通用模型直接审查代码基本不可用</strong>，必须要有一层规则与编排——而这层东西只有真正跑过大规模代码库的组织才做得出来。这也解释了为什么近期霸榜的都是大厂项目：个人项目很难积累出可用的规则集。</p>

<p style="{P}"><strong>其二，评审的价值不只是找 bug。</strong>有开发者撰文指出「AI 让代码评审失去了对齐功能」（19 分讨论）：评审原本还承担着知识传播、让新人理解系统、团队在关键决策上达成共识的功能。把评审外包给 Agent，效率上去了，但这些隐性的组织收益会一起消失。这是一个很难量化、却极其真实的代价。</p>

<p style="{P}"><strong>其三，数据本身有水分，引用要小心。</strong>「26% 返工税」来自 300 家中小企业的样本，规模有限；New Relic 的「评分更高、事故更多」属厂商报告口径，不是同行评审的学术研究；那篇广为流传的「43% 的 AI 生成代码改动需要到生产环境调试」调查是 4 月发布的，距今已有五个月。这些数字可以用来指方向，但不能当作精确结论。</p>

<p style="{P}"><strong>其四，规则本身会变成新的技术债。</strong>给 Agent 加门禁、加规则、加评审员，短期有效；但规则会膨胀、会互相冲突、会随业务变化而失效——这就是行业里开始被讨论的「Agent 债」（agent debt）。Cloudflare 之所以把架构做成插件式、让 VCS 与 AI 供应商都可替换，正是因为他们清楚：今天立的规矩，半年后大概需要重写。</p>

<p style="{P}"><strong style="{RED}">给 AI 立规矩的生意，最终会变成「谁能维护最不臃肿的规则库」的竞赛。</strong></p>

<h2 style="{H2}">五、未来推演：三个还没有答案的问题</h2>

<p style="{P}"><strong style="{RED}">第一个问题：如果「验收」独立成一个产业，谁掌握标准？</strong></p>

<p style="{P}">现在有两条路线在并行。一条是创业公司卖服务——CodeRabbit 拿到 15 亿美元估值，收入一年涨 5 倍多；另一条是大厂开源方法论——Cloudflare 直接把自家漏洞发现系统的源头版本放出来，阿里开源了整套规则集与混合架构。前者卖的是「你不需要自己建」，后者赌的是「标准由我先定义」。历史经验是两条路都会活下来，但标准最终会落在开源那条线上——因为验收的核心资产是可审计的规则，而可审计意味着必须能被看见。</p>

<p style="{P}"><strong style="{RED}">第二个问题：「评审分更高、事故更多」这个悖论怎么解？</strong></p>

<p style="{P}">最可能的答案是分工与隔离——就像财务审计要求外部事务所、不能自己审自己。评审 AI 与被评审的 AI 必须来自不同厂商、不同架构，甚至使用不同类型的模型（一个生成、一个判定）。这也意味着未来每个工程团队都会需要一份「模型审计矩阵」：谁写的代码，必须由谁（或者至少由哪一类模型）来查。这件事目前还没有人在产品层面认真做。</p>

<p style="{P}"><strong style="{RED}">第三个问题：当审查也被自动化，人类最后把关的那一环还剩什么？</strong></p>

<p style="{P}">可能是目标本身——「这件事该不该做、优先级是什么、什么代价可以接受」。这恰好与上周 Jev 那篇文章的结论互锁：机器负责判定，人类负责提问。技术文档、评审意见、测试用例都可以由 AI 生成，但「要不要为了这个功能承担这次上线的风险」，这句话至今没有机器能替你说。</p>

<p style="{P}">结语留一个更朴素的问题。过去两年，我们一直在庆祝 AI 写代码的能力：更快的补全、更准的重构、更长的上下文。而 2026 年 9 月这份榜单和这些数据，第一次把另一面摊在了桌面上——<strong style="{RED}">产能过剩的地方，必然出现验收危机。</strong></p>

<p style="{P}"><strong style="{RED}">不是你想不想让 AI 写代码——是当审查也交给 AI 时，还有谁能为「这行代码该不该上线」签字。</strong></p>

<p style="{P}">你怎么看这场「验收军备竞赛」？在你所在的团队里，返工税大概占多少？评论区聊聊。</p>

<hr style="border:none;border-top:1px solid #eee;margin:32px 0;">

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">参考来源：Cloudflare 官方博客《Orchestrating AI Code Review at scale》（七专职评审员 + 协调 Agent 架构、数万个合并请求实践、首次评审等待以小时计、naive prompt 失败细节，HN 145 分 / 56 评论）、阿里 open-code-review 仓库（HN 284 分 / 73 评论，7-28 首登 14,772★ → 9-19 达 36,828★）、GitHub 趋势榜 9-17 至 9-19 数据（Cloudflare 审计技能 7,054★ → 14,072★；OpenSpec 69,420★；agent-skills 96,489★）、Tech.co「AI rework tax」调查（300 家 SMB 样本）、New Relic 相关发布（评审得分更高但生产事故上升、AI 已触及企业约四分之三代码、agent debt 提法）、BairesDev 开发者调查（12% → 42%）、微软研究（PR 数量 +24%）、Black Duck 调研（采用率 97%）、CodeRabbit C 轮融资报道（1.43 亿美元 / 15 亿美元估值 / 收入增长 5 倍以上）。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">⚠️ 证据级别说明：Cloudflare 的架构与自述来自其官方博客（可放心引用）；「26% 返工税」为 300 家 SMB 问卷结果（样本有限）；New Relic 的「评分更高、事故更多」为厂商报告口径，非同行评审研究；「AI 返工税」是媒体提出的概念而非学术术语；另有「43% 的 AI 生成代码需生产调试」的调查为 2026 年 4 月发布（较旧），未作为主要论据。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">关联阅读：<a href="https://yuanlaiai.github.io/articles/jev-typesafe-system-one-no-strings-2026/" style="color:#e67e22;">Jev：放弃写字的模型，为什么不会聊天反而登顶 HN</a></p>'''

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
print("正文汉字数:", cn, "| desc 长度:", len(DESC), "| 表格标签 <ul>:", content.count('<ul'), "| 相对链接:", len(re.findall(r'href="/', content)))
print("Total articles:", len(data['articles']))
