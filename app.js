// ── Config ──
var langMap = {
  'typescript': 'ts', 'javascript': 'js', 'python': 'py', 'rust': 'rs',
  'shell': 'sh', 'go': 'go', 'jupyter notebook': 'py', 'c#': 'cs',
  'swift': 'rs', 'ruby': 'rb', 'kotlin': 'kt', 'java': 'java',
  'c++': 'cpp', 'c': 'c', 'haskell': 'hs', 'lua': 'lua',
  'zig': 'zig', 'solidity': 'sol'
};

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
      '<p class="card-excerpt">' + a.excerpt + '</p>' +
      '<div class="card-footer">' +
        '<span class="card-read">阅读全文 →</span>' +
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

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  var count = Math.min(Math.floor(canvas.width * canvas.height / 8000), 150);
  for (var i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      r: Math.random() * 2 + 1
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var color = isDark ? '255,140,66' : '200,100,50';

    particles.forEach(function(p) {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) p.x = canvas.width;
      if (p.x > canvas.width) p.x = 0;
      if (p.y < 0) p.y = canvas.height;
      if (p.y > canvas.height) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(' + color + ',0.15)';
      ctx.fill();
    });

    // Mouse connections
    particles.forEach(function(p) {
      var dx = p.x - mouse.x;
      var dy = p.y - mouse.y;
      var dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 180) {
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(mouse.x, mouse.y);
        ctx.strokeStyle = 'rgba(' + color + ',' + (0.08 * (1 - dist / 180)) + ')';
        ctx.lineWidth = 0.8;
        ctx.stroke();
      }
    });

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
  initBgParticles();
});
