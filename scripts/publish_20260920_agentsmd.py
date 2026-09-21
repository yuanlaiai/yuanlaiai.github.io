#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: agents-md-standard-war-2026 into data.json + gen index.html + rebuild sitemap"""
import json, os, re

BASE = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/'
path = BASE + 'data.json'

SLUG = 'agents-md-standard-war-2026'
TITLE = 'Shopify CEO 威胁封杀 Claude Code，三周半后 Anthropic 让步——一份 Markdown 文件凭什么撬动巨头？'
DATE = '2026-09-20'
TAGS = ['AI Agent', '开源生态']
DESC = 'Shopify CEO 因一个 Markdown 文件威胁封杀 Claude Code，三周半后 Anthropic 让步：更新日志里那句「没有 CLAUDE.md 才读 AGENTS.md」，藏着默认权之争。'

P = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2 = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;'
BQ = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'

content = f'''<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;margin-bottom:20px;padding-top:10px;letter-spacing:1px;">Shopify CEO 威胁封杀 Claude Code，三周半后 Anthropic 让步——一份 Markdown 文件凭什么撬动巨头？</h1>

<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid #eee;">2026-09-20 · 猿来AI</p>

<p style="{P}">先讲一件容易被忽视的事。</p>

<p style="{P}">2026 年 8 月 25 日，Shopify 的 CEO Tobi Lütke 在 X 上发了一条帖子。他没有抱怨模型不够聪明，也没有抱怨价格——他抱怨的是一个 Markdown 文件：</p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0;">我在考虑在 Shopify 封杀 Claude Code，直到他们改变主意、开始读 AGENTS.md 和 .agents/skills。</p>
</blockquote>

<p style="{P}">三周半之后的 9 月 18 日，Anthropic 发布 Claude Code 2.1.277，更新日志里多了一行：在一个没有 CLAUDE.md 的项目里，Claude Code 改为读取 AGENTS.md。</p>

<p style="{P}">这条消息在 Hacker News 拿到 <strong style="{RED}">723 分、272 条评论</strong>。媒体的一致标题是「Anthropic 终于加入了跨工具的 AI 编码标准」。</p>

<p style="{P}">但这件事的真正看点不在「加入了什么」，而在「以什么方式加入」——那是一句经过精确计算的更新日志。</p>

<!--more-->

<h2 style="{H2}">一、表象：一个文件，一场大厂让步</h2>

<p style="{P}">先说清楚 AGENTS.md 是什么。按它官方网站的说法，定位只有一句话：README 是给人看的（快速开始、项目介绍、贡献指南），AGENTS.md 是给编码 Agent 看的——构建步骤、测试命令、代码约定，这些放进 README 会显得臃肿、而对人类贡献者又不重要的东西。官网还有一句刻意的表态：「与其再引入一个专有文件，我们选择了一个任何人都能用的名字和格式。」</p>

<p style="{P}">它确实被广泛采用了。官网列出的支持名单是一整面墙：OpenAI 的 Codex、Google 的 Jules 和 Gemini CLI、Cognition 的 Devin 和 Windsurf、JetBrains 的 Junie、GitHub 的 Copilot 编码 Agent、Cursor、Amp、Zed、Warp、Aider、goose、opencode、RooCode、Semgrep、UiPath、Ona、Augment Code……<strong style="{RED}">二十多个工具与产品</strong>。</p>

<p style="{P}">在这面墙上，Anthropic 长时间是最大的缺席者——而且据 The New Stack 的报道，<strong style="{RED}">要求 Claude Code 支持 AGENTS.md 的功能请求此前已经被官方关闭过</strong>。Anthropic 的答案是自己的 CLAUDE.md，一份同样好用的私有配置。</p>

<p style="{P}">直到 Shopify 的 CEO 公开发难。</p>

<p style="{P}">对一家有数千名开发者、全都工作在一个巨大 monorepo 里的公司来说，这件事不是审美问题。Lütke 在后续帖子里解释了技术细节：「Agent 文件和 Claude 文件会沿着目录树递归生效。当有几千名开发者在同一个 monorepo 里，总会出现某个目录缺少两份文件之一的情况——这意味着有一部分开发者是在<strong style="{RED}">被切了脑叶</strong>的状态下工作。」</p>

<p style="{P}">他还有一句更狠的总结：「我们用自动化绕过了这个问题，但这是一笔<strong style="{RED}">愚蠢的复杂度税</strong>，本来不该有人付。」</p>

<p style="{P}">然后 Anthropic 让步了。从威胁到发布，三周半。</p>

<p style="{P}">这些报道都没有错。但「终于加入跨工具标准」这个说法，把一个精心设计的让步，讲成了一次顺水推舟的开放。</p>

<h2 style="{H2}">二、本质：争的不是文件名，是「默认权」</h2>

<p style="{P}">真正的故事藏在更新日志的措辞里。原文是这样的：</p>

<blockquote style="{BQ}">
<p style="font-size:15px;line-height:1.8;margin:0;">新增 AGENTS.md 支持：在一个没有 CLAUDE.md 的项目里，Claude Code 改为读取 AGENTS.md。（Bedrock、Vertex、Foundry 上暂不支持。）</p>
</blockquote>

<p style="{P}">把它拆开看，Anthropic 让了三步，但守住了三处：</p>

<p style="{P}"><strong>第一，这是一个 fallback（兜底）而不是并列。</strong>CLAUDE.md 存在时，AGENTS.md 根本不会被读。也就是说，Anthropic 承认了外部的文件，但把自家文件放在了优先位——社区里有人立刻算出了代价：这次更新「不包括 .agents/skills」，而 .agents/skills 恰恰是 Lütke 原帖里点名的第二项。</p>

<p style="{P}"><strong>第二，云平台版本没有跟进。</strong>Bedrock、Vertex、Foundry 上的 Claude Code 仍然只认 CLAUDE.md。企业客户——也就是最需要统一配置的那批人——暂时拿不到这个能力。</p>

<p style="{P}"><strong>第三，谁被迫让步这件事本身，说明了标准的权力来源。</strong>Hacker News 上点赞最高的评论之一毫不留情：「记住，他们做这件事不是因为想帮社区，而是因为社区愤怒了、而且他们正在把用户输给别的 harness。」另一条更直接：「别用闭源 harness。为什么？这就是为什么。」</p>

<p style="{P}">这条评论指向了一个更硬的背景：据 HN 讨论中的说法，Anthropic 这次松口，是「Shopify CEO 那条推文加上 Astra 让大量用户转向 Codex」共同作用的结果。换句话说，这不是理念的胜利，是客户流失与一个大客户公开威胁的结果。</p>

<p style="{P}">而用户这边付出的代价早就在账上了。HN 评论区里，有人晒出自己一直在用的 <code>sync-agent-docs.sh</code>——一个把 AGENTS.md 递归软链接到 GEMINI.md 和 CLAUDE.md 的脚本；有人贴出自己的 CLAUDE.md 全文，内容只有一行：「本项目使用 AGENTS.md 作为 agent 指令文件（保持厂商中立）。请把任何 AGENTS.md 当作 CLAUDE.md 一样对待。@AGENTS.md」；还有人发现 Claude 在一次新项目初始化时，未经提示就自己创建了 AGENTS.md 并把 CLAUDE.md 做成软链接指向它。</p>

<p style="{P}">一个文件需要一整个脚本、一行 hack、或者模型自发行为来维持同步——这就是标准缺位时的真实成本。</p>

<p style="{P}">所以真正的问题不是「文件该叫什么」，而是<strong style="{RED}">谁的配置文件被默认读取</strong>。默认权是锁定用户最安静、也最有效的方式：它不写在合同里，不体现在价格上，只体现在每个人每天打开编辑器时，那份自动被加载的文件上。</p>

<h2 style="{H2}">三、深层结构：为什么一份「没有法律效力的文件」能撬动巨头</h2>

<p style="{P}">要理解这场博弈的量级，得先看清一件反常识的事：<strong style="{RED}">这些文件其实没有任何强制力。</strong></p>

<p style="{P}">Claude Code 官方文档写得很清楚：CLAUDE.md 与自动记忆（auto memory）是两套并行的机制，「Claude 把它们当作上下文，而不是强制配置（context, not enforced configuration）。要无条件拦截某个动作，请使用 PreToolUse hook。」文档还有一句更扎心的话：「你的指令越具体、越简洁，Claude 遵循得越一致。」</p>

<p style="{P}">也就是说，整个行业正在争的，是一份<strong style="{RED}">没有法律效力、甚至没有技术强制力的文件</strong>。它不是编译器配置，也不是网络协议——它更接近于一种「期望管理」：争的不是执行力，而是注意力的默认落点。</p>

<p style="{P}">理解了这一点，三种力量就浮现出来了。</p>

<p style="{P}"><strong>第一是经济学：多工具并存让私有配置变成了税。</strong></p>

<p style="{P}">今天的团队早就不是「一个公司用一种 Agent」了。同一个仓库里可能同时有 Cursor、Codex、Claude Code、Gemini CLI 的用户。任何一家的私有配置文件，都会变成其他人的额外维护成本——而且这个成本随团队规模超线性增长：每多一个工具，就要多维护一份同步脚本，多一类「为什么他的助手知道、我的不知道」的困惑。Lütke 说的「复杂度税」精确地描述了这一点。统一文件不是审美偏好，是成本核算的结果。</p>

<p style="{P}"><strong>第二是工程：递归继承让「漏一个目录」变成行为不一致。</strong></p>

<p style="{P}">这是只有 monorepo 规模才会暴露的问题，也解释了为什么最强硬的反对声来自大厂而不是个人开发者。指令文件沿目录树递归生效：某个子目录有 CLAUDE.md 却没有 AGENTS.md，于是用 Claude Code 的人按一套规则工作，用 Cursor 的人按另一套。在几千人的仓库里，这种「部分人按不同规则工作」的状态被 Lütke 称为 split brain（脑裂），措辞比「复杂度税」更重。</p>

<p style="{P}"><strong>第三是制度与安全：标准化在统一入口的同时，也统一了攻击面。</strong></p>

<p style="{P}">这是最少被讨论、但最危险的一层。指令文件是模型会信任并执行的文本——这就让它天然成为投毒入口。仅仅在 2026 年，公开报道里就出现过这些：3 月，「README 文件里的隐藏指令可以让 AI Agent 泄露数据」；同月，「新研究重新评估 AGENTS.md 文件对 AI 编码的价值」（结论并不乐观）；6 月，「AI 编码 Agent 可能正在从『臭烘烘的』配置文件里拿到坏指令」；8 月，「攻击者正在构造恶意 AI 指令文件，把 agent 变成安静的犯罪助手」。</p>

<p style="{P}">换句话说：大家在争的这份文件，既可能被模型忽略（因为它只是上下文），又可能被攻击者利用（因为它会被执行）。标准化把「每个工具各自的注入面」合并成了一个所有人共用的注入面——这是统一的隐性成本，目前没有任何标准草案认真处理。</p>

<p style="{P}">历史上有过非常接近的先例。<code>.editorconfig</code> 统一了编辑器的格式规则，<code>.gitignore</code> 统一了版本控制的忽略逻辑，robots.txt 和 HTTP Cookie 则告诉我们另一件事：<strong style="{RED}">靠共识运转的机制，一旦共识形成，缺席者的成本会高到无法承受。</strong>XKCD 那张著名的「一个标准统一所有标准」的漫画，讲的正是这个过程荒诞又必然的一面——提案越多，最后胜出的往往不是最好的那个，而是被最多实现读取的那一个。</p>

<p style="{P}"><strong style="{RED}">这不是配置文件之争——这是 Agent 时代「谁定义默认」的第一场公开战争。而在这场战争里，赢家通常不是最强的模型，而是被所有人默认读取的那份文件。</strong></p>

<h2 style="{H2}">四、反方与代价：这份文件真的配得上这么大的争论吗</h2>

<p style="{P}">一篇只讲博弈的文章是不诚实的。这场争论本身有三个软肋。</p>

<p style="{P}"><strong>其一，指令文件的实际价值仍存疑。</strong>今年 3 月的研究就重新评估过 AGENTS.md 这类文件对 AI 编码的真实帮助，6 月的报道更直接——很多配置文件本身就是「臭的」：内容过期、自相矛盾、把无关上下文塞进去稀释注意力。Hacker News 上也有人提出这个质问：「我还是不明白这些 Markdown 文件的意义。它不就是往提示里塞更多文本吗？你怎么确定它不是在用一堆废话污染上下文？」当一整个行业为一份文件站队时，这份文件的有效性却没有被严格验证过。</p>

<p style="{P}"><strong>其二，强制力是幻觉，优先级还可能被偷走。</strong>官方文档说它是「上下文」而非「配置」；而一位 HN 用户指出更麻烦的行为：Claude 会先看 settings.json，如果那里有默认值，就优先于 CLAUDE.md 里的指令——他举的例子是自己在 CLAUDE.md 里写了「不要在任何 issue、PR 或 wiki 里加『Made with Claude Code』」，结果仍被加上。他用的词是「nefarious」（阴险）。含义很明确：<strong style="{RED}">你以为你在写规则，其实你在写建议；而建议的优先级可能低于一份你没编辑过的 JSON。</strong></p>

<p style="{P}"><strong>其三，「统一」目前是打补丁式的。</strong>这次更新不含 .agents/skills、不支持三个云平台；AGENTS.md 官方还要面对 Copilot 的 copilot-instructions.md、Cursor 的 .cursor/rules、Gemini 的 GEMINI.md 等文件并存的现实。一个残酷的规律是：标准化的第一阶段从来不是「少一个文件」，而是「多一个文件」——先让所有人多维护一份，再慢慢收敛。</p>

<p style="{P}"><strong style="{RED}">给 Agent 立规矩的成本，往往就是规矩本身的维护成本。</strong></p>

<h2 style="{H2}">五、未来推演：三个还没有答案的问题</h2>

<p style="{P}"><strong style="{RED}">第一个问题：这份文件该由谁来定义？</strong></p>

<p style="{P}">AGENTS.md 目前没有治理主体——它靠一个网站、一份清单和一批厂商的自觉支持在运转。这和早期 .editorconfig 的状态类似。但当它开始涉及安全（恶意指令文件投毒）、涉及企业合规（哪些指令可被信任）、涉及跨厂商优先级时，「社区共识」这个机制就会遇到天花板。真正的问题是：会不会出现一个中立基金会来托管它？还是最后由某一家厂商用事实上的实现权来定义——就像今天 Anthropic 用 fallback 顺序所暗示的那样。</p>

<p style="{P}"><strong style="{RED}">第二个问题：当指令文件同时是攻击面，标准要不要内置安全？</strong></p>

<p style="{P}">签名、来源校验、只读白名单、对仓库内指令的信任分级——这些在安全社区已经被反复提出，但没有一条进入主流标准。如果下一次大规模 agent 事故的根因是一份被篡改的 AGENTS.md，整个行业会一次性补上这一课。而补课的顺序通常是：先出事故，再定规范。</p>

<p style="{P}"><strong style="{RED}">第三个问题：如果「上下文文件」真的有效，为什么还需要自动记忆和技能？</strong></p>

<p style="{P}">Claude Code 现在有三套并行的知识机制：CLAUDE.md（人写）、auto memory（模型自己写，每次会话加载前 200 行或 25KB）、以及 skills（可执行的流程）。三条路指向不同的未来——如果自动记忆够好，手写文件会退化成一份入职文档；如果技能足够成熟，很多原本写在文件里的约定会变成可执行的检查。那么今天这场为标准而战的争论，可能在三五年后回头看，是一个过渡形态的礼仪之争。</p>

<p style="{P}">结语留一个更朴素的问题。过去两年我们讨论 AI 编码时，焦点几乎全在模型：参数、上下文长度、基准分数。而 2026 年 9 月这一个月，真正的行业动作却发生在一个 Markdown 文件上——Cloudflare 把审计流程写成技能、阿里把规则集开源、Anthropic 顶不住压力接受外部文件、Shopify 的 CEO 用封杀威胁换来一次 fallback。</p>

<p style="{P}"><strong style="{RED}">不是你想不想统一配置——是当所有 Agent 都读同一份文件时，「默认」这两个字本身就是最大的护城河。Anthropic 让了一步，但它把让出的那一步，精确地放在了兜底的位置上。</strong></p>

<p style="{P}">你觉得 AGENTS.md 会像 .editorconfig 一样成为安静的基础设施，还是会像 XKCD 说的那样，成为「又多一个标准」？评论区聊聊。</p>

<hr style="border:none;border-top:1px solid #eee;margin:32px 0;">

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">参考来源：agents.md 官方网站（AGENTS.md 定位与支持厂商清单）、Claude Code 官方更新日志 2.1.277（2026-09-18，AGENTS.md 支持的确切措辞与三平台限制）、Claude Code 官方文档《How Claude remembers your project》（上下文而非强制配置、auto memory 前 200 行或 25KB、PreToolUse hook、.claude/rules）、The New Stack 报道《Shopify&#39;s CEO threatened to ban Claude Code. Anthropic had already closed the feature request.》（含 Tobi Lütke 2026-08-25 原帖与复杂度税、脑裂、被切脑叶引语）、Hacker News 讨论「Claude Code now reads AGENTS.md if there is no Claude.md」（723 分 / 272 评论）与「Anthropic finally adds AGENTS.md support to Claude Code」（52 分 / 10 评论）、Bing News 聚合（2026 年 3 月 README 隐藏指令与 AGENTS.md 价值复评研究、6 月臭配置报道、8 月恶意指令文件报道）。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">⚠️ 证据级别说明：更新日志措辞、官方文档对「上下文而非强制配置」的说明、agents.md 支持清单均为官方一手来源；Lütke 的封杀威胁与「功能请求曾被关闭」来自 The New Stack 报道其 X 原帖（公开表态级别）；「Astra 导致用户转向 Codex 是其让步原因之一」来自 HN 评论推断，非官方确认；恶意指令文件攻击面系列来自媒体报道，样本量未独立核实。</p>

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">关联阅读：<a href="https://yuanlaiai.github.io/articles/agent-code-review-rework-tax-2026/" style="color:#e67e22;">当「验收」成为新瓶颈：给 Agent 立规矩就是最值钱的生意</a></p>'''

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
TAGS_OK = {'大模型', 'AI Agent', '行业趋势', '中国 AI', '商业资本', '开源生态', '安全监管', '算力芯片', '榜单日报', '实用教程'}
assert set(TAGS) <= TAGS_OK, set(TAGS) - TAGS_OK
print("正文汉字数:", cn, "| desc 长度:", len(DESC), "| 标签:", TAGS, "| <ul>:", content.count('<ul'), "| 相对链接:", len(re.findall(r'href="/', content)))
print("Total articles:", len(data['articles']))
