# parts/dom_markup.py
# Semantic HTML5 DOM Markup Structure for MPSeDC Modernized Portal
# Embedded and organized into structured component strings

from parts.svg_assets import (
  MPSEDC_LOGO_SVG,
  LION_CAPITAL_EMBLEM_SVG,
  MP_MAP_SVG,
  ISOMETRIC_DIGITAL_HUB_SVG,
  HERO_TOPOLOGY_SVG,
  SVG_ICONS
)

TOP_UTILITY_BAR_MARKUP = f"""<!-- TOP UTILITY BAR (GIGW 3.0 & ACCESSIBILITY) -->
<aside class="top-utility-bar" aria-label="Accessibility and Language Controls">
  <div class="container top-bar-controls">
    <div class="gov-branding-tag">
      {LION_CAPITAL_EMBLEM_SVG}
      <span class="state-gov-title" data-i18n="state_gov_tag">Government of Madhya Pradesh | Dept. of Science & Technology</span>
    </div>

    <div class="top-control-group">
      <a href="#main-content" class="skip-link" data-i18n="skip_to_content">Skip to Main Content</a>
      
      <button type="button" class="top-btn" id="btn-screen-reader" onclick="openScreenReaderModal()" title="Screen Reader Access information" aria-label="Screen Reader Access">
        {SVG_ICONS['info']}
        <span class="sr-only-text" data-i18n="screen_reader">Screen Reader</span>
      </button>

      <div class="font-resizer-cluster" role="group" aria-label="Adjust font size">
        <button type="button" class="top-btn font-btn" id="btn-font-sm" onclick="setFontSize('sm')" title="Decrease Font Size" aria-label="Decrease Font Size">A-</button>
        <button type="button" class="top-btn font-btn active" id="btn-font-md" onclick="setFontSize('md')" title="Default Font Size" aria-label="Default Font Size">A</button>
        <button type="button" class="top-btn font-btn" id="btn-font-lg" onclick="setFontSize('lg')" title="Increase Font Size" aria-label="Increase Font Size">A+</button>
      </div>

      <button type="button" class="top-btn" id="btn-contrast-toggle" onclick="toggleHighContrast()" title="Toggle High Contrast Display" aria-label="Toggle High Contrast">
        {SVG_ICONS['sun']}
        <span class="contrast-label-text" data-i18n="contrast">Contrast</span>
      </button>

      <button type="button" class="top-btn lang-switch-btn" id="btn-lang-toggle" onclick="toggleLanguage()" title="Switch Language" aria-label="Switch Language to Hindi">
        {SVG_ICONS['globe']}
        <span class="lang-text" id="lang-indicator">हिन्दी</span>
      </button>

      <button type="button" class="top-btn cms-preview-badge" id="btn-cms-preview" onclick="openCmsModal()" title="Simulate CMS Publishing & Workflow" aria-label="CMS Admin Workflow Simulator">
        {SVG_ICONS['shield']}
        <span class="cms-text" data-i18n="cms_admin">CMS Admin Preview</span>
      </button>
    </div>
  </div>
</aside>"""

MAIN_HEADER_MARKUP = f"""<!-- MAIN HEADER & MEGA-MENU NAVIGATION -->
<header class="main-header" id="site-header">
  <div class="container header-inner">
    <div class="brand-wrapper">
      <a href="#home" class="brand-logo-svg" aria-label="MPSeDC Home Link">
        {MPSEDC_LOGO_SVG}
      </a>
      <div class="brand-text-block">
        <div class="brand-title-group">
          <span class="brand-acronym" data-i18n="org_name">MPSeDC</span>
          <span class="brand-full-name" data-i18n="org_subtitle">Madhya Pradesh State Electronics Development Corporation Ltd.</span>
        </div>
        <div class="brand-undertaking" data-i18n="org_undertaking">A Government of Madhya Pradesh Undertaking</div>
      </div>
    </div>

    <div class="header-right-actions">
      <button type="button" class="search-trigger-btn" onclick="openSearchModal()" aria-label="Search portal (Ctrl+K)">
        {SVG_ICONS['search']}
        <span class="search-prompt-text" data-i18n="search_placeholder">Search Tenders, Policies, Projects...</span>
        <span class="search-kbd-shortcut">Ctrl+K</span>
      </button>

      <button type="button" class="hamburger-btn" id="mobile-hamburger-btn" onclick="toggleMobileDrawer()" aria-label="Toggle Navigation Menu" aria-expanded="false">
        {SVG_ICONS['menu']}
      </button>
    </div>
  </div>

  <!-- DESKTOP MEGA-MENU NAVIGATION BAR -->
  <nav class="desktop-nav-bar" aria-label="Primary Navigation">
    <div class="container">
      <ul class="nav-menu-list" role="menubar">
        <li class="nav-item" role="none">
          <a href="#home" class="nav-link active" role="menuitem" data-i18n="nav_home">Home</a>
        </li>

        <li class="nav-item has-mega" role="none">
          <a href="#about" class="nav-link" role="menuitem" aria-haspopup="true" aria-expanded="false" onclick="openAboutModal(); return false;">
            <span data-i18n="nav_about">About Us</span>
            <span class="chevron">{SVG_ICONS['chevron_down']}</span>
          </a>
          <div class="mega-menu-panel" role="region" aria-label="About Us Submenu">
            <div class="mega-grid-3col">
              <a href="#about" class="mega-menu-item" onclick="openAboutModal(); return false;">
                <div class="mega-item-icon">{SVG_ICONS['building']}</div>
                <div class="mega-item-text">
                  <strong>Corporate Profile</strong>
                  <span>History, mandate and pivotal role in MP digital ecosystem since 1983.</span>
                </div>
              </a>
              <a href="#about-officers" class="mega-menu-item" onclick="openOfficersModal(); return false;">
                <div class="mega-item-icon">{SVG_ICONS['users']}</div>
                <div class="mega-item-text">
                  <strong>Who's Who Directory</strong>
                  <span>Board of Directors, Executive Leadership and Nodal Officers.</span>
                </div>
              </a>
              <a href="#about-rti" class="mega-menu-item" onclick="openRtiModal(); return false;">
                <div class="mega-item-icon">{SVG_ICONS['file_text']}</div>
                <div class="mega-item-text">
                  <strong>RTI & Disclosures</strong>
                  <span>Proactive Section 4(1)(b) statutory public disclosures and appellate authorities.</span>
                </div>
              </a>
            </div>
          </div>
        </li>

        <li class="nav-item has-mega" role="none">
          <a href="#services" class="nav-link" role="menuitem" aria-haspopup="true" aria-expanded="false" onclick="scrollToSection('projects', 'Core Infrastructure'); return false;">
            <span data-i18n="nav_services">Services & Solutions</span>
            <span class="chevron">{SVG_ICONS['chevron_down']}</span>
          </a>
          <div class="mega-menu-panel" role="region" aria-label="Services Submenu">
            <div class="mega-grid-3col">
              <a href="#projects" class="mega-menu-item" onclick="filterProjects('Core Infrastructure')">
                <div class="mega-item-icon">{SVG_ICONS['server']}</div>
                <div class="mega-item-text">
                  <strong>SDC Cloud & Co-location</strong>
                  <span>Tier-IV data centre infrastructure, virtual servers, and sovereign cloud backup.</span>
                </div>
              </a>
              <a href="#projects" class="mega-menu-item" onclick="filterProjects('Core Infrastructure')">
                <div class="mega-item-icon">{SVG_ICONS['network']}</div>
                <div class="mega-item-text">
                  <strong>MPSWAN & Telecom</strong>
                  <span>Statewide optical fiber connectivity and secure governmental video routing.</span>
                </div>
              </a>
              <a href="#projects" class="mega-menu-item" onclick="filterProjects('GIS & Emerging Tech')">
                <div class="mega-item-icon">{SVG_ICONS['satellite']}</div>
                <div class="mega-item-text">
                  <strong>Spatial GIS & Surveying</strong>
                  <span>Enterprise drone mapping, cadastral integration, and 3D terrain modeling.</span>
                </div>
              </a>
            </div>
          </div>
        </li>

        <li class="nav-item has-mega" role="none">
          <a href="#projects" class="nav-link" role="menuitem" aria-haspopup="true" aria-expanded="false">
            <span data-i18n="nav_projects">Projects & Infrastructure</span>
            <span class="chevron">{SVG_ICONS['chevron_down']}</span>
          </a>
          <div class="mega-menu-panel" role="region" aria-label="Projects Submenu">
            <div class="mega-grid-3col">
              <a href="#projects" class="mega-menu-item" onclick="filterProjects('All')">
                <div class="mega-item-icon">{SVG_ICONS['cpu']}</div>
                <div class="mega-item-text">
                  <strong>12 Core Verticals</strong>
                  <span>Browse all state IT projects including CoE, ETDC Labs and MP Online.</span>
                </div>
              </a>
              <a href="#itparks" class="mega-menu-item">
                <div class="mega-item-icon">{SVG_ICONS['building']}</div>
                <div class="mega-item-text">
                  <strong>IT Parks & Clusters</strong>
                  <span>Bhopal, Indore, Jabalpur, Gwalior and Sinhasa plug-and-play facilities.</span>
                </div>
              </a>
              <a href="#itparks" class="mega-menu-item" onclick="selectItPark('malanpur')">
                <div class="mega-item-icon">{SVG_ICONS['shield']}</div>
                <div class="mega-item-text">
                  <strong>Malanpur EMC 2.0</strong>
                  <span>Electronics manufacturing cluster with heavy industrial infrastructure.</span>
                </div>
              </a>
            </div>
          </div>
        </li>

        <li class="nav-item" role="none">
          <a href="#policies" class="nav-link" role="menuitem" data-i18n="nav_policies">Policies & Rules</a>
        </li>

        <li class="nav-item" role="none">
          <a href="#tenders" class="nav-link" role="menuitem" data-i18n="nav_tenders">Tenders & RFPs</a>
        </li>

        <li class="nav-item" role="none">
          <a href="#updates" class="nav-link" role="menuitem" data-i18n="nav_media">Media & Updates</a>
        </li>

        <li class="nav-item" role="none">
          <a href="#contact" class="nav-link" role="menuitem" data-i18n="nav_contact">Contact Us</a>
        </li>
      </ul>
    </div>
  </nav>

  <!-- MOBILE HAMBURGER DRAWER -->
  <div class="drawer-backdrop" id="drawer-backdrop" onclick="toggleMobileDrawer()"></div>
  <aside class="mobile-drawer" id="mobile-drawer" aria-label="Mobile Navigation Drawer">
    <div class="mobile-drawer-header">
      <span class="mobile-drawer-title">MPSeDC Menu</span>
      <button type="button" class="close-drawer-btn" onclick="toggleMobileDrawer()" aria-label="Close navigation drawer">
        {SVG_ICONS['close']}
      </button>
    </div>
    <ul class="mobile-nav-list">
      <li class="mobile-nav-item"><a href="#home" class="mobile-nav-link" onclick="toggleMobileDrawer()">Home</a></li>
      <li class="mobile-nav-item"><a href="#about" class="mobile-nav-link" onclick="toggleMobileDrawer(); openAboutModal();">About Us</a></li>
      <li class="mobile-nav-item"><a href="#services" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('projects', 'Core Infrastructure');">Services & Solutions</a></li>
      <li class="mobile-nav-item"><a href="#projects" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('projects');">Projects & Infrastructure</a></li>
      <li class="mobile-nav-item"><a href="#policies" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('policies');">Policies & Rules</a></li>
      <li class="mobile-nav-item"><a href="#tenders" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('tenders');">Tenders & Corrigendums</a></li>
      <li class="mobile-nav-item"><a href="#itparks" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('itparks');">IT Parks Explorer</a></li>
      <li class="mobile-nav-item"><a href="#updates" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('updates');">Recruitment & News</a></li>
      <li class="mobile-nav-item"><a href="#contact" class="mobile-nav-link" onclick="toggleMobileDrawer(); scrollToSection('contact');">Contact & Helpdesk</a></li>
    </ul>
  </aside>
</header>"""

HERO_SECTION_MARKUP = f"""<!-- HERO SECTION (INTERACTIVE CAROUSEL & TOPOLOGY) -->
<section class="hero-section" id="home" aria-label="MPSeDC Featured Showcase">
  <div class="hero-topology-bg" aria-hidden="true">{HERO_TOPOLOGY_SVG}</div>
  <div class="container hero-grid">
    <!-- Left Content Column (Slider Slides) -->
    <div class="hero-content">
      <div class="hero-slider-container" id="hero-slider" aria-live="polite">
        <!-- Slide 1 -->
        <article class="hero-slide active" id="hero-slide-1" data-slide="1">
          <div class="hero-badge-tag">
            <span>Enterprise Digital Infrastructure</span>
          </div>
          <h1 class="hero-heading" data-i18n="hero_title">Powering Madhya Pradesh Through Digital Innovation</h1>
          <p class="hero-subtext" data-i18n="hero_desc">
            Driving digital transformation through state-of-the-art IT infrastructure, single-window investment promotion, resilient cyber-defense, and citizen-centric governance solutions.
          </p>
          <div class="hero-cta-group">
            <a href="#services" class="btn btn-accent" data-i18n="cta_explore_services">Explore Services</a>
            <a href="#itparks" class="btn btn-outline-white" data-i18n="cta_explore_infra">Explore IT Infrastructure</a>
            <a href="#policies" class="btn btn-outline-white" data-i18n="cta_investment">Investment Opportunities</a>
          </div>
        </article>

        <!-- Slide 2 -->
        <article class="hero-slide" id="hero-slide-2" data-slide="2">
          <div class="hero-badge-tag">
            <span>Single-Window Investment Promotion</span>
          </div>
          <h1 class="hero-heading">Catalyzing IT, ITeS, ESDM & GCC Investments</h1>
          <p class="hero-subtext">
            Attractive capital subsidies up to 30%, 100% stamp duty waiver, and ready-to-occupy Grade-A workspaces across Bhopal, Indore, Jabalpur, and Gwalior IT Parks.
          </p>
          <div class="hero-cta-group">
            <button type="button" class="btn btn-accent" onclick="openIncentiveModal()">Calculate Policy Incentives</button>
            <a href="#itparks" class="btn btn-outline-white">Explore IT Park Plots</a>
          </div>
        </article>

        <!-- Slide 3 -->
        <article class="hero-slide" id="hero-slide-3" data-slide="3">
          <div class="hero-badge-tag">
            <span>Sovereign Cyber Backbone</span>
          </div>
          <h1 class="hero-heading">Tier-IV State Data Center & Statewide Optical Network</h1>
          <p class="hero-subtext">
            Connecting 55 districts, 350+ blocks, and 1,000+ government offices over 10 Gbps MPSWAN with 24x7 SOC incident response and 99.9% uptime SLA.
          </p>
          <div class="hero-cta-group">
            <a href="#projects" class="btn btn-accent" onclick="filterProjects('Core Infrastructure')">G2G Infrastructure</a>
            <a href="#updates" class="btn btn-outline-white">Cyber Security Advisories</a>
          </div>
        </article>
      </div>

      <!-- Carousel Controls Bar -->
      <div class="hero-controls-bar">
        <div class="hero-controls-inner">
          <button type="button" class="hero-nav-arrow" id="btn-hero-prev" onclick="prevHeroSlide()" aria-label="Previous Slide">
            {SVG_ICONS['chevron_left']}
          </button>
          
          <div class="hero-dots-cluster" role="tablist" aria-label="Hero carousel slide navigation">
            <button type="button" class="hero-dot active" role="tab" aria-selected="true" aria-controls="hero-slide-1" onclick="goToHeroSlide(1)" aria-label="Go to slide 1"></button>
            <button type="button" class="hero-dot" role="tab" aria-selected="false" aria-controls="hero-slide-2" onclick="goToHeroSlide(2)" aria-label="Go to slide 2"></button>
            <button type="button" class="hero-dot" role="tab" aria-selected="false" aria-controls="hero-slide-3" onclick="goToHeroSlide(3)" aria-label="Go to slide 3"></button>
          </div>

          <button type="button" class="hero-nav-arrow" id="btn-hero-next" onclick="nextHeroSlide()" aria-label="Next Slide">
            {SVG_ICONS['chevron_right']}
          </button>

          <button type="button" class="hero-play-pause-btn" id="btn-hero-pause" onclick="toggleHeroAutoPlay()" aria-label="Pause Carousel Auto-play" title="Pause / Resume Carousel">
            {SVG_ICONS['pause']}
          </button>
        </div>
      </div>
    </div>

    <!-- Right Visual Column (Interactive Isometric Hub) -->
    <div class="hero-visual-col">
      <div class="hero-isometric-card">
        {ISOMETRIC_DIGITAL_HUB_SVG}
      </div>
    </div>
  </div>
</section>"""

PERSONA_SECTION_MARKUP = f"""<!-- PERSONA-BASED QUICK ENTRY (4 ROLE CARDS) -->
<section class="persona-section" aria-label="Quick Entry by Stakeholder Role">
  <div class="container">
    <div class="persona-grid">
      <!-- Card 1: Vendors & OEMs -->
      <article class="persona-card" onclick="scrollToSection('tenders', 'All')">
        <div class="persona-icon-box">{SVG_ICONS['file_text']}</div>
        <h3 class="persona-title" data-i18n="persona_vendors_title">Vendors & OEMs</h3>
        <p class="persona-desc" data-i18n="persona_vendors_desc">
          Discover procurement opportunities, active e-tenders, hardware/software RFPs, and corrigendums.
        </p>
        <span class="persona-link">
          <span data-i18n="persona_vendors_cta">Explore Live Tenders</span>
          {SVG_ICONS['arrow_right']}
        </span>
      </article>

      <!-- Card 2: Investors & Startups -->
      <article class="persona-card" onclick="scrollToSection('itparks')">
        <div class="persona-icon-box">{SVG_ICONS['building']}</div>
        <h3 class="persona-title" data-i18n="persona_investors_title">Investors & Startups</h3>
        <p class="persona-desc" data-i18n="persona_investors_desc">
          Discover plug-and-play IT parks, attractive capital subsidies, and policies for IT, GCC & AVGC.
        </p>
        <span class="persona-link">
          <span data-i18n="persona_investors_cta">Explore Investment</span>
          {SVG_ICONS['arrow_right']}
        </span>
      </article>

      <!-- Card 3: Government Departments -->
      <article class="persona-card" onclick="scrollToSection('projects', 'Core Infrastructure')">
        <div class="persona-icon-box">{SVG_ICONS['server']}</div>
        <h3 class="persona-title" data-i18n="persona_govt_title">Government Departments</h3>
        <p class="persona-desc" data-i18n="persona_govt_desc">
          Leverage Tier-IV State Data Center hosting, secure MPSWAN connectivity, and e-Office suites.
        </p>
        <span class="persona-link">
          <span data-i18n="persona_govt_cta">Explore G2G Services</span>
          {SVG_ICONS['arrow_right']}
        </span>
      </article>

      <!-- Card 4: Citizens & Job Seekers -->
      <article class="persona-card" onclick="scrollToSection('updates', 'recruitment')">
        <div class="persona-icon-box">{SVG_ICONS['users']}</div>
        <h3 class="persona-title" data-i18n="persona_citizens_title">Citizens & Job Seekers</h3>
        <p class="persona-desc" data-i18n="persona_citizens_desc">
          Access GET recruitment notices, summer internship rosters, recruitment exam results, and RTI.
        </p>
        <span class="persona-link">
          <span data-i18n="persona_citizens_cta">Explore Updates</span>
          {SVG_ICONS['arrow_right']}
        </span>
      </article>
    </div>
  </div>
</section>"""

QUICK_ACCESS_STRIP_MARKUP = f"""<!-- QUICK ACCESS SERVICE STRIP (8 ICON TILES) -->
<section class="quick-strip-section" aria-label="Direct Quick Access Links">
  <div class="container">
    <div class="section-header-block text-center">
      <span class="section-eyebrow">FAST ACCESS</span>
      <h2 class="section-heading">Quick Access Services</h2>
      <p class="section-subtext">Instant gateways to high-frequency state portals, statutory disclosures and active registries.</p>
    </div>

    <div class="tiles-grid-8">
      <a href="#tenders" class="service-tile" onclick="filterTenders('All')">
        <div class="tile-icon-wrapper">{SVG_ICONS['file_text']}</div>
        <span class="tile-label" data-i18n="quick_tenders">Active Tenders</span>
        <span class="tile-badge">7 Live</span>
      </a>

      <a href="#policies" class="service-tile">
        <div class="tile-icon-wrapper">{SVG_ICONS['trending_up']}</div>
        <span class="tile-label" data-i18n="quick_portal">IT Investment Portal</span>
      </a>

      <a href="#itparks" class="service-tile">
        <div class="tile-icon-wrapper">{SVG_ICONS['building']}</div>
        <span class="tile-label" data-i18n="quick_itparks">IT Parks & Plots</span>
      </a>

      <a href="#policies" class="service-tile">
        <div class="tile-icon-wrapper">{SVG_ICONS['award']}</div>
        <span class="tile-label" data-i18n="quick_policies">Policies & Rules</span>
      </a>

      <a href="#updates" class="service-tile" onclick="filterUpdatesTab('notifications')">
        <div class="tile-icon-wrapper">{SVG_ICONS['calendar']}</div>
        <span class="tile-label" data-i18n="quick_circulars">Circulars & Orders</span>
      </a>

      <a href="#updates" class="service-tile" onclick="filterUpdatesTab('recruitment')">
        <div class="tile-icon-wrapper">{SVG_ICONS['users']}</div>
        <span class="tile-label" data-i18n="quick_recruitment">Recruitment & Results</span>
      </a>

      <a href="#about" class="service-tile" onclick="openRtiModal(); return false;">
        <div class="tile-icon-wrapper">{SVG_ICONS['shield']}</div>
        <span class="tile-label" data-i18n="quick_rti">RTI Disclosures</span>
      </a>

      <a href="#projects" class="service-tile" onclick="openProjectModal('PRJ-12'); return false;">
        <div class="tile-icon-wrapper">{SVG_ICONS['satellite']}</div>
        <span class="tile-label" data-i18n="quick_geoportal">MP Geoportal</span>
      </a>
    </div>
  </div>
</section>"""

STATS_SECTION_MARKUP = f"""<!-- MPSeDC AT A GLANCE (ANIMATED STATS STRIP) -->
<section class="stats-banner-section" id="stats-section" aria-label="Key Performance Indicators">
  <div class="container">
    <div class="section-header-block text-center text-white">
      <span class="section-eyebrow text-accent">INSTITUTIONAL METRICS</span>
      <h2 class="section-heading text-white" data-i18n="stats_section_title">MPSeDC at a Glance</h2>
      <p class="section-subtext text-white-muted" data-i18n="stats_section_subtitle">
        Decades of driving Madhya Pradesh's technological pre-eminence and digital sovereignty.
      </p>
    </div>

    <div class="stats-grid">
      <div class="stat-item-card">
        <div class="stat-number" data-target="40" data-suffix="+">0</div>
        <div class="stat-label">Years of Digital Excellence</div>
        <span class="stat-demo-tag">[Demo Metrics]</span>
      </div>

      <div class="stat-item-card">
        <div class="stat-number" data-target="120" data-suffix="+">0</div>
        <div class="stat-label">e-Governance Projects Delivered</div>
        <span class="stat-demo-tag">[Demo Metrics]</span>
      </div>

      <div class="stat-item-card">
        <div class="stat-number" data-target="6" data-suffix="">0</div>
        <div class="stat-label">Operational IT Parks & Clusters</div>
        <span class="stat-demo-tag">[Official Data]</span>
      </div>

      <div class="stat-item-card">
        <div class="stat-number" data-target="50" data-suffix="+">0</div>
        <div class="stat-label">State Departments Hosted on SDC</div>
        <span class="stat-demo-tag">[Demo Metrics]</span>
      </div>

      <div class="stat-item-card">
        <div class="stat-number" data-target="99.9" data-suffix="%" data-decimals="1">0</div>
        <div class="stat-label">State Data Center Core Uptime</div>
        <span class="stat-demo-tag">[SLA Benchmark]</span>
      </div>
    </div>
  </div>
</section>"""

PROJECTS_SECTION_MARKUP = f"""<!-- PROJECTS & TECHNOLOGY VERTICALS -->
<section class="projects-section" id="projects" aria-label="Flagship Projects and Infrastructure Verticals">
  <div class="container">
    <div class="section-header-block">
      <div class="section-header-flex">
        <div>
          <span class="section-eyebrow">TECHNOLOGY PORTFOLIO</span>
          <h2 class="section-heading" data-i18n="projects_section_title">Projects & Technology Verticals</h2>
          <p class="section-subtext" data-i18n="projects_section_subtitle">
            Pioneering state-wide digital backbones, geospatial intelligence, and institutional frameworks.
          </p>
        </div>
      </div>
    </div>

    <!-- Category Filter Pills Bar -->
    <div class="filter-pills-bar" role="tablist" aria-label="Project Categories">
      <button type="button" class="filter-pill-btn active" role="tab" aria-selected="true" onclick="filterProjects('All')">All Verticals (12)</button>
      <button type="button" class="filter-pill-btn" role="tab" aria-selected="false" onclick="filterProjects('Core Infrastructure')">Core Infrastructure (5)</button>
      <button type="button" class="filter-pill-btn" role="tab" aria-selected="false" onclick="filterProjects('GIS & Emerging Tech')">GIS & Emerging Tech (4)</button>
      <button type="button" class="filter-pill-btn" role="tab" aria-selected="false" onclick="filterProjects('Citizen & Investment Portals')">Citizen & Investment Portals (3)</button>
    </div>

    <!-- Dynamic Projects Grid Container -->
    <div class="projects-grid" id="projects-grid-container" aria-live="polite">
      <!-- Dynamically injected via JavaScript -->
    </div>
  </div>
</section>"""

TENDERS_SECTION_MARKUP = f"""<!-- INTERACTIVE TENDER & RFP HUB (CORE MODULE) -->
<section class="tenders-section" id="tenders" aria-label="Public Procurement, Tenders and Corrigendums">
  <div class="container">
    <div class="section-header-block">
      <span class="section-eyebrow">PUBLIC PROCUREMENT</span>
      <h2 class="section-heading" data-i18n="tenders_section_title">Interactive Tender & RFP Hub</h2>
      <p class="section-subtext" data-i18n="tenders_section_subtitle">
        Transparent, electronic public procurement adhering to MP PWD & Store Purchase Rules. Grouped corrigendums with live IST timestamps.
      </p>
    </div>

    <!-- Tenders Multi-Filter Controls Card -->
    <div class="tenders-filter-card">
      <div class="tenders-filter-grid">
        <div class="filter-field-group">
          <label class="filter-label" for="tender-search-input">Search Tender No. / Keyword</label>
          <input type="text" id="tender-search-input" class="form-control-input" placeholder="e.g. SDC, Cloud, RF..." oninput="handleTenderSearchDebounced()">
        </div>

        <div class="filter-field-group">
          <label class="filter-label" for="tender-cat-select">Procurement Category</label>
          <select id="tender-cat-select" class="form-control-select" onchange="applyTenderFilters()">
            <option value="All">All Categories</option>
            <option value="Hardware">Hardware & Electronics</option>
            <option value="Software">Software & Cloud Applications</option>
            <option value="Infrastructure">Infrastructure & Telecom</option>
            <option value="Manpower">Manpower & Consultancy</option>
            <option value="Consultancy">Specialized Surveys</option>
          </select>
        </div>

        <div class="filter-field-group">
          <label class="filter-label" for="tender-status-select">Status</label>
          <select id="tender-status-select" class="form-control-select" onchange="applyTenderFilters()">
            <option value="All">All Statuses</option>
            <option value="Live">Live (Active Bidding)</option>
            <option value="Extended">Extended Deadline</option>
            <option value="Closed">Evaluation / Closed</option>
            <option value="Cancelled">Cancelled</option>
            <option value="Archived">Archived</option>
          </select>
        </div>

        <div class="filter-field-group">
          <button type="button" class="btn btn-outline btn-reset-filters" onclick="resetTenderFilters()">
            {SVG_ICONS['filter']}
            <span>Clear Filters</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Responsive Tenders Table Card -->
    <div class="tender-table-container">
      <div class="table-responsive">
        <table class="tender-table" aria-label="Tenders and Corrigendums Listing">
          <thead>
            <tr>
              <th scope="col" style="width: 22%;">Tender Reference</th>
              <th scope="col" style="width: 38%;">Title & Work Description</th>
              <th scope="col" style="width: 14%;">Category</th>
              <th scope="col" style="width: 16%;">Submission Deadline (IST)</th>
              <th scope="col" style="width: 10%;">Actions</th>
            </tr>
          </thead>
          <tbody id="tenders-table-body">
            <!-- Dynamically populated rows with parent-child corrigendum accordions -->
          </tbody>
        </table>
      </div>

      <!-- Pagination Footer Bar -->
      <div class="pagination-bar">
        <div class="pagination-info" id="tenders-pagination-info">
          Showing 1 to 5 of 7 tenders
        </div>
        <div class="pagination-buttons" id="tenders-pagination-buttons">
          <!-- Dynamically populated page buttons -->
        </div>
      </div>
    </div>
  </div>
</section>"""

IT_PARKS_SECTION_MARKUP = f"""<!-- IT PARKS & INFRASTRUCTURE INTERACTIVE EXPLORER -->
<section class="itparks-section" id="itparks" aria-label="IT Parks and Infrastructure Across Madhya Pradesh">
  <div class="container">
    <div class="section-header-block">
      <span class="section-eyebrow">INDUSTRIAL INFRASTRUCTURE</span>
      <h2 class="section-heading" data-i18n="itparks_section_title">IT Parks & Infrastructure Explorer</h2>
      <p class="section-subtext" data-i18n="itparks_section_subtitle">
        Ready-to-occupy Grade-A workspaces, electronics clusters, and developed industrial plots across MP. Click on map pins to view dossiers.
      </p>
    </div>

    <div class="itparks-explorer-grid">
      <!-- Left Column: Interactive MP SVG Map with Pins -->
      <div class="map-container-card">
        <div class="map-header-bar">
          <span class="map-header-title">Madhya Pradesh State Technology Map</span>
          <span class="map-hint-pill">Select City Pin to Inspect</span>
        </div>
        <div class="mp-svg-map-wrapper">
          {MP_MAP_SVG}

          <!-- Pin 1: Bhopal -->
          <button type="button" class="map-pin-btn active" id="pin-bhopal" style="top: 52%; left: 46%;" onclick="selectItPark('bhopal')" aria-label="Select Bhopal IT Park">
            <span class="pin-dot"></span>
            <span class="pin-label-pill">Bhopal IT Park</span>
          </button>

          <!-- Pin 2: Indore -->
          <button type="button" class="map-pin-btn" id="pin-indore" style="top: 60%; left: 33%;" onclick="selectItPark('indore')" aria-label="Select Indore IT Park">
            <span class="pin-dot"></span>
            <span class="pin-label-pill">Indore IT Park</span>
          </button>

          <!-- Pin 3: Jabalpur -->
          <button type="button" class="map-pin-btn" id="pin-jabalpur" style="top: 54%; left: 68%;" onclick="selectItPark('jabalpur')" aria-label="Select Jabalpur IT Park">
            <span class="pin-dot"></span>
            <span class="pin-label-pill">Jabalpur IT Park</span>
          </button>

          <!-- Pin 4: Gwalior -->
          <button type="button" class="map-pin-btn" id="pin-gwalior" style="top: 22%; left: 48%;" onclick="selectItPark('gwalior')" aria-label="Select Gwalior IT Park">
            <span class="pin-dot"></span>
            <span class="pin-label-pill">Gwalior IT Park</span>
          </button>

          <!-- Pin 5: Malanpur -->
          <button type="button" class="map-pin-btn" id="pin-malanpur" style="top: 18%; left: 54%;" onclick="selectItPark('malanpur')" aria-label="Select Malanpur EMC">
            <span class="pin-dot"></span>
            <span class="pin-label-pill">Malanpur EMC</span>
          </button>

          <!-- Pin 6: Sinhasa -->
          <button type="button" class="map-pin-btn" id="pin-sinhasa" style="top: 66%; left: 29%;" onclick="selectItPark('sinhasa')" aria-label="Select Sinhasa IT Park">
            <span class="pin-dot"></span>
            <span class="pin-label-pill">Sinhasa Cluster</span>
          </button>
        </div>
      </div>

      <!-- Right Column: Live Synchronized IT Park Dossier Card -->
      <div class="itpark-dossier-card" id="itpark-dossier-card" aria-live="polite">
        <!-- Dynamically updated via selectItPark(key) -->
      </div>
    </div>
  </div>
</section>"""

POLICIES_SECTION_MARKUP = f"""<!-- POLICIES & GOVERNMENT INITIATIVES LIBRARY -->
<section class="policies-section" id="policies" aria-label="Policies and Government Initiatives Library">
  <div class="container">
    <div class="section-header-block">
      <div class="section-header-flex">
        <div>
          <span class="section-eyebrow">INVESTOR PROMOTION</span>
          <h2 class="section-heading" data-i18n="policies_section_title">Policies & Government Initiatives</h2>
          <p class="section-subtext" data-i18n="policies_section_subtitle">
            Progressive, investor-friendly frameworks offering capital rebates, employment assistance & power subsidies.
          </p>
        </div>
        <div>
          <button type="button" class="btn btn-accent" onclick="openIncentiveModal()">
            {SVG_ICONS['cpu']}
            <span>Mini Incentive Estimator</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Policies Cards Grid -->
    <div class="policies-grid" id="policies-grid-container">
      <!-- Dynamically generated via JavaScript -->
    </div>
  </div>
</section>"""

NEWS_SECTION_MARKUP = f"""<!-- LATEST NEWS, RECRUITMENT & CIRCULARS (TABBED + ARCHIVE) -->
<section class="updates-section" id="updates" aria-label="Latest News, Recruitment and Circulars">
  <div class="container">
    <div class="section-header-block">
      <span class="section-eyebrow">NOTIFICATIONS & CAREERS</span>
      <h2 class="section-heading" data-i18n="news_section_title">Latest News, Recruitment & Circulars</h2>
      <p class="section-subtext" data-i18n="news_section_subtitle">
        Timely notifications, employment rosters, corrigendum bulletins, and official state orders.
      </p>
    </div>

    <div class="updates-card-box">
      <!-- Tabs Header with Archive Switch & Search -->
      <div class="updates-tabs-header">
        <div class="updates-tabs-list" role="tablist" aria-label="Updates Category Tabs">
          <button type="button" class="update-tab-btn active" data-tab="all" role="tab" aria-selected="true" onclick="filterUpdatesTab('all', this)">All Updates</button>
          <button type="button" class="update-tab-btn" data-tab="recruitment" role="tab" aria-selected="false" onclick="filterUpdatesTab('recruitment', this)">Recruitment (GET)</button>
          <button type="button" class="update-tab-btn" data-tab="internship" role="tab" aria-selected="false" onclick="filterUpdatesTab('internship', this)">Internship</button>
          <button type="button" class="update-tab-btn" data-tab="results" role="tab" aria-selected="false" onclick="filterUpdatesTab('results', this)">Assessment Results</button>
          <button type="button" class="update-tab-btn" data-tab="notifications" role="tab" aria-selected="false" onclick="filterUpdatesTab('notifications', this)">Govt. Orders</button>
          <button type="button" class="update-tab-btn" data-tab="events" role="tab" aria-selected="false" onclick="filterUpdatesTab('events', this)">Events & Hackathons</button>
        </div>

        <div class="updates-archive-toggle">
          <label class="switch-control" for="toggle-archive-checkbox">
            <input type="checkbox" id="toggle-archive-checkbox" onchange="toggleArchiveUpdates(this.checked)">
            <span class="switch-slider"></span>
          </label>
          <span class="archive-label-text">Show Archived Only</span>
        </div>
      </div>

      <!-- Updates List Container -->
      <div class="updates-list-container" id="updates-list-container" aria-live="polite">
        <!-- Dynamically generated accordion-style news items -->
      </div>
    </div>
  </div>
</section>"""

FOOTER_MARKUP = f"""<!-- COMPREHENSIVE GOVERNMENT FOOTER -->
<footer class="main-footer" id="contact" aria-label="Site Footer and Legal Links">
  <div class="container">
    <div class="footer-grid">
      <!-- Col 1: About MPSeDC & Address -->
      <div class="footer-col">
        <h3 class="footer-col-title" data-i18n="footer_about_title">About MPSeDC</h3>
        <p class="footer-address-text">
          <strong>Madhya Pradesh State Electronics Development Corporation Ltd.</strong><br>
          (A Government of Madhya Pradesh Undertaking)<br>
          State IT Centre, 47-A, Arera Hills, Bhopal, M.P. – 462011
        </p>
        <div class="footer-contact-item">
          {SVG_ICONS['phone']}
          <span>Phone: +91-755-2518300, 2518301</span>
        </div>
        <div class="footer-contact-item">
          {SVG_ICONS['mail']}
          <span>Email: info@mpsedc.com, invest@mpsedc.com</span>
        </div>
        <div class="footer-badge-item" style="margin-top: 14px;">
          <span class="badge badge-extended">GIGW 3.0 & UX4G Benchmark Prototype</span>
        </div>
      </div>

      <!-- Col 2: Quick Links -->
      <div class="footer-col">
        <h3 class="footer-col-title" data-i18n="footer_quick_title">Quick Links</h3>
        <ul class="footer-links-list">
          <li><a href="#tenders" onclick="filterTenders('All')">Active Tenders & RFPs</a></li>
          <li><a href="#itparks">IT Parks & Developed Plots</a></li>
          <li><a href="#policies">Investment Promotion Policies</a></li>
          <li><a href="#updates" onclick="filterUpdatesTab('recruitment')">Recruitment & Careers</a></li>
          <li><a href="#about" onclick="openOfficersModal(); return false;">Who's Who Directory</a></li>
          <li><a href="#about" onclick="openRtiModal(); return false;">Right to Information (RTI)</a></li>
        </ul>
      </div>

      <!-- Col 3: Important Government Portals -->
      <div class="footer-col">
        <h3 class="footer-col-title" data-i18n="footer_govt_title">Important Government Links</h3>
        <ul class="footer-links-list">
          <li><a href="https://mp.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">Government of Madhya Pradesh {SVG_ICONS['external']}</a></li>
          <li><a href="https://dst.mp.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">Dept. of Science & Technology, MP {SVG_ICONS['external']}</a></li>
          <li><a href="https://invest.mp.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">Invest Madhya Pradesh / MPIDC {SVG_ICONS['external']}</a></li>
          <li><a href="https://mponline.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MP Online Citizen Portal {SVG_ICONS['external']}</a></li>
          <li><a href="https://mpedistrict.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MP e-District / Public Services {SVG_ICONS['external']}</a></li>
          <li><a href="https://geoportal.mp.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MP Geoportal {SVG_ICONS['external']}</a></li>
          <li><a href="https://drone.mp.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MP Drone Portal {SVG_ICONS['external']}</a></li>
          <li><a href="https://mptenders.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MP e-Procurement Portal {SVG_ICONS['external']}</a></li>
          <li><a href="https://cmhelpline.mp.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MP CM Helpline 181 {SVG_ICONS['external']}</a></li>
          <li><a href="https://www.meity.gov.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">MeitY, Government of India {SVG_ICONS['external']}</a></li>
          <li><a href="https://www.nic.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">National Informatics Centre (NIC) {SVG_ICONS['external']}</a></li>
          <li><a href="https://www.cdac.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">C-DAC R&D {SVG_ICONS['external']}</a></li>
          <li><a href="https://www.cert-in.org.in/" target="_blank" rel="noopener noreferrer" onclick="notifyExternalLink(event, this.href)">CERT-In Cyber Security {SVG_ICONS['external']}</a></li>
        </ul>
      </div>

      <!-- Col 4: Legal & Compliance -->
      <div class="footer-col">
        <h3 class="footer-col-title" data-i18n="footer_legal_title">Legal & Compliance</h3>
        <ul class="footer-links-list">
          <li><a href="#about" onclick="openLegalModal('privacy'); return false;">Privacy Policy</a></li>
          <li><a href="#about" onclick="openLegalModal('copyright'); return false;">Copyright Policy</a></li>
          <li><a href="#about" onclick="openLegalModal('disclaimer'); return false;">Disclaimer Policy</a></li>
          <li><a href="#about" onclick="openLegalModal('hyperlinking'); return false;">Hyperlinking Policy</a></li>
          <li><a href="#about" onclick="openScreenReaderModal(); return false;">Accessibility Statement</a></li>
          <li><a href="#about" onclick="openLegalModal('sitemap'); return false;">Portal Sitemap</a></li>
        </ul>
      </div>
    </div>

    <!-- Bottom Legal Sub-Strip -->
    <div class="footer-bottom-strip">
      <div class="footer-bottom-flex">
        <div>
          <span data-i18n="footer_copyright">© 2026 MPSeDC Ltd. A Government of Madhya Pradesh Undertaking.</span><br>
          <small class="text-white-muted" data-i18n="footer_disclaimer">[Demonstration Prototype] Developed for technical review and modernization benchmarking.</small>
        </div>
        <div style="text-align: right;">
          <span class="visitor-counter-pill">Visitor Counter [Demo]: <strong>1,482,920</strong></span><br>
          <small class="text-white-muted">Last Updated: <span id="portal-last-updated">19-Nov-2026 10:48 IST</span></small>
        </div>
      </div>
    </div>
  </div>

  <!-- Smooth Back to Top Floating Button -->
  <button type="button" class="back-to-top-btn" id="btn-back-to-top" onclick="scrollToTop()" aria-label="Scroll back to top of page" title="Back to Top">
    {SVG_ICONS['chevron_up']}
  </button>
</footer>"""

MODALS_MARKUP = f"""<!-- MODALS SYSTEM (GLOBAL SEARCH, TENDER, DOSSIER, ESTIMATOR, CMS) -->

<!-- 1. Global Smart Search Modal (Ctrl+K) -->
<div class="modal-overlay" id="modal-global-search" role="dialog" aria-modal="true" aria-labelledby="search-modal-label">
  <div class="search-modal-box">
    <div class="search-input-header">
      {SVG_ICONS['search']}
      <input type="text" id="global-search-input" class="search-field-input" placeholder="Type to search tenders, policies, circulars, officers..." aria-label="Type to search" oninput="handleGlobalSearchDebounced()">
      <button type="button" class="top-btn" onclick="closeSearchModal()" aria-label="Close search">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="search-results-container" id="search-results-container" style="max-height: 400px; overflow-y: auto; padding: 12px 20px;">
      <div class="search-empty-state text-center" style="padding: 24px; color: var(--text-muted);">
        Type at least 2 characters to search across Tenders, Policies, Projects, and News.
      </div>
    </div>
  </div>
</div>

<!-- 2. Project Details Modal -->
<div class="modal-overlay" id="modal-project-details" role="dialog" aria-modal="true" aria-labelledby="project-modal-title">
  <div class="modal-dialog modal-lg">
    <div class="modal-header">
      <h3 id="project-modal-title">Project Details</h3>
      <button type="button" class="modal-close-btn" onclick="closeModal('modal-project-details')" aria-label="Close modal">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="modal-body" id="project-modal-body">
      <!-- Injected via JavaScript -->
    </div>
    <div class="modal-footer" id="project-modal-footer">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-project-details')">Close</button>
    </div>
  </div>
</div>

<!-- 3. Tender Details Modal (with Spec Sheet trigger) -->
<div class="modal-overlay" id="modal-tender-details" role="dialog" aria-modal="true" aria-labelledby="tender-modal-title">
  <div class="modal-dialog modal-lg">
    <div class="modal-header">
      <h3 id="tender-modal-title">Tender & RFP Details</h3>
      <button type="button" class="modal-close-btn" onclick="closeModal('modal-tender-details')" aria-label="Close modal">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="modal-body" id="tender-modal-body">
      <!-- Injected via JavaScript -->
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-tender-details')">Close</button>
      <button type="button" class="btn btn-primary" onclick="simulateSpecDownload()">
        {SVG_ICONS['download']}
        <span>Download Full Spec Sheet (ZIP)</span>
      </button>
    </div>
  </div>
</div>

<!-- 4. Policy Details & Mini Incentive Estimator Modal -->
<div class="modal-overlay" id="modal-policy-details" role="dialog" aria-modal="true" aria-labelledby="policy-modal-title">
  <div class="modal-dialog modal-lg">
    <div class="modal-header">
      <h3 id="policy-modal-title">Policy Framework & Incentive Calculator</h3>
      <button type="button" class="modal-close-btn" onclick="closeModal('modal-policy-details')" aria-label="Close modal">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="modal-body" id="policy-modal-body">
      <!-- Injected via JavaScript -->
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-policy-details')">Close</button>
      <button type="button" class="btn btn-primary" onclick="downloadPolicyPdf('POL-01')">
        {SVG_ICONS['download']}
        <span>Download Official Gazette Notification</span>
      </button>
    </div>
  </div>
</div>

<!-- 5. Apply for Plot / Space EOI Modal -->
<div class="modal-overlay" id="modal-itpark-eoi" role="dialog" aria-modal="true" aria-labelledby="eoi-modal-title">
  <div class="modal-dialog">
    <div class="modal-header">
      <h3 id="eoi-modal-title">Apply for Plot / Space EOI</h3>
      <button type="button" class="modal-close-btn" onclick="closeModal('modal-itpark-eoi')" aria-label="Close modal">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="modal-body">
      <form id="eoi-application-form" onsubmit="handleEoiSubmit(event)">
        <div style="margin-bottom: 14px;">
          <label class="filter-label">Selected IT Park / Cluster *</label>
          <input type="text" id="eoi-park-name" class="form-control-input" readonly>
        </div>
        <div style="margin-bottom: 14px;">
          <label class="filter-label">Applicant Company Name *</label>
          <input type="text" id="eoi-company-name" class="form-control-input" placeholder="e.g. Acme Tech Solutions Pvt Ltd" required>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px;">
          <div>
            <label class="filter-label">Space Requirement *</label>
            <select id="eoi-space-type" class="form-control-select" required>
              <option value="Plug & Play Warm Shell">Plug & Play Warm Shell</option>
              <option value="Bare Shell Office Floor">Bare Shell Office Floor</option>
              <option value="Industrial Plot (Land)">Industrial Plot (Land)</option>
              <option value="Incubator Coworking Desk">Incubator Desk</option>
            </select>
          </div>
          <div>
            <label class="filter-label">Required Area (Sq. Ft. / Acres) *</label>
            <input type="text" id="eoi-area-req" class="form-control-input" placeholder="e.g. 15,000 Sq. Ft." required>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px;">
          <div>
            <label class="filter-label">Authorized Contact Person *</label>
            <input type="text" id="eoi-contact-name" class="form-control-input" placeholder="Full Name" required>
          </div>
          <div>
            <label class="filter-label">Email ID *</label>
            <input type="email" id="eoi-contact-email" class="form-control-input" placeholder="name@company.com" required>
          </div>
        </div>
        <div style="margin-bottom: 14px;">
          <label class="filter-label">Project Domain *</label>
          <select id="eoi-domain" class="form-control-select" required>
            <option value="IT / ITeS Software Development">IT / ITeS Software Development</option>
            <option value="Global Capability Center (GCC)">Global Capability Center (GCC)</option>
            <option value="Electronics System Design & Manufacturing (ESDM)">Electronics Manufacturing (ESDM)</option>
            <option value="AVGC-XR & Animation">AVGC-XR & Animation</option>
            <option value="Data Center & Cloud Infrastructure">Data Center & Cloud Infrastructure</option>
          </select>
        </div>
        <div class="modal-footer" style="padding: 16px 0 0 0; border-top: 1px solid var(--border);">
          <button type="button" class="btn btn-outline" onclick="closeModal('modal-itpark-eoi')">Cancel</button>
          <button type="submit" class="btn btn-accent">Submit Expression of Interest</button>
        </div>
      </form>
    </div>
  </div>
</div>

<!-- 6. CMS Maker-Checker-Publisher Simulator Modal -->
<div class="modal-overlay" id="modal-cms-preview" role="dialog" aria-modal="true" aria-labelledby="cms-modal-title">
  <div class="modal-dialog modal-lg">
    <div class="modal-header">
      <h3 id="cms-modal-title">CMS Multi-Tier Workflow & Auto-Archival Simulator</h3>
      <button type="button" class="modal-close-btn" onclick="closeModal('modal-cms-preview')" aria-label="Close modal">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="modal-body">
      <div style="padding: 14px; background: var(--surface-alt); border-radius: var(--radius-md); border: 1px solid var(--border); margin-bottom: 20px;">
        <strong>Maker-Checker-Publisher (GIGW 3.0 Compliance Simulation)</strong><br>
        <span style="font-size: 0.85rem; color: var(--text-secondary);">
          Demonstrates how portal content undergoes multi-stage cryptographic validation, bilingual parity verification, and automated deadline-driven archival before publication on the live portal.
        </span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 24px;">
        <div style="padding: 14px; border: 2px solid var(--border); border-radius: var(--radius-md); text-align: center;" id="workflow-maker-box">
          <div style="font-size: 1.5rem; margin-bottom: 6px;">📝</div>
          <strong>1. Maker (Operator)</strong>
          <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Drafts tender, corrigendum, or gazette notification with PDF upload.</p>
          <span class="badge badge-live">Completed</span>
        </div>
        <div style="padding: 14px; border: 2px solid var(--secondary); border-radius: var(--radius-md); text-align: center; background: rgba(23, 105, 170, 0.05);" id="workflow-checker-box">
          <div style="font-size: 1.5rem; margin-bottom: 6px;">🔍</div>
          <strong>2. Checker (Reviewer)</strong>
          <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Reviews bilingual text, financial thresholds & EMD stipulations.</p>
          <span class="badge badge-extended">Active Queue</span>
        </div>
        <div style="padding: 14px; border: 2px solid var(--border); border-radius: var(--radius-md); text-align: center;" id="workflow-publisher-box">
          <div style="font-size: 1.5rem; margin-bottom: 6px;">🚀</div>
          <strong>3. Publisher (Authorized)</strong>
          <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Affixes DSC e-Sign, broadcasts to portal, and schedules auto-archival.</p>
          <span class="badge badge-closed">Pending</span>
        </div>
      </div>

      <div style="border-top: 1px solid var(--border); padding-top: 16px;">
        <h4>Interactive Simulation Trigger</h4>
        <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px;">
          Click the button below to simulate approval of an urgent Corrigendum and instant portal broadcast:
        </p>
        <button type="button" class="btn btn-primary" onclick="simulateCmsApprove()">
          {SVG_ICONS['check']}
          <span>Authorize & Publish Sample Corrigendum</span>
        </button>
      </div>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-outline" onclick="closeModal('modal-cms-preview')">Close Preview</button>
    </div>
  </div>
</div>

<!-- 7. Screen Reader & Accessibility Guide Modal -->
<div class="modal-overlay" id="modal-screen-reader" role="dialog" aria-modal="true" aria-labelledby="sr-modal-title">
  <div class="modal-dialog">
    <div class="modal-header">
      <h3 id="sr-modal-title">Accessibility & Screen Reader Information</h3>
      <button type="button" class="modal-close-btn" onclick="closeModal('modal-screen-reader')" aria-label="Close modal">
        {SVG_ICONS['close']}
      </button>
    </div>
    <div class="modal-body">
      <p style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
        The modernized MPSeDC portal has been designed to strictly comply with <strong>World Wide Web Consortium (W3C) Web Content Accessibility Guidelines (WCAG) 2.1 Level AA</strong> and the <strong>Guidelines for Indian Government Websites (GIGW 3.0)</strong>.
      </p>
      <h4 style="margin-bottom: 8px;">Compatible Screen Readers:</h4>
      <ul style="padding-left: 20px; font-size: 0.9rem; line-height: 1.8; margin-bottom: 16px;">
        <li>NonVisual Desktop Access (NVDA) - Free & Open Source for Windows</li>
        <li>Job Access With Speech (JAWS) - Windows</li>
        <li>VoiceOver - Built into macOS and iOS devices</li>
        <li>TalkBack - Android accessibility service</li>
      </ul>
      <h4 style="margin-bottom: 8px;">Accessibility Keyboard Shortcuts:</h4>
      <ul style="padding-left: 20px; font-size: 0.9rem; line-height: 1.8;">
        <li><code>Ctrl + K</code>: Instant Global Smart Search</li>
        <li><code>Tab</code> / <code>Shift + Tab</code>: Navigate focus sequentially</li>
        <li><code>Enter</code>: Activate buttons, expand accordions, and follow links</li>
        <li><code>Esc</code>: Dismiss any open modal overlay</li>
      </ul>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-primary" onclick="closeModal('modal-screen-reader')">Understood</button>
    </div>
  </div>
</div>

<!-- Toast Notifications Container -->
<div class="toast-container" id="toast-container" aria-live="polite" aria-atomic="true"></div>
"""
