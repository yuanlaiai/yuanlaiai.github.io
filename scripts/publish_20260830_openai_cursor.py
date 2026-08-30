#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: openai-cuts-cursor-spacex-2026 into data.json"""
import json

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

P = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2 = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;'
BQ = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'

content = f'''<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;margin-bottom:20px;padding-top:10px;letter-spacing:1px;">OpenAI 切断 Cursor：600 亿美元收购背后的 AI 战争——Musk 与 Altman 从法庭打到产品层</h1>

<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid #eee;">2026-08-30 · 猿来AI</p>

<p style="{P}">8 月 29 日，OpenAI 发布官方声明，标题冷静得像一纸公告：「我们关于 Cursor 被 SpaceX 收购后的决定」。</p>

<p style="{P}">决定是什么？两个字：<strong style="{RED}">断供</strong>。OpenAI 终止与 Cursor 的模型合作协议——从今往后，Cursor 的 GPT 系列模型访问被切断。</p>

<p style="{P}">这条声明在 Hacker News 拿下 <strong style="{RED}">822 分、513 条评论</strong>，是近一周社区讨论量最大的 AI 新闻之一。CNBC、Bloomberg、Reuters 三大财经媒体全线跟进，Musk 被曝「暴怒」。</p>

<p style="{P}">事情本身不复杂：Cursor——全球最火的 AI 编码工具，被 SpaceX 以 <strong style="{RED}">600 亿美元</strong>收购；收购落地的 24 小时内，OpenAI 就切断了模型供应，理由是「Musk 的公司违反合同」。</p>

<p style="{P}">但这背后，是两个男人长达十一年的恩怨，从法庭一路打到了产品层。</p>

<p style="{P}">先看 Cursor 的分量：它是 AI 编码工具赛道无可争议的头部玩家，全球数千万开发者用它写代码，估值在 2026 年已冲到数百亿美元量级。更关键的是，它长期是 OpenAI 模型在编码场景的最大分销渠道——无数开发者的第一次 GPT 系列体验，就是在 Cursor 里完成的。这样一个「印钞机级」的合作伙伴，一夜之间变成对手的资产，OpenAI 的反应速度比任何市场预期都快。</p>

<!--more-->

<h2 style="{H2}">一、表象：事件时间线</h2>

<p style="{P}">先还原发生了什么。</p>

<p style="{P}"><strong>第一步，收购。</strong>Cursor 是 AI 编码工具领域的头部玩家——千万级开发者用它写代码，而它最核心的卖点之一，就是深度集成的 GPT 系列模型。SpaceX（马斯克的太空公司）以 600 亿美元完成收购，Cursor 一夜之间变成「马斯克的公司」。</p>

<p style="{P}"><strong>第二步，断供。</strong>收购消息落地的 24 小时内，OpenAI 官方声明：终止与 Cursor 的模型合作协议。措辞克制但态度明确——「因为 Musk 的关联公司违反了合同条款」。</p>

<p style="{P}"><strong>第三步，连锁反应。</strong>Musk 被曝在社交媒体上暴怒回应；CNBC 立刻抛出灵魂拷问：「Cursor 没了 OpenAI 的模型，会投向 Anthropic 还是 xAI？」；开发者社区在 HN 上热烈讨论「要不要换掉 Cursor」。</p>

<p style="{P}"><strong>第四步，生态震动。</strong>这不是一次普通的商业终止——OpenAI 的模型是 Cursor 的核心弹药，断供等于把 Cursor 的「发动机」拆了。而 Cursor 也是 OpenAI 模型最大的分销渠道之一，切断渠道对 OpenAI 自己也有损失。这是一场双输的战争宣言。</p>

<p style="{P}">还要看清断供的实际杀伤力：Cursor 用户里相当一部分的主力模型就是 GPT 系列，断供意味着他们的日常编码体验将被迫改变——要么接受替代模型的性能落差，要么迁移工具。对一款「习惯型」产品来说，这种被迫的改变就是流失的开始。</p>

<h2 style="{H2}">二、本质一：这不是合同纠纷，是生态战争</h2>

<p style="{P}">表面看，OpenAI 的理由是「合同违约」；实际上，这是一次赤裸裸的生态封锁。</p>

<p style="{P}">为什么？因为<strong>模型是编码 Agent 的弹药，而 OpenAI 的 GPT 系列是 Cursor 的核武器库</strong>。Cursor 之所以能成为千万开发者的首选，很大程度靠的是 GPT 模型强大的代码生成能力。断供之后，Cursor 要么换弹药（接入 Claude/Gemini/xAI），要么裸奔——无论哪种，战斗力都要打折。</p>

<p style="{P}">反过来看 OpenAI 的算盘：Cursor 是 GPT 模型在编码场景的最大出口。马斯克买下 Cursor，等于控制了 OpenAI 模型的一条关键分销渠道——一个正在和 OpenAI 打官司的对手，掌握了你最大的销售管道。换谁都会切断。</p>

<p style="{P}">分销渠道的价值往往被低估。编码工具不是模型公司的「客户」那么简单——它是模型的「露出位」：开发者每天在 Cursor 里写十小时代码，每一次自动补全都在强化对 GPT 模型的依赖。这种高频露出带来的心智占领，比任何广告都有效。失去 Cursor，OpenAI 失去的不只是一个 API 采购方，是一条直达千万开发者的品牌管道。</p>

<p style="{P}">这不是商战里的「断供」第一次出现。历史上有过太多类似剧本：当年 Intel 拒绝给 AMD 供货、苹果拒绝给第三方应用开放核心 API、微软用 IE 捆绑干掉 Netscape——<strong>生态的掌控者，永远有「不给弹药」的终极权力</strong>。OpenAI 这次只是把剧本又演了一遍，只是这次的主角换成了编码 Agent。</p>

<blockquote style="{BQ}"><p style="margin:0;font-size:15px;line-height:1.8;color:#333;"><strong>合同纠纷只是借口，生态封锁才是目的——模型就是编码 Agent 的弹药，而 OpenAI 握住了弹药库的钥匙。</strong></p></blockquote>

<h2 style="{H2}">三、本质二：Musk 与 Altman 的十一年战争</h2>

<p style="{P}">这场断供的真正主角不是公司，是两个人：Elon Musk 和 Sam Altman。</p>

<p style="{P}">2015 年，两人共同创立 OpenAI，Musk 是最大的早期投资人之一，还亲自参与招揽人才。2018 年，Musk 因路线分歧离开——他想要更强的 AGI 掌控权，而 Altman 主导的 OpenAI 走向了商业化。离开后，Musk 不止一次公开批评 OpenAI「背弃了非营利的初心」。</p>

<p style="{P}">2023 年，Musk 创立 xAI，正式成为 OpenAI 的竞争对手。2024 年起，两人进入诉讼模式：Musk 起诉 OpenAI 商业化违背创立协议，OpenAI 反手公布邮件反击，指控 Musk「当年想控制 OpenAI 未遂、愤而离开」。</p>

<p style="{P}">而 2026 年的这场 Cursor 收购，把战争推向了新阶段：<strong>从法庭打到了产品层</strong>。以前是「你告我我告你」的法律战，现在是「你的产品不能用我的模型」的生态战。Musk 花 600 亿买下 Cursor，是想在 AI 应用层插旗；Altman 24 小时内断供，是把旗子连根拔起。</p>

<p style="{P}">时间线拉长看，这场战争已经打了很多轮：2023 年 xAI 成立，Musk 从 OpenAI 挖人；2024 年 Musk 起诉 OpenAI 要求恢复开源初心，Altman 公布邮件反击；2025 年 xAI 和 OpenAI 在模型发布、数据中心、融资上全面对撞；2026 年 8 月，SpaceX 以 600 亿美元拿下 Cursor——这是 Musk 第一次在 OpenAI 的核心地盘（编码工具）插旗。而 Altman 的回应是一贯的风格：快、狠、不留余地。24 小时断供，既是商业决策，也是性格展示。</p>

<p style="{P}">这场战争的驱动力，个人恩怨和商业利益各占一半。Musk 要的是「我不用你的，你也别想用我的生态」；Altman 要的是「你买什么都可以，但别想在我的地盘上立旗」。两个亿万富翁的意气，正在变成千万开发者的选择困境。</p>

<p style="{P}">更有意思的是角色互换：2015 年，Musk 是 OpenAI 的最大资助者，Altman 是执行者；2026 年，Altman 的 OpenAI 估值是 Musk xAI 的数倍，Musk 反而成了追赶者。这场战争最讽刺的地方在于：当年一起写创始宣言的两个人，现在一个手握模型、一个手握工具，都在试图证明「没有对方，我也能赢」。</p>

<blockquote style="{BQ}"><p style="margin:0;font-size:15px;line-height:1.8;color:#333;"><strong>法庭上的战争还要等法官判决，产品层的战争 24 小时就能打完——这一次，Altman 抢了先手。</strong></p></blockquote>

<h2 style="{H2}">四、本质三：编码 Agent 生态的地缘政治</h2>

<p style="{P}">Cursor 断供事件，把编码 Agent 生态的一个残酷现实摆上了台面：<strong>模型供应商与工具厂商的绑定关系，就是 AI 时代的地缘政治</strong>。</p>

<p style="{P}"><strong>第一，弹药替代战已经开打。</strong>CNBC 问得直接：「Cursor 会投向 Anthropic 还是 xAI？」答案几乎已经写在牌面上：Anthropic 的 Claude 是编码能力最强的对手（之前 Claude Code 在 GitHub 连续霸榜），xAI 有 Grok 自家模型，Google 有 Gemini。Cursor 大概率会「多模型」化——但问题在于，换弹药不是换零件，模型适配、性能调优、用户习惯都要重来。</p>

<p style="{P}"><strong>第二，开发者被迫站队。</strong>用 Cursor 的千万开发者，现在被迫思考一个问题：我的编码工具和我的模型供应商，是不是同一阵营？这听起来荒谬，但正在变成现实——就像当年开发者被迫在 iOS 和 Android 之间选边。AI 生态正在从「开放互联」滑向「围墙花园」：你用谁的工具，就间接选择了谁的阵营。</p>

<p style="{P}"><strong>第三，OpenAI 的阳谋。</strong>断供 Cursor 的同时，OpenAI 自家的 Codex CLI 正在 GitHub 连续霸榜（8 月 23 日首登 +1,978★，此后连续多天破千）。拆掉对手的弹药，扶持自己的工具——OpenAI 的目标从来不是「赢下编码工具市场」，而是「编码工具市场只能有一个赢家，那就是我」。</p>

<p style="{P}">HN 评论区的声音很有代表性：有开发者开始研究怎么把 Cursor 的配置迁移到 Claude Code；有人说「早就该换，依赖单一模型供应商本来就是定时炸弹」；有人翻出 OpenAI 自家 Codex CLI 的 GitHub 榜单战绩，嘲讽「断供是为了给亲儿子让路」；也有人冷静提醒：「不管 Cursor 换哪家模型，适配和性能都要重新折腾，这段时间的体验下降是确定的」。情绪的分裂，恰恰说明这场战争没有赢家——只有被迫做选择的开发者。</p>

<blockquote style="{BQ}"><p style="margin:0;font-size:15px;line-height:1.8;color:#333;"><strong>Cursor 失去的不是一个模型接口，是它作为「中立编码工具」的资格——AI 时代，工具也要选边站。</strong></p></blockquote>

<h2 style="{H2}">五、未来走向：三条路线与三张风险牌</h2>

<p style="{P}">接下来会发生什么？</p>

<p style="{P}"><strong>第一，Cursor 的弹药转型。</strong>最可能的路径是「多模型 + 自家模型」：接入 Claude 和 Gemini 保住基本盘，同时用 SpaceX/xAI 的资源训练自家编码模型。但转型期就是空窗期——这期间，大量开发者会试用 Codex CLI、Claude Code、Windsurf 等替代品，Cursor 的流失率取决于空窗期多长。</p>

<p style="{P}"><strong>第二，OpenAI 的渠道重建。</strong>切断 Cursor 后，OpenAI 需要新的编码分销渠道——自家 Codex 是主推，但也要警惕：当 OpenAI 同时是「模型供应商」和「工具厂商」，其他工具厂商还敢深度依赖 GPT 模型吗？「OpenAI 会不会也切断我」的恐惧，会推动更多工具厂商走多模型路线——这对 OpenAI 是双刃剑。</p>

<p style="{P}"><strong>第三，监管的阴影。</strong>Musk 是反垄断诉讼的常客，这次也不会善罢甘休。OpenAI 以「合同违约」为由断供，是否构成滥用市场支配地位？如果 Musk 把这场仗打到监管层，OpenAI 的断供决定可能会成为反垄断案例的教科书素材。</p>

<p style="{P}">三张风险牌：一是开发者信任——断供决定让所有依赖 OpenAI 模型的三方工具都开始评估风险，「OpenAI 依赖」本身成了风险标签；二是 Cursor 用户流失——换工具成本虽高，但「被断供」的恐惧会加速迁移；三是战争外溢——Musk 和 Altman 的战争不会止于 Cursor，AI 视频、机器人、数据中心，每一块都是下一个战场。</p>

<p style="{P}">对 Anthropic 和 xAI 来说，这是天上掉下来的机会：Anthropic 的 Claude 是编码能力最接近 GPT 的模型，拿下 Cursor 等于凭空获得千万级用户入口；xAI 更是背靠 SpaceX，自家模型 + 自家工具的组合可以立刻落地。但接盘的代价也很现实：Cursor 的模型适配、性能调优、用户迁移成本都压在接盘者身上——而且谁接盘，谁就接下与 OpenAI 的战争。</p>

<p style="{P}">对开发者，建议很直接：<strong>别再深度绑定单一模型供应商</strong>。你的编码工作流应该支持多模型切换——今天 OpenAI 可以切断 Cursor，明天它就可能切断你的服务商。多模型路由不是可选项，是生存必备技能。</p>

<p style="{P}">历史总是押韵。1995 年，微软用 IE 捆绑 Windows，Netscape 被扼杀，浏览器市场进入十年垄断；2010 年，Google 与 Apple 在移动端全面开战，开发者被迫选边；2026 年，Musk 与 Altman 的战争打到编码工具——<strong>AI 时代的每一次「断供」，都在提醒开发者同一个道理：不要把身家性命押在别人的弹药库上</strong>。这场战争的第一枪已经打响，而扳机，握在每一个开发者的手里。而这场战争唯一的确定性，就是不确定性本身。</p>

<blockquote style="{BQ}">
<p style="margin:0 0 8px 0;font-size:15px;color:#333;line-height:1.8;"><strong>一句话总结：</strong>SpaceX 以 600 亿美元收购 Cursor 后，OpenAI 24 小时内宣布断供模型，HN 822 分/513 评论引爆。本质三层：一是生态战争——模型是编码 Agent 的弹药，切断对手弹药库比合同纠纷更根本；二是 Musk 与 Altman 十一年恩怨从法庭打到产品层；三是编码 Agent 生态的地缘政治——工具被迫选边站，开发者被迫站队。Cursor 将多模型化求生，Anthropic/xAI 接盘窗口开启，而开发者的生存法则是：别把身家性命押在别人的弹药库上。</p>
</blockquote>

<p style="{P}">你怎么看 OpenAI 切断 Cursor？编码工具的「选边站队」时代来了吗？评论区聊聊。</p>

<hr style="border:none;border-top:1px solid #eee;margin:32px 0;">

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">参考来源：OpenAI 官方声明（2026-08-29，openai.com「Our decision on Cursor following its acquisition by SpaceX」，HN 822 分/513 评论）、Bloomberg/Reuters/CNBC 多源报道（SpaceX $60B 收购 Cursor、OpenAI 终止合作、Musk 愤怒回应）、HN 讨论帖。收购金额与违约细节以官方口径为准。</p>'''

article = {
    "id": 28,
    "title": "OpenAI 切断 Cursor：600 亿美元收购背后的 AI 战争——Musk 与 Altman 从法庭打到产品层",
    "tags": ["OpenAI", "Cursor", "SpaceX", "Musk", "Altman", "编码Agent", "深度分析"],
    "date": "2026-08-30",
    "readTime": "9 分钟",
    "desc": "SpaceX $60B 收购 Cursor 后，OpenAI 24 小时内切断模型供应，HN 822 分/513 评论引爆。拆三层本质：生态战争、十一年恩怨、编码 Agent 的地缘政治。",
    "slug": "openai-cuts-cursor-spacex-2026",
    "content": content,
    "wechatUrl": ""
}

with open(path, encoding='utf-8') as f:
    data = json.load(f)

data['articles'].insert(0, article)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Inserted article id=28, slug=openai-cuts-cursor-spacex-2026")
print("Total articles:", len(data['articles']))
