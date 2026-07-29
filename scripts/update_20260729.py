#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update GitHub trending data for 2026-07-29 (1-day gap from 7/28)"""
import json
from datetime import datetime, date

path = '/Users/xuefei/ai_project/yuanlaiai/yuanlaiai.github.io/data.json'

with open(path) as f:
    data = json.load(f)

last = datetime.strptime(data['lastUpdated'], '%Y-%m-%d').date()
today = date(2026, 7, 29)
gap_days = (today - last).days  # 1
shift = gap_days + 1  # 2
print(f"Last: {last}, Today: {today}, Gap: {gap_days}, Shift: {shift}")

def find_latest_count(project_name):
    for day in data['days']:
        for proj in day['projects']:
            if proj['name'] == project_name:
                return proj['count']
    return 0

today_projects = [
    {
        "rank": 1,
        "owner": "bradautomates",
        "name": "claude-video",
        "fullName": "bradautomates / claude-video",
        "org": "bradautomates",
        "url": "https://github.com/bradautomates/claude-video",
        "lang": "Python",
        "langClass": "py",
        "stars": "12,069",
        "forks": "1,211",
        "starsToday": "988",
        "count": 3,
        "description": "🔥 亮点 —— 今日 +988★！12.1K★ 连续三天登榜热度翻倍！/watch 下载→抽帧→转录→Claude 分析视频，开发者刚需工具。",
        "problems": [
            "<strong>Claude 不能看视频：</strong>Claude 理解图片文字很棒，但无法直接处理视频内容。",
            "<strong>视频分析流程割裂：</strong>下载→抽帧→转录→分析，每一步都需要手动切换工具。",
            "<strong>缺少一站式解决方案：</strong>没有简单命令就能让 Claude 完整分析视频的工具。"
        ],
        "usage": [
            "安装：<pre><code>pip install claude-video</code></pre>",
            "让 Claude 看视频：<pre><code>/watch https://youtube.com/watch?v=xxx</code></pre>",
            "或本地文件：<pre><code>/watch path/to/video.mp4</code></pre>"
        ],
        "insights": [
            "<strong>连续三天登榜热度翻倍：</strong>7/27 +434★ → 7/28 +988★ → 热度翻倍！视频分析是压倒性的刚需。",
            "<strong>Claude 能力的「外挂」扩展：</strong>Claude 原生不支持视频，但抽帧+转录实现了——工具链创新比等模型升级更快。",
            "<strong>AI 视频分析赛道：</strong>开发者每天处理大量视频教程/会议记录/直播回放——一键分析将改变内容消费方式。"
        ],
        "tags": ["claude", "video-analysis", "agent-tool", "ai-tool", "automation"]
    },
    {
        "rank": 2,
        "owner": "moeru-ai",
        "name": "airi",
        "fullName": "moeru-ai / airi",
        "org": "萌 AI",
        "url": "https://github.com/moeru-ai/airi",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "44,736",
        "forks": "4,447",
        "starsToday": "797",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +797★！44.7K★ 连续两天登榜！自托管 Grok 伴侣 AI——实时语音聊天、Minecraft/Factorio 陪玩，全平台支持。",
        "problems": [
            "<strong>AI 伴侣都是云端的：</strong>Character.AI 等平台依赖云端，隐私不安全且需付费。",
            "<strong>AI 与游戏整合难：</strong>想让 AI 进入游戏世界一起玩，但缺乏自托管方案。",
            "<strong>跨平台 AI 集成碎片化：</strong>Web/macOS/Windows 各有一套方案，没有统一框架。"
        ],
        "usage": [
            "克隆：<pre><code>git clone https://github.com/moeru-ai/airi.git</code></pre>",
            "启动：<pre><code>docker compose up</code></pre>",
            "接入游戏：在 Minecraft/Factorio 中配置 mod 连接即可。"
        ],
        "insights": [
            "<strong>连续两天登榜保持高热度：</strong>+572★ → +797★ —— 44.7K★ 自托管 AI 伴侣需求持续增长。",
            "<strong>情感陪伴是 AI 的下一个增长曲线：</strong>从实用工具到生活伴侣——AI 正从工作场景进入日常生活。",
            "<strong>全平台 + 游戏集成的壁垒：</strong>Web/macOS/Windows + Minecraft/Factorio——不只是聊天助手，是跨平台 AI 伙伴。"
        ],
        "tags": ["ai-companion", "self-hosted", "grok", "gaming", "realtime-voice"]
    },
    {
        "rank": 3,
        "owner": "yorukot",
        "name": "superfile",
        "fullName": "yorukot / superfile",
        "org": "yorukot",
        "url": "https://github.com/yorukot/superfile",
        "lang": "Go",
        "langClass": "go",
        "stars": "21,463",
        "forks": "695",
        "starsToday": "662",
        "count": 2,
        "description": "🔥 亮点 —— 今日 +662★！21.5K★ 连续两天登榜！高颜值终端文件管理器——Go 语言单二进制，交互体验对标 GUI。",
        "problems": [
            "<strong>终端文件管理体验差：</strong>cd/ls/mv/cp 命令行操作繁琐，缺少可视化导航。",
            "<strong>GUI 文件管理器启动慢：</strong>Finder/Nautilus 在服务器或无桌面环境不可用。",
            "<strong>终端工具各司其职：</strong>没有统一的、现代化的文件管理体验。"
        ],
        "usage": [
            "安装：<pre><code>brew install superfile</code></pre> 或从 Releases 下载二进制。",
            "启动：<pre><code>spf</code></pre> 即可打开终端文件管理器。",
            "快捷键导航：<pre><code>hjkl</code></pre> 移动，<pre><code>Enter</code></pre> 进入目录，<pre><code>q</code></pre> 退出。"
        ],
        "insights": [
            "<strong>连续两天登榜持续增长：</strong>+600★ → +662★，superfile 的热度不是昙花一现——终端工具的设计革新是持久需求。",
            "<strong>Go 语言的终端生态：</strong>单二进制 + 零依赖 + 高性能 = 终端工具的首选技术栈。",
            "<strong>21.5K★ 证明：</strong>CLI 工具也可以有设计感——终端用户对「好看又好用」的需求不容忽视。"
        ],
        "tags": ["terminal", "file-manager", "go", "cli", "productivity"]
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
        "stars": "234,785",
        "forks": "35,774",
        "starsToday": "636",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +636★！235K★ 重磅回归！Agent Harness 性能优化系统——技能/直觉/记忆/安全，Claude Code/Codex/OpenCode/Cursor 全兼容。",
        "problems": [
            "<strong>Agent 运行效率低：</strong>编码 Agent 执行任务时缺乏系统化的性能优化机制。",
            "<strong>Agent 能力孤岛：</strong>技能、记忆、安全各管各的，缺少统一的性能调度层。",
            "<strong>跨平台兼容困难：</strong>Claude Code、Codex、Cursor 各有配置体系，无法复用。"
        ],
        "usage": [
            "安装：<pre><code>npm install -g ecc</code></pre>",
            "初始化 Agent：<pre><code>ecc init</code></pre>",
            "优化当前项目：<pre><code>ecc optimize --harness</code></pre>"
        ],
        "insights": [
            "<strong>235K★ 的狠角色回归：</strong>ECC 上次登榜还是 6 月初，56 天后回归——持久型基础设施，不是短期热点。",
            "<strong>Agent 性能优化的终极方案：</strong>从技能管理到记忆优化到安全护栏——ECC 是 AI 编码 Agent 的操作系统层。",
            "<strong>跨平台兼容是壁垒：</strong>同时支持 Claude Code、Codex、OpenCode、Cursor——兼容性本身就是护城河。"
        ],
        "tags": ["agent-harness", "performance", "claude-code", "codex", "agent-framework"]
    },
    {
        "rank": 5,
        "owner": "opengeos",
        "name": "GeoLibre",
        "fullName": "opengeos / GeoLibre",
        "org": "OpenGeos",
        "url": "https://github.com/opengeos/GeoLibre",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "3,379",
        "forks": "390",
        "starsToday": "607",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +607★！3.4K★ 轻量云原生 GIS 平台！浏览器/桌面/移动/Jupyter 全端运行，可视化探索地理空间数据。",
        "problems": [
            "<strong>GIS 工具重量级：</strong>传统 GIS 软件（ArcGIS/QGIS）安装复杂、资源占用大。",
            "<strong>地理空间数据可视化门槛高：</strong>需要专业 GIS 知识和专门软件才能做地图分析。",
            "<strong>跨平台 GIS 工具稀缺：</strong>浏览器、桌面、移动各有各的 GIS 方案，没有统一平台。"
        ],
        "usage": [
            "Web 版：直接访问在线版本即可使用。",
            "安装 CLI：<pre><code>pip install geolibre</code></pre>",
            "Jupyter 集成：<pre><code>import geolibre; geolibre.show_map()</code></pre>"
        ],
        "insights": [
            "<strong>3.4K★ 爆发式增长：</strong>从 2.7K 到 3.4K 只用了两天——轻量 GIS 需求被严重低估。",
            "<strong>云原生 GIS 的破局者：</strong>在浏览器中跑 GIS，零安装——让地理空间数据可视化触手可及。",
            "<strong>Jupyter 集成是杀手锏：</strong>数据科学家可以在地理空间分析 Notebook 中直接调用——无缝嵌入现有工作流。"
        ],
        "tags": ["gis", "geospatial", "cloud-native", "typescript", "data-visualization"]
    },
    {
        "rank": 6,
        "owner": "virgiliojr94",
        "name": "book-to-skill",
        "fullName": "virgiliojr94 / book-to-skill",
        "org": "virgiliojr94",
        "url": "https://github.com/virgiliojr94/book-to-skill",
        "lang": "Python",
        "langClass": "py",
        "stars": "11,316",
        "forks": "1,335",
        "starsToday": "423",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +423★！11.3K★ 任何技术书 PDF 转 Claude Code 技能——边编码边学，PDF 知识自动注入 Agent。",
        "problems": [
            "<strong>技术书知识难复用：</strong>看完 PDF 后知识点忘得快，编码时不能随时查阅。",
            "<strong>Agent 缺少领域知识：</strong>AI 编码助手不了解你正在读的技术书中的特定内容。",
            "<strong>PDF 信息与编码割裂：</strong>频繁在 PDF 阅读器和 IDE 之间切换，打断心流。"
        ],
        "usage": [
            "安装：<pre><code>pip install book-to-skill</code></pre>",
            "转换：<pre><code>book-to-skill path/to/book.pdf</code></pre>",
            "在 Claude Code 中加载生成的 SKILL.md 即可。"
        ],
        "insights": [
            "<strong>11K★ 的首日爆发：</strong>技术书知识注入 Agent——切中开发者「学以致用」的核心痛点。",
            "<strong>Agent 技能生成自动化：</strong>不再是手动写 SKILL.md，而是「一本书 → 一个技能」的全自动管线。",
            "<strong>知识库与 Agent 的桥梁：</strong>PDF 是最大的知识孤岛——book-to-skill 打通了从书本知识到 AI 助手的直达通道。"
        ],
        "tags": ["skill", "claude-code", "pdf", "learning", "developer-tools"]
    },
    {
        "rank": 7,
        "owner": "pascalorg",
        "name": "editor",
        "fullName": "pascalorg / editor",
        "org": "Pascal",
        "url": "https://github.com/pascalorg/editor",
        "lang": "TypeScript",
        "langClass": "ts",
        "stars": "18,674",
        "forks": "2,526",
        "starsToday": "341",
        "count": 1,
        "description": "🔥 亮点 —— 今日 +341★！18.7K★ 3D 建筑项目在线编辑器——TypeScript 编写，Web 端创建和分享 3D 建筑模型。",
        "problems": [
            "<strong>3D 建筑工具贵且复杂：</strong>Blender/SketchUp 学习曲线陡峭，AutoCAD 价格昂贵。",
            "<strong>3D 项目协作困难：</strong>传统 3D 文件格式大、版本管理难，分享不便。",
            "<strong>Web 端 3D 工具稀缺：</strong>浏览器中能做 3D 建模的工具少之又少。"
        ],
        "usage": [
            "直接访问：<pre><code>https://editor.pascal.app</code></pre>",
            "创建项目：选择模板开始建模。",
            "分享：一键生成链接，任何人可在线查看。"
        ],
        "insights": [
            "<strong>18.7K★ 的 Web 3D 新星：</strong>在浏览器里做 3D 建筑设计——零安装、即时分享，这正是 Web 3D 工具的未来。",
            "<strong>AI + 3D 建筑设计赛道：</strong>结合 AI 生成 3D 模型的能力——editor 可能是建筑行业 AI 化的重要入口。",
            "<strong>TypeScript 全栈 3D：</strong>用纯 Web 技术栈做 3D 编辑——证明了浏览器 3D 渲染已经达到生产标准。"
        ],
        "tags": ["3d", "architecture", "web-editor", "typescript", "design-tools"]
    }
]

# Shift labels for 1-day gap
days = data['days']
for day in days:
    label = day['label']
    if label == '今天':
        day['label'] = '昨天'
    elif label == '昨天':
        day['label'] = '前天'
    elif label == '前天':
        day['label'] = '3天前'
    elif label.endswith('天前'):
        num = int(label.replace('天前', ''))
        day['label'] = f'{num + 2}天前'

# Insert new day
new_day = {
    "date": "2026-07-29",
    "label": "今天",
    "icon": "",
    "projects": today_projects
}
days.insert(0, new_day)
data['lastUpdated'] = '2026-07-29'
data['topic'] = '🔥 <strong>Claude Video 连续三天热度翻倍 + Airi 自托管伴侣连涨 + Superfile 终端革新持续 + ECC 重磅回归 + GeoLibre GIS 爆发 + Book-to-Skill 知识注入 + Pascal 3D 编辑</strong> —— bradautomates/claude-video（+988★）12.1K★ 连续三天登榜！热度从 434→988 翻倍，视频分析压倒性刚需。moeru-ai/airi（+797★）44.7K★ 连续两天 +572→+797，AI 伴侣赛道爆发。yorukot/superfile（+662★）21.5K★ 连续两天登榜，终端工具设计革新不止。affaan-m/ECC（+636★）235K★ 56 天后重磅回归——Agent 性能优化的终极方案。opengeos/GeoLibre（+607★）3.4K★ 轻量云原生 GIS 平台爆发。virgiliojr94/book-to-skill（+423★）11.3K★ 技术书转 Agent 技能——知识库到 Agent 的直达通道。pascalorg/editor（+341★）18.7K★ 3D 建筑编辑器，Web 端 3D 工具赛道升温。视频分析 × AI 伴侣 × 终端革新 × Agent 优化 × GIS × 知识注入 × 3D 建筑——七条赛道同时加速，AI 工具链进入日常化阶段。'

print(f"Before: {len(days)-1} days, After: {len(days)} days")
print(f"New labels: {[d['label'] for d in days[:8]]}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated successfully!")
for p in data['days'][0]['projects']:
    print(f"  #{p['rank']} {p['name']}: +{p['starsToday']}★ total={p['stars']}★ count={p['count']}")
