# 精选 Prompt 模块 — 设计文档

## 概述

在猿来AI网站新增「精选 Prompt」模块，以卡片网格 + 弹窗模式展示优质 AI Prompt 模板，用户可浏览、筛选、复制使用。

## 数据模型

新建 `prompts.json`，数据结构：

```json
{
  "lastUpdated": "2026-05-26",
  "prompts": [
    {
      "id": 1,
      "title": "让 AI 帮你写周报",
      "category": "写作",
      "description": "描述本周工作要点，AI 自动生成结构化周报",
      "prompt": "你是一位专业的职场写作助手...",
      "useCase": "团队周报、个人工作汇报、跨部门同步",
      "models": ["ChatGPT", "Claude", "Kimi"],
      "tips": "提供越具体的项目名称和数据，生成效果越好"
    }
  ]
}
```

字段说明：

- `id` — 唯一标识
- `title` — Prompt 标题
- `category` — 分类（写作/编程/分析/创意/办公等）
- `description` — 简短描述，展示在卡片上
- `prompt` — 完整 Prompt 正文
- `useCase` — 使用场景说明
- `models` — 适用模型列表
- `tips` — 使用小贴士

## 布局位置

- 在 AI热点（`#trending`）和技术文章（`#articles`）section 之间插入新 section `#prompts`
- 导航栏新增「Prompt」入口
- 数据通过 `fetch('prompts.json')` 异步加载

## 卡片设计（正面）

- 网格布局：CSS Grid `auto-fill, minmax(320px, 1fr)`，响应式
- 卡片内容从上到下：分类标签 + 适用模型小图标 → 标题（粗体）→ 简短描述（灰色小字）→ 「查看 Prompt →」提示
- 样式复用现有文章卡片的 `--bg-card`、`--border`、hover 效果
- 点击卡片 → 打开 Modal

## 弹窗设计（Modal）

- 深色遮罩（`rgba(0,0,0,0.7)`），点击关闭
- 居中弹窗，最大宽度 640px，圆角，内边距
- 内容从上到下：标题 → 分类标签 → Prompt 正文（等宽字体深色底代码块风格，带复制按钮）→ 使用场景 → 适用模型 → 小贴士
- 底部按钮：复制（点击后文字变「已复制 ✓」）+ 关闭
- 右上角 X 按钮关闭
- ESC 键关闭

## 分类筛选

- 板块标题下方 filter-tags 横排按钮组
- 从 prompts 数据动态提取分类列表，「全部」为默认选中
- 点击筛选按钮过滤卡片
- 样式完全复用文章板块的 `.filter-btn`

## 复制功能

- 使用 `navigator.clipboard.writeText()` 复制 Prompt 正文
- 点击复制按钮后，按钮文字切换为「已复制 ✓」，2 秒后恢复
- 兜底：不支持 clipboard API 时用 `textarea` + `execCommand` 降级

## 文件改动

| 文件 | 操作 | 说明 |
|---|---|---|
| `prompts.json` | 新建 | Prompt 数据 |
| `index.html` | 编辑 | 新增 `#prompts` section + 导航入口 |
| `app.js` | 编辑 | 新增 `loadPrompts()` `renderPrompts()` `openPromptModal()` `closePromptModal()` `copyPrompt()` 等函数 |
| `style.css` | 编辑 | 新增 Prompt 卡片样式 + Modal 样式 |

## 技术要点

- 数据异步加载，有 loading/error 状态处理
- Modal 使用 fixed 定位，body 加 `overflow: hidden` 防止背景滚动
- 复用现有 `reveal` + `IntersectionObserver` 滚动动画
- 分类筛选逻辑参考现有文章板块的 `renderArticles(filter)` 模式
