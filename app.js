// ── Config ──
var langMap = {
  'typescript': 'ts', 'javascript': 'js', 'python': 'py', 'rust': 'rs',
  'shell': 'sh', 'go': 'go', 'jupyter notebook': 'py', 'c#': 'cs',
  'swift': 'rs', 'ruby': 'rb', 'kotlin': 'kt', 'java': 'java',
  'c++': 'cpp', 'c': 'c', 'haskell': 'hs', 'lua': 'lua',
  'zig': 'zig', 'solidity': 'sol'
};

// ── Data ──────────────────────────────────────

// Articles now come from data.js (siteData.articles)
var articles = (typeof window !== 'undefined' && window.siteData && window.siteData.articles)
  ? window.siteData.articles
  : [];

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

// ── Topic Insight ──
function renderTopicInsight() {
  var el = document.getElementById('trendingTopic');
  if (!el || !window.siteData || !window.siteData.topic) { if (el) el.style.display = 'none'; return; }
  el.style.display = '';
  el.innerHTML = '<div class="topic-card"><div class="topic-icon">📌</div><div class="topic-content"><div class="topic-label">今日看点</div><div class="topic-text">' + window.siteData.topic + '</div></div></div>';
}

// ── Timeline ──
function renderTimeline() {
  var container = document.getElementById('trendingTimeline');
  if (!container || !window.siteData) return;
  renderTopicInsight();

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
      html += '<button class="day-toggle" type="button" onclick="toggleDay(event,this)">';
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
      html += '<button class="btn-load-more" type="button" onclick="loadMoreDays()">📅 展开更早记录 <span class="load-more-count">(' + remaining + ' 天)</span></button>';
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

function toggleDay(e, btn) {
  if (e) { e.preventDefault(); e.stopPropagation(); }
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

// ── Theme Toggle ──────────────────────────

(function() {
  var html = document.documentElement;
  var btn = document.getElementById('themeToggle');
  if (!btn) return;

  // Restore saved theme
  var saved = localStorage.getItem('theme');
  if (saved === 'light') {
    html.setAttribute('data-theme', 'light');
    btn.textContent = '☀️';
  }

  btn.addEventListener('click', function() {
    var current = html.getAttribute('data-theme');
    if (current === 'light') {
      html.removeAttribute('data-theme');
      localStorage.setItem('theme', 'dark');
      btn.textContent = '🌙';
    } else {
      html.setAttribute('data-theme', 'light');
      localStorage.setItem('theme', 'light');
      btn.textContent = '☀️';
    }
  });
})();

// ── Navbar Scroll Behavior ────────────────

(function() {
  var navbar = document.getElementById('navbar');
  if (!navbar) return;
  var lastScrollY = window.scrollY;
  var scrollThreshold = 100;  // pixels before showing background

  function onScroll() {
    var currentScrollY = window.scrollY;

    // Add/remove background (.scrolled)
    if (currentScrollY > scrollThreshold) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // At the very top — always fully visible, transparent
    if (currentScrollY < 50) {
      navbar.classList.remove('nav-hidden');
      navbar.classList.remove('scrolled');
      lastScrollY = currentScrollY;
      return;
    }

    // Scrolling down → hide navbar
    if (currentScrollY > lastScrollY && currentScrollY > scrollThreshold) {
      navbar.classList.add('nav-hidden');
    }
    // Scrolling up → show navbar
    else if (currentScrollY < lastScrollY) {
      navbar.classList.remove('nav-hidden');
    }

    lastScrollY = currentScrollY;
  }

  // Debounce for performance
  var ticking = false;
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        onScroll();
        ticking = false;
      });
      ticking = true;
    }
  });

  // Initial check
  onScroll();
})();

function renderArticles(filter) {
  if (typeof filter === 'undefined') filter = 'all';
  var grid = document.getElementById('articlesGrid');
  var filtered = filter === 'all'
    ? articles
    : articles.filter(function(a) { return a.tags.some(function(t) { return t === filter; }); });

  // Only show latest 6 on homepage
  var showCount = Math.min(filtered.length, 6);

  grid.innerHTML = filtered.slice(0, showCount).map(function(a, i) {
    return '<a href="articles/' + a.slug + '/" class="article-card reveal" style="text-decoration:none;transition-delay: ' + (i * 0.07) + 's">' +
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
    '</a>';
  }).join('');
  observeReveal();
}

// ── Article Filter ─────────────────────────

function renderFilters() {
  var container = document.getElementById('filterTags');
  if (!container) return;
  // Collect all unique tags from articles
  var tagSet = {};
  for (var i = 0; i < articles.length; i++) {
    for (var j = 0; j < articles[i].tags.length; j++) {
      tagSet[articles[i].tags[j]] = true;
    }
  }
  var allTags = Object.keys(tagSet).sort();
  // Build filter buttons
  var html = '<button class="filter-btn active" data-filter="all">全部</button>';
  for (var k = 0; k < allTags.length; k++) {
    html += '<button class="filter-btn" data-filter="' + allTags[k] + '">' + allTags[k] + '</button>';
  }
  container.innerHTML = html;

  // Attach click handlers
  document.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeFilter = btn.getAttribute('data-filter');
      renderArticles(activeFilter);
    });
  });
}

var activeFilter = 'all';

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

var _revealObserver = null;

function observeReveal() {
  if (_revealObserver) _revealObserver.disconnect();
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
  _revealObserver = obs;
}

// ── Collapsible Day Toggle ────────────────────

// ── Full-Background Particle Animation ────────

function initBgParticles() {
  var canvas = document.getElementById('bgCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var particles = [];
  var mouse = { x: -9999, y: -9999, tx: -9999, ty: -9999 };
  var isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  var accent = isDark ? '0,217,255' : '0,150,200';
  var warm = isDark ? '255,140,66' : '200,100,50';

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  // Starfield particles
  var count = Math.min(Math.floor(canvas.width * canvas.height / 10000), 120);
  for (var i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      z: Math.random() * 3 + 0.5,        // depth: 1=close, 3=far
      size: Math.random() * 2 + 0.5,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      baseVx: (Math.random() - 0.5) * 0.3,
      baseVy: (Math.random() - 0.5) * 0.3,
      alpha: Math.random() * 0.5 + 0.15,
      pulse: Math.random() * Math.PI * 2
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Smooth mouse follow
    mouse.tx += (mouse.x - mouse.tx) * 0.05;
    mouse.ty += (mouse.y - mouse.ty) * 0.05;

    var isActive = mouse.x > -100;

    particles.forEach(function(p) {
      p.pulse += 0.03;

      if (isActive) {
        // Flow toward mouse
        var dx = mouse.tx - p.x;
        var dy = mouse.ty - p.y;
        var dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 300) {
          var strength = (1 - dist / 300) * 0.15 / p.z;
          p.vx += (dx / dist) * strength;
          p.vy += (dy / dist) * strength;
        }

        // Data stream alignment - particles near cursor align to flow lines
        if (dist < 150) {
          var orbitStr = (1 - dist / 150) * 0.05;
          p.vx += Math.sin(p.pulse + p.y * 0.01) * orbitStr;
          p.vy += Math.cos(p.pulse + p.x * 0.01) * orbitStr;
        }
      }

      // Return to base velocity
      p.vx += (p.baseVx - p.vx) * 0.01;
      p.vy += (p.baseVy - p.vy) * 0.01;

      // Speed limit
      var speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
      if (speed > 2) { p.vx = (p.vx / speed) * 2; p.vy = (p.vy / speed) * 2; }

      p.x += p.vx;
      p.y += p.vy;

      if (p.x < -30) p.x = canvas.width + 30;
      if (p.x > canvas.width + 30) p.x = -30;
      if (p.y < -30) p.y = canvas.height + 30;
      if (p.y > canvas.height + 30) p.y = -30;

      // Glow based on proximity to mouse
      var glowBoost = 1;
      if (isActive) {
        var d = Math.sqrt(Math.pow(p.x - mouse.tx, 2) + Math.pow(p.y - mouse.ty, 2));
        if (d < 200) glowBoost = 1 + (1 - d / 200) * 2;
      }

      var color = p.z > 2 ? accent : warm;
      var glowSize = p.size * 4 * glowBoost;
      var pulseAlpha = p.alpha + Math.sin(p.pulse) * 0.12;

      // Outer glow
      var gradient = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, glowSize);
      gradient.addColorStop(0, 'rgba(' + color + ',' + (pulseAlpha * 0.6) + ')');
      gradient.addColorStop(0.5, 'rgba(' + color + ',' + (pulseAlpha * 0.15) + ')');
      gradient.addColorStop(1, 'rgba(' + color + ',0)');
      ctx.beginPath();
      ctx.arc(p.x, p.y, glowSize, 0, Math.PI * 2);
      ctx.fillStyle = gradient;
      ctx.fill();

      // Core
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size * 0.7, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(' + color + ',' + pulseAlpha + ')';
      ctx.fill();
    });

    // Mouse cursor halo
    if (isActive) {
      // Outer ring
      var ring = ctx.createRadialGradient(mouse.tx, mouse.ty, 0, mouse.tx, mouse.ty, 150);
      ring.addColorStop(0, 'rgba(' + accent + ',0.04)');
      ring.addColorStop(0.5, 'rgba(' + accent + ',0.02)');
      ring.addColorStop(1, 'rgba(' + accent + ',0)');
      ctx.beginPath();
      ctx.arc(mouse.tx, mouse.ty, 150, 0, Math.PI * 2);
      ctx.fillStyle = ring;
      ctx.fill();

      // Bright center
      var core = ctx.createRadialGradient(mouse.tx, mouse.ty, 0, mouse.tx, mouse.ty, 30);
      core.addColorStop(0, 'rgba(' + accent + ',0.08)');
      core.addColorStop(1, 'rgba(' + accent + ',0)');
      ctx.beginPath();
      ctx.arc(mouse.tx, mouse.ty, 30, 0, Math.PI * 2);
      ctx.fillStyle = core;
      ctx.fill();

      // Faint crosshair
      ctx.strokeStyle = 'rgba(' + accent + ',0.06)';
      ctx.lineWidth = 0.5;
      ctx.beginPath();
      ctx.arc(mouse.tx, mouse.ty, 8, 0, Math.PI * 2);
      ctx.stroke();
    }

    requestAnimationFrame(draw);
  }

  document.addEventListener('mousemove', function(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  document.addEventListener('mouseleave', function() {
    mouse.x = -9999;
    mouse.y = -9999;
  });

  draw();
}

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
    html += '<button class="filter-btn" data-filter="' + escapeHtml(cat) + '">' + escapeHtml(cat) + '</button>';
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
      return '<span class="prompt-model-icon">' + escapeHtml(m) + '</span>';
    }).join('');

    return '<div class="prompt-card reveal" style="transition-delay:' + (i * 0.06) + 's" onclick="openPromptModal(' + p.id + ')">' +
      '<div class="prompt-card-top">' +
        '<span class="prompt-category-tag">' + escapeHtml(p.category) + '</span>' +
        '<span class="prompt-model-icons">' + modelIcons + '</span>' +
      '</div>' +
      '<h3 class="prompt-card-title">' + escapeHtml(p.title) + '</h3>' +
      '<p class="prompt-card-desc">' + escapeHtml(p.description) + '</p>' +
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
    return '<span class="modal-model-tag">' + escapeHtml(m) + '</span>';
  }).join('');

  var bodyHtml =
    '<h2 class="modal-title">' + escapeHtml(prompt.title) + '</h2>' +
    '<span class="modal-category">' + escapeHtml(prompt.category) + '</span>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">📝 Prompt 正文</div>' +
      '<div class="modal-prompt-block">' + escapeHtml(prompt.prompt) + '</div>' +
    '</div>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">🎯 使用场景</div>' +
      '<div class="modal-section-text">' + escapeHtml(prompt.useCase) + '</div>' +
    '</div>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">🤖 适用模型</div>' +
      '<div class="modal-model-list">' + modelTags + '</div>' +
    '</div>' +
    '<div class="modal-section">' +
      '<div class="modal-section-label">💡 使用小贴士</div>' +
      '<div class="modal-section-text">' + escapeHtml(prompt.tips) + '</div>' +
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
  if (!modal) return;
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

// ── Init ──
document.addEventListener('DOMContentLoaded', function() {
  if (window.siteData) renderTimeline();
  renderFilters();
  renderArticles();
  renderProjects();
  loadPrompts();
  initBgParticles();
});
