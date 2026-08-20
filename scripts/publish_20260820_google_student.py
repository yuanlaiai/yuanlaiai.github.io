#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish article: google-student-gemini-free-2026 into data.json"""
import json

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

P = 'font-size:15px;line-height:1.8;color:#333;margin-bottom:16px;'
H2 = 'font-size:18px;font-weight:700;color:#1a1a2e;margin-top:32px;margin-bottom:14px;padding-left:10px;border-left:3px solid #e67e22;'
RED = 'color:#c0392b;'
BQ = 'margin:24px 0;padding:14px 18px;background:#faf7f4;border-left:3px solid #e67e22;border-radius:4px;'

content = f'''<h1 style="font-size:22px;font-weight:700;line-height:1.6;color:#1a1a2e;text-align:center;margin-bottom:20px;padding-top:10px;letter-spacing:1px;">Google 免费送学生一年 Gemini，OpenAI 却在教孩子不做作业——AI 双雄的教育攻防战</h1>

<p style="font-size:14px;color:#888;text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid #eee;">2026-08-20 · 猿来AI</p>

<p style="{P}">8 月 19 日，Google 官宣：<strong style="{RED}">在校大学生可免费获得一年 Gemini AI Pro 套餐</strong>，外加一个全新的「AI 学习中心」（Student Hub），配套一批学习工具——Gemini Live 接入 Deep Research、NotebookLM 并入 AI Mode、Search 内置 AI 学习功能。一句话：把最高档的 AI 白送一年给大学生。</p>

<p style="{P}">同一天往前数 24 小时，OpenAI 干的是另一件事：推出「ChatGPT for Teens」——面向青少年的专用版本，主打家长控制、学习模式，并且明确宣布：<strong style="{RED}">ChatGPT 将不再帮孩子完成作业</strong>。</p>

<p style="{P}">一个给钱，一个立规矩；一个抢大学生，一个防未成年人。</p>

<p style="{P}">这不是巧合，这是 AI 双雄在教育市场的一次正面对撞——而且撞出了完全相反的路线。</p>

<p style="{P}">为什么要把这两条新闻放在一起看？因为它们发生在同一个时间窗口，瞄准的是同一个市场——教育。当 AI 双雄同时把教育当成主战场，说明教育已经从一个「伦理议题」变成了「商业战场」。两年前教育圈还在争论要不要禁止 ChatGPT，今天争论的是用哪家的——这个转变本身就是新闻。</p>

<!--more-->

<h2 style="{H2}">一、表象：两个动作各是什么</h2>

<p style="{P}">先拆 Google。</p>

<p style="{P}">这次的「学生套餐」不是打折，是白送：一年 Gemini Pro 免费，外加专属的 AI 学习中心。学习中心是什么？是把 AI 塞进学生日常的每一个环节：用 Gemini Live 的 Deep Research 做文献调研，用 NotebookLM 把课程资料变成可对话的知识库，用 Search 的 AI 功能直接生成学习大纲。Google 还给学生账号配了 AI 主题的视觉界面——连「看起来像学生产品」都做到了。申请流程也压到最低：验证学生身份即可开通，几乎零门槛——连注册流程都替学生想好了。</p>

<p style="{P}">再拆 OpenAI。</p>

<p style="{P}">ChatGPT for Teens 的思路完全相反：重点是「控制」。家长控制面板、学习模式（Study Mode）、年龄适配的模型行为，最狠的一条——ChatGPT 将停止帮未成年人完成作业。OpenAI 在主动给产品「降能力」，来换取家长和监管的信任。</p>

<p style="{P}">两条路线，一个撒钱扩张，一个收缩自保。</p>

<h2 style="{H2}">二、本质一：学生是 AI 时代的第一口奶</h2>

<p style="{P}">Google 为什么要白送一年 Pro？一年 Pro 的成本是实打实的，但 Google 算的账从来不是这一年。</p>

<p style="{P}">学生的价值在于：他们是未来十年进入劳动力市场的知识工作者。今天在校园里用 Gemini 写论文、做项目、跑数据的大学生，毕业后会把使用习惯带进公司、带进团队、带进采购决策。<strong style="{RED}">Google 送的不是一年订阅，是未来十年的用户习惯。</strong></p>

<p style="{P}">这是科技公司最经典的长期投资剧本：GitHub 用 Education Pack 免费套餐培养了一代开发者的 Git 习惯；Spotify 给学生半价，换来的是毕业后全价续费的终身客户；微软的 Office 教育版，几乎免费地让整个学生时代长在微软生态里。免费给学生，从来不是慈善，是最高性价比的获客。</p>

<p style="{P}">习惯之外，学生还有第二重价值：数据。一个大学生一年的学习数据——论文草稿、研究笔记、复习路径、提问方式——是最干净、最完整的「人类学习行为样本」。这些数据既能用来做个性化推荐，也是模型对齐训练的黄金素材。学生免费，等于用一年的订阅成本，换取一整代知识工作者的行为数据。这笔账，怎么算都不亏。</p>

<p style="{P}">AI 时代的逻辑更极端：模型有网络效应和习惯粘性。一个用惯了 Gemini 的学生的上下文、知识库、工作流全在 Google 生态里——切换成本高到毕业也不会走。</p>

<p style="{P}">免费一年还有一个心理学设计：锚定与损失厌恶。一年后，学生的论文、笔记、知识库全部长在 Gemini 里，续费只需要每月几十美元——比起重建整个工作流，续费是阻力最小的选择。Spotify 的学生半价续全价、GitHub 的学生包毕业转 Pro，都是同一个转化漏斗：先免费种下习惯，再靠损失厌恶收割。这一年的免费额度，本质是 Google 给每个学生发的「订阅习惯养成券」。</p>

<blockquote style="{BQ}"><p style="margin:0;font-size:15px;line-height:1.8;color:#333;"><strong>大学四年是 AI 产品唯一一次「免费获取终身客户」的机会——Google 没有错过，OpenAI 也看到了，只是选择了不同的姿势。</strong></p></blockquote>

<h2 style="{H2}">三、本质二：为什么两条路线相反？</h2>

<p style="{P}">同一个市场，为什么 Google 撒钱、OpenAI 设防？</p>

<p style="{P}"><strong>第一，客户群体不同。</strong>Google 瞄准的是大学生——成年人，有自主选择权，付费能力近在眼前，监管风险最低。OpenAI 瞄准的是未成年人——K12 和低龄群体，家长买单、监管最严，一个 AI 帮孩子做作业的新闻就能引发听证会。同样是教育，一个是「可收割的流量」，一个是「需谨慎的雷区」，策略当然相反。</p>

<p style="{P}"><strong>第二，商业模式不同。</strong>Google 有搜索和广告的现金牛，可以拿广告利润补贴 AI 价格战，送一年 Pro 对它是获客成本；OpenAI 的收入基本全靠订阅，每一份免费额度都是真实的利润让渡，它没有打价格战的底气，只能在安全叙事上做差异化。<strong style="{RED}">免费战的本质是补贴战，补贴战只有现金牛玩家玩得起。</strong></p>

<p style="{P}">还要看清一点：教育市场从来不是单纯的 B2C。Google 有 Gemini for Education，OpenAI 有 ChatGPT Edu，微软有教育版 Copilot——学校采购协议才是真正的利润来源。免费送学生一年，本质上是在 B2C 端抢心智，为 B2B 端的学校采购铺路：当学生们都在用 Gemini，学校还有什么理由不买 Gemini for Education？C 端免费、B 端收费，双层结构的算盘打得清清楚楚。</p>

<p style="{P}"><strong>第三，监管处境不同。</strong>OpenAI 这几年在未成年人保护上挨的打够多了——学校禁用、家长投诉、监管调查。「ChatGPT 不再帮孩子做作业」不是产品决策，是求生决策。Google 在 K12 的声誉包袱轻得多，所以敢直接冲向高等教育。</p>

<blockquote style="{BQ}"><p style="margin:0;font-size:15px;line-height:1.8;color:#333;"><strong>OpenAI 在教育市场防守的是信任，Google 进攻的是入口——防守的人立规矩，进攻的人撒钱。</strong></p></blockquote>

<h2 style="{H2}">四、本质三：为什么是现在？</h2>

<p style="{P}">教育市场的争夺，为什么偏偏在这一周引爆？</p>

<p style="{P}"><strong>第一，AI 进校园的拐点到了。</strong>前两年学校还在「禁用 ChatGPT」和「拥抱 AI」之间摇摆，现在制度化的窗口打开了：高校开始采购 AI 工具、设计 AI 素养课程、把 AI 写进教学大纲。谁能在这个窗口期成为校园默认，谁就锁定了下一代。</p>

<p style="{P}"><strong>第二，AI 商业化进入获客成本大战。</strong>模型能力趋同之后，竞争从「谁的模型强」变成「谁的用户多」。教育是最后一个尚未被瓜分的高价值流量入口——学生群体规模大、黏性高、生命周期长。Google 和 OpenAI 同时意识到：再不抢，就晚了。</p>

<p style="{P}"><strong>第三，传统教育科技公司被 AI 血洗后的真空。</strong>Chegg 的股价因为 ChatGPT 暴跌过，Course Hero 们靠题库和答案的生意被 AI 问答直接颠覆——教育科技赛道被 AI 打穿之后，留下了一个巨大的真空。现在 AI 公司自己下场填这个真空：不是收购教育公司，而是直接把 AI 变成教育基础设施。Chegg 们的悲剧，就是 Google 和 OpenAI 的机会。</p>

<p style="{P}"><strong>第四，生成式 AI 正在重塑「学习」本身。</strong>NotebookLM 把教材变成对话，Deep Research 把文献调研变成对话式问答——AI 不只是学习工具，它在重新定义学习方式。谁能定义学生怎么用 AI 学习，谁就定义了未来知识工作者的工作方式。</p>

<blockquote style="{BQ}"><p style="margin:0;font-size:15px;line-height:1.8;color:#333;"><strong>教育市场这一战，抢的不是今天的收入，是十年后整个劳动力市场的 AI 使用习惯。</strong></p></blockquote>

<h2 style="{H2}">五、未来走向：教育 AI 的双轨制与三张风险牌</h2>

<p style="{P}"><strong>第一，教育 AI 双轨制成型。</strong>一条轨是「未成年人保护轨」：家长控制、能力降级、合规优先——OpenAI 已经立了标杆，后续所有面向 K12 的产品都得跟着做。另一条轨是「高等教育争夺轨」：免费、补贴、生态绑定——Google 开了第一枪，微软的 Copilot 大概率跟进。两条轨道的产品哲学完全不同，未来会出现「同一个 AI 公司，两套教育产品」的常态。</p>

<p style="{P}"><strong>第二，免费战争的连锁反应。</strong>Google 免费一年，OpenAI 要么跟进（伤利润），要么差异化（安全牌），要么靠学校采购协议（ChatGPT Edu 类产品）绕开 C 端价格战。可以预见：接下来几个月，教育市场的营销预算会暴涨，学生成了 AI 公司最贵也最便宜的流量。</p>

<p style="{P}"><strong>第三，三张风险牌。</strong>一是学生数据隐私：学生把论文、作业、考试资料喂给 AI，这些数据归谁、能不能用于训练，是随时会爆的雷。二是学术诚信：AI 帮做作业的边界正在模糊——OpenAI 说「不帮未成年人做作业」，但大学生的边界谁来定义？三是免费陷阱：一年免费期结束后，是续费转化、还是换一家更便宜的——学生的忠诚度，取决于这十二个月里 Google 能不能把习惯焊死。</p>

<p style="{P}">学生数据隐私的风险不是假设：论文里可能藏着未发表的研究创意，作业里可能写着个人的困惑与短板，聊天记录里可能是最真实的思考过程。这些数据一旦被用于模型训练或商业分析，就是对信任的透支。欧洲的 GDPR 和美国的 FERPA 都盯着这一块——哪家 AI 公司在学生数据上翻车，哪家就会在教育市场满盘皆输。这也是 OpenAI 选择「少做而不是多做」的深层原因。</p>

<p style="{P}">对普通学生，建议很简单：这一年的免费额度，别只用来写作业。把 Gemini 的训练营开起来——Deep Research 学调研、NotebookLM 搭个人知识库、用 AI 重构你的学习工作流。<strong style="{RED}">这一年的免费 AI，可能是你职业生涯里最值钱的一笔「奖学金」。</strong></p>

<p style="{P}">还有一个人群容易被忽略：教师。当学生人手一个免费 Gemini，教师的处境变得微妙——不是被取代，而是被迫重新定义「布置什么作业才有价值」。Google 和 OpenAI 都推出了教师工具，但这把双刃剑的另一面是：如果 AI 替学生完成一切，教育的评估体系就得重建。谁能帮学校解决这个难题，谁才能真正拿下教育市场——教育 AI 的终局，不是取代教师，是重新发明考试。</p>

<p style="{P}">历史总是押韵。1997 年，微软把 IE 免费捆绑进 Windows，用免费击垮了 Netscape；2004 年，Google 用 Gmail 的邀请制和 1GB 免费空间，把邮箱市场从付费时代拽进免费时代；2026 年，Google 又对学生按下了免费键。<strong>免费的从来不是产品，是通往垄断的入场券。</strong></p>

<p style="{P}">这场教育攻防战的胜负手，不在产品功能，而在一个朴素的问题：十年后，当这一批学生成为社会中坚，他们最先想到的 AI 工具是哪一个？Google 赌的是习惯，OpenAI 赌的是信任——而学生用脚投票的结果，会写在十年后的每一份简历里。这场仗的裁判是时间，十年后见分晓。</p>

<blockquote style="{BQ}">
<p style="margin:0 0 8px 0;font-size:15px;color:#333;line-height:1.8;"><strong>一句话总结：</strong>同一周，Google 免费送大学生一年 Gemini Pro（含 AI 学习中心），OpenAI 推出 ChatGPT for Teens（家长控制、停止代做作业）——一个撒钱、一个设防。本质是 AI 双雄争夺教育入口：学生是未来十年的知识工作者，免费一年换的是终身习惯、行为数据和学校采购。Google 有现金牛敢打补贴战，OpenAI 只能打安全牌。教育 AI 双轨制成型：未成年人保护轨 + 高等教育争夺轨。对学生：这一年免费 AI 是最值钱的「奖学金」；对行业：免费的从来不是产品，是通往垄断的入场券。</p>
</blockquote>

<p style="{P}">你怎么看 Google 的「学生免费一年」——这是教育福利，还是 AI 时代的「第一口奶」？教育市场没有输家，只有迟到者——而这一次，Google 和 OpenAI 都准时到场了。评论区聊聊。</p>

<hr style="border:none;border-top:1px solid #eee;margin:32px 0;">

<p style="font-size:13px;color:#aaa;line-height:1.6;text-align:center;">参考来源：Google 官方发布（2026-08-19 学生免费一年 Gemini Pro + AI 学习中心 + Gemini Live Deep Research + NotebookLM AI Mode）、OpenAI 发布（2026-08-18 ChatGPT for Teens：家长控制/学习模式/停止代做作业）、Bing News 多源报道（Google gives students free Gemini / OpenAI launches ChatGPT for Teens）、HN 讨论帖。产品细节以官方公告为准。</p>'''

article = {
    "id": 24,
    "title": "Google 免费送学生一年 Gemini，OpenAI 却在教孩子不做作业——AI 双雄的教育攻防战",
    "tags": ["Google", "Gemini", "OpenAI", "教育", "学生", "ChatGPT", "AI竞争", "深度分析"],
    "date": "2026-08-20",
    "readTime": "9 分钟",
    "desc": "8月19日 Google 官宣大学生免费一年 Gemini Pro + AI 学习中心；同一天前 OpenAI 发布 ChatGPT for Teens（家长控制、学习模式、停止代做作业）。一个撒钱一个设防——拆三层本质：学生是第一口奶、为什么路线相反、为什么是现在；教育 AI 双轨制成型。",
    "slug": "google-student-gemini-free-2026",
    "content": content,
    "wechatUrl": ""
}

with open(path, encoding='utf-8') as f:
    data = json.load(f)

data['articles'].insert(0, article)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Inserted article id=24, slug=google-student-gemini-free-2026")
print("Total articles:", len(data['articles']))
