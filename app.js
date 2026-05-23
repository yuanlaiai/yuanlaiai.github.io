// ── Config ──
var langMap = {
  'typescript': 'ts', 'javascript': 'js', 'python': 'py', 'rust': 'rs',
  'shell': 'sh', 'go': 'go', 'jupyter notebook': 'py', 'c#': 'cs',
  'swift': 'rs', 'ruby': 'rb', 'kotlin': 'kt', 'java': 'java',
  'c++': 'cpp', 'c': 'c', 'haskell': 'hs', 'lua': 'lua',
  'zig': 'zig', 'solidity': 'sol'
};

// ── Data ──────────────────────────────────────

var articles = [
  {
    id: 1,
    readTime: '12 分钟',
    title: 'React 18 并发特性深度解析',
    tags: ['React', '性能优化'],
    date: '2026-03-15',
    desc: '深入探讨 React 18 的 Fiber 架构升级、Concurrent Mode、useTransition、Suspense 等并发特性，以及它们在生产环境中的实战应用。',
  },
  {
    id: 2,
    readTime: '18 分钟',
    title: '从 0 到 1：构建 Node.js 微服务系统',
    tags: ['Backend', '架构'],
    date: '2026-02-28',
    desc: '手把手搭建基于 Node.js 的微服务架构，涵盖 API Gateway、服务注册发现、链路追踪、熔断限流等核心能力。',
  },
  {
    id: 3,
    readTime: '22 分钟',
    title: 'Kubernetes 实战：容器编排完全指南',
    tags: ['DevOps', 'K8s'],
    date: '2026-02-10',
    desc: '从集群搭建到生产部署，涵盖 Pod、Deployment、Service、Ingress、HPA 自动扩缩容，以及 Helm Chart 打包最佳实践。',
  },
  {
    id: 4,
    readTime: '10 分钟',
    title: '现代前端工具链对比：Webpack vs Vite vs esbuild',
    tags: ['前端工程'],
    date: '2026-01-20',
    desc: '深度对比三大构建工具的架构差异、性能表现和适用场景，帮你在不同项目中做出最优的技术选型决策。',
  },
  {
    id: 5,
    readTime: '8 分钟',
    title: '构建高性能 React 应用的 5 个技巧',
    tags: ['React', '性能优化'],
    date: '2026-03-01',
    desc: '深入探讨代码分割、懒加载、Memo 优化、虚拟列表以及 Web Worker 在 React 应用中的实战技巧。',
  },
  {
    id: 6,
    readTime: '15 分钟',
    title: 'Go 语言高并发实战：goroutine 与 channel',
    tags: ['Backend'],
    date: '2026-01-05',
    desc: '通过实战案例掌握 Go 的并发编程模型，深入讲解 goroutine 调度器、channel 通信模式与常见并发陷阱规避。',
  },
  {
    id: 7,
    readTime: '15 分钟',
    title: 'Java 21 新特性实战：虚拟线程与模式匹配',
    tags: ['Java'],
    date: '2026-04-10',
    desc: '深入解析 Java 21 的虚拟线程（Virtual Threads）、模式匹配（Pattern Matching）、Record Pattern 等重磅特性，以及在实际项目中的迁移策略和性能对比。',
  },
  {
    id: 8,
    readTime: '20 分钟',
    title: 'Android Jetpack Compose 从入门到精通',
    tags: ['Android'],
    date: '2026-04-20',
    desc: '全面掌握 Jetpack Compose 声明式 UI 开发，涵盖状态管理、导航、动画、Material3 设计系统，以及与传统 View 系统的互操作最佳实践。',
  },
  {
    id: 9,
    readTime: '18 分钟',
    title: 'Spring Boot 3 + GraalVM 原生编译实战',
    tags: ['Java', 'Backend'],
    date: '2026-05-05',
    desc: '使用 Spring Boot 3 + GraalVM Native Image 构建毫秒级启动的云原生应用，详解 AOT 编译原理、反射配置和 Docker 镜像优化。',
  },
  {
    id: 10,
    readTime: '16 分钟',
    title: 'Android 性能优化：从启动到渲染的全链路分析',
    tags: ['Android', '性能优化'],
    date: '2026-05-12',
    desc: '系统化分析 Android 应用性能问题，覆盖启动优化、布局渲染、内存管理、网络优化、包体积缩减等核心维度，附实战工具链。',
  },
  {
    id: 11,
    readTime: '14 分钟',
    title: 'Go 语言进阶：泛型、错误处理与测试策略',
    tags: ['Go', 'Backend'],
    date: '2026-05-18',
    desc: '深入 Go 1.18+ 泛型实际应用、error wrapping 与 sentinel errors 最佳实践，以及 Table-driven 测试、fuzz testing 和基准测试的实战技巧。',
  },
];

var projects = [
  {
    id: 1,
    icon: '⚡',
    name: '高并发分布式缓存系统',
    desc: '基于 Go + Redis + Raft 共识算法构建的分布式缓存系统，支持百万级 QPS，具备自动故障转移和水平扩容能力。',
    stack: ['Go', 'Redis', 'Kubernetes', 'gRPC', 'Raft'],
    stars: '520+',
  },
  {
    id: 2,
    icon: '🧩',
    name: '开源 React UI 组件库',
    desc: '基于 React + TypeScript 打造的高质量 UI 组件库，完整 Storybook 文档，覆盖 60+ 组件，支持主题定制。',
    stack: ['React', 'TypeScript', 'Storybook', 'Vitest'],
    stars: '310+',
  },
  {
    id: 3,
    icon: '📊',
    name: '云原生应用监控平台',
    desc: '集成 Prometheus + Grafana + OpenTelemetry 的一站式可观测性平台，支持链路追踪、指标聚合和智能告警。',
    stack: ['React', 'Node.js', 'Prometheus', 'Docker'],
    stars: '180+',
  },
];

// ── Render Trending Timeline ─────────────────

var VISIBLE_DAYS = 3;
var BATCH_SIZE = 3;
var dayLoadCount = 0;

function renderTimeline() {
  var container = document.getElementById('trendingTimeline');
  if (!container || !window.siteData) return;

  dayLoadCount = VISIBLE_DAYS;
  container.innerHTML = buildTimelineHtml(dayLoadCount);
  observeReveal();
}

function buildTimelineHtml(showUpTo) {
  var allDays = window.siteData.days;
  var totalDays = allDays.length;
  var fadeDayIdx = showUpTo; // 第4天（索引3）添加渐变
  var displayUpTo = Math.min(showUpTo + 1, totalDays);
  var remaining = totalDays - showUpTo;

  var html = '<div class="timeline" id="timeline">';

  for (var di = 0; di < displayUpTo; di++) {
    var day = allDays[di];
    var isFirst = di === 0;
    var isFadeDay = di === fadeDayIdx && fadeDayIdx < totalDays;
    var bodyExtra = isFirst ? '' : ' collapsed';

    // 渐变日的外层包裹
    if (isFadeDay) {
      html += '<div class="day-group-fade-wrap">';
    }

    // ── day-group（与所有天数完全相同的样式）──
    html += '<div class="day-group reveal" style="transition-delay:' + (di * 0.05) + 's">';
    html += '<div class="day-node">';
    html += '<div class="day-dot"></div>';
    html += '<span class="day-label">' + day.label + '</span>';
    html += '<span class="day-date">' + day.date + '</span>';
    html += '</div>';
    html += '<div class="day-body' + bodyExtra + '">';
    html += '<div class="day-projects">';

    day.projects.forEach(function(p) {
      var cardExtra = isFirst ? '' : ' dimmed';

      var problemsHtml = '<ul>';
      if (p.problems) p.problems.forEach(function(x) { problemsHtml += '<li>' + x + '</li>'; });
      problemsHtml += '</ul>';

      var usageHtml = '<ol>';
      if (p.usage) p.usage.forEach(function(x) { usageHtml += '<li>' + x + '</li>'; });
      usageHtml += '</ol>';

      var insightsHtml = '<ul>';
      if (p.insights) p.insights.forEach(function(x) { insightsHtml += '<li>' + x + '</li>'; });
      insightsHtml += '</ul>';

      html += '<div class="project-card reveal' + cardExtra + '" data-rank="' + p.rank + '" style="transition-delay:' + (di * 0.05 + 0.05) + 's">';
      html += '<div class="rank-ribbon"></div>';
      html += '<div class="pc-header">';
      html += '<span class="rank-num">#' + p.rank + '</span>';
      html += '<a href="' + p.url + '" class="repo-name" target="_blank">' + p.fullName + '</a>';
      html += '<span class="org">' + p.org + '</span>';
      html += '</div>';
      html += '<div class="pc-meta">';
      html += '<span class="lang">' + p.lang + '</span>';
      html += '<span class="stats">';
      html += '⭐ <strong>' + p.stars + '</strong>';
      html += ' · 🍴 <strong>' + p.forks + '</strong>';
      html += '</span>';
      html += '<span class="today">+ ' + p.starsToday + ' today</span>';
      html += '</div>';
      html += '<p class="pc-desc">' + p.description + '</p>';
      html += '<div class="pc-details">';
      html += '<div class="pc-section"><div class="pc-section-label problem">📌 解决什么问题</div><div class="pc-section-content">' + problemsHtml + '</div></div>';
      html += '<div class="pc-section"><div class="pc-section-label usage">🔧 如何使用</div><div class="pc-section-content">' + usageHtml + '</div></div>';
      html += '<div class="pc-section"><div class="pc-section-label insight">💡 产品价值思路</div><div class="pc-section-content">' + insightsHtml + '</div></div>';
      html += '</div>';
      html += '<div class="pc-tags">';
      p.tags.forEach(function(t) { html += '<span class="pc-tag">' + t + '</span>'; });
      var countText = p.count > 1 ? p.count + '次上榜' : '首次上榜';
      html += '<span class="pc-count">' + countText + '</span>';
      html += '</div>';
      html += '</div>';
    });

    html += '</div>'; // day-projects
    html += '<div class="day-fade"></div>';
    html += '</div>'; // day-body

    // Toggle button for past days
    if (!isFirst) {
      html += '<button class="day-toggle" onclick="toggleDay(this)">';
      html += '<span class="toggle-dot"></span>';
      html += '<span class="toggle-label">' + day.label + '</span>';
      html += '<span class="toggle-date">' + day.date + '</span>';
      html += '<span class="toggle-count">' + day.projects.length + ' 个项目</span>';
      html += '<span class="toggle-icon">▾</span>';
      html += '</button>';
    }

    html += '</div>'; // day-group

    // 渐变日的外层包裹关闭——渐变遮罩 + 按钮
    if (isFadeDay && remaining > 0) {
      html += '<div class="day-group-fade-overlay"></div>';
      html += '<div class="load-more-overlay" id="loadMoreWrap">';
      html += '<button class="btn-load-more" onclick="loadMoreDays()">📅 展开更早记录 <span class="load-more-count">(' + remaining + ' 天)</span></button>';
      html += '</div>';
      html += '</div>'; // day-group-fade-wrap
    }
  }

  html += '</div>'; // timeline

  html += '<div style="text-align:center;margin-top:32px">';
  html += '<a href="https://github.com/trending" class="btn-ghost" target="_blank">查看完整 GitHub Trending →</a>';
  html += '</div>';

  return html;
}

function loadMoreDays() {
  dayLoadCount += BATCH_SIZE;
  var container = document.getElementById('trendingTimeline');
  if (!container) return;
  container.innerHTML = buildTimelineHtml(dayLoadCount);
  observeReveal();
}

function toggleDay(btn) {
  var dayGroup = btn.closest('.day-group');
  if (!dayGroup) return;
  var dayBody = dayGroup.querySelector('.day-body');
  if (!dayBody) return;

  var isOpening = dayBody.classList.contains('collapsed');
  var icon = btn.querySelector('.toggle-icon');

  if (isOpening) {
    dayBody.style.maxHeight = 'none';
    var fullHeight = dayBody.scrollHeight;
    dayBody.classList.remove('collapsed');
    dayBody.style.maxHeight = '0px';
    requestAnimationFrame(function() {
      dayBody.style.maxHeight = fullHeight + 'px';
    });
    icon.classList.add('open');
  } else {
    dayBody.style.maxHeight = dayBody.scrollHeight + 'px';
    requestAnimationFrame(function() {
      dayBody.classList.add('collapsed');
    });
    icon.classList.remove('open');
  }
}

// ── Render Articles ────────────────────────────

function renderArticles(filter) {
  if (typeof filter === 'undefined') filter = 'all';
  var grid = document.getElementById('articlesGrid');
  var filtered = filter === 'all'
    ? articles
    : articles.filter(function(a) { return a.tags.some(function(t) { return t === filter; }); });

  grid.innerHTML = filtered.map(function(a, i) {
    return '<div class="article-card reveal" style="transition-delay: ' + (i * 0.07) + 's">' +
      '<div class="card-meta">' +
        a.tags.map(function(t, idx) { return '<span class="card-tag' + (idx % 2 === 1 ? ' purple' : '') + '">' + t + '</span>'; }).join('') +
        '<span class="card-date">' + a.date + '</span>' +
      '</div>' +
      '<h3 class="card-title">' + a.title + '</h3>' +
      '<p class="card-desc">' + a.desc + '</p>' +
      '<div class="card-footer">' +
        '<span class="card-read-time">' + a.readTime + '</span>' +
        '<span class="card-arrow">→</span>' +
      '</div>' +
    '</div>';
  }).join('');
  observeReveal();
}

// ── Article Filter ─────────────────────────

var activeFilter = 'all';
document.querySelectorAll('.filter-btn').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    activeFilter = btn.getAttribute('data-filter');
    renderArticles(activeFilter);
  });
});

// ── Render Projects ──────────────────────────

function renderProjects() {
  var grid = document.getElementById('projectsGrid');
  if (!grid) return;
  grid.innerHTML = projects.map(function(p, i) {
    return '<div class="project-card reveal" style="transition-delay: ' + (i * 0.1) + 's">' +
      '<div class="project-header">' +
        '<div class="project-icon">' + p.icon + '</div>' +
        '<div class="project-stars"><span class="star-icon">★</span> ' + p.stars + '</div>' +
      '</div>' +
      '<h3 class="project-name">' + p.name + '</h3>' +
      '<p class="project-desc">' + p.desc + '</p>' +
      '<div class="project-stack">' +
        p.stack.map(function(s) { return '<span class="stack-tag">' + s + '</span>'; }).join('') +
      '</div>' +
    '</div>';
  }).join('');
  observeReveal();
}

// ── Scroll Reveal Animation ─────────────────

function observeReveal() {
  var els = document.querySelectorAll('.reveal');
  var obs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });
  els.forEach(function(el) { obs.observe(el); });
}

// ── Collapsible Day Toggle ────────────────────

// ── Full-Background Particle Animation ────────

function initBgParticles() {
  var canvas = document.getElementById('bgCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var particles = [];
  var mouse = { x: -9999, y: -9999 };
  var isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  var colors = isDark
    ? ['255,140,66', '255,179,71', '0,217,255', '167,139,250']
    : ['230,120,50', '210,150,60', '0,180,220', '140,110,220'];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  var count = Math.min(Math.floor(canvas.width * canvas.height / 6000), 200);
  for (var i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      r: Math.random() * 3 + 0.5,
      color: colors[Math.floor(Math.random() * colors.length)],
      alpha: Math.random() * 0.5 + 0.1,
      phase: Math.random() * Math.PI * 2
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var time = Date.now() / 3000;

    // Draw connections between nearby particles
    for (var i = 0; i < particles.length; i++) {
      for (var j = i + 1; j < particles.length; j++) {
        var dx = particles[i].x - particles[j].x;
        var dy = particles[i].y - particles[j].y;
        var dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = 'rgba(' + colors[0] + ',' + (0.06 * (1 - dist / 120)) + ')';
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }

    particles.forEach(function(p) {
      // Floating motion with sine wave
      p.vx += Math.sin(time + p.phase) * 0.01;
      p.vy += Math.cos(time + p.phase * 1.3) * 0.01;
      // Damping
      p.vx *= 0.99;
      p.vy *= 0.99;

      // Mouse repulsion
      var mdx = p.x - mouse.x;
      var mdy = p.y - mouse.y;
      var mDist = Math.sqrt(mdx * mdx + mdy * mdy);
      if (mDist < 150) {
        var force = (150 - mDist) / 150 * 0.5;
        var angle = Math.atan2(mdy, mdx);
        p.vx += Math.cos(angle) * force;
        p.vy += Math.sin(angle) * force;
      }

      p.x += p.vx;
      p.y += p.vy;

      // Wrap around edges
      if (p.x < -20) p.x = canvas.width + 20;
      if (p.x > canvas.width + 20) p.x = -20;
      if (p.y < -20) p.y = canvas.height + 20;
      if (p.y > canvas.height + 20) p.y = -20;

      // Draw particle with glow
      var gradient = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 4);
      gradient.addColorStop(0, 'rgba(' + p.color + ',' + p.alpha + ')');
      gradient.addColorStop(0.3, 'rgba(' + p.color + ',' + (p.alpha * 0.3) + ')');
      gradient.addColorStop(1, 'rgba(' + p.color + ',0)');
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r * 4, 0, Math.PI * 2);
      ctx.fillStyle = gradient;
      ctx.fill();

      // Core dot
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(' + p.color + ',' + (p.alpha * 1.2) + ')';
      ctx.fill();
    });

    // Mouse glow
    if (mouse.x > 0) {
      var glow = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 200);
      glow.addColorStop(0, 'rgba(' + colors[0] + ',0.03)');
      glow.addColorStop(1, 'rgba(' + colors[0] + ',0)');
      ctx.beginPath();
      ctx.arc(mouse.x, mouse.y, 200, 0, Math.PI * 2);
      ctx.fillStyle = glow;
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  document.addEventListener('mousemove', function(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  draw();
}

// ── Init ──
document.addEventListener('DOMContentLoaded', function() {
  if (window.siteData) renderTimeline();
  renderArticles();
  renderProjects();
  initBgParticles();
});
