# parts/app_logic.py
# Production Vanilla JavaScript Application Engine for MPSeDC Modernized Portal
# Embedded into <script> tag - Zero external libraries required

APP_LOGIC_JS = """
// ==========================================================================
// MPSeDC Modernized Portal - Complete Interactive Logic
// ==========================================================================

(function() {
  'use strict';

  // Global State Containers
  window.APP_STATE = {
    lang: localStorage.getItem('mpsedc_lang') || 'en',
    fontSize: localStorage.getItem('mpsedc_font_size') || 'md',
    highContrast: localStorage.getItem('mpsedc_contrast') === 'true',
    currentHeroSlide: 1,
    heroAutoPlayInterval: null,
    heroPaused: false,
    projectFilter: 'All',
    tenderSearch: '',
    tenderCategory: 'All',
    tenderStatus: 'All',
    tenderPage: 1,
    tenderPageSize: 5,
    selectedItPark: 'bhopal',
    newsCategory: 'all',
    newsArchived: false,
    searchDebounceTimer: null
  };

  // --------------------------------------------------------------------------
  // 1. INITIALIZATION & LIFECYCLE
  // --------------------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', function() {
    initAccessibilitySettings();
    initLanguage();
    initHeroCarousel();
    initStatsObserver();
    renderProjects(APP_STATE.projectFilter);
    renderTenders();
    selectItPark(APP_STATE.selectedItPark);
    renderPolicies();
    renderUpdates();
    initKeyboardShortcuts();
    initScrollHeader();

    // Set dynamic last updated timestamp in IST
    const lastUp = document.getElementById('portal-last-updated');
    if (lastUp) {
      const now = new Date();
      lastUp.textContent = now.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' }) + ' ' +
                           now.toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', hour12: false }) + ' IST';
    }
  });

  // --------------------------------------------------------------------------
  // 2. ACCESSIBILITY & DISPLAY PREFERENCES
  // --------------------------------------------------------------------------
  function initAccessibilitySettings() {
    // Font scale
    setFontSize(APP_STATE.fontSize, false);

    // High contrast
    if (APP_STATE.highContrast) {
      document.body.classList.add('contrast-mode');
    }
  }

  window.setFontSize = function(size, save = true) {
    APP_STATE.fontSize = size;
    const root = document.documentElement;
    if (size === 'sm') {
      root.style.fontSize = '14px';
    } else if (size === 'lg') {
      root.style.fontSize = '18px';
    } else {
      root.style.fontSize = '16px';
    }

    document.querySelectorAll('.font-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    const activeBtn = document.getElementById('btn-font-' + size);
    if (activeBtn) activeBtn.classList.add('active');

    if (save) {
      localStorage.setItem('mpsedc_font_size', size);
      showToast('Font scale updated to ' + size.toUpperCase(), 'info');
    }
  };

  window.toggleHighContrast = function() {
    APP_STATE.highContrast = !APP_STATE.highContrast;
    if (APP_STATE.highContrast) {
      document.body.classList.add('contrast-mode');
      showToast('High Contrast Mode Enabled', 'info');
    } else {
      document.body.classList.remove('contrast-mode');
      showToast('Standard Display Mode Enabled', 'info');
    }
    localStorage.setItem('mpsedc_contrast', APP_STATE.highContrast);
  };

  window.openScreenReaderModal = function() {
    openModal('modal-screen-reader');
  };

  // --------------------------------------------------------------------------
  // 3. BILINGUAL EXPERIENCE (ENGLISH & HINDI)
  // --------------------------------------------------------------------------
  function initLanguage() {
    applyLanguage(APP_STATE.lang);
  }

  window.toggleLanguage = function() {
    APP_STATE.lang = (APP_STATE.lang === 'en') ? 'hi' : 'en';
    localStorage.setItem('mpsedc_lang', APP_STATE.lang);
    applyLanguage(APP_STATE.lang);
    showToast(APP_STATE.lang === 'hi' ? 'भाषा हिन्दी में बदली गई' : 'Language switched to English', 'success');
  };

  function applyLanguage(lang) {
    document.documentElement.lang = lang;
    const dict = BILINGUAL_DATA[lang] || BILINGUAL_DATA['en'];
    
    // Update elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        if (el.tagName === 'INPUT' && el.getAttribute('placeholder')) {
          el.setAttribute('placeholder', dict[key]);
        } else {
          el.textContent = dict[key];
        }
      }
    });

    // Update Language Toggle Button Indicator
    const indicator = document.getElementById('lang-indicator');
    if (indicator) {
      indicator.textContent = (lang === 'en') ? 'हिन्दी' : 'English';
    }

    // Re-render dynamic components with appropriate language
    renderProjects(APP_STATE.projectFilter);
    renderTenders();
    selectItPark(APP_STATE.selectedItPark);
    renderPolicies();
    renderUpdates();
  }

  // --------------------------------------------------------------------------
  // 4. HEADER NAVIGATION & MOBILE DRAWER
  // --------------------------------------------------------------------------
  function initScrollHeader() {
    const header = document.getElementById('site-header');
    const backToTop = document.getElementById('btn-back-to-top');

    window.addEventListener('scroll', function() {
      if (window.scrollY > 40) {
        if (header) header.classList.add('scrolled');
      } else {
        if (header) header.classList.remove('scrolled');
      }

      if (window.scrollY > 400) {
        if (backToTop) backToTop.classList.add('visible');
      } else {
        if (backToTop) backToTop.classList.remove('visible');
      }
    });
  }

  window.toggleMobileDrawer = function() {
    const drawer = document.getElementById('mobile-drawer');
    const backdrop = document.getElementById('drawer-backdrop');
    const btn = document.getElementById('mobile-hamburger-btn');
    if (drawer && backdrop) {
      const isOpen = drawer.classList.contains('open');
      if (isOpen) {
        drawer.classList.remove('open');
        backdrop.classList.remove('open');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      } else {
        drawer.classList.add('open');
        backdrop.classList.add('open');
        if (btn) btn.setAttribute('aria-expanded', 'true');
      }
    }
  };

  window.closeAllMegaMenus = function() {
    // Mega menus close automatically when links are clicked
  };

  window.scrollToSection = function(sectionId, filterParam = null) {
    const el = document.getElementById(sectionId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
    if (sectionId === 'projects' && filterParam) {
      filterProjects(filterParam);
    } else if (sectionId === 'tenders' && filterParam) {
      filterTenders(filterParam);
    } else if (sectionId === 'updates' && filterParam) {
      filterUpdatesTab(filterParam);
    }
  };

  window.scrollToTop = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // --------------------------------------------------------------------------
  // 5. HERO CAROUSEL INTERACTION
  // --------------------------------------------------------------------------
  function initHeroCarousel() {
    startHeroAutoPlay();
  }

  function startHeroAutoPlay() {
    if (APP_STATE.heroAutoPlayInterval) clearInterval(APP_STATE.heroAutoPlayInterval);
    APP_STATE.heroAutoPlayInterval = setInterval(function() {
      if (!APP_STATE.heroPaused) {
        let next = APP_STATE.currentHeroSlide + 1;
        if (next > 3) next = 1;
        goToHeroSlide(next, false);
      }
    }, 6000);
  }

  window.goToHeroSlide = function(slideIndex, resetTimer = true) {
    APP_STATE.currentHeroSlide = slideIndex;
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dot');

    slides.forEach(s => {
      const idx = parseInt(s.getAttribute('data-slide'));
      if (idx === slideIndex) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });

    dots.forEach((d, i) => {
      if (i + 1 === slideIndex) {
        d.classList.add('active');
        d.setAttribute('aria-selected', 'true');
      } else {
        d.classList.remove('active');
        d.setAttribute('aria-selected', 'false');
      }
    });

    if (resetTimer) startHeroAutoPlay();
  };

  window.nextHeroSlide = function() {
    let next = APP_STATE.currentHeroSlide + 1;
    if (next > 3) next = 1;
    goToHeroSlide(next);
  };

  window.prevHeroSlide = function() {
    let prev = APP_STATE.currentHeroSlide - 1;
    if (prev < 1) prev = 3;
    goToHeroSlide(prev);
  };

  window.toggleHeroAutoPlay = function() {
    APP_STATE.heroPaused = !APP_STATE.heroPaused;
    const btn = document.getElementById('btn-hero-pause');
    if (btn) {
      if (APP_STATE.heroPaused) {
        btn.innerHTML = SVG_ICONS['play'];
        btn.setAttribute('title', 'Resume Carousel Auto-play');
        showToast('Carousel Paused', 'info');
      } else {
        btn.innerHTML = SVG_ICONS['pause'];
        btn.setAttribute('title', 'Pause Carousel Auto-play');
        showToast('Carousel Resumed', 'info');
      }
    }
  };

  // --------------------------------------------------------------------------
  // 6. ANIMATED STATISTICS (INTERSECTION OBSERVER)
  // --------------------------------------------------------------------------
  function initStatsObserver() {
    const statsSection = document.getElementById('stats-section');
    if (!statsSection) return;

    let animated = false;
    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          animateStatCounters();
        }
      });
    }, { threshold: 0.25 });

    observer.observe(statsSection);
  }

  function animateStatCounters() {
    const counters = document.querySelectorAll('.stat-number');
    counters.forEach(counter => {
      const target = parseFloat(counter.getAttribute('data-target'));
      const suffix = counter.getAttribute('data-suffix') || '';
      const decimals = parseInt(counter.getAttribute('data-decimals') || '0');
      const duration = 1800; // ms
      const startTime = performance.now();

      function update(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Easing out cubic
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const current = target * easeOut;

        counter.textContent = current.toFixed(decimals) + suffix;

        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          counter.textContent = target.toFixed(decimals) + suffix;
        }
      }

      requestAnimationFrame(update);
    });
  }

  // --------------------------------------------------------------------------
  // 7. PROJECTS & TECHNOLOGY VERTICALS
  // --------------------------------------------------------------------------
  window.filterProjects = function(category) {
    APP_STATE.projectFilter = category;
    
    // Update active filter pill
    document.querySelectorAll('.filter-pill-btn').forEach(btn => {
      if (btn.textContent.includes(category) || (category === 'All' && btn.textContent.includes('All'))) {
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-selected', 'false');
      }
    });

    renderProjects(category);
  };

  function renderProjects(category) {
    const container = document.getElementById('projects-grid-container');
    if (!container) return;

    const filtered = (category === 'All') 
      ? PROJECTS_DATA 
      : PROJECTS_DATA.filter(p => p.category === category);

    const isHi = (APP_STATE.lang === 'hi');

    container.innerHTML = filtered.map(p => {
      const name = isHi ? p.name_hi : p.name;
      const iconSvg = SVG_ICONS[p.icon_key] || SVG_ICONS['cpu'];

      return `
        <article class="project-card">
          <div class="project-card-header">
            <div class="project-card-icon">${iconSvg}</div>
            <span class="project-tag-badge">${p.category}</span>
          </div>
          <div class="project-card-body">
            <h3 class="project-name">${name}</h3>
            <p class="project-desc">${p.short_desc}</p>
            <div style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 14px; font-weight: 500;">
              <strong>Key Metrics:</strong> ${p.impact_metrics}
            </div>
            <button type="button" class="btn btn-outline project-action-btn" onclick="openProjectModal('${p.id}')">
              <span>Know More</span>
              ${SVG_ICONS['arrow_right']}
            </button>
          </div>
        </article>
      `;
    }).join('');
  }

  window.openProjectModal = function(id) {
    const project = PROJECTS_DATA.find(p => p.id === id);
    if (!project) return;

    const isHi = (APP_STATE.lang === 'hi');
    const name = isHi ? project.name_hi : project.name;
    const body = document.getElementById('project-modal-body');
    const title = document.getElementById('project-modal-title');

    if (title) title.textContent = name;
    if (body) {
      body.innerHTML = `
        <div style="margin-bottom: 18px;">
          <span class="badge badge-live" style="margin-right: 8px;">${project.category}</span>
          <span class="badge badge-extended">Project Code: ${project.id}</span>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.6; color: var(--text-primary); margin-bottom: 16px;">
          ${project.full_desc}
        </p>
        <div style="background: var(--surface-alt); padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 16px;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            <div>
              <span style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Nodal Officer / Division</span>
              <div style="font-size: 0.95rem; font-weight: 600; color: var(--primary);">${project.nodal_officer}</div>
            </div>
            <div>
              <span style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">State-wide Impact Scope</span>
              <div style="font-size: 0.95rem; font-weight: 600; color: var(--secondary);">${project.impact_metrics}</div>
            </div>
          </div>
        </div>
        <div style="font-size: 0.85rem; color: var(--text-muted);">
          Official integration with MP State Portal and National e-Governance Division (NeGD) architecture.
        </div>
      `;
    }

    const footer = document.getElementById('project-modal-footer');
    if (footer) {
      let extBtn = '';
      if (project.live_url && project.live_url.startsWith('http')) {
        extBtn = `
          <a href="${project.live_url}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" onclick="notifyExternalLink(event, '${project.live_url}')" style="text-decoration:none;">
            <span>Launch Official Portal</span>
            ${SVG_ICONS['external']}
          </a>
        `;
      }
      footer.innerHTML = `
        <button type="button" class="btn btn-outline" onclick="closeModal('modal-project-details')">Close</button>
        ${extBtn}
      `;
    }

    openModal('modal-project-details');
  };

  // --------------------------------------------------------------------------
  // 8. INTERACTIVE TENDER & RFP HUB
  // --------------------------------------------------------------------------
  window.handleTenderSearchDebounced = function() {
    clearTimeout(APP_STATE.searchDebounceTimer);
    APP_STATE.searchDebounceTimer = setTimeout(function() {
      const input = document.getElementById('tender-search-input');
      APP_STATE.tenderSearch = input ? input.value.trim().toLowerCase() : '';
      APP_STATE.tenderPage = 1;
      renderTenders();
    }, 250);
  };

  window.applyTenderFilters = function() {
    const catSelect = document.getElementById('tender-cat-select');
    const statusSelect = document.getElementById('tender-status-select');
    
    APP_STATE.tenderCategory = catSelect ? catSelect.value : 'All';
    APP_STATE.tenderStatus = statusSelect ? statusSelect.value : 'All';
    APP_STATE.tenderPage = 1;
    renderTenders();
  };

  window.resetTenderFilters = function() {
    APP_STATE.tenderSearch = '';
    APP_STATE.tenderCategory = 'All';
    APP_STATE.tenderStatus = 'All';
    APP_STATE.tenderPage = 1;

    const sInput = document.getElementById('tender-search-input');
    const cSelect = document.getElementById('tender-cat-select');
    const stSelect = document.getElementById('tender-status-select');

    if (sInput) sInput.value = '';
    if (cSelect) cSelect.value = 'All';
    if (stSelect) stSelect.value = 'All';

    renderTenders();
    showToast('Tender filters reset', 'info');
  };

  window.filterTenders = function(category) {
    const cSelect = document.getElementById('tender-cat-select');
    if (cSelect) cSelect.value = category;
    APP_STATE.tenderCategory = category;
    APP_STATE.tenderPage = 1;
    renderTenders();
    scrollToSection('tenders');
  };

  function renderTenders() {
    const tbody = document.getElementById('tenders-table-body');
    if (!tbody) return;

    const isHi = (APP_STATE.lang === 'hi');

    // Filtering
    let list = TENDERS_DATA.filter(t => {
      const matchCat = (APP_STATE.tenderCategory === 'All') || (t.category === APP_STATE.tenderCategory);
      const matchStatus = (APP_STATE.tenderStatus === 'All') || (t.status === APP_STATE.tenderStatus);
      const titleStr = (isHi && t.title_hi ? t.title_hi : t.title).toLowerCase();
      const noStr = t.tender_no.toLowerCase();
      const matchSearch = (!APP_STATE.tenderSearch) || titleStr.includes(APP_STATE.tenderSearch) || noStr.includes(APP_STATE.tenderSearch);
      return matchCat && matchStatus && matchSearch;
    });

    const totalCount = list.length;
    const startIndex = (APP_STATE.tenderPage - 1) * APP_STATE.tenderPageSize;
    const pagedList = list.slice(startIndex, startIndex + APP_STATE.tenderPageSize);

    // Update Pagination Info
    const info = document.getElementById('tenders-pagination-info');
    if (info) {
      if (totalCount === 0) {
        info.textContent = 'No matching tenders found';
      } else {
        const end = Math.min(startIndex + APP_STATE.tenderPageSize, totalCount);
        info.textContent = `Showing ${startIndex + 1} to ${end} of ${totalCount} tenders`;
      }
    }

    renderTenderPaginationControls(totalCount);

    if (totalCount === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="5" style="text-align: center; padding: 36px; color: var(--text-muted);">
            No procurement records match your filter criteria. Try resetting filters.
          </td>
        </tr>
      `;
      return;
    }

    tbody.innerHTML = pagedList.map(t => {
      const title = (isHi && t.title_hi) ? t.title_hi : t.title;
      let statusBadge = `<span class="badge badge-live">Live</span>`;
      if (t.status === 'Extended') statusBadge = `<span class="badge badge-extended">Extended</span>`;
      else if (t.status === 'Closed') statusBadge = `<span class="badge badge-closed">Closed</span>`;
      else if (t.status === 'Cancelled') statusBadge = `<span class="badge badge-cancelled">Cancelled</span>`;
      else if (t.status === 'Archived') statusBadge = `<span class="badge badge-closed">Archived</span>`;

      const hasCorr = t.corrigendums && t.corrigendums.length > 0;
      const corrBadge = hasCorr ? `
        <button type="button" class="corrigendum-toggle-btn" onclick="toggleCorrigendumRow('${t.id}')" aria-expanded="false" id="btn-corr-${t.id}">
          <span>${t.corrigendums.length} Corrigendum(s)</span>
          ${SVG_ICONS['chevron_down']}
        </button>
      ` : '';

      // Deadline rendering
      let deadlineHtml = `<span>${t.submission_deadline}</span>`;
      if (t.original_deadline) {
        deadlineHtml = `
          <div class="date-original-struck">${t.original_deadline}</div>
          <div class="date-revised-highlight">${t.submission_deadline}</div>
        `;
      }

      // Main Row
      const mainRow = `
        <tr class="tender-parent-row" id="row-${t.id}">
          <td class="tender-id-cell">
            <span class="tender-ref-number">${t.tender_no}</span>
            <div style="margin-top: 4px;">${statusBadge}</div>
            <div style="margin-top: 6px;">${corrBadge}</div>
          </td>
          <td class="tender-title-cell">
            <strong>${title}</strong>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px; line-height: 1.4;">${t.description}</p>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 4px;">
              <span><strong>EMD:</strong> ${t.emd_val}</span> &nbsp;|&nbsp; <span><strong>Tender Fee:</strong> ${t.doc_fee}</span>
            </div>
          </td>
          <td>
            <span class="badge" style="background: var(--surface-alt); border: 1px solid var(--border); color: var(--text-secondary);">
              ${t.category}
            </span>
          </td>
          <td>${deadlineHtml}</td>
          <td>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              <button type="button" class="btn btn-sm btn-outline" onclick="openTenderModal('${t.id}')" style="white-space: nowrap;">
                View RFP
              </button>
              <button type="button" class="btn btn-sm btn-primary" onclick="simulateSpecDownload('${t.id}')" title="Download tender spec sheet">
                ${SVG_ICONS['download']}
                <span>Docs</span>
              </button>
            </div>
          </td>
        </tr>
      `;

      // Accordion Sub-row for Corrigendums
      let corrSubRow = '';
      if (hasCorr) {
        const corrItems = t.corrigendums.map(c => `
          <tr>
            <td><strong>${c.corrigendum_no}</strong></td>
            <td><code>${c.memo_no}</code></td>
            <td>${c.remarks}</td>
            <td style="color: var(--accent-hover); font-weight: 600;">${c.revised_deadline}</td>
            <td>
              <button type="button" class="btn btn-sm btn-outline" onclick="simulateDownload('${c.memo_no}.pdf')" style="padding: 4px 8px; font-size: 0.75rem;">
                ${SVG_ICONS['download']} ${c.file_size}
              </button>
            </td>
          </tr>
        `).join('');

        corrSubRow = `
          <tr class="corrigendum-row" id="corr-row-${t.id}">
            <td colspan="5">
              <div class="corrigendum-content-box">
                <h4 style="font-size: 0.9rem; margin-bottom: 8px; color: var(--primary);">Official Corrigendum History & Timeline Revisions</h4>
                <table class="corrigendum-table">
                  <thead>
                    <tr>
                      <th>Notice</th>
                      <th>Memo Number</th>
                      <th>Revision Remarks</th>
                      <th>Revised Deadline (IST)</th>
                      <th>Download</th>
                    </tr>
                  </thead>
                  <tbody>${corrItems}</tbody>
                </table>
              </div>
            </td>
          </tr>
        `;
      }

      return mainRow + corrSubRow;
    }).join('');
  }

  window.toggleCorrigendumRow = function(tenderId) {
    const row = document.getElementById('corr-row-' + tenderId);
    const btn = document.getElementById('btn-corr-' + tenderId);
    if (!row) return;

    if (row.classList.contains('open')) {
      row.classList.remove('open');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    } else {
      row.classList.add('open');
      if (btn) btn.setAttribute('aria-expanded', 'true');
    }
  };

  function renderTenderPaginationControls(totalItems) {
    const container = document.getElementById('tenders-pagination-buttons');
    if (!container) return;

    const totalPages = Math.ceil(totalItems / APP_STATE.tenderPageSize) || 1;
    let buttons = '';

    buttons += `
      <button type="button" class="page-btn" onclick="goToTenderPage(${APP_STATE.tenderPage - 1})" ${APP_STATE.tenderPage === 1 ? 'disabled' : ''}>
        Prev
      </button>
    `;

    for (let p = 1; p <= totalPages; p++) {
      buttons += `
        <button type="button" class="page-btn ${p === APP_STATE.tenderPage ? 'active' : ''}" onclick="goToTenderPage(${p})">
          ${p}
        </button>
      `;
    }

    buttons += `
      <button type="button" class="page-btn" onclick="goToTenderPage(${APP_STATE.tenderPage + 1})" ${APP_STATE.tenderPage === totalPages ? 'disabled' : ''}>
        Next
      </button>
    `;

    container.innerHTML = buttons;
  }

  window.goToTenderPage = function(page) {
    const list = TENDERS_DATA.filter(t => {
      const matchCat = (APP_STATE.tenderCategory === 'All') || (t.category === APP_STATE.tenderCategory);
      const matchStatus = (APP_STATE.tenderStatus === 'All') || (t.status === APP_STATE.tenderStatus);
      return matchCat && matchStatus;
    });
    const totalPages = Math.ceil(list.length / APP_STATE.tenderPageSize) || 1;
    if (page < 1 || page > totalPages) return;

    APP_STATE.tenderPage = page;
    renderTenders();
  };

  window.openTenderModal = function(id) {
    const tender = TENDERS_DATA.find(t => t.id === id);
    if (!tender) return;

    const isHi = (APP_STATE.lang === 'hi');
    const title = (isHi && tender.title_hi) ? tender.title_hi : tender.title;
    const body = document.getElementById('tender-modal-body');
    const modalTitle = document.getElementById('tender-modal-title');

    if (modalTitle) modalTitle.textContent = tender.tender_no;
    if (body) {
      const docsList = tender.documents.map(d => `
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; background: var(--surface-alt); border-radius: var(--radius-sm); border: 1px solid var(--border); margin-bottom: 8px;">
          <div>
            <strong>${d.name}</strong>
            <div style="font-size: 0.75rem; color: var(--text-muted);">${d.type} &bull; ${d.size}</div>
          </div>
          <button type="button" class="btn btn-sm btn-outline" onclick="simulateDownload('${d.name}')">
            ${SVG_ICONS['download']} Download
          </button>
        </div>
      `).join('');

      body.innerHTML = `
        <div style="margin-bottom: 16px;">
          <span class="badge badge-live">${tender.status}</span>
          <span class="badge" style="background: var(--surface-alt); border: 1px solid var(--border); color: var(--text-secondary); margin-left: 8px;">${tender.category}</span>
        </div>
        <h4 style="font-size: 1.15rem; margin-bottom: 12px; color: var(--primary);">${title}</h4>
        <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 16px;">
          ${tender.description}
        </p>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; background: #F8FAFC; padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 18px;">
          <div><span style="font-size: 0.8rem; color: var(--text-muted);">Published:</span><br><strong>${tender.published_date}</strong></div>
          <div><span style="font-size: 0.8rem; color: var(--text-muted);">Submission Deadline:</span><br><strong style="color: var(--accent-hover);">${tender.submission_deadline}</strong></div>
          <div><span style="font-size: 0.8rem; color: var(--text-muted);">Earnest Money Deposit (EMD):</span><br><strong>${tender.emd_val}</strong></div>
          <div><span style="font-size: 0.8rem; color: var(--text-muted);">Tender Document Fee:</span><br><strong>${tender.doc_fee}</strong></div>
        </div>
        <h5 style="margin-bottom: 10px; font-size: 0.95rem;">Available Tender Documents & BOQ Templates</h5>
        <div>${docsList}</div>
      `;
    }

    openModal('modal-tender-details');
  };

  // --------------------------------------------------------------------------
  // 9. IT PARKS & INFRASTRUCTURE MAP EXPLORER
  // --------------------------------------------------------------------------
  window.selectItPark = function(parkKey) {
    APP_STATE.selectedItPark = parkKey;
    const park = IT_PARKS_DATA[parkKey];
    if (!park) return;

    const isHi = (APP_STATE.lang === 'hi');
    const parkName = isHi ? park.name_hi : park.name;

    // Update active map pin styling
    document.querySelectorAll('.map-pin-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    const pin = document.getElementById('pin-' + parkKey);
    if (pin) pin.classList.add('active');

    // Update Dossier Card HTML
    const dossier = document.getElementById('itpark-dossier-card');
    if (dossier) {
      const tenantsHtml = park.key_tenants.map(t => `<span class="tenant-chip">${t}</span>`).join('');

      dossier.innerHTML = `
        <div class="dossier-header">
          <span class="dossier-district">District: ${park.district} &bull; Operational IT Cluster</span>
          <h3 class="dossier-title">${parkName}</h3>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">${park.description}</p>
        </div>

        <div class="dossier-specs-grid">
          <div class="spec-box">
            <span class="spec-box-label">Total Campus Area</span>
            <div class="spec-box-val">${park.total_area}</div>
          </div>
          <div class="spec-box">
            <span class="spec-box-label">Constructed Built-up</span>
            <div class="spec-box-val">${park.built_up}</div>
          </div>
          <div class="spec-box">
            <span class="spec-box-label">Immediate Vacant Space</span>
            <div class="spec-box-val" style="color: var(--status-live); font-weight: 700;">${park.available_space}</div>
          </div>
          <div class="spec-box">
            <span class="spec-box-label">Optical Fiber Rings</span>
            <div class="spec-box-val">${park.fiber_connectivity}</div>
          </div>
          <div class="spec-box" style="grid-column: 1 / -1;">
            <span class="spec-box-label">Power Reliability Specs</span>
            <div class="spec-box-val">${park.power_redundancy}</div>
          </div>
        </div>

        <div class="tenants-block">
          <span class="tenants-title">Key Operational Enterprise Tenants</span>
          <div class="tenant-badges-list">${tenantsHtml}</div>
        </div>

        <div style="margin-top: 22px; display: flex; gap: 10px;">
          <button type="button" class="btn btn-accent" onclick="openEoiModal('${parkKey}')" style="flex: 1;">
            Apply for Plot / Space EOI
          </button>
          <button type="button" class="btn btn-outline" onclick="simulateDownload('${parkKey}_Dossier_Specs.pdf')">
            ${SVG_ICONS['download']} Download Brochure
          </button>
        </div>
      `;
    }
  };

  window.openEoiModal = function(parkKey) {
    const park = IT_PARKS_DATA[parkKey || APP_STATE.selectedItPark];
    const parkInput = document.getElementById('eoi-park-name');
    if (parkInput && park) {
      parkInput.value = park.name;
    }
    openModal('modal-itpark-eoi');
  };

  window.handleEoiSubmit = function(e) {
    e.preventDefault();
    const company = document.getElementById('eoi-company-name').value;
    const refNo = 'EOI-MPSEDC-' + Math.floor(100000 + Math.random() * 900000);

    closeModal('modal-itpark-eoi');
    showToast(`EOI Reference ${refNo} submitted successfully for ${company}! Our Investment Promotion team will contact within 2 business days.`, 'success');
  };

  // --------------------------------------------------------------------------
  // 10. POLICIES & MINI INCENTIVE ESTIMATOR
  // --------------------------------------------------------------------------
  function renderPolicies() {
    const container = document.getElementById('policies-grid-container');
    if (!container) return;

    const isHi = (APP_STATE.lang === 'hi');

    container.innerHTML = POLICIES_DATA.map(pol => {
      const title = (isHi && pol.title_hi) ? pol.title_hi : pol.title;
      const highlightsHtml = pol.highlights.map(h => `<li>${h}</li>`).join('');

      const estimatorBtn = pol.has_estimator ? `
        <button type="button" class="btn btn-sm btn-accent" onclick="openIncentiveModal()" style="margin-top: 6px;">
          ${SVG_ICONS['cpu']} Calculate Incentives
        </button>
      ` : '';

      return `
        <article class="policy-card">
          <div class="policy-card-top">
            <span class="policy-category-tag">${pol.category}</span>
            <span class="policy-year-badge">${pol.year}</span>
          </div>
          <h3 class="policy-title">${title}</h3>
          <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.45; margin-bottom: 14px;">${pol.summary}</p>
          <ul class="policy-highlights-list">${highlightsHtml}</ul>
          
          <div class="policy-actions-group">
            <button type="button" class="btn btn-outline" onclick="openPolicyModal('${pol.id}')" style="flex: 1;">
              View Details
            </button>
            <button type="button" class="btn btn-primary" onclick="downloadPolicyPdf('${pol.id}')" title="Download Official PDF">
              ${SVG_ICONS['download']} ${pol.download_size}
            </button>
          </div>
          ${estimatorBtn}
        </article>
      `;
    }).join('');
  }

  window.openPolicyModal = function(id) {
    const pol = POLICIES_DATA.find(p => p.id === id);
    if (!pol) return;

    const isHi = (APP_STATE.lang === 'hi');
    const title = (isHi && pol.title_hi) ? pol.title_hi : pol.title;
    const body = document.getElementById('policy-modal-body');
    const modalTitle = document.getElementById('policy-modal-title');

    if (modalTitle) modalTitle.textContent = title;
    if (body) {
      const estimatorMarkup = pol.has_estimator ? getEstimatorMarkup() : '';

      body.innerHTML = `
        <div style="margin-bottom: 14px;">
          <span class="badge badge-live">${pol.category}</span>
          <span class="badge badge-extended" style="margin-left: 8px;">Notified Year: ${pol.year}</span>
        </div>
        <p style="font-size: 1rem; color: var(--text-primary); line-height: 1.6; margin-bottom: 16px;">
          ${pol.summary}
        </p>
        <div style="background: #F8FAFC; padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 20px;">
          <h4 style="font-size: 0.95rem; margin-bottom: 10px; color: var(--primary);">Key Statutory Incentive Provisions:</h4>
          <ul style="padding-left: 20px; font-size: 0.9rem; line-height: 1.7; color: var(--text-secondary);">
            ${pol.highlights.map(h => `<li>${h}</li>`).join('')}
          </ul>
        </div>
        ${estimatorMarkup}
      `;
    }

    openModal('modal-policy-details');
    if (pol.has_estimator) calculateIncentives();
  };

  window.openIncentiveModal = function() {
    openPolicyModal('POL-01');
  };

  function getEstimatorMarkup() {
    return `
      <div style="border: 2px solid var(--secondary); border-radius: var(--radius-md); padding: 20px; background: #FFFFFF; margin-top: 16px;">
        <h4 style="font-size: 1.1rem; color: var(--primary); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
          ${SVG_ICONS['cpu']} MP IT Policy 2023 - Mini Incentive Estimator
        </h4>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 16px;">
          Simulate statutory capital subsidy and recurring employment generation grants for your proposed investment.
        </p>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 16px;">
          <div>
            <label class="filter-label" for="calc-capex">Proposed Capex (₹ Cr) *</label>
            <input type="number" id="calc-capex" class="form-control-input" value="25" min="1" max="500" oninput="calculateIncentives()">
          </div>
          <div>
            <label class="filter-label" for="calc-jobs">Expected IT Jobs (Nos.) *</label>
            <input type="number" id="calc-jobs" class="form-control-input" value="150" min="10" max="10000" oninput="calculateIncentives()">
          </div>
          <div>
            <label class="filter-label" for="calc-area">Lease Space (Sq. Ft.) *</label>
            <input type="number" id="calc-area" class="form-control-input" value="20000" min="1000" max="500000" oninput="calculateIncentives()">
          </div>
        </div>

        <!-- Live Results Box -->
        <div style="background: var(--surface-alt); border-radius: var(--radius-md); padding: 16px; border: 1px solid var(--border);">
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; text-align: center;">
            <div style="padding: 10px; background: #FFFFFF; border-radius: var(--radius-sm); border: 1px solid var(--border);">
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Capital Subsidy (30%)</span>
              <div id="est-capex-sub" style="font-size: 1.25rem; font-weight: 700; color: var(--primary); margin-top: 4px;">₹ 7.50 Cr</div>
            </div>
            <div style="padding: 10px; background: #FFFFFF; border-radius: var(--radius-sm); border: 1px solid var(--border);">
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Jobs Grant (5 Yrs)</span>
              <div id="est-jobs-sub" style="font-size: 1.25rem; font-weight: 700; color: var(--secondary); margin-top: 4px;">₹ 75.00 L</div>
            </div>
            <div style="padding: 10px; background: #FFFFFF; border-radius: var(--radius-sm); border: 1px solid var(--border);">
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Duty Waiver</span>
              <div id="est-duty-sub" style="font-size: 1.25rem; font-weight: 700; color: var(--status-live); margin-top: 4px;">100% Free</div>
            </div>
          </div>
          <div style="text-align: center; margin-top: 14px; padding-top: 10px; border-top: 1px dashed var(--border);">
            <span style="font-size: 0.85rem; color: var(--text-secondary); font-weight: 600;">Total Estimated State Benefit: </span>
            <strong id="est-total-benefit" style="font-size: 1.35rem; color: var(--accent); margin-left: 6px;">₹ 8.25 Cr</strong>
            <small style="display: block; font-size: 0.72rem; color: var(--text-muted); margin-top: 4px;">*Subject to high-level committee review and terms of MP IT Policy 2023 Gazette.</small>
          </div>
        </div>
      </div>
    `;
  }

  window.calculateIncentives = function() {
    const capexInput = document.getElementById('calc-capex');
    const jobsInput = document.getElementById('calc-jobs');

    if (!capexInput || !jobsInput) return;

    const capex = parseFloat(capexInput.value) || 0;
    const jobs = parseInt(jobsInput.value) || 0;

    // 30% of Capex, capped at ₹ 30 Cr
    const capexSub = Math.min(capex * 0.30, 30.0);
    // ₹ 10,000 per person per year for 5 years = ₹ 50,000 per person
    const jobsSubInLakhs = (jobs * 10000 * 5) / 100000;
    const jobsSubInCr = jobsSubInLakhs / 100;

    const totalCr = capexSub + jobsSubInCr;

    const elCapex = document.getElementById('est-capex-sub');
    const elJobs = document.getElementById('est-jobs-sub');
    const elTotal = document.getElementById('est-total-benefit');

    if (elCapex) elCapex.textContent = `₹ ${capexSub.toFixed(2)} Cr`;
    if (elJobs) elJobs.textContent = `₹ ${jobsSubInLakhs.toFixed(2)} L`;
    if (elTotal) elTotal.textContent = `₹ ${totalCr.toFixed(2)} Cr`;
  };

  window.downloadPolicyPdf = function(id) {
    const pol = POLICIES_DATA.find(p => p.id === id);
    const filename = pol ? pol.title.replace(/[^a-zA-Z0-9]/g, '_') + '.pdf' : 'MP_Policy_Document.pdf';
    simulateDownload(filename);
  };

  // --------------------------------------------------------------------------
  // 11. NEWS, RECRUITMENT & CIRCULARS
  // --------------------------------------------------------------------------
  window.filterUpdatesTab = function(category, btnElement = null) {
    APP_STATE.newsCategory = category;
    
    document.querySelectorAll('.update-tab-btn').forEach(btn => {
      btn.classList.remove('active');
      btn.setAttribute('aria-selected', 'false');
    });

    const targetBtn = btnElement || document.querySelector(`.update-tab-btn[data-tab="${category}"]`);
    if (targetBtn) {
      targetBtn.classList.add('active');
      targetBtn.setAttribute('aria-selected', 'true');
    }

    renderUpdates();
  };

  window.toggleArchiveUpdates = function(isArchived) {
    APP_STATE.newsArchived = isArchived;
    renderUpdates();
    showToast(isArchived ? 'Showing Archived Notices' : 'Showing Active Announcements', 'info');
  };

  function renderUpdates() {
    const container = document.getElementById('updates-list-container');
    if (!container) return;

    const isHi = (APP_STATE.lang === 'hi');

    let list = UPDATES_DATA.filter(u => {
      const matchArchive = u.is_archived === APP_STATE.newsArchived;
      const matchCat = (APP_STATE.newsCategory === 'all') || (u.category === APP_STATE.newsCategory);
      return matchArchive && matchCat;
    });

    if (list.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 36px; color: var(--text-muted);">
          No notices found in this category. Toggle archive switch to view historical records.
        </div>
      `;
      return;
    }

    container.innerHTML = list.map(item => {
      const title = (isHi && item.title_hi) ? item.title_hi : item.title;
      let catBadge = `<span class="update-meta-badge" style="background: rgba(23, 105, 170, 0.1); color: var(--secondary);">${item.category.toUpperCase()}</span>`;

      return `
        <div class="update-item-row" id="update-item-${item.id}">
          <div class="update-item-header" onclick="toggleUpdateAccordion('${item.id}')">
            <span class="update-date-badge">${item.date}</span>
            <div class="update-title-col">
              <span class="update-title-text">${title}</span>
              <div style="margin-top: 4px;">
                ${catBadge}
                <span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 8px;">Memo: <code>${item.memo_no}</code></span>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <button type="button" class="btn btn-sm btn-outline" onclick="event.stopPropagation(); simulateDownload('${item.memo_no}.pdf')">
                ${SVG_ICONS['download']} ${item.file_size}
              </button>
              <span class="chevron" style="display: inline-block; transition: transform 0.2s;">${SVG_ICONS['chevron_down']}</span>
            </div>
          </div>
          <div class="update-expandable-body">
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 8px;">
              ${item.description}
            </p>
            <div style="font-size: 0.75rem; color: var(--text-muted);">
              Notice published under authority of Managing Director, MPSeDC. Issued in Bhopal on ${item.date}.
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  window.toggleUpdateAccordion = function(id) {
    const item = document.getElementById('update-item-' + id);
    if (!item) return;

    if (item.classList.contains('expanded')) {
      item.classList.remove('expanded');
    } else {
      item.classList.add('expanded');
    }
  };

  // --------------------------------------------------------------------------
  // 12. GLOBAL SMART SEARCH (CTRL + K)
  // --------------------------------------------------------------------------
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
        e.preventDefault();
        openSearchModal();
      } else if (e.key === 'Escape') {
        closeAllModals();
      }
    });
  }

  window.openSearchModal = function() {
    openModal('modal-global-search');
    const input = document.getElementById('global-search-input');
    if (input) {
      input.value = '';
      setTimeout(() => input.focus(), 150);
    }
  };

  window.closeSearchModal = function() {
    closeModal('modal-global-search');
  };

  window.handleGlobalSearchDebounced = function() {
    clearTimeout(APP_STATE.searchDebounceTimer);
    APP_STATE.searchDebounceTimer = setTimeout(performGlobalSearch, 200);
  };

  function performGlobalSearch() {
    const input = document.getElementById('global-search-input');
    const container = document.getElementById('search-results-container');
    if (!input || !container) return;

    const query = input.value.trim().toLowerCase();
    if (query.length < 2) {
      container.innerHTML = `
        <div class="search-empty-state text-center" style="padding: 24px; color: var(--text-muted);">
          Type at least 2 characters to search across Tenders, Policies, Projects, and News.
        </div>
      `;
      return;
    }

    const results = [];

    // Search Projects
    PROJECTS_DATA.forEach(p => {
      if (p.name.toLowerCase().includes(query) || p.short_desc.toLowerCase().includes(query)) {
        results.push({
          category: 'Project Vertical',
          title: p.name,
          desc: p.short_desc,
          action: () => { closeSearchModal(); openProjectModal(p.id); }
        });
      }
    });

    // Search Tenders
    TENDERS_DATA.forEach(t => {
      if (t.title.toLowerCase().includes(query) || t.tender_no.toLowerCase().includes(query)) {
        results.push({
          category: 'Tender / RFP',
          title: `${t.tender_no}: ${t.title}`,
          desc: `Status: ${t.status} | Deadline: ${t.submission_deadline}`,
          action: () => { closeSearchModal(); openTenderModal(t.id); }
        });
      }
    });

    // Search Policies
    POLICIES_DATA.forEach(pol => {
      if (pol.title.toLowerCase().includes(query) || pol.category.toLowerCase().includes(query)) {
        results.push({
          category: 'Policy & Incentive',
          title: pol.title,
          desc: pol.summary,
          action: () => { closeSearchModal(); openPolicyModal(pol.id); }
        });
      }
    });

    // Search IT Parks
    Object.keys(IT_PARKS_DATA).forEach(k => {
      const park = IT_PARKS_DATA[k];
      if (park.name.toLowerCase().includes(query) || park.district.toLowerCase().includes(query)) {
        results.push({
          category: 'IT Park Infrastructure',
          title: park.name,
          desc: `District: ${park.district} | Vacant: ${park.available_space}`,
          action: () => { closeSearchModal(); scrollToSection('itparks'); selectItPark(k); }
        });
      }
    });

    // Search News & Notices
    UPDATES_DATA.forEach(u => {
      if (u.title.toLowerCase().includes(query) || u.memo_no.toLowerCase().includes(query)) {
        results.push({
          category: 'News & Recruitment',
          title: u.title,
          desc: `Date: ${u.date} | Memo: ${u.memo_no}`,
          action: () => { closeSearchModal(); scrollToSection('updates'); }
        });
      }
    });

    // Render results with <mark> highlighting
    if (results.length === 0) {
      container.innerHTML = `
        <div class="search-empty-state text-center" style="padding: 24px; color: var(--text-muted);">
          No results found for "<strong>${escapeHtml(query)}</strong>". Try broader keywords.
        </div>
      `;
      return;
    }

    container.innerHTML = results.slice(0, 8).map((r, i) => {
      const highlightedTitle = highlightKeyword(r.title, query);
      const highlightedDesc = highlightKeyword(r.desc, query);

      return `
        <div class="search-result-item" onclick="executeSearchResult(${i})" style="padding: 10px 14px; border-bottom: 1px solid var(--border); cursor: pointer; transition: background 0.15s;" onmouseover="this.style.background='var(--surface-alt)'" onmouseout="this.style.background='transparent'">
          <span class="search-result-cat" style="font-size: 0.72rem; text-transform: uppercase; font-weight: 700; color: var(--secondary);">${r.category}</span>
          <div class="search-result-title" style="font-size: 0.95rem; font-weight: 600; color: var(--text-primary); margin-top: 2px;">${highlightedTitle}</div>
          <div class="search-result-meta" style="font-size: 0.8rem; color: var(--text-muted); margin-top: 2px;">${highlightedDesc}</div>
        </div>
      `;
    }).join('');

    window._currentSearchResults = results;
  }

  window.executeSearchResult = function(index) {
    if (window._currentSearchResults && window._currentSearchResults[index]) {
      window._currentSearchResults[index].action();
    }
  };

  function highlightKeyword(text, keyword) {
    if (!text || !keyword) return text;
    const regex = new RegExp(`(${escapeRegExp(keyword)})`, 'gi');
    return text.replace(regex, '<mark style="background: rgba(242, 155, 56, 0.35); padding: 0 2px; border-radius: 2px;">$1</mark>');
  }

  function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
  }

  function escapeHtml(string) {
    return string.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // --------------------------------------------------------------------------
  // 13. CMS WORKFLOW SIMULATOR (MAKER-CHECKER-PUBLISHER)
  // --------------------------------------------------------------------------
  window.openCmsModal = function() {
    openModal('modal-cms-preview');
  };

  window.simulateCmsApprove = function() {
    const makerBox = document.getElementById('workflow-maker-box');
    const checkerBox = document.getElementById('workflow-checker-box');
    const publisherBox = document.getElementById('workflow-publisher-box');

    if (checkerBox) {
      checkerBox.style.background = '#FFFFFF';
      checkerBox.querySelector('.badge').className = 'badge badge-live';
      checkerBox.querySelector('.badge').textContent = 'Approved';
    }

    if (publisherBox) {
      publisherBox.style.background = 'rgba(15, 118, 110, 0.08)';
      publisherBox.style.borderColor = 'var(--status-live)';
      publisherBox.querySelector('.badge').className = 'badge badge-live';
      publisherBox.querySelector('.badge').textContent = 'DSC Signed & Published';
    }

    setTimeout(function() {
      closeModal('modal-cms-preview');
      showToast('Corrigendum Approved, Digitally Signed & Broadcast to Portal!', 'success');
      // Expand corrigendum in live table
      toggleCorrigendumRow('TND-2026-001');
      scrollToSection('tenders');
    }, 900);
  };

  // --------------------------------------------------------------------------
  // 14. MODAL SYSTEM & MISCELLANEOUS ACTIONS
  // --------------------------------------------------------------------------
  window.openModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.add('open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  };

  function closeAllModals() {
    document.querySelectorAll('.modal-overlay.open').forEach(m => {
      m.classList.remove('open');
      m.setAttribute('aria-hidden', 'true');
    });
    document.body.style.overflow = '';
  }

  window.openOfficersModal = function() {
    const body = document.getElementById('project-modal-body');
    const title = document.getElementById('project-modal-title');
    const footer = document.getElementById('project-modal-footer');

    if (title) title.textContent = "MPSeDC Key Officers & Leadership Directory";
    if (footer) {
      footer.innerHTML = `<button type="button" class="btn btn-outline" onclick="closeModal('modal-project-details')">Close</button>`;
    }
    if (body) {
      const rows = OFFICERS_DATA.map(o => `
        <tr style="border-bottom: 1px solid var(--border);">
          <td style="padding: 10px 14px; font-weight: 600; color: var(--primary);">${o.name}</td>
          <td style="padding: 10px 14px;">${o.dept}</td>
          <td style="padding: 10px 14px;"><code>${o.phone}</code></td>
          <td style="padding: 10px 14px;"><a href="mailto:${o.email}" style="color: var(--secondary);">${o.email}</a></td>
        </tr>
      `).join('');

      body.innerHTML = `
        <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
          Statutory executive contact directory for Madhya Pradesh State Electronics Development Corporation Ltd.
        </p>
        <div class="table-responsive">
          <table class="tender-table" style="font-size: 0.85rem;">
            <thead>
              <tr>
                <th>Designation</th>
                <th>Department / Portfolio</th>
                <th>Telephone</th>
                <th>Official Email</th>
              </tr>
            </thead>
            <tbody>${rows}</tbody>
          </table>
        </div>
      `;
    }

    openModal('modal-project-details');
  };

  window.openRtiModal = function() {
    const body = document.getElementById('project-modal-body');
    const title = document.getElementById('project-modal-title');
    const footer = document.getElementById('project-modal-footer');

    if (title) title.textContent = "Right to Information (RTI) Statutory Disclosures";
    if (footer) {
      footer.innerHTML = `<button type="button" class="btn btn-outline" onclick="closeModal('modal-project-details')">Close</button>`;
    }
    if (body) {
      body.innerHTML = `
        <div style="padding: 16px; background: #F8FAFC; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 16px;">
          <h4 style="font-size: 1rem; color: var(--primary); margin-bottom: 8px;">Proactive Disclosure under Section 4(1)(b) of RTI Act 2005</h4>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            MPSeDC maintains full transparency regarding public funds, tender awards, recruitments, and corporate governance.
          </p>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
          <div style="padding: 12px; border: 1px solid var(--border); border-radius: var(--radius-sm);">
            <strong>Public Information Officer (PIO)</strong><br>
            <span style="font-size: 0.85rem; color: var(--text-secondary);">General Manager (Administration)<br>Phone: +91-755-2518350<br>Email: pio@mpsedc.com</span>
          </div>
          <div style="padding: 12px; border: 1px solid var(--border); border-radius: var(--radius-sm);">
            <strong>First Appellate Authority (FAA)</strong><br>
            <span style="font-size: 0.85rem; color: var(--text-secondary);">Chief General Manager, MPSeDC<br>Phone: +91-755-2518310<br>Email: faa@mpsedc.com</span>
          </div>
        </div>
        <button type="button" class="btn btn-outline" onclick="simulateDownload('MPSeDC_RTI_Section_4_Disclosure.pdf')">
          ${SVG_ICONS['download']} Download Complete Section 4 Manual (PDF)
        </button>
      `;
    }

    openModal('modal-project-details');
  };

  window.openLegalModal = function(policyType) {
    const body = document.getElementById('project-modal-body');
    const title = document.getElementById('project-modal-title');
    const footer = document.getElementById('project-modal-footer');

    const titles = {
      privacy: 'Privacy Policy & Data Protection',
      copyright: 'Copyright & Intellectual Property Policy',
      disclaimer: 'Disclaimer & Limitation of Liability',
      hyperlinking: 'Hyperlinking Guidelines',
      sitemap: 'Interactive Portal Sitemap'
    };

    if (title) title.textContent = titles[policyType] || 'Government Legal Policy';
    if (footer) {
      footer.innerHTML = `<button type="button" class="btn btn-outline" onclick="closeModal('modal-project-details')">Close</button>`;
    }
    if (body) {
      body.innerHTML = `
        <div style="font-size: 0.95rem; line-height: 1.7; color: var(--text-secondary);">
          <p>
            This portal is maintained by <strong>Madhya Pradesh State Electronics Development Corporation Ltd. (MPSeDC)</strong>, a Government of Madhya Pradesh Undertaking.
          </p>
          <p>
            All contents are reviewed for accuracy in compliance with GIGW 3.0 and UX4G guidelines. Information provided does not constitute formal legal counsel. For statutory disputes, original official gazette notifications take precedence.
          </p>
          <div style="margin-top: 16px; padding: 12px; background: var(--surface-alt); border-radius: var(--radius-sm);">
            <strong>Governing Jurisdiction:</strong> High Court of Madhya Pradesh at Jabalpur / Principal Bench Bhopal.
          </div>
        </div>
      `;
    }

    openModal('modal-project-details');
  };

  window.openAboutModal = function() {
    const isHi = (APP_STATE.lang === 'hi');
    const body = document.getElementById('project-modal-body');
    const title = document.getElementById('project-modal-title');
    const footer = document.getElementById('project-modal-footer');

    if (title) {
      title.textContent = isHi 
        ? "एमपीएसईडीसी - कॉर्पोरेट परिचय एवं अधिदेश" 
        : "About MPSeDC - Corporate Profile & Mandate";
    }

    if (body) {
      body.innerHTML = `
        <div style="margin-bottom: 18px;">
          <span class="badge badge-live" style="margin-right: 8px;">Established 1983</span>
          <span class="badge badge-extended">Government of Madhya Pradesh Undertaking</span>
        </div>
        <p style="font-size: 1.05rem; line-height: 1.6; color: var(--text-primary); margin-bottom: 16px;">
          <strong>Madhya Pradesh State Electronics Development Corporation Ltd. (MPSeDC)</strong> was incorporated in 1983 under the Companies Act, 1956. Operating as the premier nodal agency under the <strong>Department of Science & Technology, Government of Madhya Pradesh</strong>, MPSeDC leads the execution of large-scale e-governance architectures, state digital backbones, and electronics manufacturing ecosystems.
        </p>

        <div style="background: var(--surface-alt); padding: 18px; border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 18px;">
          <h4 style="font-size: 1rem; color: var(--primary); margin-bottom: 10px;">Core Mandates & Sovereign Pillars:</h4>
          <ul style="padding-left: 20px; font-size: 0.9rem; line-height: 1.8; color: var(--text-secondary);">
            <li><strong>State Data Center (SDC):</strong> Managing the central Tier-IV cloud compute & storage repository delivering secure hosting to 50+ government departments.</li>
            <li><strong>MPSWAN Telecom Network:</strong> Operating the state optical fiber communication arterial connecting all 55 district collectorates and 350+ blocks.</li>
            <li><strong>IT Parks & Clusters:</strong> Development, maintenance, and investor land allotment across Bhopal, Indore, Jabalpur, Gwalior, and EMC Malanpur.</li>
            <li><strong>Investment Promotion:</strong> Single-window evaluation and statutory subsidy disbursement under MP IT, ITeS & ESDM Policy 2023.</li>
            <li><strong>Cyber Security & Standards:</strong> Operating MP-CERT for 24x7 incident response, security audits, and state data sovereignty enforcement.</li>
            <li><strong>Public Testing Labs (ETDC):</strong> NABL-accredited precision environmental, EMI/EMC, and safety testing for electronics and telecom equipment.</li>
          </ul>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; background: #FFFFFF; padding: 14px; border: 1px solid var(--border); border-radius: var(--radius-md); margin-bottom: 12px;">
          <div>
            <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Corporate Headquarters</span>
            <div style="font-size: 0.88rem; color: var(--text-primary); margin-top: 4px;">State IT Centre, 47-A, Arera Hills, Bhopal – 462011</div>
          </div>
          <div>
            <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Administrative Department</span>
            <div style="font-size: 0.88rem; color: var(--text-primary); margin-top: 4px;">Dept. of Science & Technology, Govt. of MP</div>
          </div>
        </div>
      `;
    }

    if (footer) {
      footer.innerHTML = `
        <button type="button" class="btn btn-outline" onclick="closeModal('modal-project-details')">Close</button>
        <a href="https://mpsedc.mp.gov.in/" target="_blank" rel="noopener noreferrer" class="btn btn-primary" onclick="notifyExternalLink(event, 'https://mpsedc.mp.gov.in/')" style="text-decoration:none;">
          <span>Visit Official Portal (mpsedc.mp.gov.in)</span>
          ${SVG_ICONS['external']}
        </a>
      `;
    }

    openModal('modal-project-details');
  };

  window.notifyExternalLink = function(event, url) {
    showToast(`External Website Notice: Navigating to ${url} (in accordance with GIGW 3.0 guidelines)`, 'info');
  };

  window.simulateDownload = function(fileName) {
    showToast(`Downloading: ${fileName} [Mock File Triggered]`, 'info');
  };

  window.simulateSpecDownload = function(tenderId) {
    showToast(`Generating tender specification package for ${tenderId || 'TND-2026'}... (ZIP)`, 'success');
  };

  window.showToast = function(msg, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-msg toast-${type}`;
    toast.innerHTML = `
      <div style="display: flex; align-items: center; gap: 8px;">
        <span>${type === 'success' ? '✓' : 'ℹ'}</span>
        <span>${msg}</span>
      </div>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(() => toast.remove(), 250);
    }, 3500);
  };

})();
"""
