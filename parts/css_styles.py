# parts/css_styles.py
# Comprehensive CSS Stylesheet for MPSeDC Modernized Portal

CSS_CONTENT = """
/* ==========================================================================
   1. RESET & BASE VARIABLES (WCAG 2.1 AA & UX4G / GIGW 3.0 COMPLIANT)
   ========================================================================== */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  /* Color Palette */
  --primary: #102B50;           /* Deep Navy Blue */
  --primary-dark: #0B1E38;      /* Top utility bar & dark accents */
  --primary-light: #1A3E6D;     /* Hover state for primary */
  --secondary: #1769AA;         /* Digital Governance Blue */
  --secondary-hover: #12558A;
  --secondary-light: #EBF3FA;
  --accent: #F29B38;            /* Saffron / Gold */
  --accent-hover: #D98220;
  --accent-light: #FEF5EA;
  --text-primary: #1E293B;      /* Slate 800 */
  --text-secondary: #475569;    /* Slate 600 */
  --text-muted: #64748B;        /* Slate 500 */
  --bg-page: #F5F7FA;           /* Crisp Slate Background */
  --bg-card: #FFFFFF;
  --bg-subtle: #F8FAFC;
  --border: #E2E8F0;
  --border-subtle: #F1F5F9;
  
  /* Status Colors */
  --badge-live: #0F766E;
  --badge-live-bg: #CCFBF1;
  --badge-extended: #D97706;
  --badge-extended-bg: #FEF3C7;
  --badge-closed: #64748B;
  --badge-closed-bg: #F1F5F9;
  --badge-cancelled: #DC2626;
  --badge-cancelled-bg: #FEE2E2;

  /* Surface & Status Aliases */
  --surface-alt: #F8FAFC;
  --status-live: #0F766E;

  /* Typography */
  --font-base: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-hi: 'Noto Sans Devanagari', 'Inter', -apple-system, sans-serif;
  --root-font-size: 16px;
  --line-height-en: 1.5;
  --line-height-hi: 1.68;

  /* Elevations & Shapes */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -1px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -2px rgba(0,0,0,0.04);
  --shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 20px;
  --radius-full: 9999px;

  --container-max: 1280px;
  --header-height: 78px;
  --topbar-height: 42px;
  --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* High Contrast Mode */
body.contrast-mode {
  --primary: #000000;
  --primary-dark: #000000;
  --primary-light: #1A1A1A;
  --secondary: #FFFF00;
  --secondary-hover: #E6E600;
  --secondary-light: #222200;
  --accent: #FFFF00;
  --accent-hover: #FFFF66;
  --accent-light: #333300;
  --text-primary: #FFFFFF;
  --text-secondary: #E2E8F0;
  --text-muted: #CBD5E1;
  --bg-page: #000000;
  --bg-card: #121212;
  --bg-subtle: #1E1E1E;
  --border: #FFFF00;
  --border-subtle: #888800;
  --shadow-sm: none;
  --shadow-md: none;
  --shadow-lg: 0 0 0 1px #FFFF00;
  --shadow-xl: 0 0 0 2px #FFFF00;
  --badge-live: #00FF00;
  --badge-live-bg: #003300;
  --badge-extended: #FFFF00;
  --badge-extended-bg: #333300;
  --badge-closed: #CCCCCC;
  --badge-closed-bg: #222222;
  --badge-cancelled: #FF3333;
  --badge-cancelled-bg: #440000;
  --surface-alt: #1E293B;
  --status-live: #34D399;
  color: #FFFFFF !important;
  background-color: #000000 !important;
}

body.contrast-mode a,
body.contrast-mode button,
body.contrast-mode .nav-link,
body.contrast-mode h1,
body.contrast-mode h2,
body.contrast-mode h3,
body.contrast-mode h4,
body.contrast-mode p {
  color: #FFFFFF !important;
}

body.contrast-mode button.btn-primary,
body.contrast-mode .badge,
body.contrast-mode .accent-text {
  color: #000000 !important;
  background-color: #FFFF00 !important;
  border-color: #FFFF00 !important;
}

/* Accessibility Focus Outline */
:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}

/* Screen Reader Only Utility */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Skip to Content Anchor */
.skip-link {
  position: absolute;
  top: -60px;
  left: 20px;
  background: var(--accent);
  color: #000000;
  font-weight: 700;
  padding: 10px 18px;
  z-index: 10000;
  border-radius: 0 0 var(--radius-md) var(--radius-md);
  box-shadow: var(--shadow-lg);
  text-decoration: none;
  transition: top 0.2s ease;
}
.skip-link:focus {
  top: 0;
}

html {
  font-size: var(--root-font-size);
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-base);
  color: var(--text-primary);
  background-color: var(--bg-page);
  line-height: var(--line-height-en);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

[data-lang="hi"] body,
body[data-lang="hi"] {
  font-family: var(--font-hi);
  line-height: var(--line-height-hi);
}

a {
  color: inherit;
  text-decoration: none;
  transition: var(--transition);
}

img, svg {
  display: block;
  max-width: 100%;
}

button, input, select, textarea {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  border: none;
  background: none;
}

button {
  cursor: pointer;
}

.container {
  width: 100%;
  max-width: var(--container-max);
  margin-left: auto;
  margin-right: auto;
  padding-left: 24px;
  padding-right: 24px;
}

/* ==========================================================================
   2. TOP UTILITY BAR & ACCESSIBILITY CONTROLS
   ========================================================================== */
.top-utility-bar {
  background-color: var(--primary-dark);
  color: #E2E8F0;
  font-size: 0.8125rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  position: relative;
  z-index: 1010;
}

.top-utility-bar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--topbar-height);
  flex-wrap: wrap;
  gap: 8px;
}

.gov-branding-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  letter-spacing: 0.2px;
}

.gov-branding-tag svg {
  width: 18px;
  height: 18px;
  fill: var(--accent);
}

.top-bar-controls {
  display: flex;
  align-items: center;
  gap: 14px;
}

.top-control-group {
  display: flex;
  align-items: center;
  gap: 4px;
  border-right: 1px solid rgba(255, 255, 255, 0.15);
  padding-right: 12px;
}

.top-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  background: rgba(255, 255, 255, 0.08);
  color: #FFFFFF;
  font-size: 0.75rem;
  font-weight: 600;
  transition: var(--transition);
}

.top-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: var(--accent);
}

.top-btn.active {
  background: var(--accent);
  color: #000000;
}

.lang-switch-btn {
  background: rgba(242, 155, 56, 0.18);
  border: 1px solid var(--accent);
  color: var(--accent);
  padding: 3px 10px;
  font-weight: 700;
  border-radius: var(--radius-sm);
}
.lang-switch-btn:hover {
  background: var(--accent);
  color: #000000;
}

.cms-preview-badge {
  background: linear-gradient(135deg, #1769AA, #102B50);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  font-size: 0.72rem;
  padding: 3px 10px;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  font-weight: 600;
  transition: var(--transition);
}
.cms-preview-badge:hover {
  background: var(--secondary);
  border-color: var(--accent);
}
.cms-preview-badge::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: #10B981;
  display: inline-block;
  box-shadow: 0 0 6px #10B981;
}

/* ==========================================================================
   3. MAIN HEADER & MEGA MENU NAVIGATION
   ========================================================================== */
.main-header {
  background-color: #FFFFFF;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.main-header.scrolled {
  box-shadow: var(--shadow-md);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--header-height);
  gap: 20px;
}

.brand-wrapper {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
}

.brand-logo-svg {
  width: 52px;
  height: 52px;
  flex-shrink: 0;
}

.brand-text-block {
  display: flex;
  flex-direction: column;
}

.brand-title-group {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.brand-acronym {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--primary);
  letter-spacing: -0.5px;
  line-height: 1.1;
}

.brand-acronym span {
  color: var(--accent);
}

.brand-full-name {
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--secondary);
  line-height: 1.25;
}

.brand-undertaking {
  font-size: 0.72rem;
  color: var(--text-muted);
  font-weight: 500;
  margin-top: 1px;
}

.header-right-actions {
  display: flex;
  align-items: center;
  gap: 14px;
}

.search-trigger-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--bg-page);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 8px 16px;
  color: var(--text-muted);
  font-size: 0.875rem;
  cursor: pointer;
  transition: var(--transition);
}
.search-trigger-btn:hover {
  border-color: var(--secondary);
  background: #FFFFFF;
  box-shadow: var(--shadow-sm);
  color: var(--primary);
}

.search-kbd-shortcut {
  font-size: 0.6875rem;
  background: #FFFFFF;
  border: 1px solid var(--border);
  padding: 2px 6px;
  border-radius: 4px;
  color: var(--text-secondary);
  font-weight: 700;
}

.helpline-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  background: var(--secondary-light);
  border: 1px solid rgba(23, 105, 170, 0.2);
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  color: var(--secondary);
  font-weight: 600;
}

.helpline-pill svg {
  width: 14px;
  height: 14px;
  fill: var(--secondary);
}

.hamburger-btn {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 42px;
  height: 42px;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  gap: 5px;
}
.hamburger-btn span {
  display: block;
  width: 20px;
  height: 2px;
  background: var(--primary);
  transition: var(--transition);
}

/* Desktop Navigation Menu */
.desktop-nav-bar {
  background-color: var(--primary);
  color: #FFFFFF;
  position: relative;
  z-index: 990;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.nav-menu-list {
  display: flex;
  list-style: none;
  align-items: center;
  justify-content: flex-start;
  gap: 2px;
}

.nav-item {
  position: relative;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 13px 14px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #F1F5F9;
  letter-spacing: 0.1px;
  white-space: nowrap;
  transition: var(--transition);
  border-bottom: 3px solid transparent;
}

.nav-link:hover, .nav-item.active .nav-link, .nav-item:focus-within .nav-link {
  color: #FFFFFF;
  background-color: var(--primary-light);
  border-bottom-color: var(--accent);
}

.nav-link svg.chevron {
  width: 10px;
  height: 10px;
  stroke: currentColor;
  stroke-width: 2.5;
  transition: transform 0.2s ease;
}

.nav-item:hover .nav-link svg.chevron,
.nav-item:focus-within .nav-link svg.chevron {
  transform: rotate(180deg);
}

/* Mega Menu Dropdowns */
.mega-menu-panel {
  position: absolute;
  top: 100%;
  left: 0;
  background: #FFFFFF;
  color: var(--text-primary);
  min-width: 680px;
  max-width: 820px;
  border-radius: 0 0 var(--radius-lg) var(--radius-lg);
  box-shadow: var(--shadow-xl);
  border: 1px solid var(--border);
  border-top: 3px solid var(--accent);
  padding: 24px;
  display: none;
  z-index: 1050;
  animation: slideDownFade 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-item:hover .mega-menu-panel,
.nav-item:focus-within .mega-menu-panel {
  display: block;
}

@keyframes slideDownFade {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.mega-grid-2col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.mega-grid-3col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.mega-menu-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px;
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.mega-menu-item:hover {
  background: var(--bg-page);
  transform: translateX(3px);
}

.mega-item-icon {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: var(--secondary-light);
  color: var(--secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.mega-item-icon svg {
  width: 18px;
  height: 18px;
  fill: currentColor;
}

.mega-item-text h4 {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 2px;
}

.mega-item-text p {
  font-size: 0.75rem;
  color: var(--text-muted);
  line-height: 1.35;
}

/* Mobile Drawer Menu */
.mobile-drawer {
  position: fixed;
  top: 0;
  left: -320px;
  width: 320px;
  height: 100vh;
  background: #FFFFFF;
  z-index: 9999;
  box-shadow: var(--shadow-xl);
  overflow-y: auto;
  transition: left 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

.mobile-drawer.open {
  left: 0;
}

.mobile-drawer-header {
  padding: 18px 20px;
  background: var(--primary-dark);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mobile-drawer-header h3 {
  font-size: 1rem;
  font-weight: 700;
}

.close-drawer-btn {
  color: #FFFFFF;
  font-size: 1.5rem;
  cursor: pointer;
}

.mobile-nav-list {
  list-style: none;
  padding: 16px;
}

.mobile-nav-item {
  border-bottom: 1px solid var(--border-subtle);
  padding: 12px 0;
}

.mobile-nav-link {
  font-weight: 600;
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 9998;
  display: none;
}

.drawer-backdrop.active,
.drawer-backdrop.open {
  display: block;
}

/* ==========================================================================
   4. HERO CAROUSEL & NETWORK TOPOLOGY
   ========================================================================== */
.hero-section {
  position: relative;
  background: radial-gradient(circle at 80% 20%, #174276 0%, #102B50 60%, #08162B 100%);
  color: #FFFFFF;
  overflow: hidden;
  min-height: 520px;
}

/* Animated SVG background topology */
.hero-topology-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0.28;
  pointer-events: none;
  z-index: 1;
}

.hero-topology-bg svg {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-slider-container {
  position: relative;
  z-index: 2;
  height: 100%;
  min-height: 520px;
  display: flex;
  align-items: center;
}

.hero-slide {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.6s ease, visibility 0.6s ease;
  padding: 40px 0;
}

.hero-slide.active {
  position: relative;
  opacity: 1;
  visibility: visible;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  align-items: center;
  gap: 40px;
  width: 100%;
}

.hero-content {
  max-width: 640px;
}

.hero-badge-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(242, 155, 56, 0.18);
  border: 1px solid var(--accent);
  color: var(--accent);
  padding: 6px 14px;
  border-radius: var(--radius-full);
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.3px;
  margin-bottom: 20px;
}

.hero-heading {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.8px;
  margin-bottom: 18px;
  color: #FFFFFF;
}

.hero-heading span.gradient-text {
  background: linear-gradient(90deg, #FFFFFF, var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtext {
  font-size: 1.0625rem;
  line-height: 1.6;
  color: #CBD5E1;
  margin-bottom: 28px;
}

.hero-cta-group {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  font-size: 0.9375rem;
  font-weight: 700;
  border-radius: var(--radius-md);
  transition: var(--transition);
  cursor: pointer;
  text-align: center;
  border: 1px solid transparent;
  line-height: 1.25;
}

.btn-primary,
.btn-accent {
  background-color: var(--accent);
  color: #000000;
  border: 1px solid var(--accent);
  box-shadow: 0 4px 14px rgba(242, 155, 56, 0.35);
  font-weight: 700;
}
.btn-primary:hover,
.btn-accent:hover {
  background-color: var(--accent-hover);
  border-color: var(--accent-hover);
  color: #000000;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(242, 155, 56, 0.45);
}

.btn-secondary {
  background-color: rgba(255, 255, 255, 0.12);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(4px);
}
.btn-secondary:hover {
  background-color: rgba(255, 255, 255, 0.22);
  border-color: #FFFFFF;
  transform: translateY(-2px);
}

.btn-outline-white {
  background: transparent;
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.45);
  font-weight: 600;
}
.btn-outline-white:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: #FFFFFF;
  color: #FFFFFF;
  transform: translateY(-2px);
}

.btn-outline,
.btn-outline-primary {
  background: transparent;
  color: var(--secondary);
  border: 1px solid var(--secondary);
  font-weight: 600;
}
.btn-outline:hover,
.btn-outline-primary:hover {
  background: var(--secondary);
  color: #FFFFFF;
  transform: translateY(-2px);
}

.btn-sm {
  padding: 6px 12px;
  font-size: 0.78rem;
}

/* Explicit SVG sizing rules across interactive buttons & links */
.top-btn svg,
.search-trigger-btn svg,
.persona-link svg,
.project-action-btn svg,
.corrigendum-toggle-btn svg,
.footer-links-list a svg,
.btn svg {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.hero-visual-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-isometric-card {
  width: 100%;
  max-width: 440px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-xl);
  padding: 24px;
  box-shadow: var(--shadow-xl);
  backdrop-filter: blur(10px);
  animation: floatSubtle 6s ease-in-out infinite;
}

@keyframes floatSubtle {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

@media (prefers-reduced-motion: reduce) {
  .hero-isometric-card {
    animation: none;
  }
}

/* Slider Controls Bar */
.hero-controls-bar {
  position: absolute;
  bottom: 24px;
  left: 0;
  right: 0;
  z-index: 10;
}

.hero-controls-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.slider-dots {
  display: flex;
  align-items: center;
  gap: 10px;
}

.slider-dot {
  width: 32px;
  height: 6px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.28);
  cursor: pointer;
  transition: var(--transition);
}

.slider-dot.active {
  background: var(--accent);
  width: 54px;
}

.slider-arrows {
  display: flex;
  align-items: center;
  gap: 10px;
}

.slider-arrow-btn, .slider-pause-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.slider-arrow-btn:hover, .slider-pause-btn:hover {
  background: var(--accent);
  color: #000000;
  border-color: var(--accent);
}

/* ==========================================================================
   5. PERSONA-BASED QUICK ACCESS (4 ROLE CARDS)
   ========================================================================== */
.persona-section {
  position: relative;
  z-index: 10;
  margin-top: -50px;
  margin-bottom: 50px;
}

.persona-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.persona-card {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border);
  padding: 24px;
  box-shadow: var(--shadow-md);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.persona-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--secondary);
  transition: height 0.2s ease, background 0.2s ease;
}

.persona-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-xl);
  border-color: var(--secondary);
}

.persona-card:hover::before {
  height: 6px;
  background: var(--accent);
}

.persona-icon-box {
  width: 50px;
  height: 50px;
  border-radius: var(--radius-md);
  background: var(--secondary-light);
  color: var(--secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  transition: var(--transition);
}

.persona-card:hover .persona-icon-box {
  background: var(--accent);
  color: #000000;
}

.persona-icon-box svg {
  width: 26px;
  height: 26px;
  fill: currentColor;
}

.persona-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 8px;
}

.persona-desc {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 20px;
  flex-grow: 1;
}

.persona-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--secondary);
  margin-top: auto;
}

.persona-card:hover .persona-link {
  color: var(--accent-hover);
}

/* ==========================================================================
   6. QUICK ACCESS SERVICE STRIP (8 ICON TILES)
   ========================================================================== */
.quick-strip-section {
  padding: 20px 0 50px 0;
}

.section-header-block {
  text-align: center;
  max-width: 720px;
  margin: 0 auto 36px auto;
}

.section-header-block:has(.section-header-flex),
.section-header-block.has-flex {
  max-width: 100%;
  text-align: left;
  margin-bottom: 28px;
}

.section-header-flex {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 16px;
  text-align: left;
}

.section-eyebrow {
  display: inline-block;
  font-size: 0.8125rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--secondary);
  margin-bottom: 8px;
}

.section-heading {
  font-size: 2rem;
  font-weight: 800;
  color: var(--primary);
  letter-spacing: -0.5px;
  line-height: 1.25;
  margin-bottom: 12px;
}

.section-subtext {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

.tiles-grid-8 {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 14px;
}

.service-tile {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 18px 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  cursor: pointer;
  position: relative;
}

.service-tile:hover {
  transform: translateY(-4px);
  border-color: var(--secondary);
  box-shadow: var(--shadow-md);
  background: var(--bg-subtle);
}

.tile-icon-wrapper {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--bg-page);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary);
  transition: var(--transition);
}

.service-tile:hover .tile-icon-wrapper {
  background: var(--secondary);
  color: #FFFFFF;
}

.tile-icon-wrapper svg {
  width: 22px;
  height: 22px;
  fill: currentColor;
}

.tile-label {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--primary);
  line-height: 1.3;
}

.tile-badge {
  position: absolute;
  top: 6px;
  right: 6px;
  font-size: 0.65rem;
  font-weight: 800;
  background: var(--accent);
  color: #000000;
  padding: 2px 6px;
  border-radius: var(--radius-full);
}

/* ==========================================================================
   7. MPSeDC AT A GLANCE (ANIMATED STATS STRIP)
   ========================================================================== */
.stats-banner-section {
  background: linear-gradient(135deg, var(--primary) 0%, #0F2342 100%);
  color: #FFFFFF;
  padding: 50px 0;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 2px 8px rgba(0,0,0,0.2);
}

.stats-banner-section::after {
  content: "";
  position: absolute;
  right: -50px;
  bottom: -50px;
  width: 260px;
  height: 260px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(242, 155, 56, 0.15) 0%, transparent 70%);
  pointer-events: none;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 24px;
  text-align: center;
}

.stat-item-card {
  padding: 12px;
  position: relative;
}

.stat-item-card:not(:last-child)::after {
  content: "";
  position: absolute;
  right: 0;
  top: 20%;
  height: 60%;
  width: 1px;
  background: rgba(255, 255, 255, 0.15);
}

.stat-number {
  font-size: 2.75rem;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: -1px;
  line-height: 1.1;
  margin-bottom: 6px;
  font-feature-settings: "tnum";
}

.stat-label {
  font-size: 0.9375rem;
  font-weight: 600;
  color: #E2E8F0;
  line-height: 1.4;
}

.stat-demo-tag {
  display: inline-block;
  font-size: 0.65rem;
  color: #94A3B8;
  margin-top: 4px;
}

/* ==========================================================================
   8. PROJECTS & TECHNOLOGY VERTICALS
   ========================================================================== */
.projects-section {
  padding: 70px 0;
  background-color: var(--bg-page);
}

.filter-pills-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 36px;
}

.filter-pill-btn {
  padding: 8px 20px;
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-secondary);
  transition: var(--transition);
  cursor: pointer;
}

.filter-pill-btn:hover {
  border-color: var(--secondary);
  color: var(--secondary);
}

.filter-pill-btn.active {
  background: var(--secondary);
  color: #FFFFFF;
  border-color: var(--secondary);
  box-shadow: 0 4px 10px rgba(23, 105, 170, 0.3);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.project-card {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--secondary);
}

.project-card-header {
  height: 140px;
  background: linear-gradient(135deg, #102B50 0%, #1A3E6D 100%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  padding: 20px;
}

.project-card-icon {
  width: 56px;
  height: 56px;
  background: rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-md);
  border: 1px solid rgba(255, 255, 255, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent);
}

.project-card-icon svg {
  width: 28px;
  height: 28px;
  fill: currentColor;
}

.project-tag-badge {
  position: absolute;
  top: 14px;
  right: 14px;
  font-size: 0.7rem;
  font-weight: 700;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  padding: 4px 10px;
  border-radius: var(--radius-full);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.project-card-body {
  padding: 24px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.project-name {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 8px;
}

.project-desc {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.55;
  margin-bottom: 20px;
}

.project-action-btn {
  align-self: flex-start;
  padding: 8px 16px;
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--secondary);
  border: 1px solid var(--secondary);
  border-radius: var(--radius-md);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition);
}

.project-action-btn:hover {
  background: var(--secondary);
  color: #FFFFFF;
}

/* ==========================================================================
   9. INTERACTIVE TENDER & RFP HUB (SHOWCASE MODULE)
   ========================================================================== */
.tenders-section {
  padding: 70px 0;
  background-color: #FFFFFF;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

.tenders-filter-card {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}

.tenders-filter-grid {
  display: grid;
  grid-template-columns: 2fr 1.2fr 1.2fr auto;
  gap: 16px;
  align-items: end;
}

.filter-field-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.filter-label {
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--primary);
}

.form-control-input, .form-control-select {
  width: 100%;
  padding: 10px 14px;
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  color: var(--text-primary);
  transition: var(--transition);
}

.form-control-input:focus, .form-control-select:focus {
  border-color: var(--secondary);
  box-shadow: 0 0 0 3px rgba(23, 105, 170, 0.15);
}

.btn-reset-filters {
  padding: 10px 18px;
  background: #FFFFFF;
  border: 1px solid var(--border);
  color: var(--text-secondary);
  font-weight: 600;
  border-radius: var(--radius-md);
  font-size: 0.875rem;
}
.btn-reset-filters:hover {
  background: var(--border-subtle);
  color: var(--primary);
}

/* Tender Table */
.tender-table-container {
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  margin-bottom: 20px;
}

.table-responsive {
  width: 100%;
  overflow-x: auto;
}

.tender-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
  text-align: left;
}

.tender-table thead {
  background: var(--primary);
  color: #FFFFFF;
}

.tender-table th {
  padding: 14px 18px;
  font-weight: 700;
  letter-spacing: 0.3px;
  white-space: nowrap;
}

.tender-table tbody tr {
  border-bottom: 1px solid var(--border);
  transition: var(--transition);
}

.tender-table tbody tr:hover {
  background-color: var(--secondary-light);
}

.tender-table td {
  padding: 14px 18px;
  vertical-align: middle;
}

.tender-id-cell {
  font-family: monospace;
  font-weight: 700;
  color: var(--secondary);
}

.tender-title-cell {
  font-weight: 600;
  color: var(--primary);
  max-width: 320px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.badge-live {
  background: var(--badge-live-bg);
  color: var(--badge-live);
}

.badge-extended {
  background: var(--badge-extended-bg);
  color: var(--badge-extended);
}

.badge-closed {
  background: var(--badge-closed-bg);
  color: var(--badge-closed);
}

.badge-cancelled {
  background: var(--badge-cancelled-bg);
  color: var(--badge-cancelled);
}

.corrigendum-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  background: #FEF3C7;
  color: #92400E;
  font-size: 0.75rem;
  font-weight: 700;
  border-radius: var(--radius-sm);
  border: 1px solid #FCD34D;
  margin-top: 6px;
  cursor: pointer;
}

.corrigendum-toggle-btn:hover {
  background: #FDE68A;
}

/* Accordion nested rows */
.corrigendum-row {
  background: #FFFBEB !important;
  display: none;
}

.corrigendum-row.open {
  display: table-row;
}

.corrigendum-content-box {
  padding: 16px 20px;
  border-left: 4px solid var(--accent);
}

.corrigendum-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.8125rem;
  margin-top: 8px;
}

.corrigendum-table th, .corrigendum-table td {
  padding: 8px 12px;
  border-bottom: 1px solid #FDE68A;
}

.corrigendum-table th {
  background: rgba(242, 155, 56, 0.15);
  color: #92400E;
  font-weight: 700;
}

.date-original-struck {
  text-decoration: line-through;
  color: var(--text-muted);
  font-size: 0.78rem;
  display: block;
}

.date-revised-highlight {
  color: #B45309;
  font-weight: 700;
}

/* Table Pagination Bar */
.pagination-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.pagination-info {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.pagination-buttons {
  display: flex;
  align-items: center;
  gap: 6px;
}

.page-btn {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  border: 1px solid var(--border);
  background: #FFFFFF;
  font-weight: 600;
  font-size: 0.875rem;
}

.page-btn:hover:not(:disabled) {
  border-color: var(--secondary);
  color: var(--secondary);
}

.page-btn.active {
  background: var(--secondary);
  color: #FFFFFF;
  border-color: var(--secondary);
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ==========================================================================
   10. IT PARKS & INFRASTRUCTURE INTERACTIVE EXPLORER
   ========================================================================== */
.itparks-section {
  padding: 70px 0;
  background-color: var(--bg-page);
}

.itparks-explorer-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 32px;
  align-items: start;
}

.map-container-card {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 24px;
  box-shadow: var(--shadow-md);
  position: relative;
}

.mp-svg-map-wrapper {
  position: relative;
  width: 100%;
  max-width: 620px;
  margin: 0 auto;
}

.mp-state-svg {
  width: 100%;
  height: auto;
  filter: drop-shadow(0 8px 18px rgba(16, 43, 80, 0.12));
}

.map-pin-btn {
  position: absolute;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 10;
}

.map-pin-btn:hover {
  transform: translate(-50%, -60%) scale(1.1);
  z-index: 20;
}

.pin-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--secondary);
  border: 3px solid #FFFFFF;
  box-shadow: 0 0 10px rgba(23, 105, 170, 0.6);
  position: relative;
}

.map-pin-btn.active .pin-dot {
  background: var(--accent);
  box-shadow: 0 0 16px rgba(242, 155, 56, 0.9);
}

.pin-dot::after {
  content: "";
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid var(--secondary);
  opacity: 0.7;
  animation: pulsePin 2s infinite;
}

.map-pin-btn.active .pin-dot::after {
  border-color: var(--accent);
}

@keyframes pulsePin {
  0% { transform: scale(0.8); opacity: 1; }
  100% { transform: scale(1.8); opacity: 0; }
}

.pin-label-pill {
  margin-top: 4px;
  background: var(--primary-dark);
  color: #FFFFFF;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  white-space: nowrap;
  box-shadow: var(--shadow-sm);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.map-pin-btn.active .pin-label-pill {
  background: var(--accent);
  color: #000000;
}

/* IT Park Live Dossier Card */
.itpark-dossier-card {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 30px;
  box-shadow: var(--shadow-md);
  position: relative;
}

.dossier-header {
  border-bottom: 1px solid var(--border);
  padding-bottom: 18px;
  margin-bottom: 20px;
}

.dossier-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 6px;
}

.dossier-district {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--secondary);
  font-weight: 600;
  font-size: 0.875rem;
}

.dossier-specs-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.spec-box {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 14px;
}

.spec-box-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  font-weight: 600;
  margin-bottom: 4px;
}

.spec-box-val {
  font-size: 1.0625rem;
  font-weight: 800;
  color: var(--primary);
}

.tenants-block {
  margin-bottom: 26px;
}

.tenants-title {
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 10px;
}

.tenant-badges-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tenant-chip {
  background: var(--bg-page);
  border: 1px solid var(--border);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  color: var(--primary);
}

/* ==========================================================================
   11. POLICIES & GOVERNMENT INITIATIVES LIBRARY
   ========================================================================== */
.policies-section {
  padding: 70px 0;
  background-color: #FFFFFF;
}

.policies-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.policy-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 26px;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.policy-card:hover {
  transform: translateY(-5px);
  border-color: var(--secondary);
  box-shadow: var(--shadow-md);
}

.policy-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.policy-year-badge {
  font-size: 0.75rem;
  font-weight: 800;
  background: var(--accent-light);
  color: var(--accent-hover);
  border: 1px solid var(--accent);
  padding: 3px 10px;
  border-radius: var(--radius-full);
}

.policy-category-tag {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--secondary);
}

.policy-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--primary);
  line-height: 1.35;
  margin-bottom: 12px;
}

.policy-highlights-list {
  list-style: none;
  margin-bottom: 22px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.policy-highlights-list li {
  font-size: 0.8125rem;
  color: var(--text-secondary);
  display: flex;
  align-items: flex-start;
  gap: 8px;
  line-height: 1.4;
}

.policy-highlights-list li svg {
  width: 14px;
  height: 14px;
  fill: #10B981;
  flex-shrink: 0;
  margin-top: 3px;
}

.policy-actions-group {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: auto;
}

/* ==========================================================================
   12. LATEST NEWS, RECRUITMENT & CIRCULARS
   ========================================================================== */
.updates-section {
  padding: 70px 0;
  background-color: var(--bg-page);
}

.updates-card-box {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.updates-tabs-header {
  background: var(--primary);
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.updates-tabs-list {
  display: flex;
  list-style: none;
  overflow-x: auto;
}

.update-tab-btn {
  padding: 16px 20px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #CBD5E1;
  border-bottom: 3px solid transparent;
  white-space: nowrap;
  transition: var(--transition);
}

.update-tab-btn:hover {
  color: #FFFFFF;
}

.update-tab-btn.active {
  color: #FFFFFF;
  border-bottom-color: var(--accent);
  background: rgba(255, 255, 255, 0.08);
}

.updates-archive-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #FFFFFF;
  font-size: 0.8125rem;
  font-weight: 600;
}

.switch-control {
  position: relative;
  display: inline-block;
  width: 38px;
  height: 20px;
}

.switch-control input {
  opacity: 0;
  width: 0;
  height: 0;
}

.switch-slider {
  position: absolute;
  cursor: pointer;
  inset: 0;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 20px;
  transition: .3s;
}

.switch-slider:before {
  position: absolute;
  content: "";
  height: 14px;
  width: 14px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  border-radius: 50%;
  transition: .3s;
}

input:checked + .switch-slider {
  background-color: var(--accent);
}

input:checked + .switch-slider:before {
  transform: translateX(18px);
}

.updates-list-container {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.update-item-row {
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  background: #FFFFFF;
  transition: var(--transition);
  cursor: pointer;
}

.update-item-row:hover {
  border-color: var(--secondary);
  background: var(--bg-subtle);
  transform: translateX(4px);
}

.update-item-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.update-title-col {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.update-date-badge {
  font-size: 0.75rem;
  font-weight: 700;
  background: var(--secondary-light);
  color: var(--secondary);
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  white-space: nowrap;
}

.update-title-text {
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--primary);
}

.update-meta-badge {
  font-size: 0.72rem;
  font-family: monospace;
  color: var(--text-muted);
}

.update-expandable-body {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px dashed var(--border);
  font-size: 0.8125rem;
  color: var(--text-secondary);
  display: none;
}

.update-item-row.expanded .update-expandable-body {
  display: block;
}

/* ==========================================================================
   13. MODALS SYSTEM (GLOBAL SEARCH, TENDER, DOSSIER, ESTIMATOR, CMS)
   ========================================================================== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(11, 30, 56, 0.65);
  backdrop-filter: blur(4px);
  z-index: 9999;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
  opacity: 0;
  transition: opacity 0.25s ease;
}

.modal-overlay.open {
  display: flex;
  opacity: 1;
}

.modal-dialog {
  background: #FFFFFF;
  border-radius: var(--radius-xl);
  max-width: 760px;
  width: 100%;
  max-height: 88vh;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-xl);
  border: 1px solid var(--border);
  overflow: hidden;
  animation: modalScaleUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.modal-dialog.modal-lg {
  max-width: 960px;
}

@keyframes modalScaleUp {
  from {
    transform: scale(0.94);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

.modal-header {
  padding: 20px 26px;
  background: var(--primary);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 800;
}

.modal-close-btn {
  color: #FFFFFF;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  cursor: pointer;
  transition: var(--transition);
}
.modal-close-btn:hover {
  background: var(--accent);
  color: #000000;
}

.modal-body {
  padding: 26px;
  overflow-y: auto;
  font-size: 0.9375rem;
  line-height: 1.6;
}

.modal-footer {
  padding: 16px 26px;
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
}

/* Global Search Overlay Special Styling */
.search-modal-box {
  max-width: 700px;
  width: 100%;
  background: #FFFFFF;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  overflow: hidden;
  border: 1px solid var(--border);
}

.search-input-header {
  padding: 18px 24px;
  background: #FFFFFF;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-input-header svg {
  width: 22px;
  height: 22px;
  fill: var(--secondary);
}

.search-field-input {
  width: 100%;
  font-size: 1.15rem;
  color: var(--text-primary);
  font-weight: 600;
}

.search-results-container {
  max-height: 440px;
  overflow-y: auto;
  padding: 16px;
}

.search-result-item {
  padding: 12px 14px;
  border-radius: var(--radius-md);
  margin-bottom: 6px;
  cursor: pointer;
  transition: var(--transition);
  border: 1px solid transparent;
}

.search-result-item:hover, .search-result-item.selected {
  background: var(--secondary-light);
  border-color: rgba(23, 105, 170, 0.3);
}

.search-result-category {
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--secondary);
  text-transform: uppercase;
}

.search-result-title {
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--primary);
  margin-top: 2px;
}

mark {
  background: #FEF08A;
  color: #854D0E;
  padding: 1px 3px;
  border-radius: 3px;
}

/* Mini Incentive Estimator in Policy Modal */
.estimator-calc-card {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 22px;
  margin-top: 20px;
}

.estimator-inputs-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 20px;
}

.estimator-results-box {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 18px;
  box-shadow: var(--shadow-sm);
}

.estimator-total-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 2px solid var(--border);
  padding-top: 12px;
  margin-top: 12px;
  font-size: 1.125rem;
  font-weight: 800;
  color: var(--badge-live);
}

/* ==========================================================================
   14. COMPREHENSIVE GOVERNMENT FOOTER
   ========================================================================== */
.main-footer {
  background-color: var(--primary-dark);
  color: #CBD5E1;
  font-size: 0.875rem;
  padding-top: 60px;
  border-top: 4px solid var(--accent);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1.2fr;
  gap: 36px;
  padding-bottom: 50px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-col-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 18px;
  position: relative;
  padding-bottom: 8px;
}

.footer-col-title::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 32px;
  height: 2px;
  background: var(--accent);
}

.footer-links-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-links-list a {
  color: #CBD5E1;
  transition: var(--transition);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.footer-links-list a:hover {
  color: var(--accent);
  transform: translateX(4px);
}

.footer-address-text {
  line-height: 1.6;
  margin-bottom: 16px;
}

.footer-contact-item {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.footer-contact-item svg {
  width: 16px;
  height: 16px;
  fill: var(--accent);
}

.footer-bottom-strip {
  padding: 24px 0;
  font-size: 0.8125rem;
  color: #94A3B8;
}

.footer-bottom-flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}

.footer-badge-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.08);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  color: #E2E8F0;
  font-size: 0.75rem;
}

/* Toast Container */
.toast-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 11000;
  display: flex;
  flex-direction: column;
  gap: 10px;
  pointer-events: none;
}

.toast-msg {
  background: var(--primary);
  color: #FFFFFF;
  border-left: 4px solid var(--accent);
  padding: 14px 20px;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-xl);
  font-size: 0.875rem;
  font-weight: 600;
  pointer-events: auto;
  display: flex;
  align-items: center;
  gap: 10px;
  animation: toastSlideIn 0.3s ease;
}

@keyframes toastSlideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Back to Top Floating Button */
.back-to-top-btn {
  position: fixed;
  bottom: 26px;
  right: 26px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--secondary);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-lg);
  cursor: pointer;
  z-index: 900;
  opacity: 0;
  visibility: hidden;
  transition: var(--transition);
}

.back-to-top-btn.visible {
  opacity: 1;
  visibility: visible;
}

.back-to-top-btn:hover {
  background: var(--accent);
  color: #000000;
  transform: translateY(-4px);
}

/* ==========================================================================
   15. RESPONSIVE BREAKPOINTS (DESKTOP, LAPTOP, TABLET, MOBILE)
   ========================================================================== */
@media (max-width: 1200px) {
  .tiles-grid-8 {
    grid-template-columns: repeat(4, 1fr);
  }
  .persona-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .stats-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .stat-item-card:nth-child(3)::after {
    display: none;
  }
  .projects-grid, .policies-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .itparks-explorer-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 992px) {
  .desktop-nav-bar {
    display: none;
  }
  .hamburger-btn {
    display: flex;
  }
  .hero-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .hero-content {
    max-width: 100%;
    margin: 0 auto;
  }
  .hero-cta-group {
    justify-content: center;
  }
  .hero-visual-col {
    display: none;
  }
  .tenders-filter-grid {
    grid-template-columns: 1fr 1fr;
  }
  .footer-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 768px) {
  :root {
    --header-height: 68px;
  }
  .top-utility-bar {
    display: none; /* Accessible controls moved to mobile drawer */
  }
  .persona-section {
    margin-top: 20px;
  }
  .persona-grid {
    grid-template-columns: 1fr;
  }
  .tiles-grid-8 {
    grid-template-columns: repeat(2, 1fr);
  }
  .stats-grid {
    grid-template-columns: 1fr;
  }
  .stat-item-card::after {
    display: none !important;
  }
  .projects-grid, .policies-grid {
    grid-template-columns: 1fr;
  }
  .tenders-filter-grid {
    grid-template-columns: 1fr;
  }
  .footer-grid {
    grid-template-columns: 1fr;
  }
  .estimator-inputs-grid {
    grid-template-columns: 1fr;
  }
  .hero-heading {
    font-size: 1.875rem;
  }
}
"""
