// Source: data.json — Edit that file, regenerate with: bash scripts/update-data.sh
// Last updated: 2026-06-02
var siteData = {
  "lastUpdated": "2026-06-02",
  "topic": "🏗️ <strong>AI Agent 基础设施大爆发</strong> —— 今天 GitHub Trending 前 5 清一色 Agent 基础设施项目：token 压缩（Headroom）、编排优化（ECC, 203K★）、Web 界面（Hermes WebUI）、语音交互（VoxCPM）、记忆引擎（Supermemory）。Agent 正从「能做」迈向「做好」，谁先铺好基础设施，谁就赢。",
  "days": [
    {
      "date": "2026-06-02",
      "label": "今天",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "chopratejas",
          "name": "headroom",
          "fullName": "chopratejas / headroom",
          "org": "Chopratejas",
          "url": "https://github.com/chopratejas/headroom",
          "lang": "Python",
          "langClass": "py",
          "stars": "5,418",
          "forks": "399",
          "starsToday": "1,266",
          "count": 1,
          "description": "Token 压缩引擎 —— 在数据到达 LLM 前压缩工具输出、日志、文件和 RAG 块，60-95% 更少 Token 同样答案",
          "problems": [
            "<strong>LLM 上下文窗口浪费严重：</strong>Agent 工具调用输出、日志文件、RAG 检索结果中 60-95% 都是冗余内容，白白消耗 Token 和费用。Headroom 在数据到达 LLM 之前进行智能压缩。",
            "<strong>没有统一的压缩方案：</strong>不同场景需要不同压缩策略——工具输出用结构压缩，日志用去重压缩，RAG 用语义压缩。Headroom 统一提供 Library、Proxy、MCP Server 三种使用方式。",
            "<strong>压缩后仍要保证回答质量：</strong>不是简单的丢弃内容。Headroom 使用专门的压缩算法保证压缩后 LLM 仍然能给出和原始内容一致的答案。"
          ],
          "usage": [
            "作为 Python 库：<pre><code>pip install headroom\nfrom headroom import compress\ncompressed = compress(tool_output)</code></pre>",
            "作为代理服务器：配置 Headroom Proxy 自动压缩所有 LLM 请求。",
            "作为 MCP Server：集成到 AI Agent 工具链中自动压缩。",
            "支持 Claude Code、Codex、OpenAI API 等。"
          ],
          "insights": [
            "<strong>Token 压缩是 Agent 经济学的核心：</strong>Agent 的每次工具调用都会产生大量输出。压缩 60-95% Token = 推理成本降低 60-95%。这是 Agent 规模化的关键基础设施。",
            "<strong>MCP Server 形态很聪明：</strong>作为 MCP Server 集成意味着所有兼容 MCP 的 Agent 都能自动使用压缩能力，无需逐个工具适配。",
            "<strong>Agent 工具链的新品类：</strong>Headroom 是「LLM 前置处理器」——不是增强 LLM 的能力，而是让 LLM 输入更高效。这类工具将越来越多。"
          ],
          "tags": [
            "token-compression",
            "agent-tools",
            "llm-efficiency",
            "mcp-server",
            "python"
          ]
        },
        {
          "rank": 2,
          "owner": "affaan-m",
          "name": "ECC",
          "fullName": "affaan-m / ECC",
          "org": "Affaan M",
          "url": "https://github.com/affaan-m/ECC",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "203,236",
          "forks": "31,177",
          "starsToday": "1,842",
          "count": 3,
          "description": "Agent 编排优化系统 —— 为 Claude Code、Codex、Cursor 提供技能、直觉、记忆、安全的 Agent 性能优化平台，203K★",
          "problems": [
            "<strong>Agent 性能没有统一衡量标准：</strong>不同 Agent 工具对技能、记忆、安全各有各的实现，缺乏横向对比。ECC 定义了一套完整的 Agent 性能评估体系——技能管理、直觉优化、记忆持久化、安全基线。",
            "<strong>Agent 配置碎片化：</strong>每个 Agent 工具（Claude Code、Codex、Cursor、OpenCode）有自己的配置格式。ECC 提供跨工具的统一配置和管理。",
            "<strong>缺乏 Research-first 的开发方法：</strong>大多数 Agent 开发是先写代码再验证。ECC 倡导 research-first——先研究再开发，基于数据而非直觉做决策。"
          ],
          "usage": [
            "在 Claude Code 中使用：加载 ECC 技能文件。",
            "在 Codex 中使用：配置 ECC 插件集成。",
            "在 Cursor 中使用：安装 ECC 规则集。",
            "使用 ECC 的 Agent 性能仪表盘监控优化效果。"
          ],
          "insights": [
            "<strong>203K★ 的 Agent 基础设施热度：</strong>ECC 的爆发式增长（+1,842/天）说明开发者社区迫切需要 Agent 性能优化工具。Agent 正在从「能用」走向「好用」。",
            "<strong>跨 Agent 工具的标准制定者：</strong>ECC 支持 Claude Code、Codex、OpenCode、Cursor 等几乎所有主流编码 Agent，试图成为 Agent 工具链的标准化层。",
            "<strong>Research-first 开发范式：</strong>ECC 提出的 research-first 方法论——先做实验收集数据，再基于数据做决策——正是 Agent 开发从碰运气到工程化的关键转变。"
          ],
          "tags": [
            "agent-harness",
            "performance-optimization",
            "multi-agent",
            "agent-platform",
            "javascript"
          ]
        },
        {
          "rank": 3,
          "owner": "nesquena",
          "name": "hermes-webui",
          "fullName": "nesquena / hermes-webui",
          "org": "nesquena",
          "url": "https://github.com/nesquena/hermes-webui",
          "lang": "Python",
          "langClass": "py",
          "stars": "12,353",
          "forks": "1,521",
          "starsToday": "1,725",
          "count": 2,
          "description": "Hermes Agent 的 Web 界面 —— 连续两天上榜 +1,725，社区对图形化 Agent 界面的需求持续高涨",
          "problems": [
            "<strong>Hermes Agent 只有终端界面：</strong>终端使用门槛高，移动设备不方便。Hermes WebUI 提供全功能的 Web 界面，手机也能用。",
            "<strong>CLI 和 Web 功能不同步：</strong>很多工具 CLI 和 Web 版功能不一致。Hermes WebUI 承诺与 CLI 完全对等——终端能做的 WebUI 都能做。",
            "<strong>不需要构建工具链：</strong>纯 Python + 原生 JS，无需 npm/build/bundler，一键部署即可使用。"
          ],
          "usage": [
            "Docker 一键部署：<pre><code>docker run -d -p 8080:8080 nesquena/hermes-webui</code></pre>",
            "或本地运行：<pre><code>git clone https://github.com/nesquena/hermes-webui && cd hermes-webui && python app.py</code></pre>",
            "三面板布局：左侧会话列表，中间聊天，右侧文件浏览。",
            "支持模型切换、Profile 管理、上下文用量可视化。"
          ],
          "insights": [
            "<strong>连续两天的 Agent 热潮：</strong>Hermes WebUI 和 ECC 同时出现在今天的热榜，Agent 基础设施赛道热度不减。",
            "<strong>WebUI 的 200% 增长：</strong>昨天 +320，今天 +1,725——增长超 5 倍，说明更多人发现了这个工具。",
            "<strong>Agent 的四大入口成形：</strong>终端 + Web + 手机 + 消息平台（Telegram/Discord/Slack）= 全平台覆盖。"
          ],
          "tags": [
            "hermes-agent",
            "web-ui",
            "agent-interface",
            "docker",
            "open-source",
            "ai-agent"
          ]
        },
        {
          "rank": 4,
          "owner": "OpenBMB",
          "name": "VoxCPM",
          "fullName": "OpenBMB / VoxCPM",
          "org": "OpenBMB",
          "url": "https://github.com/OpenBMB/VoxCPM",
          "lang": "Python",
          "langClass": "py",
          "stars": "24,909",
          "forks": "2,862",
          "starsToday": "779",
          "count": 3,
          "description": "清华 OpenBMB 多语言 TTS —— 连续三天上榜 +779，Tokenizer-Free TTS 热度持续",
          "problems": [
            "<strong>传统 TTS 依赖 Tokenizer：</strong>VoxCPM2 是 Tokenizer-Free 的端到端方案，不需要将文本转为离散 token。",
            "<strong>多语言 TTS 质量不均：</strong>VoxCPM2 支持多语言包括中文语音生成，效果领先。",
            "<strong>语音克隆门槛高：</strong>VoxCPM2 实现真实级语音克隆和创意声音设计，仅需少量样本。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/OpenBMB/VoxCPM</code></pre>",
            "使用预训练模型生成语音。",
            "支持语音克隆和创意声音设计。"
          ],
          "insights": [
            "<strong>连续三天的热度说明一切：</strong>VoxCPM 连续三天上榜，从 +880 → +639 → +779，说明这是个真正有持久影响力的项目。",
            "<strong>开源 TTS 的标杆：</strong>OpenBMB 持续在 NPL/语音领域输出高质量开源项目，VoxCPM 已成为开源 TTS 的标杆之一。",
            "<strong>Tokenizer-Free 的范式胜利：</strong>VoxCPM2 证明了在语音领域 tokenizer-free 方案的有效性，这是一个重要的技术方向。"
          ],
          "tags": [
            "tts",
            "speech-synthesis",
            "voice-cloning",
            "openbmb",
            "multilingual",
            "tokenizer-free"
          ]
        },
        {
          "rank": 5,
          "owner": "supermemoryai",
          "name": "supermemory",
          "fullName": "supermemoryai / supermemory",
          "org": "Supermemory AI",
          "url": "https://github.com/supermemoryai/supermemory",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "24,457",
          "forks": "2,166",
          "starsToday": "677",
          "count": 2,
          "description": "AI 时代的记忆引擎 —— 极速、可扩展的记忆 API，再次上榜 +677，为 Agent 和 AI 应用提供持久化记忆服务",
          "problems": [
            "<strong>AI Agent 没有跨会话记忆：</strong>每次新会话 Agent 都不记得用户是谁、之前聊过什么。Supermemory 提供持久化记忆 API。",
            "<strong>记忆引擎难以扩展：</strong>构建记忆系统需要向量数据库、语义搜索等复杂基础设施。Supermemory 提供开箱即用的 Memory API。",
            "<strong>没有统一的记忆 API 标准：</strong>不同框架有不同的记忆方案。Supermemory 努力成为 AI 时代的 Memory API 标准。"
          ],
          "usage": [
            "集成 API：<pre><code>npm install supermemory</code></pre>",
            "使用 Memory API 存储和检索上下文。",
            "支持向量搜索、语义缓存、会话持久化。"
          ],
          "insights": [
            "<strong>记忆赛道持续升温：</strong>Supermemory 二次上榜（+677/天），说明 AI 记忆基础设施的社区需求依然旺盛。",
            "<strong>高速增长：</strong>24.5K★，从 23K 到 24.5K 只用了一周时间，增长速度加快。",
            "<strong>Agent 记忆=下一个 Redis：</strong>就像 Redis 之于 Web 应用，Supermemory 正在成为 AI 应用的标准记忆层。"
          ],
          "tags": [
            "memory-engine",
            "agent-memory",
            "api",
            "vector-search",
            "persistence",
            "ai-infrastructure"
          ]
        }
      ]
    },
    {
      "date": "2026-06-01",
      "label": "昨天",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "pbakaus",
          "name": "impeccable",
          "fullName": "pbakaus / impeccable",
          "org": "Paul Bakaus",
          "url": "https://github.com/pbakaus/impeccable",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "32,346",
          "forks": "1,764",
          "starsToday": "317",
          "count": 1,
          "description": "AI Agent 设计语言 —— 23 个设计命令 + 27 条反模式规则，让你的 Agent 不再输出模板化前端（taste-skill 的竞品）",
          "problems": [
            "<strong>AI 生成前端千篇一律：</strong>所有模型训练在相同的 SaaS 模板上，输出同样的 AI tells——Inter 字体、紫色渐变、卡片套卡片。Impeccable 提供 7 个领域参考文件和 23 个设计命令。",
            "<strong>没有统一的设计词汇：</strong>人类和 AI 之间缺少共享的设计语言。Impeccable 提供 23 个命令——polish、audit、critique、distill、animate 等，人跟 AI 用同一套话沟通设计。",
            "<strong>AI 设计缺乏自动化检查：</strong>27 条确定性反模式规则 + 12 条 LLM 评审规则，支持 CLI 和浏览器扩展，无需 API Key 即可运行。"
          ],
          "usage": [
            "访问 <code>impeccable.style</code> 下载使用。",
            "在 Claude Code 中加载技能文件。",
            "使用设计命令与 AI 协作：<code>polish this hero section</code>",
            "运行 CLI 检查反模式：<code>npx impeccable audit</code>"
          ],
          "insights": [
            "<strong>taste-skill 的直接竞品：</strong>Impeccable 和 taste-skill 在解决同一个问题——AI 前端设计审美。两者的竞争将加速 Agent 设计技能的成熟。",
            "<strong>从技能扩展到浏览器扩展：</strong>Impeccable 不仅有 SKILL.md，还有 CLI 工具和浏览器扩展，产品形态比纯技能文件更完整。",
            "<strong>设计语言标准化：</strong>23 个设计命令本质上是定义了人-AI 协作设计的词汇表。这种标准化对于 Agent 设计领域至关重要。"
          ],
          "tags": [
            "design-language",
            "anti-slop",
            "agent-skills",
            "ui-design",
            "frontend",
            "cli-tool"
          ]
        },
        {
          "rank": 2,
          "owner": "TauricResearch",
          "name": "TradingAgents",
          "fullName": "TauricResearch / TradingAgents",
          "org": "Tauric Research",
          "url": "https://github.com/TauricResearch/TradingAgents",
          "lang": "Python",
          "langClass": "py",
          "stars": "81,504",
          "forks": "15,849",
          "starsToday": "284",
          "count": 1,
          "description": "多 Agent 金融交易框架 —— 81K star 的 LLM 量化交易系统，支持多个 LLM 提供商和策略回测",
          "problems": [
            "<strong>传统量化交易门槛高：</strong>需要编程、金融、数学三方面知识。TradingAgents 用多 Agent 架构让 LLM 直接参与交易决策。",
            "<strong>单一 Agent 交易有偏见：</strong>单个 LLM 做交易决策容易过度自信或多变。TradingAgents 使用多 Agent 架构——研究经理、交易员、投资组合经理各司其职。",
            "<strong>回测与实盘不一致：</strong>很多量化框架回测结果和实盘差异大。TradingAgents 支持结构化输出、检查点恢复、持久化决策日志。"
          ],
          "usage": [
            "安装：<pre><code>pip install trading-agents</code></pre>",
            "配置 API Key 和交易策略。",
            "运行多 Agent 交易系统：<code>trading-agents run</code>",
            "支持 OpenAI、Anthropic、DeepSeek、Qwen、GLM 等模型。"
          ],
          "insights": [
            "<strong>AI 交易进入多 Agent 时代：</strong>从单一 LLM 做预测到多 Agent 协作决策，AI 交易的架构在不断进化。",
            "<strong>81K star 的金融 AI 热度：</strong>金融是 AI 最直接的变现场景之一。交易 Agent 的市场关注度极高。",
            "<strong>中文开发者友好：</strong>支持 DeepSeek、Qwen、GLM 等国产模型，中国开发者可轻松上手。"
          ],
          "tags": [
            "trading",
            "multi-agent",
            "fintech",
            "llm-trading",
            "quantitative",
            "backtesting"
          ]
        },
        {
          "rank": 3,
          "owner": "dmtrKovalenko",
          "name": "fff",
          "fullName": "dmtrKovalenko / fff",
          "org": "Dmytro Kovalenko",
          "url": "https://github.com/dmtrKovalenko/fff",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "7,014",
          "forks": "297",
          "starsToday": "121",
          "count": 1,
          "description": "最快的文件搜索工具 —— 为 AI Agent 设计的 Rust 文件查找引擎，支持 Neovim、NodeJS 集成",
          "problems": [
            "<strong>AI Agent 文件搜索太慢：</strong>Agent 需要频繁搜索文件，传统 find/grep 在大代码库时很慢。FFF 用 Rust 实现，搜索速度远超 find 和 fd。",
            "<strong>Agent 工具调用效率低：</strong>每次文件搜索消耗 Token 和时间。FFF 针对 Agent 工作流优化，支持模糊搜索和模式匹配。",
            "<strong>跨工具集成困难：</strong>可用于 Neovim、NodeJS、Rust、C 等不同环境。"
          ],
          "usage": [
            "安装：<pre><code>cargo install fff</code></pre>",
            "在终端中搜索文件：<code>fff filename</code>",
            "在 AI Agent 中配置为默认文件搜索工具。",
            "集成到 Neovim 或 NodeJS 项目中。"
          ],
          "insights": [
            "<strong>Agent 工具链的 Rust 化：</strong>FFF 延续了 AI 工具链的 Rust 化趋势——用 Rust 重写性能敏感的组件。",
            "<strong>小而美的 Agent 基础设施：</strong>7K star 说明「快一点点」对 Agent 工作流来说就是巨大价值。Agent 每次搜索省下来的时间×搜索次数=显著提升。",
            "<strong>搜索即 Agent 的核心能力：</strong>文件搜索是编码 Agent 使用最频繁的操作。优化搜索就是优化 Agent 的核心体验。"
          ],
          "tags": [
            "file-search",
            "rust",
            "agent-tools",
            "performance",
            "developer-tools"
          ]
        },
        {
          "rank": 4,
          "owner": "OpenBMB",
          "name": "VoxCPM",
          "fullName": "OpenBMB / VoxCPM",
          "org": "OpenBMB",
          "url": "https://github.com/OpenBMB/VoxCPM",
          "lang": "Python",
          "langClass": "py",
          "stars": "24,016",
          "forks": "2,768",
          "starsToday": "880",
          "count": 2,
          "description": "清华 OpenBMB 多语言 TTS —— 无需 Tokenizer、支持语音克隆，连续两天上榜 +880",
          "problems": [
            "<strong>传统 TTS 依赖 Tokenizer：</strong>VoxCPM2 是 Tokenizer-Free 的端到端方案。",
            "<strong>多语言 TTS 质量不均：</strong>VoxCPM2 支持多语言包括中文语音生成。",
            "<strong>语音克隆门槛高：</strong>VoxCPM2 实现真实级语音克隆和创意声音设计。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/OpenBMB/VoxCPM</code></pre>",
            "使用预训练模型生成语音。",
            "支持语音克隆和创意声音设计。"
          ],
          "insights": [
            "<strong>清华 OpenBMB 持续输出：</strong>OpenBMB 在 NLP/语音/AI 基础设施领域的开源影响力持续扩大。",
            "<strong>Tokenizer-Free 的 TTS 新方向：</strong>VoxCPM2 推动 TTS 从 token-based 到直接端到端生成的范式转变。"
          ],
          "tags": [
            "tts",
            "speech-synthesis",
            "voice-cloning",
            "openbmb",
            "multilingual",
            "tokenizer-free"
          ]
        },
        {
          "rank": 5,
          "owner": "FareedKhan-dev",
          "name": "train-llm-from-scratch",
          "fullName": "FareedKhan-dev / train-llm-from-scratch",
          "org": "Fareed Khan",
          "url": "https://github.com/FareedKhan-dev/train-llm-from-scratch",
          "lang": "Jupyter Notebook",
          "langClass": "py",
          "stars": "3,474",
          "forks": "491",
          "starsToday": "860",
          "count": 2,
          "description": "从零训练 LLM 实战指南 —— 连续两天上榜 +860，AI 学习类项目热度不减",
          "problems": [
            "<strong>LLM 训练资料碎片化：</strong>端到端完整流程——从数据下载到文本生成。",
            "<strong>理论多代码少：</strong>Jupyter Notebook 形式，每一行代码都可运行。",
            "<strong>入门门槛高：</strong>提供清晰的步骤和可复现的配置。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/FareedKhan-dev/train-llm-from-scratch</code></pre>",
            "按顺序运行 Notebook，从数据到推理全流程覆盖。"
          ],
          "insights": [
            "<strong>AI 教育市场持续火热：</strong>连续两天高增长说明市场需求旺盛。",
            "<strong>动手实践是最好的学习方式：</strong>运行代码训练小型 LLM 的学习效果最好。"
          ],
          "tags": [
            "llm-training",
            "educational",
            "jupyter-notebook",
            "from-scratch",
            "deep-learning"
          ]
        }
      ]
    },
    {
      "date": "2026-05-31",
      "label": "前天",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "nesquena",
          "name": "hermes-webui",
          "fullName": "nesquena / hermes-webui",
          "org": "nesquena",
          "url": "https://github.com/nesquena/hermes-webui",
          "lang": "Python",
          "langClass": "py",
          "stars": "9,634",
          "forks": "1,333",
          "starsToday": "320",
          "count": 1,
          "description": "Hermes Agent 的 Web 界面 —— 在浏览器和手机上使用 Hermes Agent，三面板布局 + 全功能 CLI 能力",
          "problems": [
            "<strong>Hermes Agent 只有终端界面：</strong>终端使用门槛高，移动设备不方便。Hermes WebUI 提供全功能的 Web 界面，手机也能用。",
            "<strong>CLI 和 Web 功能不同步：</strong>很多工具 CLI 和 Web 版功能不一致。Hermes WebUI 承诺与 CLI 完全对等——终端能做的 WebUI 都能做。",
            "<strong>不需要构建工具链：</strong>纯 Python + 原生 JS，无需 npm/build/bundler，一键部署即可使用。"
          ],
          "usage": [
            "Docker 一键部署：<pre><code>docker run -d -p 8080:8080 nesquena/hermes-webui</code></pre>",
            "或本地运行：<pre><code>git clone https://github.com/nesquena/hermes-webui && cd hermes-webui && python app.py</code></pre>",
            "三面板布局：左侧会话列表，中间聊天，右侧文件浏览。",
            "支持模型切换、Profile 管理、上下文用量可视化。"
          ],
          "insights": [
            "<strong>Hermes 生态的 Web 入口：</strong>WebUI 是 Hermes Agent 从极客工具走向大众的关键一步。9.6K star 说明社区对图形化界面有强烈需求。",
            "<strong>全平台覆盖：</strong>终端 + 浏览器 + 手机 + 消息平台（Telegram/Discord/Slack）= Hermes 的四大入口。",
            "<strong>有趣的上榜：</strong>Hermes 生态项目登上 GitHub Trending，说明 Agent 基础设施的市场热度。"
          ],
          "tags": [
            "hermes-agent",
            "web-ui",
            "agent-interface",
            "docker",
            "open-source",
            "ai-agent"
          ]
        },
        {
          "rank": 2,
          "owner": "OpenBMB",
          "name": "VoxCPM",
          "fullName": "OpenBMB / VoxCPM",
          "org": "OpenBMB",
          "url": "https://github.com/OpenBMB/VoxCPM",
          "lang": "Python",
          "langClass": "py",
          "stars": "23,159",
          "forks": "2,701",
          "starsToday": "639",
          "count": 1,
          "description": "VoxCPM2: 无需 Tokenizer 的多语言 TTS —— 清华 OpenBMB 出品，支持语音克隆和创意声音设计",
          "problems": [
            "<strong>传统 TTS 依赖 Tokenizer：</strong>大多数语音合成系统需要将文本转为离散 token，会损失信息。VoxCPM2 是 Tokenizer-Free 的端到端方案。",
            "<strong>多语言 TTS 质量不均：</strong>很多 TTS 在英语好但对中文/其他语言支持差。VoxCPM2 支持多语言语音生成，包括真实到可以克隆的语音。",
            "<strong>声音克隆门槛高：</strong>需要大量训练数据。VoxCPM2 实现真实级语音克隆，创意声音设计功能。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/OpenBMB/VoxCPM</code></pre>",
            "查看文档使用预训练模型。",
            "支持语音克隆（少量样本）、多语言语音生成。"
          ],
          "insights": [
            "<strong>Tokenizer-Free 的 TTS 新范式：</strong>VoxCPM2 代表了 TTS 领域从 token-based 到 tokenizer-free 的技术演进。",
            "<strong>清华 OpenBMB 的持续输出：</strong>OpenBMB（Open Lab for Big Model Base）持续在 NLP/语音/AI 基础设施领域输出高质量开源项目。",
            "<strong>语音克隆的商用前景：</strong>真实级语音克隆 + 创意声音设计 = 虚拟主播、有声书、个性化语音助手等商业场景。"
          ],
          "tags": [
            "tts",
            "speech-synthesis",
            "voice-cloning",
            "openbmb",
            "multilingual",
            "tokenizer-free"
          ]
        },
        {
          "rank": 3,
          "owner": "revfactory",
          "name": "harness",
          "fullName": "revfactory / harness",
          "org": "Rev Factory",
          "url": "https://github.com/revfactory/harness",
          "lang": "HTML",
          "langClass": "",
          "stars": "4,460",
          "forks": "636",
          "starsToday": "318",
          "count": 1,
          "description": "元技能系统 —— 自动设计领域专属 Agent 团队，定义专业 Agent，并生成它们使用的技能",
          "problems": [
            "<strong>不知道 Agent 团队怎么组织：</strong>面对复杂项目，需要多个专业 Agent 协作，但不知道如何划分角色和职责。Harness 自动分析项目领域，设计最优的 Agent 团队结构。",
            "<strong>Agent 技能需要手动编写：</strong>每个专业 Agent 需要对应的技能文件。Harness 不仅设计团队，还自动生成每个 Agent 所需的技能，实现从设计到部署的自动化。",
            "<strong>多 Agent 协作缺乏框架：</strong>Harness 定义了一种「元技能」——不是直接做事的技能，而是设计 Agent 团队的技能。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/revfactory/harness</code></pre>",
            "运行 Harness 分析项目领域。",
            "自动生成 Agent 团队结构和技能文件。"
          ],
          "insights": [
            "<strong>元技能（Meta-Skill）新概念：</strong>Harness 不是教 Agent 做事，而是教 Agent 如何组织其他 Agent。这是 Agent 递归自改进的又一案例。",
            "<strong>Agent 团队设计自动化：</strong>当项目复杂度超过单个 Agent 的能力边界时，自动设计 Agent 团队就变得必要。这类似于微服务架构中服务拆分的自动化。",
            "<strong>Agent 的自我复制与分工：</strong>Harness 代表着 Agent 从「单兵作战」到「团队协作」的进化方向。"
          ],
          "tags": [
            "meta-skill",
            "agent-teams",
            "multi-agent",
            "skill-generation",
            "agent-orchestration"
          ]
        },
        {
          "rank": 4,
          "owner": "FareedKhan-dev",
          "name": "train-llm-from-scratch",
          "fullName": "FareedKhan-dev / train-llm-from-scratch",
          "org": "Fareed Khan",
          "url": "https://github.com/FareedKhan-dev/train-llm-from-scratch",
          "lang": "Jupyter Notebook",
          "langClass": "py",
          "stars": "2,622",
          "forks": "407",
          "starsToday": "627",
          "count": 1,
          "description": "从零训练 LLM 实战指南 —— 从数据下载到文本生成的全流程教程，适合学习者和研究者",
          "problems": [
            "<strong>LLM 训练资料碎片化：</strong>数据准备、模型架构、训练策略、推理部署分散在不同教程中。这个项目提供端到端的完整流程，从下载数据到生成文本。",
            "<strong>理论多代码少：</strong>很多 LLM 教程偏理论，缺少可直接运行的代码。这个教程以 Jupyter Notebook 形式提供，每一行代码都可运行。",
            "<strong>入门门槛高：</strong>训练 LLM 需要 GPU、大内存、深度学习框架……这个教程降低门槛，提供清晰的步骤和可复现的配置。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/FareedKhan-dev/train-llm-from-scratch</code></pre>",
            "按顺序运行 Jupyter Notebook。",
            "从数据下载 -> 预处理 -> 模型构建 -> 训练 -> 推理，全流程覆盖。"
          ],
          "insights": [
            "<strong>LLM 教育市场持续火热：</strong>从零训练 LLM 的教程每天 +627 star，说明 AI 学习需求仍然旺盛。AI 教育是长尾市场。",
            "<strong>动手实践是最好的学习方式：</strong>相比看论文和视频，直接运行代码训练一个小型 LLM 的学习效果最好。这类教程将越来越受欢迎。"
          ],
          "tags": [
            "llm-training",
            "educational",
            "jupyter-notebook",
            "from-scratch",
            "deep-learning"
          ]
        },
        {
          "rank": 5,
          "owner": "supermemoryai",
          "name": "supermemory",
          "fullName": "supermemoryai / supermemory",
          "org": "Supermemory AI",
          "url": "https://github.com/supermemoryai/supermemory",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "23,088",
          "forks": "2,088",
          "starsToday": "236",
          "count": 1,
          "description": "AI 时代的记忆引擎 —— 极速、可扩展的记忆 API，为 Agent 和 AI 应用提供持久化记忆服务",
          "problems": [
            "<strong>AI Agent 没有跨会话记忆：</strong>每次新会话 Agent 都不记得用户是谁、之前聊过什么。Supermemory 提供持久化记忆 API，让 AI 应用拥有长期记忆。",
            "<strong>记忆引擎难以扩展：</strong>为 AI 应用构建记忆系统需要向量数据库、语义搜索、缓存等基础设施。Supermemory 提供开箱即用的 Memory API。",
            "<strong>没有统一的记忆 API 标准：</strong>不同框架有不同的记忆方案，互不兼容。Supermemory 试图成为 AI 时代的 Memory API 标准。"
          ],
          "usage": [
            "集成 API：<pre><code>npm install supermemory</code></pre>",
            "使用 Memory API 存储和检索上下文。",
            "支持向量搜索、语义缓存、会话持久化。"
          ],
          "insights": [
            "<strong>记忆是 AI 应用的核心基础设施：</strong>没有记忆的 AI 就像失忆的人。Supermemory 定位为 AI 时代的记忆层——类似于 Redis 之于 Web 应用。",
            "<strong>Agent 记忆赛道的竞争：</strong>claude-mem（78K★）、Supermemory（23K★）等多个项目在争夺 AI Agent 记忆市场。",
            "<strong>可扩展性是核心竞争力：</strong>每天 +236 star 说明开发者需要可靠的记忆方案。谁能在规模、速度、可靠性上胜出，谁就是 AI 记忆层的赢家。"
          ],
          "tags": [
            "memory-engine",
            "agent-memory",
            "api",
            "vector-search",
            "persistence",
            "ai-infrastructure"
          ]
        }
      ]
    },
    {
      "date": "2026-05-30",
      "label": "3天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "microsoft",
          "name": "markitdown",
          "fullName": "microsoft / markitdown",
          "org": "Microsoft",
          "url": "https://github.com/microsoft/markitdown",
          "lang": "Python",
          "langClass": "py",
          "stars": "130,023",
          "forks": "8,923",
          "starsToday": "1,873",
          "count": 1,
          "description": "微软官方文件转 Markdown 工具 —— PDF/Word/Excel/PPT/图片/音频转 Markdown，专为 LLM 数据处理管道设计",
          "problems": [
            "<strong>非结构化数据难以喂给 LLM：</strong>PDF、Word、Excel 等格式 LLM 无法直接理解。MarkItDown 把所有常见文档格式转为 Markdown，让 AI 可以直接读取和处理。",
            "<strong>文档格式转换碎片化：</strong>PDF 用 PyMuPDF、Excel 用 openpyxl、PPT 用 python-pptx……各自为战。MarkItDown 统一 API：<code>convert('file.pdf')</code> 一行代码搞定。",
            "<strong>RAG 管道的文档预处理瓶颈：</strong>构建 RAG 应用需要先解析文档。MarkItDown 被设计为 LLM 数据处理管道的标准输入层，130K star 证明这是行业需求。"
          ],
          "usage": [
            "安装：<pre><code>pip install markitdown</code></pre>",
            "转换单个文件：<pre><code>from markitdown import MarkItDown\nmd = MarkItDown()\nresult = md.convert('report.docx')</code></pre>",
            "支持：PDF、PowerPoint、Word、Excel、图片(OCR)、音频、HTML、CSV、JSON、XML、ZIP。",
            "在 LLM 数据管道中作为预处理层使用。"
          ],
          "insights": [
            "<strong>LLM 数据管道的标准输入层：</strong>130K star 说明文档转 Markdown 是 LLM 应用开发的基础设施级需求。MarkItDown 正在成为行业标准——类似于 requests 之于 HTTP。",
            "<strong>微软的开源影响力：</strong>微软开源此工具并推向 130K star，说明大厂在 LLM 工具链的标准制定上正在发力。",
            "<strong>Agent 数据接入的大门：</strong>当 AI Agent 需要处理企业文档时，MarkItDown 是首选。它将成为 Agent 读取企业内部知识库的标准方式。"
          ],
          "tags": [
            "microsoft",
            "document-conversion",
            "markdown",
            "LLM-pipeline",
            "RAG",
            "data-processing"
          ]
        },
        {
          "rank": 2,
          "owner": "EveryInc",
          "name": "compound-engineering-plugin",
          "fullName": "EveryInc / compound-engineering-plugin",
          "org": "Every Inc.",
          "url": "https://github.com/EveryInc/compound-engineering-plugin",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "18,147",
          "forks": "1,378",
          "starsToday": "353",
          "count": 1,
          "description": "Compound Engineering 官方插件 —— 为 Claude Code、Codex、Cursor 等 Agent 提供复合工程方法论的工作流插件",
          "problems": [
            "<strong>AI Agent 缺乏工程方法论：</strong>编码 Agent 会写代码但不知道怎么做工程设计。Compound Engineering 插件把系统工程方法论编码成 Agent 可执行的插件——包括策略规划、产品脉冲、架构决策等。",
            "<strong>多 Agent 工作流缺乏框架：</strong>Compound Engineering 不只是单一 Agent 工具，而是定义了一套完整的工程流程——从调研到规划到执行到审查。",
            "<strong>跨 Agent 工具的统一标准：</strong>插件兼容 Claude Code、Codex、Cursor、OpenCode 等，这意味着一套工程方法可以在不同 Agent 工具间复用。"
          ],
          "usage": [
            "在 Claude Code 中安装：<pre><code>claude plugins install everyinc/compound-engineering</code></pre>",
            "在 Codex 中安装：<pre><code>codex plugins install everyinc/compound-engineering</code></pre>",
            "仓库包含完整的插件规格和多 Agent 适配器。",
            "支持 361 个分支、826 次提交，持续迭代。"
          ],
          "insights": [
            "<strong>AI 编码的系统化工程方法论：</strong>Compound Engineering 把系统工程的概念引入 AI 编码——这不是一个工具，而是一个工程框架。未来每个 AI 编码项目都会有自己的工程流程规范。",
            "<strong>Agent 插件生态初现：</strong>EveryInc 定义了 Claude Code / Codex / Cursor 的插件标准，正在成为 Agent 插件生态的基础设施提供者。"
          ],
          "tags": [
            "compound-engineering",
            "agent-plugins",
            "software-engineering",
            "workflow",
            "claude-code",
            "cursor"
          ]
        },
        {
          "rank": 3,
          "owner": "run-llama",
          "name": "liteparse",
          "fullName": "run-llama / liteparse",
          "org": "LlamaIndex",
          "url": "https://github.com/run-llama/liteparse",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "7,342",
          "forks": "445",
          "starsToday": "701",
          "count": 1,
          "description": "LlamaIndex 出品的高性能文档解析器 —— 快速、准确、开源，用 Rust 构建的下一代文档解析引擎",
          "problems": [
            "<strong>现有文档解析器太慢：</strong>Python 解析器在处理大批量文档时性能差。LiteParse 用 Rust 重写，解析速度远快于纯 Python 方案。",
            "<strong>文档解析质量差：</strong>MarkItDown 之类的工具注重通用性，但复杂排版（多列、表格、嵌套列表）解析质量不够。LiteParse 专注于保留文档的完整结构。",
            "<strong>RAG 管道的瓶颈：</strong>文档解析是 RAG 应用的第一公里，解析质量直接影响检索效果。LlamaIndex 作为 RAG 框架的领导者，自然需要自研高性能解析器。"
          ],
          "usage": [
            "安装：<pre><code>pip install liteparse</pre></code>",
            "基本使用：<pre><code>from liteparse import parse\ndoc = parse('document.pdf')</code></pre>",
            "集成到 LlamaIndex 的 RAG 管道中作为文档加载器。"
          ],
          "insights": [
            "<strong>RAG 管道的 Rust 化趋势：</strong>LiteParse 是 LlamaIndex 用 Rust 重写的核心组件。这代表了 RAG 工具链的 Rust 化趋势——核心性能敏感的组件从 Python 迁移到 Rust。",
            "<strong>LlamaIndex 的全栈布局：</strong>从 RAG 框架到文档解析器，LlamaIndex 正在构建 RAG 的全栈闭环。LiteParse + LlamaIndex = 从原始文档到检索增强生成的端到端方案。"
          ],
          "tags": [
            "llamaindex",
            "document-parser",
            "rust",
            "rag",
            "high-performance",
            "open-source"
          ]
        },
        {
          "rank": 4,
          "owner": "cursor",
          "name": "plugins",
          "fullName": "cursor / plugins",
          "org": "Cursor",
          "url": "https://github.com/cursor/plugins",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "1,307",
          "forks": "111",
          "starsToday": "134",
          "count": 1,
          "description": "Cursor 官方插件规范 —— AI 代码编辑器 Cursor 的插件标准，首批官方插件发布",
          "problems": [
            "<strong>Cursor 缺少插件生态：</strong>作为最流行的 AI 编码 IDE 之一，Cursor 之前没有官方的插件系统。现在发布了插件规范和首批官方插件，标志着 Cursor 正式开启生态化。",
            "<strong>Agent 工具的插件标准各自为战：</strong>Claude Code 有 .claude-plugin、Codex 有 .codex-plugin。Cursor 的插件标准可能成为行业参照。",
            "<strong>AI IDE 的边界扩展：</strong>插件系统让 Cursor 从单纯的编码编辑器升级为可扩展的 AI 开发平台。"
          ],
          "usage": [
            "查看插件规范：<pre><code>https://github.com/cursor/plugins</code></pre>",
            "开发 Cursor 插件，遵循目录结构和配置文件标准。",
            "目前 star 数还少（1,307），但意义重大——Cursor 的生态战略刚起步。"
          ],
          "insights": [
            "<strong>AI IDE 的生态战：</strong>Cursor 发布插件系统是 AI IDE 竞争的重要里程碑。谁先建立丰富的插件生态，谁就能锁定开发者——就像 VS Code 对传统 IDE 的颠覆。",
            "<strong>插件标准之争：</strong>EveryInc 的插件、Cursor 的插件、Claude Code 的插件……多个标准并存。未来可能出现统一的 Agent 插件标准，类似 OpenAPI 之于 API。",
            "<strong>星星虽少，意义重大：</strong>1,307 star 在这期榜单里算少的，但作为生态基建项目，其长期影响力不可忽视。"
          ],
          "tags": [
            "cursor",
            "plugin-system",
            "ide-ecosystem",
            "ai-ide",
            "plugin-specification"
          ]
        },
        {
          "rank": 5,
          "owner": "galilai-group",
          "name": "stable-worldmodel",
          "fullName": "galilai-group / stable-worldmodel",
          "org": "GALILAI Group",
          "url": "https://github.com/galilai-group/stable-worldmodel",
          "lang": "Python",
          "langClass": "py",
          "stars": "1,260",
          "forks": "149",
          "starsToday": "362",
          "count": 1,
          "description": "世界模型研究平台 —— 可复现的世界模型训练与评估基准，从视频数据中学习物理规律",
          "problems": [
            "<strong>世界模型研究缺少标准化基准：</strong>世界模型（World Model）是通往通用 AI 的关键路径——让 AI 从视频/交互数据中学习物理世界的规律。但不同论文用的数据集、评估指标不同，难以比较。",
            "<strong>世界模型难以复现：</strong>论文中的结果往往因为代码未开源或环境不一致而无法复现。Stable Worldmodel 提供标准化的训练和评估平台。",
            "<strong>从视频理解到物理理解：</strong>传统视频理解是被动的（识别物体），世界模型是主动的（预测物理变化）。这个平台推动 AI 从感知走向认知。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/galilai-group/stable-worldmodel</code></pre>",
            "使用标准数据集训练世界模型。",
            "在统一基准上评估和比较不同的世界模型方法。"
          ],
          "insights": [
            "<strong>世界模型：AI 的下一个前沿：</strong>从大语言模型到世界模型，AI 正在从理解语言进化到理解物理世界。这是通往通用 AI 的关键基础设施。",
            "<strong>研究基建化：</strong>Stable Worldmodel 类似于 ImageNet 之于计算机视觉——标准化基准推动了整个领域的发展。",
            "<strong>1.2K star 的潜力股：</strong>虽然现在 star 数少，但随着世界模型领域热度上升，这个项目的价值可能被重估。"
          ],
          "tags": [
            "world-model",
            "AI-research",
            "benchmark",
            "video-understanding",
            "physical-reasoning",
            "reproducibility"
          ]
        }
      ]
    },
    {
      "date": "2026-05-28",
      "label": "4天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "harry0703",
          "name": "MoneyPrinterTurbo",
          "fullName": "harry0703 / MoneyPrinterTurbo",
          "org": "harry0703",
          "url": "https://github.com/harry0703/MoneyPrinterTurbo",
          "lang": "Python",
          "langClass": "py",
          "stars": "61,823",
          "forks": "9,036",
          "starsToday": "1,737",
          "count": 1,
          "description": "AI 一键生成短视频 —— 输入主题/关键词，自动生成文案、素材、字幕、背景音乐并合成高清短视频",
          "problems": [
            "<strong>短视频制作门槛高：</strong>普通人想做短视频需要写脚本、找素材、配音、加字幕、配乐，流程复杂。MoneyPrinterTurbo 把这一切自动化。",
            "<strong>AI 视频工具碎片化：</strong>文案用 ChatGPT、配音用 TTS、剪辑用剪映……多个工具来回切换。这个项目端到端完成——输入主题，输出成品视频。",
            "<strong>多语言视频制作：</strong>支持中文和英文文案，多种语音合成，可实时试听效果。适合面向海外市场的短视频创作者。"
          ],
          "usage": [
            "使用 Docker 部署：<pre><code>docker run -d -p 8501:8501 harry0703/moneyprinterturbo</code></pre>",
            "或本地部署：<pre><code>git clone https://github.com/harry0703/MoneyPrinterTurbo && cd MoneyPrinterTurbo</code></pre>",
            "在 Web 界面输入视频主题，一键生成。",
            "支持 OpenAI、DeepSeek、Moonshot 等多种大模型。"
          ],
          "insights": [
            "<strong>AI 短视频自动化流水线：</strong>从文案生成到视频合成全链路自动化。可以做成 SaaS——中国短视频创作者付费订阅，输入关键词自动输出可直接发布到抖音/快手的视频。",
            "<strong>61K star 验证 PMF：</strong>市场对 AI 视频生成的需求极大。中国短视频生态巨大，这类工具的商业化空间非常可观。",
            "<strong>多模型接入策略：</strong>支持 DeepSeek、Moonshot 等国产模型（无需 VPN），精准切中中国用户痛点。"
          ],
          "tags": [
            "video-generation",
            "short-video",
            "AI-automation",
            "text-to-video",
            "chinese-market",
            "open-source"
          ]
        },
        {
          "rank": 2,
          "owner": "p-e-w",
          "name": "heretic",
          "fullName": "p-e-w / heretic",
          "org": "p-e-w",
          "url": "https://github.com/p-e-w/heretic",
          "lang": "Python",
          "langClass": "py",
          "stars": "21,995",
          "forks": "2,348",
          "starsToday": "219",
          "count": 1,
          "description": "大语言模型去审查工具 —— 自动移除 AI 模型的 safety alignment，无需昂贵的后训练",
          "problems": [
            "<strong>大模型回答过于保守：</strong>很多大模型因为 safety alignment 拒绝回答合理的问题。Heretic 通过 directional ablation（方向消融）技术自动移除审查，不需要昂贵的后训练。",
            "<strong>传统去审查方法复杂：</strong>需要理解模型内部结构、手动调参。Heretic 使用 Optuna 自动优化参数，任何会命令行的人都能用。",
            "<strong>模型兼容性差：</strong>不同模型结构不同，去审查方法不通用。Heretic 支持大多数密集模型、多模态模型、MoE 架构和混合模型。"
          ],
          "usage": [
            "安装：<pre><code>pip install heretic</code></pre>",
            "运行自动去审查：<pre><code>heretic decensor --model meta-llama/Llama-3.1-8B-Instruct</code></pre>",
            "参数自动优化，无需手动调整。",
            "支持本地和 Hugging Face 模型。"
          ],
          "insights": [
            "<strong>AI 安全的天平正在倾斜：</strong>hertic + abliteration 等工具让去审查门槛越来越低。安全对齐和安全破解的攻防战将成为 AI 行业常态。",
            "<strong>21K star 的争议性：</strong>这类工具的高关注度说明用户对 AI 过度审查的强烈不满。未来模型厂商需要重新平衡安全与自由。",
            "<strong>自动化工具链化：</strong>从手动修改到自动参数优化，去审查流程变得越来越工程化。这是一个持续演进的猫鼠游戏。"
          ],
          "tags": [
            "llm-safety",
            "abliteration",
            "decensorship",
            "model-optimization",
            "open-source",
            "ai-alignment"
          ]
        },
        {
          "rank": 3,
          "owner": "Leonxlnx",
          "name": "taste-skill",
          "fullName": "Leonxlnx / taste-skill",
          "org": "Leonxlnx",
          "url": "https://github.com/Leonxlnx/taste-skill",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "24,133",
          "forks": "1,861",
          "starsToday": "2,715",
          "count": 3,
          "description": "AI 品味技能 —— 连续霸榜第三天，+2,715 star，重新定义 AI Agent 的审美标准",
          "problems": [
            "<strong>AI 生成前端千篇一律：</strong>所有 AI Agent 写出代码都一个样。Taste-Skill 提供专业设计指南。",
            "<strong>AI 味太浓：</strong>防止 AI 输出模板化 UI，持续丰富技能类型。",
            "<strong>三天霸榜验证需求：</strong>连续三天单日 +2,000+ star 说明了市场对 AI 审美的强烈需求。"
          ],
          "usage": [
            "安装技能：<pre><code>npx skills add https://github.com/Leonxlnx/taste-skill</code></pre>",
            "在代码生成任务前加载技能，AI Agent 自动遵循设计指南。",
            "包含多套设计风格（新拟态、极简、玻璃态等）。"
          ],
          "insights": [
            "<strong>AI 审美成为刚需：</strong>连续霸榜三天说明 AI 输出审美不是锦上添花，而是核心痛点。AI 编码 Agent 面临的最大问题不是能不能写代码，而是能不能写出好看的代码。",
            "<strong>Agent 技能市场正在形成：</strong>Taste-Skill 是 Agent 技能市场化的最佳案例。一个 SKILL.md 文件吸引 24K star，证明 Agent 技能本身就是可分发、可变现的产品。"
          ],
          "tags": [
            "ui-design",
            "anti-slop",
            "design-system",
            "agent-skills",
            "frontend",
            "aesthetics"
          ]
        },
        {
          "rank": 4,
          "owner": "affaan-m",
          "name": "ECC",
          "fullName": "affaan-m / ECC",
          "org": "affaan-m",
          "url": "https://github.com/affaan-m/ECC",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "195,978",
          "forks": "30,147",
          "starsToday": "2,062",
          "count": 2,
          "description": "Agent 工具链优化系统 —— 横跨 12+ Agent 生态，195K star，持续霸榜中的王者",
          "problems": [
            "<strong>AI Agent 配置碎片化：</strong>每个 Agent 工具格式不同。ECC 提供统一的工具链优化系统。",
            "<strong>Agent 缺乏持续学习：</strong>ECC 内置记忆优化、技能积累、连续学习。",
            "<strong>Agent 安全未标准化：</strong>ECC 内置安全扫描、Prompt 防御、沙箱化运行。"
          ],
          "usage": [
            "安装：<code>npx ecc install</code>",
            "查看技能：<code>ecc skills list</code>",
            "安全扫描：<code>ecc security scan</code>"
          ],
          "insights": [
            "<strong>Agent 工具链标准化已成趋势：</strong>195K star 证明这不是小众需求。ECC 正在成为 Agent 世界的标准配置层。",
            "<strong>即将突破 200K star：</strong>每天 +2,000 star 的增长速度，ECC 将在数日内成为 200K+ star 的超爆款项目。"
          ],
          "tags": [
            "agent-harness",
            "agent-security",
            "multi-platform",
            "skills",
            "memory-optimization",
            "anthropic-winner"
          ]
        },
        {
          "rank": 5,
          "owner": "twentyhq",
          "name": "twenty",
          "fullName": "twentyhq / twenty",
          "org": "Twenty HQ",
          "url": "https://github.com/twentyhq/twenty",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "47,310",
          "forks": "6,716",
          "starsToday": "520",
          "count": 2,
          "description": "AI-Native 开源 CRM —— Salesforce 替代品，46K star，持续上榜的 AI 企业级应用标杆",
          "problems": [
            "<strong>Salesforce 体验差价格贵：</strong>Twenty 用现代技术栈重构 CRM。",
            "<strong>传统 CRM 不是为 AI 设计：</strong>Twenty 从底层为 AI 优化——GraphQL API 专为 AI Agent 调用设计。",
            "<strong>企业级开源 CRM 稀缺：</strong>12,000+ 提交、785 分支，成熟度极高。"
          ],
          "usage": [
            "自托管：<pre><code>git clone https://github.com/twentyhq/twenty</code></pre>",
            "或使用云端版：<code>twenty.com</code>",
            "API 优先设计，AI Agent 可直接操作 CRM 数据。"
          ],
          "insights": [
            "<strong>AI-Native CRM 新品类持续验证：</strong>连续两天上榜说明市场在认真关注 AI 原生企业级应用。Twenty 的开源策略正在挑战 Salesforce 的垄断地位。",
            "<strong>Agent 直接写 CRM 数据：</strong>AI 编码 Agent + Twenty = Agent 自动更新客户记录、销售管线。这是企业级 AI Agent 落地的典型场景。"
          ],
          "tags": [
            "crm",
            "salesforce-alternative",
            "ai-native",
            "graphql",
            "open-source",
            "typescript"
          ]
        }
      ]
    },
    {
      "date": "2026-05-27",
      "label": "5天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "thedotmack",
          "name": "claude-mem",
          "fullName": "thedotmack / claude-mem",
          "org": "TheDotMack",
          "url": "https://github.com/thedotmack/claude-mem",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "78,620",
          "forks": "6,764",
          "starsToday": "319",
          "count": 1,
          "description": "AI Agent 的持久记忆系统 —— 自动记录 Agent 的所有操作，压缩后用 AI 注入到后续会话中，支持 Claude Code / Codex / Gemini / Hermes 等",
          "problems": [
            "<strong>AI Agent 每次会话都失忆：</strong>每次新会话 Agent 都不记得之前做了什么。Claude-mem 自动捕获 Agent 会话中的所有操作，用 AI 压缩成结构化记忆，下次会话自动注入相关上下文。",
            "<strong>Agent 上下文窗口有限：</strong>即使有记忆，上下文窗口也容纳不了全部历史。Claude-mem 用智能压缩算法把大量操作提炼成关键记忆点，只注入当前任务需要的上下文。",
            "<strong>跨工具记忆不互通：</strong>在 Claude Code 积累的知识，切换到 Codex 就没了。Claude-mem 兼容 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等主流 Agent。"
          ],
          "usage": [
            "安装 claude-mem：<pre><code>npx claude-mem install</code></pre>",
            "自动捕获 Agent 会话，压缩并保存记忆。",
            "在 Agent 配置中启用记忆注入。",
            "支持的 Agent：Claude Code、Codex、Gemini、Hermes、Copilot 等。"
          ],
          "insights": [
            "<strong>Agent 记忆即基础设施：</strong>78K star 证明 Agent 记忆是当前最痛的需求之一。可以做成 SaaS——云端 Agent 记忆服务，跨设备、跨工具持久化。",
            "<strong>记忆压缩是核心竞争力：</strong>不是简单的日志记录，而是用 AI 压缩成高密度记忆。这需要专门的大模型优化——谁压缩得好、检索准，谁就是市场赢家。",
            "<strong>人类-AI 协作的桥梁：</strong>持久记忆让 Agent 不再每次从零开始，而是像人类同事一样积累经验。这是 Agent 从工具进化成「数字同事」的关键一步。"
          ],
          "tags": [
            "agent-memory",
            "persistent-context",
            "multi-agent",
            "session-persistence",
            "ai-compression"
          ]
        },
        {
          "rank": 2,
          "owner": "anthropics",
          "name": "knowledge-work-plugins",
          "fullName": "anthropics / knowledge-work-plugins",
          "org": "Anthropic",
          "url": "https://github.com/anthropics/knowledge-work-plugins",
          "lang": "Python",
          "langClass": "py",
          "stars": "16,633",
          "forks": "1,952",
          "starsToday": "1,698",
          "count": 2,
          "description": "Anthropic 官方知识工作者插件集 —— 持续火热，让 Claude Cowork 变身销售/支持/工程等角色的专业助手，单日 +1,698 star",
          "problems": [
            "<strong>AI Agent 不够专业：</strong>通用 AI Agent 不知道不同岗位的工作流程。11 个角色插件捆绑对应技能的连接器和子 Agent。",
            "<strong>企业工具链碎片化：</strong>Slack、Notion、Jira、HubSpot 等工具各自独立。插件预置了每个角色的关键工具连接器。",
            "<strong>跨版本持续更新：</strong>从 4 天前发布至今每天积累 star，项目不断迭代，新增更多插件和 MCP 集成。"
          ],
          "usage": [
            "在 Claude Cowork 中直接使用：<code>/plugin install sales</code>",
            "安装工程插件：<code>/plugin install engineering</code>",
            "每个插件包含技能、连接器、斜杠命令和子 Agent。"
          ],
          "insights": [
            "<strong>持续霸榜验证 PMF：</strong>连续 4 天上榜且 star 数持续增长，证明 Anthropic 的角色插件策略获得了市场的强烈认可。",
            "<strong>企业级 AI 的先发优势：</strong>Anthropic 在定义「AI 角色的标准模板」。率先占领企业心智的品牌将获得长期的生态红利。"
          ],
          "tags": [
            "anthropic-official",
            "claude-cowork",
            "role-plugins",
            "enterprise",
            "knowledge-work",
            "MCP"
          ]
        },
        {
          "rank": 3,
          "owner": "rohitg00",
          "name": "ai-engineering-from-scratch",
          "fullName": "rohitg00 / ai-engineering-from-scratch",
          "org": "Rohit G",
          "url": "https://github.com/rohitg00/ai-engineering-from-scratch",
          "lang": "Python",
          "langClass": "py",
          "stars": "20,659",
          "forks": "3,443",
          "starsToday": "2,169",
          "count": 3,
          "description": "AI 工程从零到一 —— 学习它、构建它、交付给他人，最热门的 AI 工程学习资源之一",
          "problems": [
            "<strong>AI 工程教育门槛高：</strong>从基础模型到部署上线，AI 工程的全链路知识分散。这个项目提供从零开始构建 AI 工程能力的系统化学习路径。",
            "<strong>理论多、实战少：</strong>不只是理论，强调「构建」和「交付」——每一阶段都有可运行的代码和项目。",
            "<strong>持续更新适应行业变化：</strong>AI 领域变化快，很多教材很快就过时了。这个 GitHub 项目可以持续更新。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/rohitg00/ai-engineering-from-scratch</code></pre>",
            "按章节学习，每个模块都有可运行的代码。",
            "阅读源码并动手实践。"
          ],
          "insights": [
            "<strong>AI 教育的天花板效应：</strong>这个项目已经 4 次上榜且每次都有高日增 star，说明 AI 工程学习需求持续旺盛。AI 教育的市场远未饱和。",
            "<strong>从「学 AI」到「做 AI」的转变：</strong>项目名强调「from scratch」（从零到一）和「ship it」（交付），反映了行业从学习 AI 概念到实际构建 AI 产品的需求转变。"
          ],
          "tags": [
            "ai-engineering",
            "education",
            "learning-path",
            "hands-on",
            "python"
          ]
        },
        {
          "rank": 4,
          "owner": "Leonxlnx",
          "name": "taste-skill",
          "fullName": "Leonxlnx / taste-skill",
          "org": "Leonxlnx",
          "url": "https://github.com/Leonxlnx/taste-skill",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "21,528",
          "forks": "1,734",
          "starsToday": "1,440",
          "count": 2,
          "description": "AI 品味技能 —— 正在重新定义 AI Agent 的审美标准，单日 +1,440 star，连续第二天上榜",
          "problems": [
            "<strong>AI 生成的前端审美差：</strong>所有 AI Agent 写出代码都一个样子。Taste-Skill 提供布局、排版、动效、间距的专业设计指南。",
            "<strong>AI 味太浓：</strong>专门针对 Claude Code、Codex、Cursor 等 Agent 输出进行优化，打破 AI 默认模板化 UI。",
            "<strong>持续丰富技能类型：</strong>从最初的前端设计技能扩展到图片生成技能，覆盖参考板、线框图、品牌套件等。"
          ],
          "usage": [
            "安装：<pre><code>npx skills add https://github.com/Leonxlnx/taste-skill</code></pre>",
            "在代码生成任务前加载技能，AI Agent 自动遵循设计指南。",
            "包含多套设计风格（新拟态、极简、玻璃态等）。"
          ],
          "insights": [
            "<strong>AI 审美的垂直赛道：</strong>连续两天上榜且单日 +1,440 star，证明「AI 审美」是一个真实且快速增长的市场需求。",
            "<strong>从设计技能到品牌资产：</strong>未来每个企业都会有自己的品味技能包，就像现在每个企业有自己的设计系统一样。企业的 AI 输出风格将成为品牌资产。"
          ],
          "tags": [
            "ui-design",
            "anti-slop",
            "design-system",
            "agent-skills",
            "frontend",
            "aesthetics"
          ]
        },
        {
          "rank": 5,
          "owner": "twentyhq",
          "name": "twenty",
          "fullName": "twentyhq / twenty",
          "org": "Twenty HQ",
          "url": "https://github.com/twentyhq/twenty",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "46,833",
          "forks": "6,649",
          "starsToday": "237",
          "count": 1,
          "description": "Salesforce 的开源替代品 —— 专为 AI 设计的 CRM，46K star，12,000+ 提交的成熟项目",
          "problems": [
            "<strong>传统 CRM 体验差：</strong>Salesforce 功能强大但用户体验差、配置复杂、价格昂贵。Twenty 用现代技术栈重构 CRM 体验。",
            "<strong>CRM 没有 AI 原生设计：</strong>传统 CRM 的 AI 功能是后加的。Twenty 从底层为 AI 设计——AI 可以直接操作数据结构、分析客户关系、自动更新记录。",
            "<strong>开源 CRM 选择少：</strong>企业级开源 CRM 几乎没有成熟选项。Twenty 有 12,000+ 提交和 785 分支，项目活跃度极高。"
          ],
          "usage": [
            "自托管：<pre><code>git clone https://github.com/twentyhq/twenty</code></pre>",
            "或使用云端版：<code>twenty.com</code>",
            "API 优先设计，支持 GraphQL 查询。",
            "AI Agent 可通过 API 直接操作 CRM 数据。"
          ],
          "insights": [
            "<strong>AI-Native CRM 的新品类：</strong>「Designed for AI」不是口号——Twenty 的 GraphQL API 和数据模型专门为 AI Agent 调用优化。AI 可以自动更新客户记录、分析销售管线、发送跟进邮件。",
            "<strong>Salesforce 的颠覆窗口：</strong>46K star 且持续增长，开源 CRM 正在挑战 Salesforce 的垄断地位。AI 原生设计是差异化竞争的关键。",
            "<strong>企业级开源的新标杆：</strong>12,000+ 提交、785 分支、444 标签——Twenty 不是玩具项目，而是成熟的企业级开源产品。"
          ],
          "tags": [
            "crm",
            "salesforce-alternative",
            "ai-native",
            "graphql",
            "open-source",
            "typescript"
          ]
        }
      ]
    },
    {
      "date": "2026-05-26",
      "label": "6天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "affaan-m",
          "name": "ECC",
          "fullName": "affaan-m / ECC",
          "org": "affaan-m",
          "url": "https://github.com/affaan-m/ECC",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "192,277",
          "forks": "29,765",
          "starsToday": "2,052",
          "count": 1,
          "description": "Agent 工具链性能优化系统 —— 技能/本能/记忆/安全，覆盖 Claude Code、Codex、Cursor 等 12+ 生态的完整 Agent 工作台",
          "problems": [
            "<strong>AI 编码 Agent 配置碎片化：</strong>每个 Agent 工具（Claude Code、Codex、Cursor、Gemini 等）有自己的配置格式和规则文件。ECC 提供统一的工具链优化系统，跨 12+ 平台无缝工作。",
            "<strong>Agent 缺乏持续学习能力：</strong>每次新会话 Agent 都从零开始。ECC 包含记忆优化、技能积累、连续学习机制，让 Agent 越用越聪明。",
            "<strong>Agent 安全没有标准化：</strong>Agent 生成的代码可能引入漏洞。ECC 内置安全扫描、Prompt 防御基线、沙箱化运行，来自 Anthropic 黑客松获奖项目。"
          ],
          "usage": [
            "快速安装 ECC：<pre><code>npx ecc install</code></pre>",
            "查看所有可用技能：<code>ecc skills list</code>",
            "运行安全扫描：<code>ecc security scan</code>",
            "支持 Claude Code、Codex、Cursor、OpenCode、Gemini、Zed、GitHub Copilot 等。"
          ],
          "insights": [
            "<strong>Agent 工具链的标准化层：</strong>ECC 相当于 Agent 世界的 dotfiles——不管底层用哪个 Agent，都有统一的工作流配置。可以做成 SaaS 产品，企业团队统一管理 Agent 行为。",
            "<strong>192K star 的 AI Agent 基础设施：</strong>近 20 万 star 证明了 AI Agent 工具链标准化的巨大需求。ECC 从 Anthropic 黑客松项目成长为跨生态的标准。",
            "<strong>Agent Shiled 安全新品类：</strong>ECC 内置的 AgentShield 和 Prompt 防御机制开辟了 Agent 安全的新赛道。随着 Agent 越来越自主，安全防线将成为刚需。"
          ],
          "tags": [
            "agent-harness",
            "agent-security",
            "multi-platform",
            "skills",
            "memory-optimization",
            "anthropic-winner"
          ]
        },
        {
          "rank": 2,
          "owner": "mukul975",
          "name": "Anthropic-Cybersecurity-Skills",
          "fullName": "mukul975 / Anthropic-Cybersecurity-Skills",
          "org": "mukul975",
          "url": "https://github.com/mukul975/Anthropic-Cybersecurity-Skills",
          "lang": "Python",
          "langClass": "py",
          "stars": "9,188",
          "forks": "1,134",
          "starsToday": "999",
          "count": 1,
          "description": "AI Agent 的网络安全技能库 —— 754 个结构化安全技能，覆盖 MITRE ATT&CK、NIST CSF 等 5 大框架",
          "problems": [
            "<strong>AI Agent 缺乏网络安全专业知识：</strong>AI 编码 Agent 懂写代码但不一定懂安全。这个项目提供了 754 个结构化网络安全技能，让 AI Agent 拥有高级安全分析师的知识水平。",
            "<strong>安全框架碎片化：</strong>MITRE ATT&CK、NIST CSF、NIST AI RMF 等框架各自独立，普通开发者很难全面掌握。这个技能库把 5 个框架统一映射到同一套技能集。",
            "<strong>安全知识难以复用到 Agent 工作流：</strong>传统安全知识在 SIEM 中，Agent 用不上。这 754 个技能以 agentskills.io 开放标准组织，Agent 可以直接调用——从检测 Kerberoasting 到云安全事件响应。"
          ],
          "usage": [
            "克隆仓库：<pre><code>git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills</code></pre>",
            "通过 Claude Code / Codex / Cursor 直接加载技能文件。",
            "Agent 会自动在安全审计、漏洞检测、事件响应中使用这些技能。",
            "兼容 26+ AI 平台，包括 Claude Code、Copilot、Codex CLI、Gemini CLI 等。"
          ],
          "insights": [
            "<strong>Agent 专业技能库的新品类：</strong>继通用编码技能后，垂直领域的 Agent 技能库正在爆发——网络安全、金融、法律等。可以做成技能市场，每个行业贡献自己的 Agent 技能包。",
            "<strong>安全 Agent 即服务：</strong>企业无需雇佣高级安全分析师，直接向 AI Agent 注入 754 个安全技能。安全 Agent 可以作为 DevOps 流水线的一个环节自动运行。",
            "<strong>框架合规自动化：</strong>MITRE ATT&CK/NIST CSF 映射意味着安全 Agent 可以自动生成合规报告。安全审计从季度人工检查变成持续自动化。"
          ],
          "tags": [
            "cybersecurity",
            "skills-library",
            "MITRE-ATTACK",
            "NIST-CSF",
            "agent-skills",
            "security-automation"
          ]
        },
        {
          "rank": 3,
          "owner": "colbymchenry",
          "name": "codegraph",
          "fullName": "colbymchenry / codegraph",
          "org": "Colby McHenry",
          "url": "https://github.com/colbymchenry/codegraph",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "24,830",
          "forks": "1,371",
          "starsToday": "3,171",
          "count": 3,
          "description": "预索引的代码知识图谱 —— 为 Claude Code、Codex、Cursor 等 Agent 减少 Token 消耗和工具调用，100% 本地",
          "problems": [
            "<strong>AI 编码 Agent 读代码效率低：</strong>Agent 需要频繁读取文件、搜索代码，消耗大量 Token 和时间。Codegraph 提前为整个代码库建立知识图谱，Agent 直接查询无需扫描文件。",
            "<strong>大型代码库 Agent 无法应对：</strong>百万行级项目的上下文窗口不够用。Codegraph 的预索引图谱让 Agent 精确找到需要的代码，而不是盲目搜索。",
            "<strong>跨工具不可移植：</strong>一个代码库的索引只能在一个工具中用。Codegraph 兼容 Claude Code、Codex、Cursor、OpenCode、Hermes Agent 等多个平台。"
          ],
          "usage": [
            "在项目根目录运行：<code>npx codegraph</code>",
            "支持 Claude Code、Codex、Cursor、OpenCode、Hermes Agent。",
            "Agent 启动后自动加载知识图谱。"
          ],
          "insights": [
            "<strong>Agent 上下文管理的革命：</strong>Codegraph 从根本上改变了 Agent 理解代码的方式——从实时搜索到预索引图谱。这将大幅降低 Agent 的使用成本。",
            "<strong>企业级代码库智能：</strong>大型企业代码库（百万行+）在 Agent 时代需要全新的索引基础设施。Codegraph 可以被视为 Agent 时代的 IDE 后端。",
            "<strong>持续火热（+3,171 star/天）：</strong>连续多天上榜证明市场对此类产品的强烈需求。Agent 的代码理解效率是当前最紧迫的问题。"
          ],
          "tags": [
            "code-knowledge-graph",
            "code-indexing",
            "token-optimization",
            "multi-agent",
            "local-first"
          ]
        },
        {
          "rank": 4,
          "owner": "Leonxlnx",
          "name": "taste-skill",
          "fullName": "Leonxlnx / taste-skill",
          "org": "Leonxlnx",
          "url": "https://github.com/Leonxlnx/taste-skill",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "19,647",
          "forks": "1,651",
          "starsToday": "542",
          "count": 1,
          "description": "给 AI 注入好品味 —— 从源头杜绝 AI 生成的廉价、模板化界面，让 AI Agent 输出有设计感的代码",
          "problems": [
            "<strong>AI 生成的前端太「AI 味」：</strong>所有 AI Agent 写的前端看起来都差不多——居中、白底、圆角卡片、蓝色按钮。Taste Skill 提供布局、排版、动效、间距的专业指南，让 AI 输出有真正设计感的界面。",
            "<strong>Agent UI 缺乏设计体系：</strong>AI 不懂设计原则。Taste Skill 包含了完整的前端设计体系指南，覆盖从排版到交互的所有层面。",
            "<strong>反 AI 模板化：</strong>专门针对 Claude Code、Codex、Cursor 等 Agent 的输出进行优化，打破 AI 默认的模板化 UI。"
          ],
          "usage": [
            "安装技能：<pre><code>npx skills add https://github.com/Leonxlnx/taste-skill</code></pre>",
            "在代码生成任务前加载技能，AI Agent 自动遵循设计指南。",
            "包含多套设计风格（新拟态、极简、玻璃态等）。",
            "也包含图片生成技能（参考板、线框图、品牌套件）。"
          ],
          "insights": [
            "<strong>AI 审美的商业化机会：</strong>19.6K star 证明 AI 输出的审美问题是一个巨大的痛点。可以做成 AI 前端模板市场——不同风格、不同行业的「品味包」订阅服务。",
            "<strong>Agent 技能的垂直化：</strong>Taste Skill 是 Agent 技能垂直化（编码→设计）的典型案例。未来每个设计领域都会有专门的 Agent 品味技能。",
            "<strong>AI 同质化竞争的解药：</strong>当所有 AI 工具能力趋同，审美和品味会成为差异化竞争的关键。企业的 AI 输出风格会成为品牌资产的一部分。"
          ],
          "tags": [
            "ui-design",
            "anti-slop",
            "design-system",
            "agent-skills",
            "frontend",
            "aesthetics"
          ]
        },
        {
          "rank": 5,
          "owner": "hardikpandya",
          "name": "stop-slop",
          "fullName": "hardikpandya / stop-slop",
          "org": "Hardik Pandya",
          "url": "https://github.com/hardikpandya/stop-slop",
          "lang": "Markdown",
          "langClass": "",
          "stars": "4,374",
          "forks": "381",
          "starsToday": "353",
          "count": 1,
          "description": "AI 文本反「AI 味」技能 —— 一个 skill 文件即可去除 AI 写作的模板化特征，让文字更像真人",
          "problems": [
            "<strong>AI 生成的文字「AI 味」太重：</strong>「值得注意的是」「毋庸置疑」「在这个充满挑战的时代」——AI 有自己的一套高频用语。Stop Slop 提供了反 AI 味的写作指南。",
            "<strong>AI 散文缺乏真实感：</strong>真实的人写作有个人风格、有口语化表达、有不确定性。AI 倾向于过度正式和确定性语言。这个 skill 文件教导 AI 写出更自然的散文。",
            "<strong>简单可移植：</strong>不像复杂的提示工程，Stop Slop 只是一个 skill 文件（SKILL.md），任何兼容 Agent 的工具都可以加载。"
          ],
          "usage": [
            "安装 skill：<pre><code>npx skills add https://github.com/hardikpandya/stop-slop</code></pre>",
            "或直接复制 SKILL.md 到项目 .claude/ 目录。",
            "Agent 在写作时自动应用反 AI 味指南。"
          ],
          "insights": [
            "<strong>AI 输出的「去 AI 化」市场：</strong>当 AI 内容泛滥，能写出像真人一样的 AI 工具会成为稀缺资源。去 AI 味工具（如 Stop Slop、Humanizer）会成为 AI 写作的标配。",
            "<strong>Skill 文件作为产品：</strong>一个 SKILL.md 文件获得 4K+ star——Agent 技能本身就是可发布的产品形态。未来会像 VS Code 扩展市场一样出现 Agent 技能市场。",
            "<strong>内容质量的新标准：</strong>「不像 AI 写的」正在成为内容质量的新标准。从 SEO 角度看，去 AI 味的内容在 Google 排名中更有优势。"
          ],
          "tags": [
            "anti-slop",
            "writing-tone",
            "agent-skills",
            "content-quality",
            "natural-writing"
          ]
        }
      ]
    },
    {
      "date": "2026-05-24",
      "label": "8天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "anthropics",
          "name": "knowledge-work-plugins",
          "fullName": "anthropics / knowledge-work-plugins",
          "org": "Anthropic",
          "url": "https://github.com/anthropics/knowledge-work-plugins",
          "lang": "Python",
          "langClass": "py",
          "stars": "13,355",
          "forks": "1,640",
          "starsToday": "486",
          "count": 1,
          "description": "Anthropic 官方知识工作者插件集 -- 让 Claude Cowork 变身销售/支持/工程/法务等角色的专业助手",
          "problems": [
            "<strong>AI Agent 不够专业：</strong>通用 AI Agent 不知道不同岗位的工作流程。Anthropic 推出 11 个角色插件——销售、客服、产品、工程、市场、法务、数据、设计、生物研究等，每个插件捆绑对应角色的技能、连接器、斜杠命令和子 Agent。",
            "<strong>企业工具链碎片化：</strong>Slack、Notion、Jira、HubSpot、Figma 等几十个工具各自独立。Knowledge Work Plugins 预置了每个角色的关键工具连接器，比如销售插件自动连接 Slack + HubSpot + Close + ZoomInfo。",
            "<strong>团队协作一致性差：</strong>每个人用 AI 的方式不同，产出参差不齐。插件定义标准化的角色工作流——销售人员用统一的线索研究、客户沟通、Pipeline Review 流程。"
          ],
          "usage": [
            "在 Claude Cowork 中直接使用，<code>/plugin</code> 浏览可用插件。",
            "安装销售插件：<code>/plugin install sales</code>",
            "安装工程插件：<code>/plugin install engineering</code>",
            "每个插件包含技能、连接器、斜杠命令和子 Agent。"
          ],
          "insights": [
            "<strong>AI 角色即服务（AI Role-as-a-Service）：</strong>Anthropic 定义了 AI Agent 的 11 种角色模板。可以做成 SaaS——企业订阅不同角色包，每个角色有预配置的工具链和工作流。",
            "<strong>企业 AI 岗位标准化：</strong>每家公司都可以定制自己的角色插件——把公司内部的 SOP、工具链、知识库打包成 Agent 角色。新员工入职时直接分配对应角色的 AI 助手。",
            "<strong>角色插件市场：</strong>继 claude-plugins-official 的通用插件市场后，Knowledge Work Plugins 开创了垂直领域的角色插件。未来可能有第三方角色插件商店。"
          ],
          "tags": [
            "anthropic-official",
            "claude-cowork",
            "role-plugins",
            "enterprise",
            "knowledge-work",
            "MCP"
          ]
        },
        {
          "rank": 2,
          "owner": "earendil-works",
          "name": "pi",
          "fullName": "earendil-works / pi",
          "org": "Earendil Works",
          "url": "https://github.com/earendil-works/pi",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "53,678",
          "forks": "6,416",
          "starsToday": "444",
          "count": 1,
          "description": "AI Agent 工具包全家桶 -- 编码 Agent CLI + 统一 LLM API + TUI/Web UI + Slack Bot + vLLM 集群",
          "problems": [
            "<strong>AI Agent 工具链分散：</strong>编码 Agent、LLM API、终端 UI、Web UI、Slack Bot 各自独立项目，集成成本高。Pi 把所有打包在一个 monorepo——@pi-coding-agent（CLI）、@pi-agent-core（运行时）、@pi-ai（统一 LLM API）、@pi-tui（终端 UI）。",
            "<strong>模型切换麻烦：</strong>OpenAI、Anthropic、Google 各有各的 API 格式和 SDK。@pi-ai 提供统一的多模型 API，一行代码切换模型提供商。",
            "<strong>Agent 会话缺少分享机制：</strong>Agent 的开发过程难复现、难调试。Pi 支持将 OSS 编码会话发布到 Hugging Face，公开分享 Agent 的真实工作记录。"
          ],
          "usage": [
            "安装编码 Agent CLI：<pre><code>npm install -g @earendil-works/pi-coding-agent</code></pre>",
            "启动交互式编码 Agent：<code>pi</code>",
            "使用统一 LLM API：<pre><code>import { ai } from '@earendil-works/pi-ai'</code></pre>",
            "发布会话到 HF：<pre><code>npx pi-share-hf</code></pre>"
          ],
          "insights": [
            "<strong>Agent 开发全栈平台：</strong>Pi 不只是编码 Agent，而是 Agent 开发的全栈工具包——从底层 LLM 调用到前端 UI，再到 Slack 集成。可以做成类似 Vercel 但面向 AI Agent 的一站式平台。",
            "<strong>会话数据即训练数据：</strong>Pi 的会话分享机制（发布到 Hugging Face）本质是在构建 Agent 行为的开源数据集。这些真实世界的编码会话数据对训练更好的编码 Agent 极其宝贵。",
            "<strong>vLLM 集群集成：</strong>Pi 支持 vLLM pods，意味着可以自托管开源模型做 Agent 推理。企业可部署私有 Pi 集群，数据不出内网。"
          ],
          "tags": [
            "coding-agent",
            "llm-api",
            "monorepo",
            "agent-toolkit",
            "vLLM",
            "open-source"
          ]
        },
        {
          "rank": 3,
          "owner": "Alishahryar1",
          "name": "free-claude-code",
          "fullName": "Alishahryar1 / free-claude-code",
          "org": "Alishahryar1",
          "url": "https://github.com/Alishahryar1/free-claude-code",
          "lang": "Python",
          "langClass": "py",
          "stars": "28,875",
          "forks": "4,332",
          "starsToday": "565",
          "count": 1,
          "description": "免费使用 Claude Code -- 终端/VSCode/Discord 三合一，支持语音，无需 Anthropic 付费账号",
          "problems": [
            "<strong>Claude Code 需要付费 API Key：</strong>Anthropic 的 Claude Code 需要绑定付费账号，对于学习者和开发者来说成本较高。free-claude-code 通过整合免费模型和代理，让用户在终端、VSCode 扩展或 Discord 中免费使用类似 Claude Code 的体验。",
            "<strong>多平台切换繁琐：</strong>终端编码、VSCode 扩展、Discord 机器人——不同场景需要不同工具。Free Claude Code 一个项目覆盖三种模式，包括语音输入支持。",
            "<strong>编码 Agent 门槛高：</strong>配置 API Key、管理上下文窗口、调整模型参数对新手不友好。FCC 开箱即用，像 OpenClaw 一样简单。"
          ],
          "usage": [
            "终端使用：<pre><code>pip install free-claude-code && fcc</code></pre>",
            "VSCode 扩展：在扩展市场搜索 Free Claude Code 安装。",
            "Discord Bot：邀请机器人到服务器，<code>/fcc 写一个 React 组件</code>",
            "启用语音：<code>fcc --voice</code>"
          ],
          "insights": [
            "<strong>AI 编码的民主化：</strong>28K star 证明市场对免费 AI 编码 Agent 的巨大需求。开发者想要零成本的 AI 编程体验。",
            "<strong>多模态 Agent 入口：</strong>终端 + IDE + 聊天 + 语音，四个入口覆盖所有使用场景。可以做成 Agent 的多模态接入层。",
            "<strong>教育市场黄金入口：</strong>面向编程学习者免费提供 AI 编码 Agent——学生无需付费就能获得 AI 编程体验，培养使用习惯，后续转化为付费用户。"
          ],
          "tags": [
            "free-tier",
            "claude-code",
            "vscode-extension",
            "discord-bot",
            "voice-support",
            "openclaw"
          ]
        },
        {
          "rank": 4,
          "owner": "multica-ai",
          "name": "multica",
          "fullName": "multica-ai / multica",
          "org": "Multica AI",
          "url": "https://github.com/multica-ai/multica",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "32,242",
          "forks": "3,888",
          "starsToday": "584",
          "count": 1,
          "description": "开源托管 Agent 平台 -- 把编码 Agent 变成真正的队友：分配任务、追踪进度、复用技能",
          "problems": [
            "<strong>AI Agent 各自为战：</strong>每个开发者有自己的 Claude Code / Codex，但彼此不协作、不共享上下文。Multica 把编码 Agent 变成团队成员——在项目看板上给 Agent 分配 Issue，像给同事派活一样。",
            "<strong>Agent 没有长期记忆和技能积累：</strong>每次新任务 Agent 都从头开始。Multica 让 Agent 复合技能——完成的任务转化为可复用的技能文件，下次同类任务直接使用。",
            "<strong>多 Agent 缺乏协调：</strong>多个 Agent 处理同一项目时容易冲突。Multica 的 Squads 功能提供稳定的路由层：组长 Agent 分配任务给组员 Agent，像真正的团队协作。"
          ],
          "usage": [
            "部署 Multica 平台（支持自托管）：<pre><code>git clone https://github.com/multica-ai/multica</code></pre>",
            "接入 Claude Code / Codex / Copilot 等 Agent。",
            "在项目看板上创建 Issue 分配给 Agent。",
            "Agent 自动接管任务、写代码、报告进度。"
          ],
          "insights": [
            "<strong>AI 团队管理平台：</strong>Multica 开创了 Agent 即同事的产品品类。可以做成 SaaS——企业的 AI 开发团队管理平台，每个 Agent 有独立的 Jira/Linear 任务、Git 提交记录、Code Review 历史。",
            "<strong>Agent 技能复合引擎：</strong>技能积累是 Multica 的核心价值——每次任务产生的知识自动转化为可复用的技能文件。类似人的经验积累，Agent 越用越熟练。",
            "<strong>人+AI 混合团队：</strong>Multica 的 Squads 让人类和 Agent 在同一个团队中工作——人类做架构决策，Agent 执行编码。这是未来软件开发团队的标准形态。"
          ],
          "tags": [
            "managed-agents",
            "task-assignment",
            "skill-compounding",
            "multi-agent",
            "self-hosted",
            "platform"
          ]
        },
        {
          "rank": 5,
          "owner": "manaflow-ai",
          "name": "cmux",
          "fullName": "manaflow-ai / cmux",
          "org": "Manaflow AI",
          "url": "https://github.com/manaflow-ai/cmux",
          "lang": "Swift",
          "langClass": "rs",
          "stars": "18,761",
          "forks": "1,431",
          "starsToday": "560",
          "count": 1,
          "description": "为 AI 编码 Agent 打造的 macOS 终端 -- Ghostty 内核 + 垂直标签 + 智能通知",
          "problems": [
            "<strong>终端不支持 Agent 工作流：</strong>传统终端（iTerm2、Terminal.app）没有为 AI 编码 Agent 设计。Cmux 基于 Ghostty 构建，每个 Agent 会话有独立的垂直标签页和侧边栏，显示 Git 分支、PR 状态、工作目录和端口信息。",
            "<strong>Agent 通知被忽略：</strong>Agent 完成任务后没有合适的通知机制。Cmux 的通知环（蓝色光环）和通知面板让 Agent 在需要人类介入时引起注意，不再错过 Agent 的请求。",
            "<strong>多 Agent 协作终端混乱：</strong>同时运行多个 Agent 时终端窗口混乱不堪。Cmux 支持 Claude Code Teams 模式——队友以原生分屏出现，带侧边栏元数据和通知。"
          ],
          "usage": [
            "安装 cmux：<pre><code>brew install manaflow-ai/tap/cmux</code></pre>",
            "启动 Claude Code Teams：<pre><code>cmux claude-teams</code></pre>",
            "SSH 远程开发：<pre><code>cmux ssh user@remote</code></pre>",
            "内嵌浏览器：在终端中分割浏览器面板。"
          ],
          "insights": [
            "<strong>Agent 原生终端的全新品类：</strong>Cmux 是第一个专门为 AI 编码 Agent 设计的终端。传统终端厂商（iTerm2、Warp）需要跟进——Agent 工作流需要全新的终端交互范式。",
            "<strong>Agent 协作的 UI 层：</strong>Cmux 的通知系统和 Claude Code Teams 集成意味着终端不仅是 CLI 界面，更是 Agent 团队协作的 UI 层。未来的 IDE 可能不是 VS Code，而是增强型终端。",
            "<strong>Agent 浏览器集成：</strong>内嵌浏览器 + 脚本化 API 让 Agent 可以直接在终端中操作网页（调试、截图、检查）。终端正在变成 Agent 的操作系统。"
          ],
          "tags": [
            "macos-terminal",
            "ghostty",
            "claude-code-teams",
            "agent-notifications",
            "vertical-tabs",
            "ai-native"
          ]
        }
      ]
    },
    {
      "date": "2026-05-23",
      "label": "9天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "anthropics",
          "name": "claude-plugins-official",
          "fullName": "anthropics / claude-plugins-official",
          "org": "Anthropic",
          "url": "https://github.com/anthropics/claude-plugins-official",
          "lang": "Python",
          "langClass": "py",
          "stars": "24,963",
          "forks": "2,766",
          "starsToday": "2,549",
          "count": 2,
          "description": "Anthropic 官方 Claude Code 插件目录 —— 连续两日热榜，今日 +2,549 star，插件生态持续爆发",
          "problems": [
            "<strong>插件发现仍然困难：</strong>虽然官方目录已上线，但随着插件数量增长（403 commits，314 branches），如何从数百个插件中找到最适合自己的仍然是个挑战。目录支持 Discover 浏览 + 关键词搜索。",
            "<strong>第三方插件质量审核：</strong>外部插件需要提交审核后才能进入 marketplace。审核流程确保安全性和质量标准，同时支持社区贡献。",
            "<strong>跨平台兼容：</strong>Claude Code、Cursor、Codex 等 Agent 都有自己的插件格式。官方目录统一了插件定义格式（.claude-plugin/plugin.json），一次开发多平台可用。"
          ],
          "usage": [
            "在 Claude Code 中浏览发现插件：<code>/plugin > Discover</code>",
            "一键安装插件：<pre><code>/plugin install {plugin-name}@claude-plugins-official</code></pre>",
            "查看已安装的插件列表：<code>/plugin list</code>",
            "GitHub 仓库浏览全部插件源码：<a href=\"https://github.com/anthropics/claude-plugins-official\" style=\"color:#58a6ff\">github.com/anthropics/claude-plugins-official</a>"
          ],
          "insights": [
            "<strong>插件经济的爆发前夜：</strong>25K star + 每日 2.5K+ 增速，Claude Code 的 App Store 时刻正在到来。开发者可以像 iOS 开发者一样靠插件变现。",
            "<strong>企业插件内购模式：</strong>企业可以自建私有插件目录——标准化内部工具、API、数据库的 Agent 接口，所有开发者统一使用，降低 onboarding 成本。",
            "<strong>安全审核即服务：</strong>随着插件数量爆发，插件的安全审核成为刚需——自动化插件安全扫描、行为分析、沙箱测试，类似移动 App 的安全审核市场。"
          ],
          "tags": [
            "claude-code",
            "plugin-marketplace",
            "anthropic-official",
            "one-click-install",
            "MCP",
            "Agent-extensions"
          ]
        },
        {
          "rank": 2,
          "owner": "Lum1104",
          "name": "Understand-Anything",
          "fullName": "Lum1104 / Understand-Anything",
          "org": "Lum1104",
          "url": "https://github.com/Lum1104/Understand-Anything",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "18,678",
          "forks": "1,692",
          "starsToday": "1,393",
          "count": 1,
          "description": "把任意代码库变成可视化的交互式知识图谱 —— 文件、函数、类、依赖关系一目了然，Claude Code / Codex / Cursor 全兼容",
          "problems": [
            "<strong>新项目上手像大海捞针：</strong>加入一个 20 万行代码的项目，从哪开始？逐文件阅读效率极低。Understand Anything 用多 Agent 管道分析项目，自动构建知识图谱——每个文件、函数、类、依赖都成为可点击的节点。",
            "<strong>只看代码看不透业务逻辑：</strong>代码结构不等于业务逻辑。Domain View 模式把代码映射为业务领域、流程、步骤的可视化横向图谱，帮新人理解&quot;这段代码到底在做什么业务&quot;。",
            "<strong>改代码不知道影响范围：</strong>改一个函数可能影响十个模块。Diff Impact Analysis 在提交前告诉你改动会波及系统的哪些部分，避免上线事故。"
          ],
          "usage": [
            "Claude Code 安装：<code>/plugin install understand-anything</code>",
            "分析代码库：<pre><code>/understand-code /path/to/your/project</code></pre>",
            "启动交互式知识图谱仪表盘：<pre><code>/understand-dashboard</code></pre>",
            "使用搜索功能：<code>/understand-search \"which parts handle auth?\"</code>"
          ],
          "insights": [
            "<strong>代码可视化 onboarding 平台：</strong>新员工入职时不用看文档，直接看知识图谱理解系统架构。做成 SaaS——上传仓库链接，自动生成交互式架构图，按项目数/用户数收费。",
            "<strong>代码 Impact Analysis 即服务：</strong>在 CI/CD 中集成——每次 PR 自动生成变更影响分析报告，标注被影响的上下游模块，防止低级上线事故。",
            "<strong>AI 编程时代的代码阅读器：</strong>AI 能写代码但不好理解代码。这个工具填补了&quot;AI 写的代码人类怎么看得懂&quot;的空白——反向知识图谱即 AI 代码的可解释性层。"
          ],
          "tags": [
            "knowledge-graph",
            "code-visualization",
            "onboarding",
            "multi-agent",
            "claude-code",
            "diff-impact-analysis"
          ]
        },
        {
          "rank": 3,
          "owner": "ChromeDevTools",
          "name": "chrome-devtools-mcp",
          "fullName": "ChromeDevTools / chrome-devtools-mcp",
          "org": "Chrome DevTools Team",
          "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "40,980",
          "forks": "2,603",
          "starsToday": "501",
          "count": 1,
          "description": "Chrome 官方推出的 MCP 服务器 —— 让 AI 编程 Agent 直接操控 Chrome 浏览器，调试、性能分析、自动化一条龙",
          "problems": [
            "<strong>AI Agent 不能直接操控浏览器：</strong>Agent 要做 Web 调试、性能分析、网络请求检查时，只能通过人类手动操作 DevTools，无法自动化。Chrome DevTools MCP 让 Agent 直接获得完整的 Chrome DevTools 能力——截图、网络分析、性能追踪、控制台日志。",
            "<strong>Web 自动化工具多但互不兼容：</strong>Playwright、Selenium、Puppeteer 各有各的 API。MCP 统一协议让所有 Agent（Claude Code、Cursor、Copilot、Gemini CLI）通过一套标准接口操控浏览器。",
            "<strong>性能分析门槛高：</strong>Chrome DevTools 的 Performance 面板很强大，但手动分析录制、解读火焰图对普通开发者不友好。Agent 自动录制性能追踪、提取可操作的优化建议。"
          ],
          "usage": [
            "npx 一键运行：<pre><code>npx @puppeteer/chrome-devtools-mcp</code></pre>",
            "在 Claude Code 中配置 MCP 服务器连接。",
            "Agent 自动获得 DevTools 能力——截图、网络请求检查、控制台日志读取、性能录制。",
            "支持 puppeteer 自动化，Action 自动等待结果。"
          ],
          "insights": [
            "<strong>AI 测试工程师：</strong>Agent+Chrome DevTools = 全自动的 Web 测试工程师——打开页面、截图、检查网络请求、分析性能、断言正确性。颠覆传统 E2E 测试。",
            "<strong>Web 调试助手：</strong>开发者口头描述 bug，Agent 自动打开 DevTools 检查网络/控制台/元素，定位问题根因。面向非前端开发的&quot;帮我看看这个页面为什么卡&quot;场景。",
            "<strong>Chrome 生态的 Agent 入口：</strong>Chrome 官方出品 MCP 服务器，标志着浏览器厂商正式拥抱 AI Agent 生态。未来每个浏览器功能（DevTools、Lighthouse、Accessibility）都可以通过 MCP 被 Agent 调用。"
          ],
          "tags": [
            "chrome-devtools",
            "MCP",
            "browser-automation",
            "performance-analysis",
            "debugging",
            "google-official"
          ]
        },
        {
          "rank": 4,
          "owner": "can1357",
          "name": "oh-my-pi",
          "fullName": "can1357 / oh-my-pi",
          "org": "can1357",
          "url": "https://github.com/can1357/oh-my-pi",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "6,357",
          "forks": "516",
          "starsToday": "457",
          "count": 1,
          "description": "终端 AI 编码 Agent —— hash 锚定编辑、40+ 模型、32 内置工具、LSP + DAP 深度集成，Rust 核心",
          "problems": [
            "<strong>Agent 编码效率低：</strong>很多 Agent 的编辑格式会导致模型反复重试失败（str_replace 格式下模型容易出错）。oh-my-pi 的 hash-anchored edits 让编辑一次命中率从 6.7% 飙升至 68.3%。",
            "<strong>IDE 能力与 Agent 割裂：</strong>Agent 写代码时无法利用 IDE 的 LSP（智能提示、跳转定义、引用查找）和 DAP（断点调试）。oh-my-pi 内置 13 个 LSP 操作 + 27 个 DAP 操作，把 IDE 能力直接注入 Agent。",
            "<strong>模型适配混乱：</strong>不同模型（Grok、Gemini、MiniMax）对同一工具格式的适配效果天差地别。oh-my-pi 为每个模型单独调优 prompts，Grok Code Fast 下 lift 10 倍。"
          ],
          "usage": [
            "macOS/Linux 一键安装：<pre><code>curl -fsSL https://omp.sh/install | sh</code></pre>",
            "Bun 安装：<pre><code>bun install -g @oh-my-pi/pi-coding-agent</code></pre>",
            "启动编码 Agent：<code>omp</code>",
            "支持 40+ 模型提供商，自动选择最优 prompt 配置。"
          ],
          "insights": [
            "<strong>Agent 编辑格式标准之争：</strong>oh-my-pi 的 hash-anchored edits 相比于 Anthropic 的 str_replace 编辑格式更高效。如果成为标准，可能改变所有 Agent 的底层编辑方式。",
            "<strong>本地 IDE 的 Agent 化：</strong>LSP + DAP 深度集成意味着 Agent 和 IDE 的边界在消失。可以做成&quot;Agent 原生 IDE&quot;——用户在 IDE 中聊天，Agent 自动使用 LSP/DAP 完成编码-调试循环。",
            "<strong>模型适配平台：</strong>oh-my-pi 为每个模型单独调优 prompts 的模式可以独立成服务——&quot;你的 Agent 工具哪个模型最好用？&quot; 提供模型 + 工具格式的最优匹配推荐。"
          ],
          "tags": [
            "coding-agent",
            "terminal",
            "hash-anchored-edits",
            "LSP",
            "DAP",
            "40+ providers"
          ]
        },
        {
          "rank": 5,
          "owner": "rohitg00",
          "name": "ai-engineering-from-scratch",
          "fullName": "rohitg00 / ai-engineering-from-scratch",
          "org": "rohitg00",
          "url": "https://github.com/rohitg00/ai-engineering-from-scratch",
          "lang": "Python",
          "langClass": "py",
          "stars": "11,953",
          "forks": "2,272",
          "starsToday": "988",
          "count": 2,
          "description": "从零开始的 AI 工程实战教程 —— 学→造→交付，每天近千 star 的爆款开源课程",
          "problems": [
            "<strong>AI 工程学习路径不清晰：</strong>从理论到实战的路太远——数学、框架、部署、运维，每步都有坑。这门课从零到交付提供完整路径，每章有 Jupyter Notebook + 实战项目。",
            "<strong>缺乏实战导向的教程：</strong>很多教程教概念但缺少端到端实战项目。该课程强调&quot;造出来、交付出去&quot;——每个模块都产出可部署的产品。",
            "<strong>学习社区孤岛：</strong>传统课程学完就结束。该项目采用开源社区模式，学员可以贡献自己的项目，形成持续学习网络。"
          ],
          "usage": [
            "Clone 课程仓库：<pre><code>git clone https://github.com/rohitg00/ai-engineering-from-scratch</code></pre>",
            "从第一章开始，每章有 Jupyter Notebook + 实战项目。",
            "跟着课程从零构建 AI 应用并部署到生产环境。",
            "参与社区讨论，分享自己的项目作品。"
          ],
          "insights": [
            "<strong>AI 工程培训认证：</strong>以该课程为基础提供&quot;AI 工程师&quot;认证培训——面向转行/应届生，从零到就业的全套培训方案。11.9K star 验证了巨大的市场需求。",
            "<strong>项目作品集平台：</strong>学员完成课程后产出的项目自动形成作品集——对接企业招聘需求，打造&quot;学→做→找工作&quot;闭环。",
            "<strong>企业内训定制：</strong>为企业提供定制版课程——根据团队技术栈调整内容，加上企业自己的数据集和场景，形成企业 AI 人才培养体系。"
          ],
          "tags": [
            "ai-engineering",
            "from-scratch",
            "hands-on",
            "python",
            "production-deployment",
            "open-source-course"
          ]
        }
      ]
    },
    {
      "date": "2026-05-22",
      "label": "10天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "anthropics",
          "name": "claude-plugins-official",
          "fullName": "anthropics / claude-plugins-official",
          "org": "Anthropic",
          "url": "https://github.com/anthropics/claude-plugins-official",
          "lang": "Python",
          "langClass": "py",
          "stars": "22,337",
          "forks": "2,640",
          "starsToday": "891",
          "count": 1,
          "description": "Anthropic 官方 Claude Code 插件目录 —— 官方管理的优质 Claude Code 插件市场",
          "problems": [
            "<strong>找不到靠谱的 Claude Code 插件：</strong>Claude Code 生态快速增长，但插件来源分散在 GitHub 各处，质量参差不齐。Anthropic 官方出手——发布官方插件目录，所有插件经过审核，一个命令即可安装。",
            "<strong>安装配置复杂：</strong>之前要手动配置 MCP 服务器、写 .mcp.json、管理依赖。现在 /plugin install {插件名}@claude-plugins-official 一键安装，/plugin > Discover 浏览发现。",
            "<strong>没有统一的插件发现机制：</strong>社区插件藏在 GitHub 各个角落，用户无从知道有哪些可用插件。官方目录提供搜索、发现、安装一站式体验，覆盖 Anthropic 内部插件 + 第三方社区插件。"
          ],
          "usage": [
            "在 Claude Code 中浏览发现插件：<code>/plugin > Discover</code>",
            "一键安装插件：<pre><code>/plugin install {plugin-name}@claude-plugins-official</code></pre>",
            "查看已安装的插件列表：<code>/plugin list</code>",
            "GitHub 仓库浏览插件源码：<a href=\"https://github.com/anthropics/claude-plugins-official\" style=\"color:#58a6ff\">github.com/anthropics/claude-plugins-official</a>"
          ],
          "insights": [
            "<strong>Claude Code 插件生态的 App Store：</strong>Anthropic 官方插件目录就像一个 App Store——审核准入、统一安装、版本管理。可以想象未来插件开发者提交插件到该目录，类似 iOS App Store 的经济模型。",
            "<strong>企业 Agent 插件管理：</strong>企业版可以在此基础上做私有插件目录——只有经过 IT 部门审核的插件可用，确保安全合规，同时支持企业自研内部工具插件。",
            "<strong>插件即 Agent 能力商店：</strong>Claude Code 插件本质上就是 Agent 的\"技能扩展\"。这个模式可以扩展到其他 AI Agent 平台（Cursor、Codex 等），形成跨平台的 Agent 插件经济。"
          ],
          "tags": [
            "claude-code",
            "plugin-marketplace",
            "anthropic-official",
            "one-click-install",
            "MCP",
            "Agent-extensions"
          ]
        },
        {
          "rank": 2,
          "owner": "multica-ai",
          "name": "andrej-karpathy-skills",
          "fullName": "multica-ai / andrej-karpathy-skills",
          "org": "Multica AI",
          "url": "https://github.com/multica-ai/andrej-karpathy-skills",
          "lang": "",
          "langClass": "",
          "stars": "143,098",
          "forks": "14,669",
          "starsToday": "2,590",
          "count": 1,
          "description": "一份 CLAUDE.md 文件让 Claude Code 脱胎换骨 —— 源自 Andrej Karpathy 对 LLM 编码痛点的深刻洞察",
          "problems": [
            "<strong>Claude Code 乱猜不确认：</strong>Karpathy 指出——AI Agent 会默认自己的假设是正确的，不检查、不确认、不追问、不暴露权衡。这套技能通过 Think Before Coding 原则强制 Agent 先推理再行动。",
            "<strong>过度工程化：</strong>Agent 特别喜欢写复杂抽象——不需要的灵活性、不必要的配置化、100 行能解决的问题写成 1000 行。Simplicity First 原则让 Agent 只写刚好够用的代码。",
            "<strong>误改不相关代码：</strong>Agent 经常顺手改掉旁边不该动的注释或代码块。Surgical Changes 原则要求 Agent 只动任务相关的代码行，其他保持原样。"
          ],
          "usage": [
            "直接将 CLAUDE.md 放到项目根目录：<pre><code>curl -O https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md</code></pre>",
            "或安装为 Claude Code 插件：<code>/plugin install karpathy-guidelines</code>",
            "支持 Cursor：将 CURSOR.md 放到项目 .cursor/rules/ 目录。",
            "Agent 自动遵循四条原则：Think Before Coding → Simplicity First → Surgical Changes → Goal-Driven Execution"
          ],
          "insights": [
            "<strong>AI Agent 行为配置的范式转变：</strong>143K star 证明——好的 Agent 行为指南是最大的刚需。可以做成 AI Agent 行为配置平台：不同人格/角色/场景的 CLAUDE.md 模板市场，像 WordPress 主题一样交易。",
            "<strong>企业 Agent 行为管控：</strong>企业可以制定统一的行为规范 CLAUDE.md——哪些代码风格必须遵守、哪些安全规则不能绕过、哪些测试必须通过。每个开发者提交代码前，Agent 先自检再交付。",
            "<strong>Karpathy 风格的 Agent 教育：</strong>用这个技能培训 AI 编码 Agent——像训练实习生一样教 Agent 如何思考、如何简化、如何安全地修改代码。Agent 通过技能文件\"上课\"，比任何微调都更灵活。"
          ],
          "tags": [
            "karpathy",
            "claude-code",
            "coding-guidelines",
            "think-before-coding",
            "simplicity-first",
            "cursor"
          ]
        },
        {
          "rank": 3,
          "owner": "teng-lin",
          "name": "notebooklm-py",
          "fullName": "teng-lin / notebooklm-py",
          "org": "teng-lin",
          "url": "https://github.com/teng-lin/notebooklm-py",
          "lang": "Python",
          "langClass": "py",
          "stars": "14,363",
          "forks": "1,993",
          "starsToday": "182",
          "count": 1,
          "description": "Google NotebookLM 的非官方 Python API 与 Agent 技能 —— Python、CLI、Claude Code 三合一访问 NotebookLM 全部能力",
          "problems": [
            "<strong>NotebookLM 没有公开 API：</strong>Google NotebookLM 只有 Web UI，想编程化使用无处下手。notebooklm-py 逆向工程实现完整 API，支持 Python、CLI 和 AI Agent 三种接入方式。",
            "<strong>Agent 无法使用 NotebookLM：</strong>Claude Code / Codex 等 AI Agent 需要 NotebookLM 的强大能力（音频生成、深度研究、知识管理），但没 API 就没法集成。该库作为 MCP 技能让 Agent 直接调用。",
            "<strong>Web UI 功能受限：</strong>NotebookLM Web 版不支持批量下载、不支持 Quiz/Flashcard 多种格式导出、不支持自动化研究管线。notebooklm-py 暴露了 Web UI 没有的隐藏功能。"
          ],
          "usage": [
            "Python 安装：<pre><code>pip install notebooklm-py</code></pre>",
            "CLI 使用：<pre><code>notebooklm create-notebook --title \"AI 研究综述\"</code></pre>",
            "生成音频概览：<pre><code>notebooklm generate-audio --source source.pdf</code></pre>",
            "在 Claude Code 中作为 MCP 技能导入，通过自然语言操控 NotebookLM 生成播客/视频/幻灯片等。"
          ],
          "insights": [
            "<strong>封闭 AI 产品的 API 化服务：</strong>类似 notebooklm-py 的模式可复制到其他无 API 的 AI 产品（Perplexity、Gamma 等）——逆向工程提供 API 供开发者和 Agent 使用，按调用量收费。",
            "<strong>自动化研究管线 SaaS：</strong>基于 NotebookLM 构建自动化研究管线——定时抓取论文/网页 → 自动导入 NotebookLM → 生成音频摘要/播客 → 推送到团队。面向科研团队、VC 分析师。",
            "<strong>教育内容工厂：</strong>NotebookLM 的 Audio Overview（播客式摘要）是最受欢迎的功能。批量把课件/教材转成 AI 播客供学生通勤时听——知识付费+教育科技新方向。"
          ],
          "tags": [
            "notebooklm",
            "python-api",
            "research-automation",
            "audio-overview",
            "MCP",
            "google"
          ]
        },
        {
          "rank": 4,
          "owner": "HKUDS",
          "name": "CLI-Anything",
          "fullName": "HKUDS / CLI-Anything",
          "org": "HKU DS",
          "url": "https://github.com/HKUDS/CLI-Anything",
          "lang": "Python",
          "langClass": "py",
          "stars": "39,104",
          "forks": "3,710",
          "starsToday": "644",
          "count": 3,
          "description": "让所有软件都拥有 AI Agent 原生接口 —— CLI-Hub：为每款软件一键生成命令行接口，Agent 无需 GUI 直接操控",
          "problems": [
            "<strong>AI Agent 操控软件只能靠截图+模拟点击：</strong>大多数软件没有 CLI 也没 API，Agent 只能截图识别 GUI 元素再模拟点击——不稳定、慢、一换版就崩。CLI-Anything 为任意软件自动生成稳定高效的 CLI 接口。",
            "<strong>Agent 工具定义碎片化：</strong>Claude Code 用 MCP、Cursor 用插件、OpenClaw 用工具——每个平台格式不同。CLI-Hub 统一标准，一次封装到处可用。",
            "<strong>传统 RPA 太脆弱：</strong>Selenium、Playwright 等 UI 自动化测试工具依赖页面结构，前端一重构就全部失效。CLI 接口天然稳定，不依赖 UI 元素。"
          ],
          "usage": [
            "安装 CLI-Anything Hub：<pre><code>pip install cli-anything-hub</code></pre>",
            "安装社区已有的 CLI 封装：<pre><code>cli-hub install <name></code></pre>",
            "为目标软件生成 CLI：<pre><code>cli-anything wrap <software-path></code></pre>",
            "浏览已有封装的 CLI-Hub：<a href=\"https://clianything.cc/\" style=\"color:#58a6ff\">clianything.cc</a>"
          ],
          "insights": [
            "<strong>企业软件 Agent 适配平台：</strong>CLI-Anything 解决 AI Agent 落地的核心难题——操作现有软件。可以做成 SaaS 平台：企业上传内部系统，平台自动生成 CLI 接口并持续维护，按软件数量收费。",
            "<strong>Agent 软件适配市场：</strong>CLI-Hub 类似 npm 但面向 Agent 工具生态——开发者上传 CLI 封装，Agent 开发者下载使用。39K star 证明了需求的真实性。",
            "<strong>遗留系统 Agent 化改造：</strong>银行、保险等行业有大量 COBOL/Java 老系统，没有现代 API。CLI-Anything 一键为这些老系统生成 Agent 接口，让 AI Agent 能操作任何年代的系统。"
          ],
          "tags": [
            "agent-native",
            "cli-hub",
            "software-automation",
            "MCP",
            "tool-generation",
            "39k-stars"
          ]
        },
        {
          "rank": 5,
          "owner": "obra",
          "name": "superpowers",
          "fullName": "obra / superpowers",
          "org": "obra",
          "url": "https://github.com/obra/superpowers",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "201,473",
          "forks": "17,947",
          "starsToday": "1,572",
          "count": 4,
          "description": "全栈 AI 智能体技能框架与开发方法论 —— 200K+ star 证明这是最流行的 Agent 开发标准",
          "problems": [
            "<strong>AI Agent 开发没有标准方法论：</strong>每个人用 Cursor/Claude Code 的方式各不相同——有人问问题、有人直接写代码、有人拼 prompt。Superpowers 定义了从 Spec → Plan → 子 Agent 实现 → 自动审查的完整方法论。",
            "<strong>Agent 技能文件没有统一格式：</strong>.claude/skills/ 里的 Markdown 文件格式各异，管理混乱。Superpowers 定义了标准化的技能文件格式和 CLI 管理工具。",
            "<strong>多 Agent 协作混乱：</strong>前端 Agent、后端 Agent、测试 Agent 各自为政，缺乏协调框架。Superpowers 内置 Multi-Agent 编排——一个总 Agent 拆解任务，子 Agent 并行开发，自动合并。"
          ],
          "usage": [
            "安装 Superpowers CLI：<pre><code>npx @agentic/superpowers</code></pre>",
            "初始化项目技能：<pre><code>superpowers init</code></pre>",
            "浏览可用技能库：<pre><code>superpowers list</code></pre>",
            "安装特定技能到项目：<pre><code>superpowers install react-component</code></pre>"
          ],
          "insights": [
            "<strong>Agent 开发方法论咨询：</strong>200K star 证明 Superpowers 定义了 Agent 开发的标准。可以做成企业培训+咨询产品——\"如何用 Superpowers 方法论构建 AI 原生开发团队\"。",
            "<strong>技能文件模板市场：</strong>像 GitHub Marketplace 一样交易 Agent 技能文件——前端技能包、后端技能包、DevOps 技能包，每个 $5-50。企业采购版本确保安全审计。",
            "<strong>企业 Agent 治理平台：</strong>企业版统一管理所有开发者的技能文件——强制更新、安全审查、使用统计，形成企业 AI 开发治理标准。"
          ],
          "tags": [
            "agentic-framework",
            "skills-file",
            "multi-agent",
            "development-methodology",
            "claude-code",
            "cursor"
          ]
        }
      ]
    },
    {
      "date": "2026-05-21",
      "label": "11天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "colbymchenry",
          "name": "codegraph",
          "fullName": "colbymchenry / codegraph",
          "org": "colbymchenry",
          "url": "https://github.com/colbymchenry/codegraph",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "9,448",
          "forks": "579",
          "starsToday": "2,123",
          "description": "Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode —— 给 AI 编程 Agent 装上知识图谱，减少 94% 工具调用",
          "problems": [
            "<strong>AI Agent 探索代码库太慢太贵：</strong>Claude Code / Codex 探索代码时会产生大量 grep/glob/read 工具调用，每个调用消耗 token 和时间。CodeGraph 预先构建代码知识图谱（符号关系、调用图、代码结构），Agent 直接查图而非逐文件扫描。",
            "<strong>Token 浪费惊人：</strong>在 VS Code 等 6 个真实仓库测试中，CodeGraph 平均减少 92% 工具调用、提速 71%。例如探索 VS Code 源码从 52 次调用/97 秒降至 3 次调用/17 秒。",
            "<strong>跨 Agent 兼容：</strong>一次索引，Claude Code、Cursor、Codex、OpenCode 全部可用——统一代码智能层。"
          ],
          "usage": [
            "一键安装并自动配置 Agent：<pre><code>npx @colbymchenry/codegraph</code></pre>",
            "在项目中初始化索引：<pre><code>cd your-project && codegraph init -i</code></pre>",
            "交互式安装器会自动配置 Claude Code / Cursor / Codex / OpenCode 的 MCP 连接。",
            "之后 Agent 探索代码时自动使用知识图谱，无需额外操作。"
          ],
          "insights": [
            "<strong>企业级代码智能中间件：</strong>为企业私有代码仓库提供托管的知识图谱服务——所有 AI 编程工具的代码理解都通过统一图谱，大幅降低 token 成本（94% 的工具调用减少 = 巨大的成本节省）。",
            "<strong>代码搜索 2.0：</strong>传统的代码搜索（grep、Sourcegraph）只做文本匹配。CodeGraph 的思路可发展为“语义级企业代码搜索引擎”——按“认证模块如何工作”这样的自然语言查代码结构。",
            "<strong>AI IDE 插件生态：</strong>作为所有 AI 编程工具的标配知识层——像 LSP（语言服务器协议）一样成为 AI 编程的基础设施层。"
          ],
          "tags": [
            "knowledge-graph",
            "claude-code",
            "codex",
            "94%-less-tool-calls",
            "local-first",
            "MCP"
          ],
          "count": 2
        },
        {
          "rank": 2,
          "owner": "Imbad0202",
          "name": "academic-research-skills",
          "fullName": "Imbad0202 / academic-research-skills",
          "org": "Imbad0202",
          "url": "https://github.com/Imbad0202/academic-research-skills",
          "lang": "Python",
          "langClass": "py",
          "stars": "16,121",
          "forks": "1,443",
          "starsToday": "1,667",
          "description": "Academic Research Skills for Claude Code: research → write → review → revise → finalize —— 让 AI Agent 成为学术研究助手",
          "problems": [
            "<strong>AI 不懂学术写作规范：</strong>ChatGPT/Claude 生成的学术内容缺乏规范的引用格式、文献综述结构、方法论框架。Academic Research Skills 为 Agent 注入完整的学术研究方法论。",
            "<strong>文献调研效率低：</strong>研究人员花大量时间搜索、筛选、阅读文献。Agent 按照标准化学术流程：搜索 → 筛选 → 精读 → 综述，自动完成文献调研。",
            "<strong>论文写作到发表的断层：</strong>写好论文只是第一步——选刊、格式排版、回复审稿意见等环节同样繁琐。技能覆盖 research → write → review → revise → finalize 全流程。"
          ],
          "usage": [
            "Clone 技能库：<pre><code>git clone https://github.com/Imbad0202/academic-research-skills</code></pre>",
            "复制技能到 Claude Code 技能目录：<pre><code>cp -r academic-research-skills/* .claude/skills/</code></pre>",
            "在 Claude Code 中使用研究技能：<code>/academic-research \"量子计算的最新进展\"</code>",
            "Agent 自动执行：文献搜索 → 摘要生成 → 综述撰写 → 引用格式化 → 多轮修订。"
          ],
          "insights": [
            "<strong>AI 学术写作 SaaS：</strong>面向研究生/学者的 AI 学术助手——输入研究主题，输出完整的文献综述或论文初稿，按论文数量订阅。",
            "<strong>期刊投稿自动化：</strong>不同期刊有不同格式要求、参考文献风格、字数限制。AI Agent 自动适配目标期刊格式，一键排版。",
            "<strong>科研效率评估平台：</strong>通过 Agent 辅助研究节省的时间/提升的质量做量化分析——为高校/研究所提供科研效率提升方案。"
          ],
          "tags": [
            "academic-research",
            "claude-code",
            "literature-review",
            "paper-writing",
            "research-workflow",
            "education"
          ],
          "count": 3
        },
        {
          "rank": 3,
          "owner": "tinyhumansai",
          "name": "openhuman",
          "fullName": "tinyhumansai / openhuman",
          "org": "Tiny Humans AI",
          "url": "https://github.com/tinyhumansai/openhuman",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "23,587",
          "forks": "2,111",
          "starsToday": "3,394",
          "description": "Your Personal AI super intelligence —— 桌面级个人 AI 超级智能体：私有、简单、极其强大",
          "problems": [
            "<strong>AI 碎片化与隐私焦虑：</strong>ChatGPT、Claude、Cursor 等工具各自为政，且数据全部上传云端。OpenHuman 提供统一的本地桌面 Agent，118+ 第三方集成（Gmail、Notion、GitHub、Slack 等）一键 OAuth 接入，所有数据本地处理。",
            "<strong>Agent 缺乏连续记忆：</strong>每次新对话都像初次见面。OpenHuman 内置 Memory Tree + Obsidian Wiki——本地 SQLite 存储知识图谱，自动将数据整理为 Markdown 块写入 Obsidian 仓库，Agent 能记你几周前的对话和偏好。",
            "<strong>Agent 使用门槛高：</strong>多数 Agent 框架需要配置 API Key、写提示词、管理插件。OpenHuman 是桌面应用——安装后点几下就能用，配有桌面宠物形象、语音交互、Google Meet 参会等开箱即用功能。"
          ],
          "usage": [
            "macOS/Linux 一键安装：<pre><code>curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash</code></pre>",
            "Windows 安装：<pre><code>irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex</code></pre>",
            "或从官网下载 DMG/EXE：<a href=\"https://tinyhumans.ai/openhuman\" style=\"color:#58a6ff\">tinyhumans.ai/openhuman</a>",
            "启动后通过 OAuth 一键连接 Gmail、GitHub、Notion 等服务，Agent 自动获取上下文。"
          ],
          "insights": [
            "<strong>个人 AI 操作系统：</strong>OpenHuman 证明“个人 AI 桌面超级助手”是可行的产品品类——本地优先、隐私优先、桌面优先。可做面向普通用户的订阅制个人 AI 管家，管理邮件、日历、文件、聊天，成为真正的数字分身。",
            "<strong>企业 AI 桌面工作台：</strong>企业版可统一管理员工的 AI 工作台——集成公司内部工具（Jira、Confluence、内部 API），确保数据不出企业边界，同时提供标准化 AI 能力。对标 Microsoft Copilot 但本地化部署。",
            "<strong>AI 硬件捆绑：</strong>与 Mac/Windows 设备厂商合作预装，或推出“AI PC”概念——买电脑送个人 AI 助手，形成硬件+AI 的差异化竞争。"
          ],
          "tags": [
            "personal-ai",
            "local-first",
            "118+ integrations",
            "memory-tree",
            "obsidian-wiki",
            "desktop-agent"
          ],
          "count": 5
        },
        {
          "rank": 4,
          "owner": "obra",
          "name": "superpowers",
          "fullName": "obra / superpowers",
          "org": "obra",
          "url": "https://github.com/obra/superpowers",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "199,986",
          "forks": "17,834",
          "starsToday": "1,743",
          "description": "An agentic skills framework & software development methodology that works —— 全栈 AI 智能体技能框架与开发方法论",
          "problems": [
            "<strong>Agent 技能文件没有标准：</strong>每个人写 CLAUDE.md / CURSOR.md 的方式各不相同，质量和格式参差不齐。Superpowers 定义了标准化的技能文件格式和开发方法论。",
            "<strong>AI 编程缺少系统方法论：</strong>使用 Cursor/Claude Code 时团队缺乏统一的方法论——有人习惯问问题、有人直接写代码。Superpowers 提供从需求分析到代码交付的全套方法论和技能文件。",
            "<strong>Agent 协作混乱：</strong>多 Agent 团队（前端 Agent、后端 Agent、测试 Agent）之间缺乏协调框架。Superpowers 内置 Multi-Agent 编排能力。"
          ],
          "usage": [
            "安装 Superpowers CLI：<pre><code>npx @agentic/superpowers</code></pre>",
            "初始化项目技能：<pre><code>superpowers init</code></pre>",
            "浏览可用技能库：<pre><code>superpowers list</code></pre>",
            "安装特定技能到项目：<pre><code>superpowers install react-component</code></pre>"
          ],
          "insights": [
            "<strong>Agent 开发方法论咨询：</strong>198K star 证明了 Superpowers 是当前最流行的 Agent 开发方法论。可以做成企业培训+咨询产品——“如何用 Superpowers 方法论构建 AI 原生开发团队”。",
            "<strong>技能文件模板市场：</strong>像 GitHub Marketplace 一样交易 Agent 技能文件——前端技能包、后端技能包、DevOps 技能包，每个 $5-50。",
            "<strong>团队 Agent 治理平台：</strong>企业版统一管理所有开发者的技能文件——强制更新、安全审查、使用统计，形成企业 AI 开发治理标准。"
          ],
          "tags": [
            "agentic-framework",
            "skills-file",
            "multi-agent",
            "development-methodology",
            "claude-code",
            "cursor"
          ],
          "count": 3
        },
        {
          "rank": 5,
          "owner": "rohitg00",
          "name": "ai-engineering-from-scratch",
          "fullName": "rohitg00 / ai-engineering-from-scratch",
          "org": "rohitg00",
          "url": "https://github.com/rohitg00/ai-engineering-from-scratch",
          "lang": "Python",
          "langClass": "py",
          "stars": "9,520",
          "forks": "1,940",
          "starsToday": "765",
          "description": "Learn it. Build it. Ship it for others. —— 从零开始的 AI 工程实战教程：学 → 造 → 交付",
          "problems": [
            "<strong>AI 工程学习路径不清晰：</strong>从理论到实战的路太远——数学、框架、部署、运维，每步都有坑。这门课从零到交付提供完整路径。",
            "<strong>缺数多实战项目：</strong>很多教程教概念但缺少端到端实战项目。该课程强调“造出来、交付出去”——每个模块都产出可部署的产品。",
            "<strong>社区驱动不足：</strong>传统课程学完就结束。该项目采用开源社区模式，学员可以贡献自己的项目，形成持续学习网络。"
          ],
          "usage": [
            "Clone 课程仓库：<pre><code>git clone https://github.com/rohitg00/ai-engineering-from-scratch</code></pre>",
            "从第一章开始，每章有 Jupyter Notebook + 实战项目。",
            "跟着课程从零构建 AI 应用并部署到生产环境。",
            "参与社区讨论，分享自己的项目。"
          ],
          "insights": [
            "<strong>AI 工程培训认证：</strong>以该课程为基础提供“AI 工程师”认证培训——面向转行/应届生，从零到就业的全套培训方案。",
            "<strong>项目作品集平台：</strong>学员完成课程后产出的项目自动形成作品集——对接企业招聘需求，打造“学→做→找工作”闭环。",
            "<strong>企业内训定制：</strong>为企业提供定制版课程——根据团队技术栈调整内容，加上企业自己的数据集和场景。"
          ],
          "tags": [
            "ai-engineering",
            "from-scratch",
            "hands-on",
            "python",
            "production-deployment",
            "open-source-course"
          ],
          "count": 1
        }
      ]
    },
    {
      "date": "2026-05-20",
      "label": "12天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "tinyhumansai",
          "name": "openhuman",
          "fullName": "tinyhumansai / openhuman",
          "org": "Tiny Humans AI",
          "url": "https://github.com/tinyhumansai/openhuman",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "21,181",
          "forks": "1,864",
          "starsToday": "3,973",
          "description": "Your Personal AI super intelligence —— 桌面级个人 AI 超级智能体：私有、简单、极其强大",
          "problems": [
            "<strong>AI 碎片化与隐私焦虑：</strong>ChatGPT、Claude、Cursor 等工具各自为政，且数据全部上传云端。OpenHuman 提供统一的本地桌面 Agent，118+ 第三方集成（Gmail、Notion、GitHub、Slack 等）一键 OAuth 接入，所有数据本地处理。",
            "<strong>Agent 缺乏连续记忆：</strong>每次新对话都像初次见面。OpenHuman 内置 Memory Tree + Obsidian Wiki——本地 SQLite 存储知识图谱，自动将数据整理为 Markdown 块写入 Obsidian 仓库，Agent 能记住你几周前的对话和偏好。",
            "<strong>Agent 使用门槛高：</strong>多数 Agent 框架需要配置 API Key、写提示词、管理插件。OpenHuman 是桌面应用——安装后点几下就能用，配有桌面宠物形象、语音交互、Google Meet 参会等开箱即用功能。"
          ],
          "usage": [
            "macOS/Linux 一键安装：<pre><code>curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash</code></pre>",
            "Windows 安装：<pre><code>irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex</code></pre>",
            "或从官网下载 DMG/EXE：<a href=\"https://tinyhumans.ai/openhuman\" style=\"color:#58a6ff\">tinyhumans.ai/openhuman</a>",
            "启动后通过 OAuth 一键连接 Gmail、GitHub、Notion 等服务，Agent 自动获取上下文。"
          ],
          "insights": [
            "<strong>个人 AI 操作系统：</strong>OpenHuman 证明\"个人 AI 桌面超级助手\"是可行的产品品类——本地优先、隐私优先、桌面优先。可做面向普通用户的订阅制个人 AI 管家，管理邮件、日历、文件、聊天，成为真正的数字分身。",
            "<strong>企业 AI 桌面工作台：</strong>企业版可统一管理员工的 AI 工作台——集成公司内部工具（Jira、Confluence、内部 API），确保数据不出企业边界，同时提供标准化 AI 能力。对标 Microsoft Copilot 但本地化部署。",
            "<strong>AI 硬件捆绑：</strong>与 Mac/Windows 设备厂商合作预装，或推出\"AI PC\"概念——买电脑送个人 AI 助手，形成硬件+AI 的差异化竞争。"
          ],
          "tags": [
            "personal-ai",
            "local-first",
            "118+ integrations",
            "memory-tree",
            "obsidian-wiki",
            "desktop-agent"
          ],
          "count": 4
        },
        {
          "rank": 2,
          "owner": "HKUDS",
          "name": "CLI-Anything",
          "fullName": "HKUDS / CLI-Anything",
          "org": "HKU DS",
          "url": "https://github.com/HKUDS/CLI-Anything",
          "lang": "Python",
          "langClass": "py",
          "stars": "37,692",
          "forks": "3,608",
          "starsToday": "1,038",
          "description": "\"Making ALL Software Agent-Native\" —— CLI-Hub：让每一款软件都有 AI Agent 原生命令行接口",
          "problems": [
            "<strong>软件不具备 Agent 接口：</strong>AI Agent 要操作现有软件（浏览器、IDE、设计工具等）只能靠 GUI 截图+模拟点击，不稳定又慢。CLI-Anything 为任意软件自动生成 CLI 接口，Agent 通过命令行直接操控。",
            "<strong>Agent 工具生态碎片化：</strong>每个 Agent 框架有自己的工具定义格式，互不兼容。CLI-Anything 定义统一 CLI-Hub 标准，一次封装到处可用。",
            "<strong>传统 RPA 太脆弱：</strong>基于 UI 元素的自动化（Selenium、Playwright）一换版就崩。CLI 接口稳定、轻量、可组合，是 Agent 操控软件的正确姿势。"
          ],
          "usage": [
            "安装 CLI 助手：<pre><code>pip install cli-anything</code></pre>",
            "为目标软件生成 CLI：<pre><code>cli-anything wrap &lt;software-path&gt;</code></pre>",
            "访问 CLI-Hub 发现已有封装：<a href=\"https://clianything.cc/\" style=\"color:#58a6ff\">clianything.cc</a>",
            "Agent 通过标准 CLI 接口调用，无需额外适配。"
          ],
          "insights": [
            "<strong>Agent 软件适配中间件：</strong>CLI-Anything 解决了 AI Agent 落地的核心难题——如何让 Agent 操作现有软件。可以做成\"Agent 软件适配器\"平台，企业上传软件，平台自动生成 CLI 接口。",
            "<strong>CLI-Hub 应用市场：</strong>类似 npm 但面向 Agent 工具——开发者上传 CLI 封装，Agent 开发者下载使用，形成 Agent 工具生态经济。",
            "<strong>企业软件 Agent 化改造：</strong>为企业遗留系统提供 Agent 化改造服务——旧系统没有 API？CLI-Anything 一键生成 CLI 接口，让 AI Agent 能操作任何老系统。"
          ],
          "tags": [
            "agent-native",
            "cli-hub",
            "software-automation",
            "MCP",
            "tool-generation",
            "python"
          ],
          "count": 2
        },
        {
          "rank": 3,
          "owner": "Imbad0202",
          "name": "academic-research-skills",
          "fullName": "Imbad0202 / academic-research-skills",
          "org": "Imbad0202",
          "url": "https://github.com/Imbad0202/academic-research-skills",
          "lang": "Python",
          "langClass": "py",
          "stars": "14,107",
          "forks": "1,333",
          "starsToday": "3,164",
          "description": "Academic Research Skills for Claude Code: research → write → review → revise → finalize —— 让 AI Agent 成为学术研究助手",
          "problems": [
            "<strong>AI 不懂学术写作规范：</strong>ChatGPT/Claude 生成的学术内容缺乏规范的引用格式、文献综述结构、方法论框架。Academic Research Skills 为 Agent 注入完整的学术研究方法论。",
            "<strong>文献调研效率低：</strong>研究人员花大量时间搜索、筛选、阅读文献。Agent 按照标准化学术流程：搜索 → 筛选 → 精读 → 综述，自动完成文献调研。",
            "<strong>论文写作到发表的断层：</strong>写好论文只是第一步——选刊、格式排版、回复审稿意见等环节同样繁琐。技能覆盖 research → write → review → revise → finalize 全流程。"
          ],
          "usage": [
            "Clone 技能库：<pre><code>git clone https://github.com/Imbad0202/academic-research-skills</code></pre>",
            "复制技能到 Claude Code 技能目录：<pre><code>cp -r academic-research-skills/* .claude/skills/</code></pre>",
            "在 Claude Code 中使用研究技能：<code>/academic-research \"量子计算的最新进展\"</code>",
            "Agent 自动执行：文献搜索 → 摘要生成 → 综述撰写 → 引用格式化 → 多轮修订。"
          ],
          "insights": [
            "<strong>AI 学术写作 SaaS：</strong>面向研究生/学者的 AI 学术助手——输入研究主题，输出完整的文献综述或论文初稿，按论文数量订阅。",
            "<strong>期刊投稿自动化：</strong>不同期刊有不同格式要求、参考文献风格、字数限制。AI Agent 自动适配目标期刊格式，一键排版。",
            "<strong>科研效率评估平台：</strong>通过 Agent 辅助研究节省的时间/提升的质量做量化分析——为高校/研究所提供科研效率提升方案。"
          ],
          "tags": [
            "academic-research",
            "claude-code",
            "literature-review",
            "paper-writing",
            "research-workflow",
            "education"
          ],
          "count": 2
        },
        {
          "rank": 4,
          "owner": "obra",
          "name": "superpowers",
          "fullName": "obra / superpowers",
          "org": "obra",
          "url": "https://github.com/obra/superpowers",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "198,356",
          "forks": "17,698",
          "starsToday": "1,623",
          "description": "An agentic skills framework & software development methodology that works —— 全栈 AI 智能体技能框架与开发方法论",
          "problems": [
            "<strong>Agent 技能文件没有标准：</strong>每个人写 CLAUDE.md / CURSOR.md 的方式各不相同，质量和格式参差不齐。Superpowers 定义了标准化的技能文件格式和开发方法论。",
            "<strong>AI 编程缺少系统方法论：</strong>使用 Cursor/Claude Code 时团队缺乏统一的方法论——有人习惯问问题、有人直接写代码。Superpowers 提供从需求分析到代码交付的全套方法论和技能文件。",
            "<strong>Agent 协作混乱：</strong>多 Agent 团队（前端 Agent、后端 Agent、测试 Agent）之间缺乏协调框架。Superpowers 内置 Multi-Agent 编排能力。"
          ],
          "usage": [
            "安装 Superpowers CLI：<pre><code>npx @agentic/superpowers</code></pre>",
            "初始化项目技能：<pre><code>superpowers init</code></pre>",
            "浏览可用技能库：<pre><code>superpowers list</code></pre>",
            "安装特定技能到项目：<pre><code>superpowers install react-component</code></pre>"
          ],
          "insights": [
            "<strong>Agent 开发方法论咨询：</strong>198K star 证明了 Superpowers 是当前最流行的 Agent 开发方法论。可以做成企业培训+咨询产品——\"如何用 Superpowers 方法论构建 AI 原生开发团队\"。",
            "<strong>技能文件模板市场：</strong>像 GitHub Marketplace 一样交易 Agent 技能文件——前端技能包、后端技能包、DevOps 技能包，每个 $5-50。",
            "<strong>团队 Agent 治理平台：</strong>企业版统一管理所有开发者的技能文件——强制更新、安全审查、使用统计，形成企业 AI 开发治理标准。"
          ],
          "tags": [
            "agentic-framework",
            "skills-file",
            "multi-agent",
            "development-methodology",
            "claude-code",
            "cursor"
          ],
          "count": 2
        },
        {
          "rank": 5,
          "owner": "rohitg00",
          "name": "agentmemory",
          "fullName": "rohitg00 / agentmemory",
          "org": "rohitg00",
          "url": "https://github.com/rohitg00/agentmemory",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "14,133",
          "forks": "1,179",
          "starsToday": "1,609",
          "description": "#1 Persistent memory for AI coding agents based on real-world benchmarks —— AI 编程 Agent 专属持久化记忆引擎",
          "problems": [
            "<strong>AI Agent 每次对话都失忆：</strong>Coding Agent 每次新对话都像初次见面——不记得项目配置、代码约定、你偏好的测试框架。AgentMemory 让 Agent 记住跨会话的项目上下文。",
            "<strong>记忆存储碎片化：</strong>有的 Agent 用文件、有的用向量数据库、有的用 SQLite，互不兼容。AgentMemory 提供统一记忆层——基于真实场景基准测试的 #1 记忆方案。",
            "<strong>记忆太贵太重：</strong>向量数据库需要 GPU、Embedding 服务、额外基础设施。AgentMemory 轻量级设计，直接作为 MCP 插件运行，零额外基础设施。"
          ],
          "usage": [
            "安装 AgentMemory CLI：<pre><code>npm install -g agentmemory</code></pre>",
            "在项目中初始化：<pre><code>agentmemory init</code></pre>",
            "作为 MCP 插件添加到 Claude Code / Cursor：<code>mcp add agentmemory</code>",
            "Agent 自动将项目知识保存到记忆库，跨会话自动召回。"
          ],
          "insights": [
            "<strong>Agent 记忆即服务：</strong>14K star 证明记忆是 Agent 的刚需。托管的记忆云服务——让任何 AI Agent 拥有跨会话记忆能力，按记忆量/Agent 数订阅收费。",
            "<strong>企业知识大脑：</strong>多 Agent 共享记忆空间——前端 Agent 和后端 Agent 共享项目上下文，形成统一的企业知识图谱。",
            "<strong>IDE 记忆插件：</strong>每个 IDE 都安装 AgentMemory 插件——VS Code、JetBrains、Cursor 之间的 Agent 共享同一套项目记忆。"
          ],
          "tags": [
            "persistent-memory",
            "knowledge-graph",
            "MCP-native",
            "token-efficient",
            "coding-agent",
            "cross-session"
          ],
          "count": 3
        }
      ]
    },
    {
      "date": "2026-05-19",
      "label": "13天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "tinyhumansai",
          "name": "openhuman",
          "fullName": "tinyhumansai / openhuman",
          "org": "Tiny Humans AI",
          "url": "https://github.com/tinyhumansai/openhuman",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "17,200",
          "forks": "1,495",
          "starsToday": "3,941",
          "description": "Your Personal AI super intelligence —— 桌面级个人 AI 超级智能体：私有、简单、极其强大",
          "problems": [
            "<strong>AI 碎片化与隐私焦虑：</strong>ChatGPT、Claude、Cursor 等工具各自为政，且数据全部上传云端。OpenHuman 提供统一的本地桌面 Agent，118+ 第三方集成（Gmail、Notion、GitHub、Slack 等）一键 OAuth 接入，所有数据本地处理。",
            "<strong>Agent 缺乏连续记忆：</strong>每次新对话都像初次见面。OpenHuman 内置 Memory Tree + Obsidian Wiki——本地 SQLite 存储知识图谱，自动将数据整理为 Markdown 块写入 Obsidian 仓库，Agent 能记住你几周前的对话和偏好。",
            "<strong>Agent 使用门槛高：</strong>多数 Agent 框架需要配置 API Key、写提示词、管理插件。OpenHuman 是桌面应用——安装后点几下就能用，配有桌面宠物形象、语音交互、Google Meet 参会等开箱即用功能。"
          ],
          "usage": [
            "macOS/Linux 一键安装：<pre><code>curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash</code></pre>",
            "Windows 安装：<pre><code>irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex</code></pre>",
            "或从官网下载 DMG/EXE：<a href=\"https://tinyhumans.ai/openhuman\" style=\"color:#58a6ff\">tinyhumans.ai/openhuman</a>",
            "启动后通过 OAuth 一键连接 Gmail、GitHub、Notion 等服务，Agent 自动获取上下文。"
          ],
          "insights": [
            "<strong>个人 AI 操作系统：</strong>OpenHuman 证明&quot;个人 AI 桌面超级助手&quot;是可行的产品品类——本地优先、隐私优先、桌面优先。可做面向普通用户的订阅制个人 AI 管家，管理邮件、日历、文件、聊天，成为真正的数字分身。",
            "<strong>企业 AI 桌面工作台：</strong>企业版可统一管理员工的 AI 工作台——集成公司内部工具（Jira、Confluence、内部 API），确保数据不出企业边界，同时提供标准化 AI 能力。对标 Microsoft Copilot 但本地化部署。",
            "<strong>AI 硬件捆绑：</strong>与 Mac/Windows 设备厂商合作预装，或推出&quot;AI PC&quot;概念——买电脑送个人 AI 助手，形成硬件+AI 的差异化竞争。"
          ],
          "tags": [
            "personal-ai",
            "local-first",
            "118+ integrations",
            "memory-tree",
            "obsidian-wiki",
            "desktop-agent"
          ],
          "count": 3
        },
        {
          "rank": 2,
          "owner": "HKUDS",
          "name": "CLI-Anything",
          "fullName": "HKUDS / CLI-Anything",
          "org": "HKU DS",
          "url": "https://github.com/HKUDS/CLI-Anything",
          "lang": "Python",
          "langClass": "py",
          "stars": "36,630",
          "forks": "3,556",
          "starsToday": "1,049",
          "description": "&quot;Making ALL Software Agent-Native&quot; —— CLI-Hub：让每一款软件都有 AI Agent 原生命令行接口",
          "problems": [
            "<strong>软件不具备 Agent 接口：</strong>AI Agent 要操作现有软件（浏览器、IDE、设计工具等）只能靠 GUI 截图+模拟点击，不稳定又慢。CLI-Anything 为任意软件自动生成 CLI 接口，Agent 通过命令行直接操控。",
            "<strong>Agent 工具生态碎片化：</strong>每个 Agent 框架有自己的工具定义格式，互不兼容。CLI-Anything 定义统一 CLI-Hub 标准，一次封装到处可用。",
            "<strong>传统 RPA 太脆弱：</strong>基于 UI 元素的自动化（Selenium、Playwright）一换版就崩。CLI 接口稳定、轻量、可组合，是 Agent 操控软件的正确姿势。"
          ],
          "usage": [
            "安装 CLI 助手：<pre><code>pip install cli-anything</code></pre>",
            "为目标软件生成 CLI：<pre><code>cli-anything wrap &lt;software-path&gt;</code></pre>",
            "访问 CLI-Hub 发现已有封装：<a href=\"https://clianything.cc/\" style=\"color:#58a6ff\">clianything.cc</a>",
            "Agent 通过标准 CLI 接口调用，无需额外适配。"
          ],
          "insights": [
            "<strong>Agent 软件适配中间件：</strong>CLI-Anything 解决了 AI Agent 落地的核心难题——如何让 Agent 操作现有软件。可以做成&quot;Agent 软件适配器&quot;平台，企业上传软件，平台自动生成 CLI 接口。",
            "<strong>CLI-Hub 应用市场：</strong>类似 npm 但面向 Agent 工具——开发者上传 CLI 封装，Agent 开发者下载使用，形成 Agent 工具生态经济。",
            "<strong>企业软件 Agent 化改造：</strong>为企业遗留系统提供 Agent 化改造服务——旧系统没有 API？CLI-Anything 一键生成 CLI 接口，让 AI Agent 能操作任何老系统。"
          ],
          "tags": [
            "agent-native",
            "cli-hub",
            "software-automation",
            "MCP",
            "tool-generation",
            "python"
          ],
          "count": 1
        },
        {
          "rank": 3,
          "owner": "tech-leads-club",
          "name": "agent-skills",
          "fullName": "tech-leads-club / agent-skills",
          "org": "Tech Leads Club",
          "url": "https://github.com/tech-leads-club/agent-skills",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "4,036",
          "forks": "349",
          "starsToday": "1,244",
          "description": "The secure, validated skill registry for professional AI coding agents —— 企业级 AI Agent 技能注册中心",
          "problems": [
            "<strong>Agent 技能来源不可信：</strong>从 GitHub 随便找的技能文件可能包含恶意指令或质量参差不齐。Agent Skills Registry 提供经过安全验证的技能库——每个技能经过代码审查和安全扫描。",
            "<strong>企业无法统一管理 Agent 技能：</strong>团队各自安装技能，版本混乱、安全不受控。企业版提供统一的技能审批、分发、审计流程。",
            "<strong>技能兼容性差：</strong>不同 Agent 平台（Claude Code、Cursor、Copilot）技能格式不同。Agent Skills 兼容 Antigravity、Claude Code、Cursor、Copilot 等主流平台。"
          ],
          "usage": [
            "安装 Agent Skills CLI：<pre><code>npx @tech-leads-club/agent-skills</code></pre>",
            "搜索技能：<pre><code>agent-skills search docker</code></pre>",
            "安装已验证技能到项目：<pre><code>agent-skills install typescript-best-practices</code></pre>",
            "发布自己的技能（需审核）：<pre><code>agent-skills publish ./my-skill.md</code></pre>"
          ],
          "insights": [
            "<strong>Agent 技能应用商店：</strong>企业级技能市场——安全审查 + 版本管理 + 用量统计。类似 GitHub Marketplace 但专门面向 AI Agent 技能。",
            "<strong>企业 Agent 治理平台：</strong>大型企业需要统一管控所有开发者使用的 Agent 技能——技能白名单、强制更新、安全审计，形成企业 AI 开发治理基础设施。",
            "<strong>技能认证体系：</strong>技能作者可以认证自己的技能包——认证技能获得 &quot;Verified&quot; 徽章，类似 App Store 的审核机制，打造技能质量信任体系。"
          ],
          "tags": [
            "skill-registry",
            "enterprise",
            "security-validated",
            "multi-platform",
            "governance",
            "agent-skills"
          ],
          "count": 1
        },
        {
          "rank": 4,
          "owner": "Imbad0202",
          "name": "academic-research-skills",
          "fullName": "Imbad0202 / academic-research-skills",
          "org": "Imbad0202",
          "url": "https://github.com/Imbad0202/academic-research-skills",
          "lang": "Python",
          "langClass": "py",
          "stars": "11,739",
          "forks": "1,194",
          "starsToday": "1,439",
          "description": "Academic Research Skills for Claude Code: research → write → review → revise → finalize —— 让 AI Agent 成为学术研究助手",
          "problems": [
            "<strong>AI 不懂学术写作规范：</strong>ChatGPT/Claude 生成的学术内容缺乏规范的引用格式、文献综述结构、方法论框架。Academic Research Skills 为 Agent 注入完整的学术研究方法论。",
            "<strong>文献调研效率低：</strong>研究人员花大量时间搜索、筛选、阅读文献。Agent 按照标准化学术流程：搜索 → 筛选 → 精读 → 综述，自动完成文献调研。",
            "<strong>论文写作到发表的断层：</strong>写好论文只是第一步——选刊、格式排版、回复审稿意见等环节同样繁琐。技能覆盖 research → write → review → revise → finalize 全流程。"
          ],
          "usage": [
            "Clone 技能库：<pre><code>git clone https://github.com/Imbad0202/academic-research-skills</code></pre>",
            "复制技能到 Claude Code 技能目录：<pre><code>cp -r academic-research-skills/* .claude/skills/</code></pre>",
            "在 Claude Code 中使用研究技能：<code>/academic-research &quot;量子计算的最新进展&quot;</code>",
            "Agent 自动执行：文献搜索 → 摘要生成 → 综述撰写 → 引用格式化 → 多轮修订。"
          ],
          "insights": [
            "<strong>AI 学术写作 SaaS：</strong>面向研究生/学者的 AI 学术助手——输入研究主题，输出完整的文献综述或论文初稿，按论文数量订阅。",
            "<strong>期刊投稿自动化：</strong>不同期刊有不同格式要求、参考文献风格、字数限制。AI Agent 自动适配目标期刊格式，一键排版。",
            "<strong>科研效率评估平台：</strong>通过 Agent 辅助研究节省的时间/提升的质量做量化分析——为高校/研究所提供科研效率提升方案。"
          ],
          "tags": [
            "academic-research",
            "claude-code",
            "literature-review",
            "paper-writing",
            "research-workflow",
            "education"
          ],
          "count": 1
        },
        {
          "rank": 5,
          "owner": "humanlayer",
          "name": "12-factor-agents",
          "fullName": "humanlayer / 12-factor-agents",
          "org": "HumanLayer",
          "url": "https://github.com/humanlayer/12-factor-agents",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "20,565",
          "forks": "1,558",
          "starsToday": "399",
          "description": "What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? —— LLM 软件的 12 条生产级原则",
          "problems": [
            "<strong>LLM 应用生产化缺乏最佳实践：</strong>构建 LLM 应用的团队各自为政——有人用 LangChain、有人用 Vercel AI SDK、有人自己写框架。12-Factor Agents 像 12-Factor App 一样定义了 LLM 应用的标准原则。",
            "<strong>LLM 应用运维困难：</strong>Prompt 变更如何管理？Token 成本如何追踪？模型升级如何灰度？输出质量如何监控？12 条原则逐一解答这些运维问题。",
            "<strong>团队协作无标准：</strong>前端工程师、后端工程师、AI 工程师在 LLM 项目中的协作没有统一语言。12-Factor 提供了跨职能的通用框架。"
          ],
          "usage": [
            "在线阅读 12 条原则：<pre><code>https://github.com/humanlayer/12-factor-agents</code></pre>",
            "将原则应用到自己的 LLM 项目架构设计中。",
            "配合 HumanLayer 工具实现生产级 Human-in-the-Loop 流程。",
            "遵循原则构建可观测、可回滚、可审计的 LLM 应用。"
          ],
          "insights": [
            "<strong>LLM 工程咨询/培训：</strong>基于 12-Factor Agents 提供企业培训——&quot;如何构建生产级 LLM 应用&quot;，面向技术团队的标准化培训产品。",
            "<strong>LLM 应用脚手架工具：</strong>将 12 条原则自动化——一键生成符合所有原则的 LLM 项目模板，内置日志、监控、灰度、回滚等基础设施。",
            "<strong>LLM 合规/审计服务：</strong>12 条原则天然形成审计清单——企业的 LLM 应用是否符合生产标准？提供合规审计 SaaS 服务。"
          ],
          "tags": [
            "production-llm",
            "best-practices",
            "12-factor",
            "llm-ops",
            "architecture",
            "human-in-the-loop"
          ],
          "count": 1
        }
      ]
    },
    {
      "date": "2026-05-18",
      "label": "14天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "tinyhumansai",
          "name": "openhuman",
          "fullName": "tinyhumansai / openhuman",
          "org": "Tiny Humans AI",
          "url": "https://github.com/tinyhumansai/openhuman",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "14,378",
          "forks": "1,231",
          "starsToday": "1,690",
          "description": "Your Personal AI super intelligence —— 桌面级个人 AI 超级智能体：私有、简单、极其强大",
          "problems": [
            "<strong>AI 碎片化与隐私焦虑：</strong>ChatGPT、Claude、Cursor 等工具各自为政，且数据全部上传云端。OpenHuman 提供统一的本地桌面 Agent，118+ 第三方集成（Gmail、Notion、GitHub、Slack 等）一键 OAuth 接入，所有数据本地处理。",
            "<strong>Agent 缺乏连续记忆：</strong>每次新对话都像初次见面。OpenHuman 内置 Memory Tree + Obsidian Wiki——本地 SQLite 存储知识图谱，自动将数据整理为 Markdown 块写入 Obsidian 仓库，Agent 能记住你几周前的对话和偏好。",
            "<strong>Agent 使用门槛高：</strong>多数 Agent 框架需要配置 API Key、写提示词、管理插件。OpenHuman 是桌面应用——安装后点几下就能用，配有桌面宠物形象、语音交互、Google Meet 参会等开箱即用功能。"
          ],
          "usage": [
            "macOS/Linux 一键安装：<pre><code>curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash</code></pre>",
            "Windows 安装：<pre><code>irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex</code></pre>",
            "或从官网下载 DMG/EXE：<a href=\"https://tinyhumans.ai/openhuman\" style=\"color:#58a6ff\">tinyhumans.ai/openhuman</a>",
            "启动后通过 OAuth 一键连接 Gmail、GitHub、Notion 等服务，Agent 自动获取上下文。"
          ],
          "insights": [
            "<strong>个人 AI 操作系统：</strong>OpenHuman 证明&quot;个人 AI 桌面超级助手&quot;是可行的产品品类——本地优先、隐私优先、桌面优先。可做面向普通用户的订阅制个人 AI 管家，管理邮件、日历、文件、聊天，成为真正的数字分身。",
            "<strong>企业 AI 桌面工作台：</strong>企业版可统一管理员工的 AI 工作台——集成公司内部工具（Jira、Confluence、内部 API），确保数据不出企业边界，同时提供标准化 AI 能力。对标 Microsoft Copilot 但本地化部署。",
            "<strong>AI 硬件捆绑：</strong>与 Mac/Windows 设备厂商合作预装，或推出&quot;AI PC&quot;概念——买电脑送个人 AI 助手，形成硬件+AI 的差异化竞争。"
          ],
          "tags": [
            "personal-ai",
            "local-first",
            "118+ integrations",
            "memory-tree",
            "obsidian-wiki",
            "desktop-agent"
          ],
          "count": 2
        },
        {
          "rank": 2,
          "owner": "colbymchenry",
          "name": "codegraph",
          "fullName": "colbymchenry / codegraph",
          "org": "colbymchenry",
          "url": "https://github.com/colbymchenry/codegraph",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "3,651",
          "forks": "276",
          "starsToday": "857",
          "description": "Pre-indexed code knowledge graph for AI coding agents —— 给 AI 编程 Agent 装上代码知识图谱，减少 94% 工具调用",
          "problems": [
            "<strong>AI Agent 探索代码库太慢太贵：</strong>Claude Code / Codex 探索代码时会产生大量 grep/glob/read 工具调用，每个调用消耗 token 和时间。CodeGraph 预先构建代码知识图谱（符号关系、调用图、代码结构），Agent 直接查图而非逐文件扫描。",
            "<strong>Token 浪费惊人：</strong>在 VS Code 等 6 个真实仓库测试中，CodeGraph 平均减少 92% 工具调用、提速 71%。例如探索 VS Code 源码从 52 次调用/97 秒降至 3 次调用/17 秒。",
            "<strong>跨 Agent 兼容：</strong>一次索引，Claude Code、Cursor、Codex、OpenCode 全部可用——统一代码智能层。"
          ],
          "usage": [
            "一键安装并自动配置 Agent：<pre><code>npx @colbymchenry/codegraph</code></pre>",
            "在项目中初始化索引：<pre><code>cd your-project && codegraph init -i</code></pre>",
            "交互式安装器会自动配置 Claude Code / Cursor / Codex / OpenCode 的 MCP 连接。",
            "之后 Agent 探索代码时自动使用知识图谱，无需额外操作。"
          ],
          "insights": [
            "<strong>企业级代码智能中间件：</strong>为企业私有代码仓库提供托管的知识图谱服务——所有 AI 编程工具的代码理解都通过统一图谱，大幅降低 token 成本（94% 的工具调用减少 = 巨大的成本节省）。",
            "<strong>代码搜索 2.0：</strong>传统的代码搜索（grep、Sourcegraph）只做文本匹配。CodeGraph 的思路可发展为&quot;语义级企业代码搜索引擎&quot;——按&quot;认证模块如何工作&quot;这样的自然语言查代码结构。",
            "<strong>AI IDE 插件生态：</strong>作为所有 AI 编程工具的标配知识层——像 LSP（语言服务器协议）一样成为 AI 编程的基础设施层。"
          ],
          "tags": [
            "knowledge-graph",
            "claude-code",
            "codex",
            "94%-less-tool-calls",
            "local-first",
            "MCP"
          ],
          "count": 1
        },
        {
          "rank": 3,
          "owner": "K-Dense-AI",
          "name": "scientific-agent-skills",
          "fullName": "K-Dense-AI / scientific-agent-skills",
          "org": "K-Dense Inc.",
          "url": "https://github.com/K-Dense-AI/scientific-agent-skills",
          "lang": "Python",
          "langClass": "py",
          "stars": "23,989",
          "forks": "2,549",
          "starsToday": "762",
          "description": "135 个科学研究级 Agent 技能 —— 让 AI Agent 变身专业科学家，覆盖基因组学、药物发现、材料科学等",
          "problems": [
            "<strong>AI Agent 不懂科学：</strong>通用的 AI Agent 无法处理专业科学工作流——基因组序列分析、分子对接、质谱数据处理、RNA 速度分析等需要特定工具链和领域知识。",
            "<strong>科研工具链碎片化：</strong>生物信息学用 Biopython、化学信息学用 RDKit、蛋白质组学用 PyTED…每个领域有独立工具栈，研究人员需要同时掌握多套系统。",
            "<strong>Agent 技能标准化缺失：</strong>Scientific Agent Skills 定义了 Agent Skills 开放标准——135 个技能文件覆盖生物、化学、医学等 78+ 科学数据库，一次编写跨 Agent 复用。"
          ],
          "usage": [
            "Clone 技能库：<pre><code>git clone https://github.com/K-Dense-AI/scientific-agent-skills</code></pre>",
            "将技能文件复制到 Claude Code / Cursor / Codex 的技能目录中。",
            "或在 K-Dense BYOK 桌面应用中使用：<pre><code>https://github.com/K-Dense-AI/k-dense-byok</code></pre>（免费开源、本地运行、支持 40+ 模型）。",
            "Agent 会自动加载相关科学技能，按照技能文件中定义的流程执行实验。"
          ],
          "insights": [
            "<strong>AI 科学家即服务 (AI Scientist-as-a-Service)：</strong>基于 135 个科学技能构建托管 AI 科研平台——药物公司上传靶点信息，AI Agent 自动运行虚拟筛选、ADMET 预测、分子优化全流程，按实验量订阅收费。",
            "<strong>垂直领域 AI 技能市场：</strong>科学技能天然适合做成交易市场——生物学家上传自己的分析流程技能，药企购买使用。类似代码市场但面向科研方法论。",
            "<strong>科研加速器：</strong>为大学/研究所提供 AI 科研加速方案——研究生无需从零学工具链，AI Agent 直接执行实验设计、数据分析、论文图表生成。"
          ],
          "tags": [
            "scientific-agent",
            "135-skills",
            "drug-discovery",
            "genomics",
            "bioinformatics",
            "agent-skills-standard"
          ],
          "count": 1
        },
        {
          "rank": 4,
          "owner": "Anil-matcha",
          "name": "Open-Generative-AI",
          "fullName": "Anil-matcha / Open-Generative-AI",
          "org": "Anil-matcha",
          "url": "https://github.com/Anil-matcha/Open-Generative-AI",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "15,382",
          "forks": "2,611",
          "starsToday": "703",
          "description": "开源 AI 视频/图像生成平台 —— 替代 Midjourney/Kling/Sora 的开源方案，200+ 模型，无内容过滤",
          "problems": [
            "<strong>AI 生成平台昂贵且受限：</strong>Midjourney $30/月、Kling 按次收费、Sora 仅限 ChatGPT 订阅用户。Open-Generative-AI 完全免费、MIT 开源、可自托管。",
            "<strong>内容审查困扰创作者：</strong>商业平台内容过滤器经常误杀正常创作。Open-Generative-AI 宣称&quot;无内容过滤&quot;——适合艺术创作、学术研究、成人教育等被商业平台限制的场景。",
            "<strong>模型切换繁琐：</strong>Flux 做图像、Kling 做视频、Stable Diffusion 做风格化——需要多个平台。Open-Generative-AI 集成 200+ 模型在一个界面，统一管理。"
          ],
          "usage": [
            "自托管部署：<pre><code>git clone https://github.com/Anil-matcha/Open-Generative-AI && npm install && npm start</code></pre>",
            "配置你使用的 AI 模型 API Key（Flux、Stable Diffusion、Kling 等）。",
            "通过 Web 界面选择模型、输入提示词、生成图像或视频。",
            "支持图片转视频、文本转视频等多种模式。"
          ],
          "insights": [
            "<strong>垂直行业 AI 创作 SaaS：</strong>基于 Open-Generative-AI 定制行业版——电商用 AI 生成商品图/视频、房产用 AI 生成室内设计效果图、教育用 AI 生成教学动画。每个垂直领域一个付费版本。",
            "<strong>无审查创作平台：</strong>面向艺术创作者、学术研究者、成人教育等被商业平台审查限制的群体，提供合规但不受商业公司内容政策约束的 AI 创作服务。",
            "<strong>AI 模型聚合 API：</strong>200+ 模型统一 API 本身就是产品——开发者接入一个 API 即可调用所有主流图像/视频生成模型，按流量收费。"
          ],
          "tags": [
            "open-source",
            "200+ models",
            "uncensored",
            "ai-video",
            "ai-image",
            "self-hosted"
          ],
          "count": 1
        },
        {
          "rank": 5,
          "owner": "microsoft",
          "name": "ai-agents-for-beginners",
          "fullName": "microsoft / ai-agents-for-beginners",
          "org": "Microsoft",
          "url": "https://github.com/microsoft/ai-agents-for-beginners",
          "lang": "Jupyter Notebook",
          "langClass": "py",
          "stars": "62,841",
          "forks": "21,082",
          "starsToday": "485",
          "description": "12 Lessons to Get Started Building AI Agents —— 微软官方 AI Agent 入门教程，从理论到实战",
          "problems": [
            "<strong>AI Agent 学习路径不清晰：</strong>Agent 开发涉及 Prompt Engineering、Tool Use、Memory、Planning、Multi-Agent 等多层概念。微软这 12 节课提供了一条结构化学习路径——每节课有理论 + Jupyter Notebook 动手实验。",
            "<strong>缺少权威入门材料：</strong>社区教程质量参差不齐。微软背书+62K star 验证了这是目前最权威的 AI Agent 入门教程之一。",
            "<strong>从入门到生产的断层：</strong>课程不只讲&quot;什么是 Agent&quot;，还覆盖了 Agent 安全、负责任的 AI、生产部署等实战话题。"
          ],
          "usage": [
            "在线阅读课程：<pre><code>https://microsoft.github.io/ai-agents-for-beginners/</code></pre>",
            "Clone 代码并在本地 Jupyter 中运行每节课的 Notebook。",
            "配合 Azure AI Foundry / GitHub Models 使用微软生态的 Agent 工具链。",
            "跟随课程构建自己的 AI Agent 项目。"
          ],
          "insights": [
            "<strong>企业 AI Agent 培训认证：</strong>基于微软课程开发&quot;AI Agent 开发工程师&quot;认证培训——面向企业 IT 团队的标准化技能提升方案，类似 Azure 认证体系。",
            "<strong>Agent 开发低代码平台：</strong>把课程中的 12 节课抽象为 12 个模块化组件——让非技术人员通过可视化界面搭建 Agent，产品经理也能&quot;组装&quot;AI Agent。",
            "<strong>Agent 人才招聘平台：</strong>课程完成者形成一个认证社区——企业可以在这里找到经过标准化培训的 AI Agent 开发者，形成人才供需匹配平台。"
          ],
          "tags": [
            "microsoft",
            "beginner-friendly",
            "12-lessons",
            "agent-engineering",
            "production-ready",
            "jupyter"
          ],
          "count": 1
        }
      ]
    },
    {
      "date": "2026-05-14",
      "label": "18天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "obra",
          "name": "superpowers",
          "fullName": "obra / superpowers",
          "org": "obra",
          "url": "https://github.com/obra/superpowers",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "189,777",
          "forks": "16,891",
          "starsToday": "1,401",
          "description": "An agentic skills framework & software development methodology that works. —— 让你的 AI 编程 Agent 拥有超能力的技能框架",
          "problems": [
            "<strong>AI Agent 不会做软件工程：</strong>普通的 AI 编程 Agent 拿到需求直接写代码，没有规划、没有测试、没有审查。Superpowers 提供一套完整方法论：先问清楚需求 → 拆分 Spec → 制定实现计划 → 子 Agent 并行开发 → 自动审查，让 Agent 像专业工程师一样工作。",
            "<strong>跨平台 Agent 能力不统一：</strong>Claude Code、Codex、Cursor、Gemini CLI 等每个工具行为不同。Superpowers 一套技能在所有主流 Agent 平台通用，一次配置到处生效。",
            "<strong>Agent 自主开发会跑偏：</strong>Agent 持续编码几小时后容易偏离原始设计。Superpowers 的子 Agent 驱动开发模式确保每个任务都在计划框架内执行，不偏离。"
          ],
          "usage": [
            "Claude Code 安装：<pre><code>/plugin install superpowers@claude-plugins-official</code></pre>",
            "Codex CLI 安装：在 Codex 中输入 <code>/plugins</code> 搜索 superpowers 安装。",
            "Cursor 安装：将 .cursor-plugin 目录配置到 Cursor 插件中。",
            "安装后 Agent 自动获得技能触发机制——无需额外配置，Agent 自动使用 Spec → Plan → 子 Agent 实现的工作流。"
          ],
          "insights": [
            "<strong>Agent 开发方法论市场：</strong>Superpowers 证明 AI Agent 的&quot;工作流&quot;本身可以产品化。做一个平台让开发者上传和交易自己的 Agent 开发方法论（Spec 模板、审查规则、测试策略）。",
            "<strong>企业级 Agent 标准化：</strong>企业可以为所有开发者的 Agent 统一安装 Superpowers 类方法论插件，确保 100% 的 Agent 生成代码都经过 Spec → Plan → 审查流程，解决 AI 代码质量参差不齐的问题。",
            "<strong>Agent 编程的 CI/CD 平台：</strong>把 Superpowers 的工作流集成到 CI/CD 中——PR 提交后自动触发 Agent 审查、Agent 测试、Agent 重构，形成全自动 Agent 编程流水线。"
          ],
          "tags": [
            "agent-skills",
            "tdd",
            "subagent-driven-dev",
            "multi-platform",
            "methodology"
          ],
          "count": 1
        },
        {
          "rank": 2,
          "owner": "yikart",
          "name": "AiToEarn",
          "fullName": "yikart / AiToEarn",
          "org": "yikart",
          "url": "https://github.com/yikart/AiToEarn",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "13,084",
          "forks": "2,248",
          "starsToday": "981",
          "description": "Let's use AI to Earn! —— 一人公司的 AI 内容营销智能体，一站式内容创作、分发与变现平台",
          "problems": [
            "<strong>一人公司内容营销困境：</strong>个人创作者/小团队需要同时运营抖音、小红书、YouTube、TikTok 等十几个平台，内容生产、翻译、适配、发布、数据分析全是体力活。AiToEarn 用 AI Agent 全自动化这个过程。",
            "<strong>内容变现链路太长：</strong>从内容创作 → 多平台发布 → 流量获取 → 商业变现，每一步都需要专门工具。AiToEarn 把整条链路拉通成一个平台。",
            "<strong>线下门店缺线上曝光：</strong>餐厅、零售店、民宿的老板不懂线上营销。AiToEarn 提供线下商户推广方案，把推广活动转化为可执行的内容任务。"
          ],
          "usage": [
            "直接访问网站使用：<pre><code>https://aitoearn.ai</code></pre>",
            "MCP 协议接入 Claude/Cursor：<pre><code>npx @aitoearn/mcp-server</code></pre>",
            "Docker 私有部署：<pre><code>docker pull yikart/aitoearn && docker-compose up</code></pre>",
            "获取 API Key 后在 OpenClaw（龙虾）等 Agent 中直接调用内容变现能力。"
          ],
          "insights": [
            "<strong>AI 内容工厂 SaaS：</strong>面向全球创作者/小企业的 AI 内容生产线——输入行业/产品，输出适配 14 个平台的多语言内容并自动发布，按内容量订阅收费。",
            "<strong>内容交易市场：</strong>已有内容交易市场上线。创作者可以买卖 AI 生成的内容模板、视频脚本、图文素材，形成内容资产的流通市场。",
            "<strong>线下商业 AI 推广代理：</strong>本地服务商使用 AiToEarn 为周边商家提供&quot;AI 代运营&quot;服务——餐饮、美容、健身等线下业态的标准化线上推广方案。"
          ],
          "tags": [
            "content-marketing",
            "multi-platform",
            "MCP-protocol",
            "monetization",
            "OPC",
            "Docker"
          ],
          "count": 1
        },
        {
          "rank": 3,
          "owner": "danielmiessler",
          "name": "Personal_AI_Infrastructure",
          "fullName": "danielmiessler / Personal_AI_Infrastructure",
          "org": "danielmiessler",
          "url": "https://github.com/danielmiessler/Personal_AI_Infrastructure",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "13,441",
          "forks": "1,874",
          "starsToday": "435",
          "description": "Your Life Operating System —— 个人 AI 基础设施：让每个人拥有自己的 AI 超级能力，放大人类潜能",
          "problems": [
            "<strong>AI 工具碎片化：</strong>每个人使用不同的 AI 工具（ChatGPT、Claude、Cursor 等），能力分散、数据隔离。PAI 提供统一的个人 AI 基础设施——把 40+ 个技能包、Agent、工具整合成一套&quot;人生操作系统&quot;。",
            "<strong>个人缺乏 AI 主权：</strong>目前的数据和能力都在大公司的云端。PAI 让个人拥有自己的 AI 基础设施——自己控制数据、自己选择模型、自己定制技能。",
            "<strong>AI 不会&quot;了解你&quot;：</strong>每次对话都像初次见面。PAI 通过持久化记忆和技能包系统，让 AI 了解你的工作方式、偏好、项目历史，越用越聪明。"
          ],
          "usage": [
            "Clone 仓库：<pre><code>git clone https://github.com/danielmiessler/Personal_AI_Infrastructure</code></pre>",
            "选择需要的 Packs（技能包）：40+ 个独立技能包，覆盖写作、编程、研究、创意等。",
            "安装到 Claude Code / Codex / Cursor：将 Packs 目录配置到 Agent 的技能路径。",
            "自定义：参考已有 Pack 的 SKILL.md 格式，创建自己的专属技能包。"
          ],
          "insights": [
            "<strong>&quot;人生操作系统&quot;订阅：</strong>提供托管的个人 AI 基础设施——统一管理你的 Agent 技能、记忆、数据、模型偏好，按月订阅。从&quot;工具&quot;升级为&quot;数字分身&quot;。",
            "<strong>技能包应用商店：</strong>PAI 的 Packs 体系天然适合做成技能市场——个人上传/下载/评价技能包，形成个人 AI 技能的生态经济。",
            "<strong>企业&quot;数字员工&quot;基础设施：</strong>将 PAI 模式复制到企业——每个员工拥有自己的 AI 工作台，统一管理但数据隔离，形成企业 AI 生产力平台。"
          ],
          "tags": [
            "personal-ai",
            "skill-packs",
            "data-sovereignty",
            "life-os",
            "modular"
          ],
          "count": 1
        },
        {
          "rank": 4,
          "owner": "supertone-inc",
          "name": "supertonic",
          "fullName": "supertone-inc / supertonic",
          "org": "Supertone (HYBE)",
          "url": "https://github.com/supertone-inc/supertonic",
          "lang": "Swift",
          "langClass": "rs",
          "stars": "4,468",
          "forks": "449",
          "starsToday": "859",
          "description": "Lightning-Fast, On-Device, Multilingual TTS —— 闪电般快速的端侧多语言语音合成，31 种语言原生运行",
          "problems": [
            "<strong>云端 TTS 三大痛点：</strong>延迟高（网络往返 500ms+）、隐私风险（语音数据上传云端）、成本贵（按字符计费）。Supertonic 用 ONNX Runtime 完全在设备本地运行，零延迟、零泄露、零费用。",
            "<strong>多语言 TTS 质量参差不齐：</strong>现有端侧方案大多只支持英语。Supertonic v3 支持 31 种语言，覆盖中日韩英法等主流语言，且朗读准确度大幅提升。",
            "<strong>跨平台适配困难：</strong>TTS 引擎通常只支持一两个平台。Supertonic 提供 C++/Swift/Flutter/Go/Java/Node.js/C# 全栈 SDK，iOS/Android/Desktop/Web 全覆盖。"
          ],
          "usage": [
            "Python 安装：<pre><code>pip install supertonic</code></pre>",
            "iOS 集成：Swift Package Manager 添加 supertonic 依赖。",
            "自定义声音：上传录音到 <a href=\"https://supertonic.supertone.ai/voice_builder\" style=\"color:#58a6ff\">Voice Builder</a>，生成专属 TTS 模型并永久拥有。",
            "体验 Demo：<pre><code>https://huggingface.co/spaces/Supertone/supertonic-3</code></pre>"
          ],
          "insights": [
            "<strong>端侧 AI 语音 SDK 授权：</strong>向 App 开发者提供端侧 TTS SDK——语音助手、有声书、导航、教育等场景，按设备授权收费。端侧运行意味着没有服务端成本，毛利极高。",
            "<strong>个人声音克隆 + 设备部署：</strong>Voice Builder 让用户录制几分钟就能拥有自己的 AI 声音。未来可以把这个&quot;数字声音&quot;授权给内容平台（播客、视频配音），形成声音资产经济。",
            "<strong>边缘 AI 语音芯片：</strong>与 IoT/芯片厂商合作，将 Supertonic 烧录到智能音箱、车载系统、翻译设备中——所有语音处理本地完成，不需要联网。"
          ],
          "tags": [
            "on-device-tts",
            "31-languages",
            "ONNX",
            "voice-cloning",
            "privacy-first",
            "cross-platform"
          ],
          "count": 1
        },
        {
          "rank": 5,
          "owner": "rasbt",
          "name": "LLMs-from-scratch",
          "fullName": "rasbt / LLMs-from-scratch",
          "org": "Sebastian Raschka",
          "url": "https://github.com/rasbt/LLMs-from-scratch",
          "lang": "Jupyter Notebook",
          "langClass": "py",
          "stars": "94,533",
          "forks": "14,500",
          "starsToday": "821",
          "description": "Build a Large Language Model (From Scratch) —— 从零开始用 PyTorch 实现类 ChatGPT 的大语言模型",
          "problems": [
            "<strong>LLM 是&quot;黑盒&quot;：</strong>90% 的 AI 从业者只会调用 API，不理解 Transformer、Attention、RLHF 的内部原理。这本书让你从零实现一个完整 LLM——数据预处理 → Tokenizer → GPT 架构 → 预训练 → 微调 → 对齐，每个组件都手写。",
            "<strong>学习曲线太陡：</strong>直接看 GPT-4 级别的论文和代码让人望而生畏。作者用清晰的文字、图表和逐步示例，把复杂概念拆解成可以消化的章节，配套 Jupyter Notebook 即开即用。",
            "<strong>理论脱离实践：</strong>多数 AI 课程讲理论但不写代码。本书每个概念都对应可运行的代码——今天学的 Attention 机制，今天就能跑出结果看效果。"
          ],
          "usage": [
            "Clone 代码：<pre><code>git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git</code></pre>",
            "安装依赖：<pre><code>pip install -r requirements.txt</code></pre>",
            "按章节顺序运行 Jupyter Notebook，每章一个完整模块。",
            "配套书籍：<code>Build a Large Language Model (From Scratch)</code> 在 Manning/Amazon 有售。"
          ],
          "insights": [
            "<strong>LLM 工程认证课程：</strong>基于本书内容制作&quot;从零训练 LLM 工程师&quot;认证课程——面向企业 AI 团队的系统化培训。94K star 验证了巨大市场需求。",
            "<strong>交互式 LLM 学习平台：</strong>把书中的 Jupyter Notebook 做成浏览器内可运行的交互式学习平台——像 Codecademy 一样，但学的是 LLM 底层原理，按月订阅。",
            "<strong>企业 LLM 内训方案：</strong>包装成企业培训产品——&quot;让你的团队理解 LLM 的每一层&quot;。配套考核、证书、实战项目，解决企业 AI 人才短缺问题。"
          ],
          "tags": [
            "from-scratch",
            "transformer",
            "GPT-architecture",
            "education",
            "pytorch",
            "book-companion"
          ],
          "count": 1
        }
      ]
    },
    {
      "date": "2026-05-13",
      "label": "19天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "mattpocock",
          "name": "skills",
          "fullName": "mattpocock / skills",
          "org": "mattpocock",
          "url": "https://github.com/mattpocock/skills",
          "lang": "Shell",
          "langClass": "sh",
          "stars": "76,897",
          "forks": "6,632",
          "starsToday": "3,867",
          "description": "Skills for Real Engineers —— 来自 Matt Pocock 的 AI Agent 技能集：把业界最佳实践变成 Agent 可直接加载的技能文件",
          "problems": [
            "<strong>Agent 无结构化知识：</strong>AI 编码 Agent 缺乏&quot;最佳实践&quot;注入机制，每次都要用自然语言描述工作流。Skills 把最佳实践抽象为可复用的技能文件（.claude/skills/），Agent 自动加载。",
            "<strong>团队协作碎片化：</strong>工程师各自写自己的 Agent 提示词，质量参差不齐。Skills 提供标准化格式，团队可以共享和版本管理 Agent 技能。",
            "<strong>无法沉淀领域知识：</strong>每个项目的测试规范、部署流程、代码审查标准都是一次性的口述。Skills 让这些知识变成持久化的 Agent 资产。"
          ],
          "usage": [
            "Clone 技能库：<pre><code>git clone https://github.com/mattpocock/skills</code></pre>",
            "复制需要的技能到项目：<pre><code>cp skills/typescript.md myproject/.claude/skills/</code></pre>",
            "Claude Code 会自动加载 .claude/skills/ 下的所有技能文件作为上下文。",
            "自定义：参考已有技能文件格式，编写自己项目的技能文档。"
          ],
          "insights": [
            "<strong>技能市场 / Skill Marketplace：</strong>做 AI Agent 技能的 GitHub/GitHub Gist —— 工程师上传、分享、评价技能模板，按领域/语言/框架分类搜索。",
            "<strong>企业级 Agent 配置平台：</strong>公司统一管理 Agent 技能库，新人入职自动获得团队编码规范、安全规范、部署流程等技能注入。",
            "<strong>Agent 技能 A/B 测试：</strong>不同技能配置对 Agent 代码产出质量的影响分析和优化平台。"
          ],
          "tags": [
            "agent-skills",
            "best-practices",
            "claude-code",
            "knowledge-management",
            "team-sharing"
          ],
          "count": 1
        },
        {
          "rank": 2,
          "owner": "tinyhumansai",
          "name": "openhuman",
          "fullName": "tinyhumansai / openhuman",
          "org": "Tiny Humans AI",
          "url": "https://github.com/tinyhumansai/openhuman",
          "lang": "Rust",
          "langClass": "rs",
          "stars": "3,159",
          "forks": "300",
          "starsToday": "1,014",
          "description": "Your Personal AI Super Intelligence —— 私有的、简单的、极其强大的个人 AI 超级智能体",
          "problems": [
            "<strong>AI 依赖云端：</strong>ChatGPT/Claude 等需要将数据发送到远程服务器，隐私无法保证。OpenHuman 主打本地运行、隐私优先。",
            "<strong>AI Agent 复杂难用：</strong>大多数开源 Agent 框架配置繁琐（需要多个 API Key、配置文件）。OpenHuman 追求&quot;Simple and extremely powerful&quot;，安装即用。",
            "<strong>多模型锁定：</strong>支持本地模型和云端模型混合调度，用户可根据隐私需求和任务复杂度自由选择。"
          ],
          "usage": [
            "安装（Rust 生态）：<pre><code>cargo install openhuman</code></pre>",
            "初始化并配置本地模型或 API 密钥。",
            "通过 CLI 或 API 与个人 AI 助手交互，所有数据本地处理。"
          ],
          "insights": [
            "<strong>个人 AI 助手硬件：</strong>与 Mini PC / NAS 厂商合作，预装 OpenHuman，打造&quot;家庭 AI 服务器&quot;品类。",
            "<strong>企业私有 AI 部署：</strong>为企业提供完全离线、数据不出内网的 AI Agent 解决方案——金融、医疗、法律等强隐私行业刚需。",
            "<strong>个人数据银行：</strong>个人 AI 不仅回答问题，还管理你的邮件、日历、文件，成为个人数据的中枢调度系统。"
          ],
          "tags": [
            "privacy-first",
            "local-ai",
            "personal-agent",
            "rust",
            "on-device"
          ],
          "count": 1
        },
        {
          "rank": 3,
          "owner": "rohitg00",
          "name": "agentmemory",
          "fullName": "rohitg00 / agentmemory",
          "org": "rohitg00",
          "url": "https://github.com/rohitg00/agentmemory",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "6,229",
          "forks": "575",
          "starsToday": "1,048",
          "description": "#1 持久化记忆 for AI 编程 Agent —— 基于真实世界基准测试的最佳记忆方案",
          "problems": [
            "<strong>Agent 会话间失忆：</strong>每次新会话，Agent 完全忘记之前的项目上下文、错误修复历史、用户偏好。AgentMemory 实现跨会话的持久化记忆。",
            "<strong>Token 浪费巨大：</strong>传统方案把历史全部塞进上下文窗口，token 消耗爆炸。AgentMemory 用混合搜索 + 知识图谱，减少 92% token 用量。",
            "<strong>检索精度：</strong>基于真实世界基准测试，R@5 检索精度达 95.2%，不是实验室数据而是生产环境验证。"
          ],
          "usage": [
            "安装：<pre><code>npm install -g @agentmemory/agentmemory</code></pre>",
            "初始化：<pre><code>agentmemory init</code></pre>",
            "添加到 Claude Code / Codex / Cursor 的 MCP 配置，Agent 自动获得记忆能力。",
            "支持自动记忆保存/召回（12 种 Hook）、置信度评分、知识生命周期管理。"
          ],
          "insights": [
            "<strong>Agent 长期记忆 SaaS：</strong>提供托管的 Agent 记忆云服务，开发者只需接入 API，Agent 即刻拥有跨会话记忆。",
            "<strong>企业知识图谱：</strong>多个 Agent 共享同一记忆空间——客服 Agent、研发 Agent、运维 Agent 共享企业知识，形成统一知识大脑。",
            "<strong>用户画像引擎：</strong>记忆用户偏好/习惯/历史决策，让 AI 产品从&quot;工具&quot;升级为&quot;懂你的助手&quot;。"
          ],
          "tags": [
            "persistent-memory",
            "knowledge-graph",
            "95.2%-recall",
            "token-efficient",
            "MCP-native",
            "zero-deps"
          ],
          "count": 2
        },
        {
          "rank": 4,
          "owner": "millionco",
          "name": "react-doctor",
          "fullName": "millionco / react-doctor",
          "org": "Million.co",
          "url": "https://github.com/millionco/react-doctor",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "8,896",
          "forks": "281",
          "starsToday": "788",
          "description": "Your agent writes bad React. This catches it —— AI 生成的 React 代码质量检查工具",
          "problems": [
            "<strong>AI 生成代码质量差：</strong>AI 编码 Agent（Claude Code、Codex 等）经常生成低质量 React 代码——不必要的 re-render、内存泄漏、反模式、性能陷阱。",
            "<strong>人工审查效率低：</strong>AI 每天生成几百行代码，靠人工 Code Review 逐行检查 AI 的错误既慢又不彻底。",
            "<strong>缺乏 AI 专属检测规则：</strong>ESLint 等传统工具检测不了 AI 特有的代码问题。React Doctor 专门针对 AI 编码模式设计检测规则。"
          ],
          "usage": [
            "安装：<pre><code>npm install -g react-doctor</code></pre>",
            "在项目目录运行：<pre><code>react-doctor check</code></pre>",
            "自动扫描并报告 AI 生成的 React 代码中的问题，给出修复建议。",
            "集成 CI/CD：在 PR 阶段自动拦截 AI 生成的低质量代码。"
          ],
          "insights": [
            "<strong>AI 代码质检流水线：</strong>打造&quot;AI 生成 → 自动质检 → 自动修复 → 人工确认&quot;的完整流水线，作为 AI 编程时代的代码质量门禁。",
            "<strong>多语言扩展：</strong>当前专注 React，扩展到 Vue、Angular、Python、Go 等 AI 常用语言——&quot;AI 代码的 SonarQube&quot;。",
            "<strong>AI 编码教学：</strong>基于检测出的问题反向教育开发者：&quot;这是 AI 常犯的错误，正确的写法是...&quot;，加速 AI 编程学习曲线。"
          ],
          "tags": [
            "code-quality",
            "ai-generated-code",
            "react",
            "linting",
            "ci-cd"
          ],
          "count": 1
        },
        {
          "rank": 5,
          "owner": "datawhalechina",
          "name": "hello-agents",
          "fullName": "datawhalechina / hello-agents",
          "org": "Datawhale",
          "url": "https://github.com/datawhalechina/hello-agents",
          "lang": "Python",
          "langClass": "py",
          "stars": "48,533",
          "forks": "5,829",
          "starsToday": "599",
          "description": "《从零开始构建智能体》—— 从零开始的智能体原理与实践教程，中文 AI Agent 学习圣经",
          "problems": [
            "<strong>Agent 技术门槛高：</strong>AI Agent 涉及 LLM、工具调用、记忆管理、规划推理等多层技术栈，缺乏系统性学习路径。",
            "<strong>中文资源匮乏：</strong>英文 Agent 教程居多，中文社区缺少从原理到实战的完整教材。",
            "<strong>理论与实践脱节：</strong>多数教程要么偏理论（太抽象），要么偏应用（不理解原理）。Hello-Agents 从零实现 Agent 核心组件，理解每个模块的底层逻辑。"
          ],
          "usage": [
            "在线阅读：<pre><code>https://datawhalechina.github.io/hello-agents/</code></pre>",
            "跟随教程逐步实现 Agent 的各个模块：Prompt 引擎、工具系统、记忆模块、规划器。",
            "使用配套 Python 代码动手实践，最终构建一个完整的可运行 AI Agent。"
          ],
          "insights": [
            "<strong>AI Agent 培训平台：</strong>基于 Hello-Agents 课程体系，为企业提供&quot;AI Agent 开发工程师&quot;认证培训——这是一块即将爆发的技能培训市场。",
            "<strong>低代码 Agent 构建器：</strong>将教程中的模块封装为可视化拖拽组件，让产品经理和业务人员也能搭建 AI Agent。",
            "<strong>企业内部 Agent 开发框架：</strong>基于教程抽象出企业级 Agent 开发框架，标准化公司内部的 Agent 开发模式。"
          ],
          "tags": [
            "agent-from-scratch",
            "chinese-tutorial",
            "beginners-friendly",
            "Datawhale",
            "education"
          ],
          "count": 1
        }
      ]
    },
    {
      "date": "2026-05-12",
      "label": "20天前",
      "icon": "",
      "projects": [
        {
          "rank": 1,
          "owner": "NousResearch",
          "name": "hermes-agent",
          "fullName": "NousResearch / hermes-agent",
          "org": "NousResearch",
          "url": "https://github.com/NousResearch/hermes-agent",
          "lang": "Python",
          "langClass": "py",
          "stars": "145,476",
          "forks": "22,763",
          "starsToday": "2,065",
          "description": "The agent that grows with you —— 一个会自我进化的 AI Agent，内置闭环学习系统",
          "problems": [
            "<strong>Agent 不会学习：</strong>大多数 AI Agent 每次对话都&quot;失忆&quot;，不会从经验中成长。Hermes 内置技能系统，完成任务后自动创建技能并自我改进。",
            "<strong>跨平台碎片化：</strong>Telegram、Discord、Slack、CLI —— 一个网关打通所有平台。",
            "<strong>长期记忆缺失：</strong>自动管理持久化记忆 + 跨会话搜索 + 用户画像建模。"
          ],
          "usage": [
            "安装：<pre><code>pip install hermes-agent</code></pre>",
            "初始化：<pre><code>hermes init</code></pre>",
            "对话：<pre><code>hermes &quot;帮我分析这个项目&quot;</code></pre>"
          ],
          "insights": [
            "<strong>AI 个人助手订阅制：</strong>自进化的 Agent 提供越来越精准的个人化服务，形成高粘性订阅产品。",
            "<strong>企业 Agent 编排平台：</strong>多 Agent 协作 + 统一管理 + 审计日志，企业级 Agent 基础设施。"
          ],
          "tags": [
            "self-improving",
            "multi-platform",
            "skills-system",
            "200+ models"
          ],
          "count": 1
        },
        {
          "rank": 2,
          "owner": "bytedance",
          "name": "UI-TARS-desktop",
          "fullName": "ByteDance / UI-TARS-desktop",
          "org": "ByteDance",
          "url": "https://github.com/bytedance/UI-TARS-desktop",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "33,230",
          "forks": "3,297",
          "starsToday": "956",
          "description": "多模态 AI Agent 框架 —— 让 AI 像人一样操作电脑",
          "problems": [
            "<strong>GUI 自动化难：</strong>VLM 视觉模型理解屏幕内容，像人一样看和操作界面。",
            "<strong>本地 + 远程双模式：</strong>本地操控桌面或远程调度 Agent 执行任务。"
          ],
          "usage": [
            "<pre><code>npm install -g @agent-tars/cli</code></pre>",
            "<pre><code>agent-tars config set OPENAI_API_KEY=sk-xxx...e>",
            "<pre><code>agent-tars start</code></pre>"
          ],
          "insights": [
            "<strong>RPA 2.0：</strong>AI 驱动的流程自动化取代传统 RPA，零脚本维护。",
            "<strong>远程运维 Agent：</strong>企业 IT 的 AI 操作员——远程诊断、修复、配置。"
          ],
          "tags": [
            "VLM-vision",
            "GUI-automation",
            "MCP-protocol",
            "desktop-agent"
          ],
          "count": 1
        },
        {
          "rank": 3,
          "owner": "decolua",
          "name": "9router",
          "fullName": "decolua / 9router",
          "org": "decolua",
          "url": "https://github.com/decolua/9router",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "8,654",
          "forks": "1,366",
          "starsToday": "941",
          "description": "免费 AI 编程路由器 —— 连接任意编程工具到 40+ 免费/廉价 AI 模型",
          "problems": [
            "<strong>AI 编程太贵：</strong>自动使用 40+ 免费配额和廉价模型，大幅降低成本。",
            "<strong>Token 浪费严重：</strong>RTK 引擎自动压缩工具输出，节省 20-40% token。"
          ],
          "usage": [
            "<pre><code>npm install -g 9router && 9router</code></pre>",
            "Dashboard → Providers → Connect 免费提供商。",
            "设置编程工具指向 9Router 代理地址。"
          ],
          "insights": [
            "<strong>AI API 聚合网关：</strong>面向开发者的 AI 模型统一接入层，自动路由最优模型。",
            "<strong>企业 AI 成本优化：</strong>智能 Fallback + Token 压缩，帮企业降低 60-80% AI 成本。"
          ],
          "tags": [
            "token-saver",
            "40+ providers",
            "free-tier",
            "universal-proxy"
          ],
          "count": 1
        },
        {
          "rank": 4,
          "owner": "datawhalechina",
          "name": "easy-vibe",
          "fullName": "Datawhale / easy-vibe",
          "org": "Datawhale",
          "url": "https://github.com/datawhalechina/easy-vibe",
          "lang": "JavaScript",
          "langClass": "js",
          "stars": "10,159",
          "forks": "965",
          "starsToday": "812",
          "description": "Vibe Coding 2026 —— 面向零基础用户的现代 AI 编程课程",
          "problems": [
            "<strong>编程入门门槛高：</strong>用 AI 对话让零基础用户直接&quot;说出&quot;应用。",
            "<strong>中文 AI 编程教育：</strong>中文互动教程，覆盖多个模型。"
          ],
          "usage": [
            "在线阅读：datawhalechina.github.io/easy-vibe/",
            "配合 VS Code + Cursor/Codex 上手实践。"
          ],
          "insights": [
            "<strong>AI 编程教育平台：</strong>面向非技术人群的 AI 编程培训课程和认证体系。",
            "<strong>企业内部 AI 赋能：</strong>帮助非工程师员工用 AI 解决自己的工作自动化需求。"
          ],
          "tags": [
            "vibe-coding",
            "chinese-tutorial",
            "beginner-friendly"
          ],
          "count": 1
        },
        {
          "rank": 5,
          "owner": "rohitg00",
          "name": "agentmemory",
          "fullName": "rohitg00 / agentmemory",
          "org": "rohitg00",
          "url": "https://github.com/rohitg00/agentmemory",
          "lang": "TypeScript",
          "langClass": "ts",
          "stars": "5,013",
          "forks": "470",
          "starsToday": "430",
          "description": "#1 AI 编程 Agent 持久化记忆 —— 你的 Agent 再也不会失忆（当时数据，现已涨至 6.2K）",
          "problems": [
            "<strong>Agent 失忆症：</strong>持久化记忆，R@5 检索精度 95.2%，零外部依赖。",
            "<strong>Token 爆炸：</strong>混合搜索 + 知识图谱减少 92% token 用量。"
          ],
          "usage": [
            "<pre><code>npm install -g @agentmemory/agentmemory</code></pre>",
            "<pre><code>agentmemory init</code></pre>",
            "添加到任意 MCP 客户端，自动获得记忆能力。"
          ],
          "insights": [
            "<strong>Agent 记忆即服务：</strong>托管的记忆云服务，让任何 AI Agent 拥有跨会话记忆。",
            "<strong>企业知识大脑：</strong>多 Agent 共享记忆空间，形成统一企业知识图谱。"
          ],
          "tags": [
            "persistent-memory",
            "knowledge-graph",
            "MCP-native",
            "token-efficient"
          ],
          "count": 1
        }
      ]
    }
  ]
};
