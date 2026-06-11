# 🐒 猿来AI · yuanlaiai.github.io

> 一只想让人人秒懂 AI 的猿 — AI 科普 × GitHub 趋势解读

一个基于 GitHub Pages 的静态网站，每日自动追踪 GitHub Trending 上的 AI 项目，提供中文深度解读，并发布原创 AI 分析文章。

---

## ✨ 核心功能

### 🔥 GitHub AI 热点
每日抓取 GitHub Trending，筛选 Top 5 AI 项目，输出中文分析（解决什么问题、如何使用、产品价值思路）。4天 timeline 折叠展示，支持展开历史记录。

### 📝 文章系统
- **首页** — 展示最新 6 篇文章卡片，支持按标签筛选
- **文章列表** (`/articles.html`) — 全部文章，每页加载 10 篇
- **文章详情** (`/articles/slug/`) — 语义化 URL，全文阅读
- **自动同步公众号** — 文章自动创建微信公众平台草稿，发布后更新链接

### 🎨 主题切换
深色/浅色主题一键切换，偏好存 localStorage 持久化。

### 🔍 SEO 优化
- 每篇文章独立 HTML + 语义化 Slug URL
- Open Graph / Twitter Card / Schema.org Article 结构化数据
- `sitemap.xml` + `robots.txt`

---

## 🏗️ 技术架构

```
yuanlaiai.github.io/
├── index.html              # 首页（导航 + Hero + 热点 + 文章 + 项目 + 关于）
├── articles.html           # 文章列表页（分页加载 10篇/次）
├── article.html            # 文章详情模板页（通过 ?id= 访问，保留兼容）
├── app.js                  # 全部渲染逻辑（timeline / articles / projects / prompt）
├── style.css               # 全站样式 + 深色/浅色主题变量
├── data.js                 # 数据文件 (var siteData = {...})
├── data.json               # 数据源（JSON，手动编辑后用脚本生成 data.js）
├── articles/               # 文章按 Slug 独立页面
│   ├── agent-skill-three-kingdoms/
│   ├── apple-gemini-wwdc2026/
│   └── .../
├── awesome-ai-tools/       # AI工具导航页
├── assets/                 # 图片资源
├── sitemap.xml             # 搜索引擎 Sitemap
├── robots.txt              # 搜索引擎爬虫规则
└── scripts/                # 工具脚本
```

### 数据流

```
编辑 data.json
    ↓ (python3 脚本)
生成 data.js (var siteData = {...})
    ↓ (git commit + push)
GitHub Pages 自动部署
    ↓
浏览器加载 index.html → data.js → app.js 渲染
```

---

## 📋 每日更新工作流

1. 浏览 GitHub Trending，筛选 Top 5 AI 项目
2. 为每个项目写分析（problems / usage / insights）
3. 添加到 `data.json` → `days` 数组开头
4. 重新计算所有 day label（今天/昨天/前天/n天前）
5. 重新计算项目上榜次数（oldest-first）
6. 更新 `topic`（今日看点）
7. 生成 `data.js`
8. 更新 CDN version（`data.js?v=YYYYMMDD`）
9. 生成微信公众平台草稿（可选）
10. Commit + Push

> 详细的参考文档见 `static-data-site` 技能。

---

## 📝 写文章工作流

1. 在 `data.json` → `articles` 数组新增条目（含 HTML 内容）
2. 运行 `python3 /tmp/generate-article-pages.py` 生成 Slug 页面
3. 生成 `data.js`
4. 自动创建公众号草稿
5. 发布后补充 `wechatUrl`
6. Commit + Push

### 文章字段说明

```json
{
  "id": 1,
  "slug": "agent-skill-three-kingdoms",
  "title": "文章标题",
  "tags": ["标签1", "标签2"],
  "date": "2026-06-11",
  "readTime": "8 分钟",
  "desc": "文章简介（SEO meta description）",
  "content": "<section>HTML 正文...</section>",
  "wechatUrl": "https://mp.weixin.qq.com/s/xxx"
}
```

---

## 🎨 设计系统

| Token | 深色模式 | 浅色模式 |
|-------|---------|---------|
| `--bg-primary` | `#0B0E17` | `#F8F6F3` |
| `--bg-card` | `#141B2D` | `#FFFFFF` |
| `--text-primary` | `#E6EAED` | `#1A1A2E` |
| `--text-secondary` | `#94A3B8` | `#475569` |
| `--accent-orange` | `#FF8C42` | `#E07020` |

---

## 🔗 链接

- 网站：https://yuanlaiai.github.io
- 公众号：猿来AI
- 微信：yuanlaiai
- GitHub：https://github.com/yuanlaiai
