# 精选 Prompt 模块 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在猿来AI网站新增精选 Prompt 模块，卡片网格展示 + 弹窗查看详情 + 一键复制

**Architecture:** 新建 `prompts.json` 数据文件，在 `index.html` 插入新 section，`app.js` 新增异步加载、卡片渲染、Modal 弹窗、分类筛选、剪贴板复制函数，`style.css` 新增卡片和 Modal 样式。完全复用现有设计变量和交互模式。

**Tech Stack:** Vanilla JS + CSS + HTML，零依赖

---

## File Structure

| File | Operation | Responsibility |
|---|---|---|
| `prompts.json` | Create | Prompt 数据源，fetch 异步加载 |
| `index.html` | Modify | 新增 `#prompts` section + 导航入口 |
| `app.js` | Modify | 加载、渲染、筛选、Modal、复制所有逻辑 |
| `style.css` | Modify | Prompt 卡片 + Modal + 复制按钮样式 |

---

### Task 1: 创建 prompts.json 数据文件

**Files:**
- Create: `prompts.json`

- [ ] **Step 1: 写入初始 prompt 数据（8 条，覆盖 5 个分类）**

```json
{
  "lastUpdated": "2026-05-26",
  "prompts": [
    {
      "id": 1,
      "title": "让 AI 帮你写周报",
      "category": "写作",
      "description": "描述本周工作要点，AI 自动生成结构化周报，突出重点成果",
      "prompt": "你是一位专业的职场写作助手。请根据我提供的本周工作要点，生成一份结构化周报。\n\n要求：\n1. 开头一句话总结本周最重要的成果\n2. 分「已完成」「进行中」「计划」三个板块\n3. 每个事项包含：任务名、一句话描述、关键数据（如有）\n4. 语气专业但不生硬，适当使用 emoji 增强可读性\n5. 最后加一个「下周重点」预告\n\n本周工作要点：\n[在此输入你的工作内容]",
      "useCase": "团队周报、个人工作汇报、跨部门同步",
      "models": ["ChatGPT", "Claude", "Kimi"],
      "tips": "提供越具体的项目名称和数据，生成效果越好。建议先列出 3-5 个要点再粘贴。"
    },
    {
      "id": 2,
      "title": "代码审查助手",
      "category": "编程",
      "description": "让 AI 帮你 review 代码，发现潜在 bug、性能问题和改进建议",
      "prompt": "你是一位资深代码审查专家，精通多种编程语言和最佳实践。请审查以下代码，从以下几个维度给出反馈：\n\n1. **Bug 风险**：可能导致运行时错误的代码\n2. **性能问题**：可优化的算法或资源使用\n3. **安全漏洞**：XSS、SQL 注入、敏感信息泄露等\n4. **可读性**：命名、结构、注释方面的建议\n5. **最佳实践**：不符合语言/框架惯例的写法\n\n对每个问题标注严重程度（🔴高/🟡中/🟢低），并给出修改后的代码示例。\n\n```\n[在此粘贴代码]\n```",
      "useCase": "代码提交前自查、Code Review、学习最佳实践",
      "models": ["ChatGPT", "Claude", "Copilot"],
      "tips": "粘贴完整函数或文件效果最好，片段太短 AI 缺少上下文。可以指定关注的语言和框架。"
    },
    {
      "id": 3,
      "title": "技术文章翻译",
      "category": "写作",
      "description": "将英文技术文章翻译成流畅的中文，保留技术术语的准确性",
      "prompt": "你是一位专业的技术翻译，擅长将英文技术文章翻译为流畅、准确的中文。\n\n翻译要求：\n1. 技术术语保持英文原文（如 API、SDK、Container），或用业界通用译法\n2. 代码块、命令行、配置片段保持原样不翻译\n3. 长句拆分为符合中文阅读习惯的短句\n4. 保留原文的语气风格（正式/轻松/教程式）\n5. 专有名词（公司名、产品名、人名）保持原文\n\n请翻译以下内容：\n\n[在此粘贴英文原文]",
      "useCase": "翻译技术博客、文档、论文摘要",
      "models": ["ChatGPT", "Claude", "DeepSeek"],
      "tips": "如果文章很长，分段翻译效果更好。可以先让 AI 总结全文再逐段翻译，保持术语一致性。"
    },
    {
      "id": 4,
      "title": "SQL 查询生成器",
      "category": "编程",
      "description": "用自然语言描述需求，AI 生成对应的 SQL 查询语句",
      "prompt": "你是一位数据库专家，精通 SQL 和查询优化。请根据我的需求描述，生成对应的 SQL 查询语句。\n\n要求：\n1. 优先使用标准 SQL 语法（兼容 MySQL 8.0+ / PostgreSQL）\n2. 为每个查询添加简短注释说明逻辑\n3. 如有多种写法，给出推荐方案并说明原因\n4. 注意索引利用和查询性能\n5. 如涉及 JOIN，说明使用了什么类型的连接及原因\n\n数据库表结构：\n[在此描述表结构和字段]\n\n查询需求：\n[在此用自然语言描述想要查询什么]",
      "useCase": "数据分析、报表生成、后端开发写查询",
      "models": ["ChatGPT", "Claude", "DeepSeek"],
      "tips": "提供表结构和字段名是关键，AI 才能生成可直接运行的 SQL。可以先粘贴 CREATE TABLE 语句。"
    },
    {
      "id": 5,
      "title": "产品需求文档（PRD）生成",
      "category": "办公",
      "description": "从产品想法快速生成结构化的 PRD 文档",
      "prompt": "你是一位资深产品经理。请根据我的产品想法，生成一份结构化的产品需求文档（PRD）。\n\n文档结构：\n1. **产品概述**：一句话描述 + 目标用户\n2. **用户痛点**：当前用户遇到的 3 个核心问题\n3. **解决方案**：产品如何解决这些问题\n4. **核心功能**：MVP 阶段必须包含的功能（按 P0/P1/P2 优先级）\n5. **用户故事**：2-3 个典型使用场景\n6. **成功指标**：可量化的关键指标（KPI）\n7. **非功能性需求**：性能、安全、兼容性要求\n\n产品想法：\n[在此描述你的产品想法]",
      "useCase": "产品规划、创业 BP、需求评审",
      "models": ["ChatGPT", "Claude", "Kimi"],
      "tips": "想法描述越具体越好，可以包括目标用户画像、竞品信息。如果已有用户反馈，一并提供会更精准。"
    },
    {
      "id": 6,
      "title": "学习路线规划师",
      "category": "学习",
      "description": "根据你想学的技能和时间预算，AI 生成个性化学习路线",
      "prompt": "你是一位技术学习规划专家。请根据以下信息，为我设计一份个性化的学习路线图。\n\n规划要求：\n1. 将学习目标拆分为多个阶段（入门→进阶→实战）\n2. 每个阶段包含：学习主题、推荐资源（免费优先）、预计耗时、里程碑输出\n3. 标注知识点之间的依赖关系（先修知识）\n4. 给出每个阶段的项目实战建议\n5. 最后附上常见坑点和避坑建议\n\n学习目标：[如：从零学会 Python 数据分析]\n当前基础：[如：会一点 Excel，编程零基础]\n每周可投入时间：[如：每周 10 小时]\n目标期限：[如：3 个月后能独立做数据分析项目]",
      "useCase": "自学编程、转行准备、技能提升规划",
      "models": ["ChatGPT", "Claude", "DeepSeek", "Kimi"],
      "tips": "越诚实地描述当前基础，路线越实用。可以补充你的学习风格偏好（看视频/读书/动手项目）。"
    },
    {
      "id": 7,
      "title": "会议纪要整理",
      "category": "办公",
      "description": "将会议录音转文字或笔记要点，AI 整理为结构化会议纪要",
      "prompt": "你是一位专业的会议记录秘书。请根据我提供的会议内容，整理一份结构清晰、重点突出的会议纪要。\n\n纪要结构：\n1. **会议信息**：主题、日期、参会人\n2. **核心结论**：3-5 条最重要的决定\n3. **讨论要点**：按议题分类，每项标注讨论结果\n4. **待办事项（Action Items）**：任务描述 + 负责人 + 截止日期\n5. **下次会议**：待讨论的遗留议题\n\n格式要求：\n- 用清单（bullet points）而非长段落\n- 关键决策和行动项加粗\n- 避免流水账，只保留有结论或待办的内容\n\n会议内容：\n[在此粘贴会议笔记/录音转文字]",
      "useCase": "工作总结、跨团队沟通、项目周会记录",
      "models": ["ChatGPT", "Claude", "Kimi", "通义千问"],
      "tips": "如果内容是录音转文字，建议先用工具预处理去掉语气词和重复内容。关键数字和日期要特别标注。"
    },
    {
      "id": 8,
      "title": "AI 创意命名与 Slogan",
      "category": "创意",
      "description": "为你的产品、品牌或项目生成创意名称和宣传语",
      "prompt": "你是一位资深品牌策划专家，擅长创意命名和 slogan 创作。请根据我的项目信息，生成一系列命名方案。\n\n输出要求：\n1. **命名方案**（10 个）：每个名字附一句话解释其含义和适用场景\n   - 中文名、英文名各 5 个\n   - 覆盖不同风格：科技感、简约风、趣味性、高端感\n2. **Slogan 方案**（5 条）：每条附适用场景说明\n   - 不同长度：短 slogan（4-6 字）、中 slogan（8-12 字）、长 slogan（15-20 字）\n3. **推荐组合**：选出最佳名称 + slogan 组合，说明理由\n\n项目信息：\n- 产品/品牌类型：[如：AI 写作工具]\n- 目标用户：[如：大学生和职场新人]\n- 核心卖点：[如：一键生成论文大纲和文献综述]\n- 品牌调性：[如：专业但亲切，有点幽默感]",
      "useCase": "创业项目命名、产品起名、品牌定位",
      "models": ["ChatGPT", "Claude", "DeepSeek"],
      "tips": "品牌调性描述越清晰越好，可以附上你喜欢的竞品名字作为参考风格。"
    }
  ]
}
```

- [ ] **Step 2: 验证 JSON 格式有效**

```bash
cat prompts.json | python3 -m json.tool > /dev/null && echo "Valid JSON"
```

- [ ] **Step 3: Commit**

```bash
git add prompts.json
git commit -m "feat: 添加精选 Prompt 数据文件"
```

---

### Task 2: 修改 index.html — 导航入口 + Prompt section

**Files:**
- Modify: `index.html`

- [ ] **Step 1: 在导航栏添加 Prompt 入口**

找到导航链接列表（现有：首页、AI工具、AI热点、文章、项目、关于），在 AI热点 之后插入：

```html
<a href="#prompts" class="nav-link">Prompt</a>
```

修改后的 nav-links 部分：

```html
<div class="nav-links" id="navLinks">
  <a href="#home" class="nav-link active">首页</a>
  <a href="awesome-ai-tools/" class="nav-link">AI工具</a>
  <a href="#trending" class="nav-link">AI热点</a>
  <a href="#prompts" class="nav-link">Prompt</a>
  <a href="#articles" class="nav-link">文章</a>
  <a href="#projects" class="nav-link">项目</a>
  <a href="#about" class="nav-link">关于</a>
</div>
```

- [ ] **Step 2: 在 #trending section 和 #articles section 之间插入 Prompt section**

```html
<!-- Curated Prompts Section -->
<section id="prompts" class="section">
  <div class="container">
    <div class="section-header">
      <div class="section-label">// 精选 Prompt</div>
      <h2 class="section-title">💬 Prompt 模板库</h2>
      <p class="section-subtitle">精选高质量 AI 提示词，点击卡片查看详情，一键复制使用</p>
    </div>
    <div class="filter-tags" id="promptFilterTags">
      <!-- Rendered by JS -->
    </div>
    <div id="promptsLoading" style="text-align:center;padding:40px;color:var(--text-muted)">
      加载中...
    </div>
    <div class="prompts-grid" id="promptsGrid" style="display:none">
      <!-- Rendered by JS -->
    </div>
  </div>
</section>

<!-- Prompt Modal -->
<div class="modal-overlay" id="promptModal" style="display:none">
  <div class="modal-container" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <button class="modal-close" onclick="closePromptModal()" aria-label="关闭">✕</button>
    <div class="modal-body" id="modalBody">
      <!-- Rendered by JS -->
    </div>
    <div class="modal-footer">
      <button class="btn-modal-copy" id="modalCopyBtn" onclick="copyPromptFromModal()">📋 复制 Prompt</button>
      <button class="btn-modal-close" onclick="closePromptModal()">关闭</button>
    </div>
  </div>
</div>
```

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: 添加 Prompt 模块 HTML 结构和导航入口"
```

---

### Task 3: 添加 CSS 样式 — 卡片 + 筛选 + Modal

**Files:**
- Modify: `style.css`

- [ ] **Step 1: 在 style.css 末尾追加 Prompt 卡片样式**

```css
/* ── Prompts Section ── */
.prompts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}

.prompt-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  transition: all var(--transition);
  cursor: pointer;
  display: flex;
  flex-direction: column;
}

.prompt-card:hover {
  border-color: var(--accent-orange);
  box-shadow: 0 4px 20px rgba(255, 140, 66, 0.08);
  transform: translateY(-3px);
}

.prompt-card-top {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}

.prompt-category-tag {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  padding: 3px 10px;
  background: rgba(167, 139, 250, 0.1);
  border: 1px solid rgba(167, 139, 250, 0.2);
  border-radius: 4px;
  color: var(--accent-purple);
}

.prompt-model-icons {
  font-size: 0.7rem;
  margin-left: auto;
  color: var(--text-muted);
  display: flex;
  gap: 4px;
  align-items: center;
}

.prompt-card-title {
  font-size: 1.05rem;
  font-weight: 600;
  line-height: 1.5;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.prompt-card-desc {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.7;
  flex: 1;
}

.prompt-card-hint {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  font-size: 0.78rem;
  color: var(--accent-orange);
  transition: all var(--transition);
}

.prompt-card:hover .prompt-card-hint {
  color: var(--accent-gold);
}

/* ── Prompt Modal ── */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 2000;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  animation: modalFadeIn 0.2s ease;
}

@keyframes modalFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-container {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  max-width: 640px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  position: relative;
  animation: modalSlideIn 0.25s ease;
}

@keyframes modalSlideIn {
  from { opacity: 0; transform: translateY(20px) scale(0.97); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.modal-close {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid var(--border);
  background: var(--bg-secondary);
  color: var(--text-secondary);
  font-size: 0.9rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition);
  z-index: 10;
}

.modal-close:hover {
  border-color: var(--accent-orange);
  color: var(--accent-orange);
  background: var(--accent-orange-dim);
}

.modal-body {
  padding: 32px 28px 20px;
}

.modal-body .modal-title {
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.modal-body .modal-category {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  padding: 3px 10px;
  background: rgba(167, 139, 250, 0.1);
  border: 1px solid rgba(167, 139, 250, 0.2);
  border-radius: 4px;
  color: var(--accent-purple);
  margin-bottom: 20px;
}

.modal-section {
  margin-bottom: 20px;
}

.modal-section-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--accent-cyan);
  margin-bottom: 8px;
  letter-spacing: 0.04em;
}

.modal-prompt-block {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 18px;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  line-height: 1.8;
  color: var(--text-primary);
  white-space: pre-wrap;
  word-break: break-word;
  max-height: 300px;
  overflow-y: auto;
}

.modal-section-text {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.7;
}

.modal-model-list {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.modal-model-tag {
  font-size: 0.75rem;
  padding: 4px 12px;
  background: rgba(0, 217, 255, 0.06);
  border: 1px solid rgba(0, 217, 255, 0.15);
  border-radius: 100px;
  color: var(--accent-cyan);
}

.modal-footer {
  display: flex;
  gap: 10px;
  padding: 16px 28px 24px;
  border-top: 1px solid var(--border);
}

.btn-modal-copy {
  flex: 1;
  padding: 12px 20px;
  background: linear-gradient(135deg, var(--accent-orange), #FF6B35);
  color: #fff;
  font-family: var(--font-sans);
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition);
}

.btn-modal-copy:hover {
  box-shadow: 0 4px 20px rgba(255, 140, 66, 0.35);
  transform: translateY(-1px);
}

.btn-modal-copy.copied {
  background: #22c55e;
}

.btn-modal-close {
  padding: 12px 20px;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.9rem;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition);
}

.btn-modal-close:hover {
  border-color: var(--accent-orange);
  color: var(--accent-orange);
}

/* ── Mobile Modal ── */
@media (max-width: 768px) {
  .prompts-grid {
    grid-template-columns: 1fr;
  }

  .modal-overlay {
    padding: 0;
    align-items: flex-end;
  }

  .modal-container {
    max-width: 100%;
    max-height: 90vh;
    border-radius: var(--radius) var(--radius) 0 0;
  }

  .modal-body {
    padding: 24px 18px 16px;
  }

  .modal-footer {
    padding: 12px 18px 20px;
    flex-direction: column;
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add style.css
git commit -m "feat: 添加 Prompt 卡片和 Modal 样式"
```

---

### Task 4: 添加 JS 逻辑 — 加载、渲染、筛选、Modal、复制

**Files:**
- Modify: `app.js`

- [ ] **Step 1: 在 app.js 末尾追加 Prompt 模块所有 JS 代码**

在 `initBgParticles` 函数之前（即 DOMContentLoaded 监听器之前），追加以下全部代码：

```js
// ── Prompts Module ──────────────────────────

var promptsData = [];
var activePromptFilter = 'all';
var currentModalPromptId = null;

function loadPrompts() {
  var loadingEl = document.getElementById('promptsLoading');
  var gridEl = document.getElementById('promptsGrid');

  fetch('prompts.json')
    .then(function(res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function(data) {
      promptsData = data.prompts || [];
      if (loadingEl) loadingEl.style.display = 'none';
      if (gridEl) gridEl.style.display = '';
      renderPromptFilters();
      renderPrompts();
    })
    .catch(function(err) {
      console.error('Failed to load prompts:', err);
      if (loadingEl) loadingEl.textContent = 'Prompt 数据加载失败，请刷新重试';
    });
}

function getPromptCategories() {
  var cats = [];
  promptsData.forEach(function(p) {
    if (cats.indexOf(p.category) === -1) cats.push(p.category);
  });
  return cats;
}

function renderPromptFilters() {
  var filterContainer = document.getElementById('promptFilterTags');
  if (!filterContainer) return;

  var categories = getPromptCategories();
  var html = '<button class="filter-btn active" data-filter="all">全部</button>';
  categories.forEach(function(cat) {
    html += '<button class="filter-btn" data-filter="' + cat + '">' + cat + '</button>';
  });
  filterContainer.innerHTML = html;

  filterContainer.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      filterContainer.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activePromptFilter = btn.getAttribute('data-filter');
      renderPrompts();
    });
  });
}

function renderPrompts() {
  var grid = document.getElementById('promptsGrid');
  if (!grid) return;

  var filtered = activePromptFilter === 'all'
    ? promptsData
    : promptsData.filter(function(p) { return p.category === activePromptFilter; });

  grid.innerHTML = filtered.map(function(p, i) {
    var modelIcons = p.models.map(function(m) {
      return '<span class="prompt-model-icon">' + m + '</span>';
    }).join('');

    return '<div class="prompt-card reveal" style="transition-delay:' + (i * 0.06) + 's" onclick="openPromptModal(' + p.id + ')">' +
      '<div class="prompt-card-top">' +
        '<span class="prompt-category-tag">' + p.category + '</span>' +
        '<span class="prompt-model-icons">' + modelIcons + '</span>' +
      '</div>' +
      '<h3 class="prompt-card-title">' + p.title + '</h3>' +
      '<p class="prompt-card-desc">' + p.description + '</p>' +
      '<div class="prompt-card-hint">查看 Prompt →</div>' +
    '</div>';
  }).join('');

  observeReveal();
}

// ── Modal ───────────────────────────────────

function openPromptModal(id) {
  var prompt = null;
  promptsData.forEach(function(p) {
    if (p.id === id) prompt = p;
  });
  if (!prompt) return;

  currentModalPromptId = id;

  var modelTags = prompt.models.map(function(m) {
    return '<span class="modal-model-tag">' + m + '</span>';
  }).join('');

  var bodyHtml =
    '<h2 class="modal-title">' + prompt.title + '</h2>' +
    '<span class="modal-category">' + prompt.category + '</span>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">📝 Prompt 正文</div>' +
      '<div class="modal-prompt-block">' + escapeHtml(prompt.prompt) + '</div>' +
    '</div>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">🎯 使用场景</div>' +
      '<div class="modal-section-text">' + prompt.useCase + '</div>' +
    '</div>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">🤖 适用模型</div>' +
      '<div class="modal-model-list">' + modelTags + '</div>' +
    '</div>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">💡 使用小贴士</div>' +
      '<div class="modal-section-text">' + prompt.tips + '</div>' +
    '</div>';

  document.getElementById('modalBody').innerHTML = bodyHtml;

  var copyBtn = document.getElementById('modalCopyBtn');
  copyBtn.textContent = '📋 复制 Prompt';
  copyBtn.classList.remove('copied');

  var modal = document.getElementById('promptModal');
  modal.style.display = '';
  document.body.style.overflow = 'hidden';

  // Focus trap: focus close button
  var closeBtn = modal.querySelector('.modal-close');
  if (closeBtn) closeBtn.focus();
}

function closePromptModal() {
  var modal = document.getElementById('promptModal');
  modal.style.display = 'none';
  document.body.style.overflow = '';
  currentModalPromptId = null;
}

function copyPromptFromModal() {
  var prompt = null;
  promptsData.forEach(function(p) {
    if (p.id === currentModalPromptId) prompt = p;
  });
  if (!prompt) return;

  var text = prompt.prompt;
  var btn = document.getElementById('modalCopyBtn');

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(function() {
      btn.textContent = '✅ 已复制';
      btn.classList.add('copied');
      setTimeout(function() {
        btn.textContent = '📋 复制 Prompt';
        btn.classList.remove('copied');
      }, 2000);
    }).catch(function() {
      fallbackCopy(text, btn);
    });
  } else {
    fallbackCopy(text, btn);
  }
}

function fallbackCopy(text, btn) {
  var textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.left = '-9999px';
  textarea.style.top = '-9999px';
  document.body.appendChild(textarea);
  textarea.focus();
  textarea.select();
  try {
    document.execCommand('copy');
    btn.textContent = '✅ 已复制';
    btn.classList.add('copied');
    setTimeout(function() {
      btn.textContent = '📋 复制 Prompt';
      btn.classList.remove('copied');
    }, 2000);
  } catch (e) {
    btn.textContent = '复制失败，请手动选择文本';
  }
  document.body.removeChild(textarea);
}

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Modal click-outside-to-close
document.addEventListener('click', function(e) {
  if (e.target.id === 'promptModal') {
    closePromptModal();
  }
});

// ESC to close
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape' && currentModalPromptId !== null) {
    closePromptModal();
  }
});
```

- [ ] **Step 2: 在 DOMContentLoaded 中调用 loadPrompts()**

在 `document.addEventListener('DOMContentLoaded', function() {` 函数体内，现有调用之后添加：

```js
loadPrompts();
```

修改后的 init 块：

```js
document.addEventListener('DOMContentLoaded', function() {
  if (window.siteData) renderTimeline();
  renderArticles();
  renderProjects();
  loadPrompts();
  initBgParticles();
});
```

- [ ] **Step 3: Commit**

```bash
git add app.js
git commit -m "feat: 添加 Prompt 模块 JS 逻辑 — 加载、渲染、筛选、Modal、复制"
```

---

### Task 5: 验证与收尾

- [ ] **Step 1: 启动本地服务器测试**

```bash
cd /Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io && python3 -m http.server 8080
```

打开 http://localhost:8080，验证：
1. 导航栏出现「Prompt」入口，点击可跳转到 Prompt 板块
2. 卡片网格正常展示 8 条 prompt，5 种分类
3. 分类筛选按钮可正常过滤
4. 点击卡片弹出 Modal，内容完整
5. 点击「复制 Prompt」按钮，按钮变绿显示「✅ 已复制」
6. 点击遮罩层 / X 按钮 / ESC 键可关闭 Modal
7. 移动端（Chrome DevTools 模拟）Modal 从底部弹出

- [ ] **Step 2: 确认无破坏性变更**

验证原有功能正常：AI热点、文章、项目、关于、导航滚动、粒子背景

- [ ] **Step 3: 修复发现的问题（如有）**

- [ ] **Step 4: 最终 commit（如有修复）**

```bash
git add -A
git commit -m "fix: Prompt 模块验证修复"
```
