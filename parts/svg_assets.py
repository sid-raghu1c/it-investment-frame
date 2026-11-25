# parts/svg_assets.py
# High-Definition Inline SVG Assets for MPSeDC Modernized Portal
# Zero external image dependencies - 100% self-contained vectors

MPSEDC_LOGO_SVG = """<svg class="logo-crest-svg" viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1769AA"/>
      <stop offset="100%" stop-color="#102B50"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDBA74"/>
      <stop offset="100%" stop-color="#F29B38"/>
    </linearGradient>
  </defs>
  <!-- Outer Tech Shield Octagon -->
  <polygon points="27,2 49,11 52,36 37,51 17,51 2,36 5,11" fill="url(#logoGrad)" stroke="#F29B38" stroke-width="1.8"/>
  <!-- Circuit Grid Lines -->
  <path d="M12 27 H22 M32 27 H42 M27 12 V22 M27 32 V42" stroke="rgba(255,255,255,0.3)" stroke-width="1.2" stroke-dasharray="2 2"/>
  <circle cx="12" cy="27" r="2" fill="#F29B38"/>
  <circle cx="42" cy="27" r="2" fill="#F29B38"/>
  <circle cx="27" cy="12" r="2" fill="#F29B38"/>
  <circle cx="27" cy="42" r="2" fill="#F29B38"/>
  <!-- Stylized MP State Heart/Diamond Shape -->
  <path d="M27 16 L38 27 L27 38 L16 27 Z" fill="#FFFFFF" fill-opacity="0.12" stroke="url(#goldGrad)" stroke-width="2"/>
  <!-- Microchip Core -->
  <rect x="23" y="23" width="8" height="8" rx="1.5" fill="#F29B38"/>
  <!-- Digital Pulse Nodes -->
  <circle cx="27" cy="27" r="2" fill="#FFFFFF"/>
</svg>"""

LION_CAPITAL_EMBLEM_SVG = """<svg class="ashoka-emblem-svg" viewBox="0 0 32 38" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="State Emblem of India motif">
  <path d="M16 3 C12 3 9 6 9 10 C9 14 12 17 16 17 C20 17 23 14 23 10 C23 6 20 3 16 3 Z" fill="#D97706" fill-opacity="0.85"/>
  <path d="M6 10 C4 10 3 12 3 15 C3 18 5 20 8 20 C10 20 11 18 11 15 C11 12 9 10 6 10 Z" fill="#D97706" fill-opacity="0.75"/>
  <path d="M26 10 C28 10 29 12 29 15 C29 18 27 20 24 20 C22 20 21 18 21 15 C21 12 23 10 26 10 Z" fill="#D97706" fill-opacity="0.75"/>
  <rect x="4" y="23" width="24" height="4" rx="1" fill="#B45309"/>
  <circle cx="16" cy="25" r="1.8" fill="#FFFFFF"/>
  <path d="M7 29 L25 29 L23 34 L9 34 Z" fill="#92400E"/>
  <rect x="5" y="34" width="22" height="2" fill="#78350F"/>
</svg>"""

MP_MAP_SVG = """<svg class="mp-state-svg" viewBox="0 0 800 560" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Interactive Map of Madhya Pradesh IT Parks">
  <defs>
    <linearGradient id="mpMapGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EDF4FB"/>
      <stop offset="50%" stop-color="#E2EEF9"/>
      <stop offset="100%" stop-color="#D4E5F6"/>
    </linearGradient>
    <filter id="mapGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#102B50" flood-opacity="0.15"/>
    </filter>
    <pattern id="cyberGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(23, 105, 170, 0.08)" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- Background Cyber Grid inside map frame -->
  <rect width="800" height="560" rx="12" fill="url(#cyberGrid)" opacity="0.7"/>

  <!-- High-Fidelity Silhouette Path of Madhya Pradesh State -->
  <g filter="url(#mapGlow)">
    <path class="mp-boundary-path" d="M 360,35
      C 375,32 405,30 425,38
      C 440,44 460,55 465,75
      C 470,95 460,115 450,135
      C 465,145 490,140 515,150
      C 540,160 565,180 585,175
      C 605,170 635,185 660,195
      C 690,205 720,215 745,240
      C 770,265 765,290 740,310
      C 715,330 685,320 660,345
      C 640,365 625,395 600,410
      C 575,425 550,420 530,440
      C 510,460 480,480 450,475
      C 420,470 390,445 365,450
      C 340,455 315,480 285,475
      C 255,470 230,445 205,435
      C 180,425 150,420 135,395
      C 120,370 130,340 145,320
      C 160,300 155,275 170,250
      C 185,225 210,210 235,195
      C 260,180 275,155 295,140
      C 315,125 330,95 345,65
      Z"
      fill="url(#mpMapGradient)"
      stroke="#1769AA"
      stroke-width="2.5"
      stroke-linejoin="round"/>
  </g>

  <!-- District Division Wireframe Accents -->
  <g class="mp-district-lines" stroke="#1769AA" stroke-width="1" stroke-opacity="0.2" fill="none">
    <!-- Chambal & Gwalior region divider -->
    <path d="M 425,40 C 420,80 435,120 450,140" stroke-dasharray="4 3"/>
    <!-- Malwa / Indore region divider -->
    <path d="M 145,320 C 200,310 250,330 300,345" stroke-dasharray="4 3"/>
    <!-- Central / Bhopal region ring -->
    <circle cx="375" cy="300" r="65" stroke-dasharray="3 3" stroke-opacity="0.25"/>
    <!-- Mahakoshal / Jabalpur region divider -->
    <path d="M 500,260 C 530,300 560,340 590,370" stroke-dasharray="4 3"/>
    <!-- Bundelkhand / Rewa corridor -->
    <path d="M 480,140 C 540,190 600,210 670,230" stroke-dasharray="4 3"/>
  </g>

  <!-- Major Digital Backbone Fiber Corridors (Optical Fiber Lines) -->
  <g class="backbone-fiber-corridors" stroke="#102B50" stroke-width="2" stroke-dasharray="6 4" stroke-opacity="0.4">
    <!-- Bhopal to Indore -->
    <line x1="375" y1="300" x2="265" y2="345"/>
    <!-- Bhopal to Gwalior -->
    <line x1="375" y1="300" x2="425" y2="115"/>
    <!-- Gwalior to Malanpur -->
    <line x1="425" y1="115" x2="455" y2="95"/>
    <!-- Bhopal to Jabalpur -->
    <line x1="375" y1="300" x2="560" y2="315"/>
    <!-- Indore to Sinhasa -->
    <line x1="265" y1="345" x2="240" y2="365"/>
  </g>

  <!-- Major River Accents (Narmada River stylized) -->
  <path d="M 670,335 C 600,325 540,345 470,355 C 400,365 330,380 240,390 C 180,395 140,410 135,395"
        fill="none" stroke="#38BDF8" stroke-width="2" stroke-opacity="0.4" stroke-linecap="round"/>

  <!-- Map Legend / Watermark -->
  <g transform="translate(30, 480)" opacity="0.8">
    <rect width="170" height="52" rx="6" fill="#FFFFFF" fill-opacity="0.9" stroke="#CBD5E1"/>
    <circle cx="18" cy="18" r="6" fill="#1769AA"/>
    <text x="32" y="22" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#102B50">Operational IT Park</text>
    <circle cx="18" cy="36" r="6" fill="#F29B38"/>
    <text x="32" y="40" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#102B50">EMC / Special Cluster</text>
  </g>

  <!-- Compass Rose -->
  <g transform="translate(740, 50)" opacity="0.7">
    <circle cx="0" cy="0" r="18" fill="#FFFFFF" stroke="#CBD5E1"/>
    <polygon points="0,-14 4,-3 0,0 -4,-3" fill="#102B50"/>
    <polygon points="0,14 4,3 0,0 -4,3" fill="#94A3B8"/>
    <text x="0" y="-18" text-anchor="middle" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#102B50">N</text>
  </g>
</svg>"""

ISOMETRIC_DIGITAL_HUB_SVG = """<svg class="hero-isometric-svg" viewBox="0 0 540 420" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MPSeDC Tier-IV State Data Center and Cloud Infrastructure">
  <defs>
    <linearGradient id="hubIsoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="serverFace" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#1D4ED8"/>
    </linearGradient>
    <linearGradient id="goldAccent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDBA74"/>
      <stop offset="100%" stop-color="#F29B38"/>
    </linearGradient>
    <filter id="glowFilter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Isometric Ground Base Platform -->
  <polygon points="270,50 490,175 270,300 50,175" fill="#1E293B" stroke="#334155" stroke-width="2"/>
  <polygon points="50,175 270,300 270,335 50,210" fill="#0F172A" stroke="#1E293B"/>
  <polygon points="490,175 270,300 270,335 490,210" fill="#020617" stroke="#1E293B"/>

  <!-- Glowing Isometric Circuit Traces on Platform -->
  <path d="M 140,185 L 220,230 L 220,270 M 320,270 L 320,230 L 400,185 M 270,120 L 270,190"
        stroke="#38BDF8" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
  <circle cx="140" cy="185" r="3.5" fill="#38BDF8"/>
  <circle cx="400" cy="185" r="3.5" fill="#38BDF8"/>
  <circle cx="270" cy="120" r="3.5" fill="#F29B38"/>

  <!-- Tower 1: State Data Center Main Server Rack (Center-Left) -->
  <g class="iso-server-rack-1">
    <!-- Top Face -->
    <polygon points="180,95 240,130 200,155 140,120" fill="#3B82F6" stroke="#60A5FA" stroke-width="1.5"/>
    <!-- Left Face -->
    <polygon points="140,120 200,155 200,245 140,210" fill="#1E40AF" stroke="#1D4ED8" stroke-width="1.5"/>
    <!-- Right Face (Front Blade Rack) -->
    <polygon points="200,155 240,130 240,220 200,245" fill="#1E3A8A" stroke="#1D4ED8" stroke-width="1.5"/>
    <!-- Server Blades & LEDs -->
    <line x1="150" y1="145" x2="190" y2="168" stroke="#93C5FD" stroke-width="2"/>
    <line x1="150" y1="165" x2="190" y2="188" stroke="#93C5FD" stroke-width="2"/>
    <line x1="150" y1="185" x2="190" y2="208" stroke="#93C5FD" stroke-width="2"/>
    <circle cx="192" cy="169" r="2" fill="#10B981"/>
    <circle cx="192" cy="189" r="2" fill="#10B981"/>
    <circle cx="192" cy="209" r="2" fill="#F29B38"/>
  </g>

  <!-- Tower 2: MPSWAN Telecom & Core Router Stack (Center-Right) -->
  <g class="iso-server-rack-2">
    <!-- Top Face -->
    <polygon points="300,130 360,95 420,130 360,165" fill="#2563EB" stroke="#60A5FA" stroke-width="1.5"/>
    <!-- Left Face (Front Blades) -->
    <polygon points="300,130 360,165 360,255 300,220" fill="#1E3A8A" stroke="#1D4ED8" stroke-width="1.5"/>
    <!-- Right Face -->
    <polygon points="360,165 420,130 420,220 360,255" fill="#0F172A" stroke="#1D4ED8" stroke-width="1.5"/>
    <!-- Router Port Lights -->
    <line x1="310" y1="155" x2="350" y2="178" stroke="#93C5FD" stroke-width="2"/>
    <line x1="310" y1="175" x2="350" y2="198" stroke="#93C5FD" stroke-width="2"/>
    <line x1="310" y1="195" x2="350" y2="218" stroke="#93C5FD" stroke-width="2"/>
    <circle cx="312" cy="156" r="2" fill="#10B981"/>
    <circle cx="312" cy="176" r="2" fill="#38BDF8"/>
    <circle cx="312" cy="196" r="2" fill="#10B981"/>
  </g>

  <!-- Central Cloud Gateway Hologram (Floating Above) -->
  <g class="iso-cloud-gateway" filter="url(#glowFilter)">
    <ellipse cx="270" cy="85" rx="45" ry="22" fill="url(#serverFace)" fill-opacity="0.4" stroke="#60A5FA" stroke-width="2"/>
    <path d="M 250,85 C 250,75 260,65 270,65 C 280,65 290,75 290,85" stroke="#F29B38" stroke-width="3" fill="none"/>
    <circle cx="270" cy="85" r="8" fill="#F29B38"/>
    <circle cx="270" cy="85" r="3" fill="#FFFFFF"/>
  </g>

  <!-- Cybersecurity Shield Badge (Floating Front-Center) -->
  <g class="iso-security-shield" transform="translate(250, 220)">
    <path d="M 20,0 L 38,8 L 38,28 C 38,40 20,48 20,48 C 20,48 2,40 2,28 L 2,8 Z"
          fill="#0F172A" stroke="#F29B38" stroke-width="2.5"/>
    <path d="M 14,24 L 18,28 L 27,18" stroke="#10B981" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Metric Badges Floating -->
  <g class="iso-badge-tag-1" transform="translate(80, 75)">
    <rect width="100" height="32" rx="6" fill="#0F172A" fill-opacity="0.9" stroke="#38BDF8" stroke-width="1.2"/>
    <text x="10" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#38BDF8">SDC Tier-IV</text>
  </g>

  <g class="iso-badge-tag-2" transform="translate(380, 270)">
    <rect width="115" height="32" rx="6" fill="#0F172A" fill-opacity="0.9" stroke="#10B981" stroke-width="1.2"/>
    <text x="10" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#10B981">99.9% Core Uptime</text>
  </g>
</svg>"""

HERO_TOPOLOGY_SVG = """<svg viewBox="0 0 1440 600" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">
  <defs>
    <linearGradient id="topoLineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#F29B38" stop-opacity="0.35"/>
    </linearGradient>
    <radialGradient id="nodeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="goldNodeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F29B38" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F29B38" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Background Coordinate Matrix Grid -->
  <g opacity="0.18" stroke="#38BDF8" stroke-width="0.8">
    <line x1="0" y1="100" x2="1440" y2="100" stroke-dasharray="6 6"/>
    <line x1="0" y1="250" x2="1440" y2="250" stroke-dasharray="6 6"/>
    <line x1="0" y1="400" x2="1440" y2="400" stroke-dasharray="6 6"/>
    <line x1="180" y1="0" x2="180" y2="600" stroke-dasharray="6 6"/>
    <line x1="480" y1="0" x2="480" y2="600" stroke-dasharray="6 6"/>
    <line x1="780" y1="0" x2="780" y2="600" stroke-dasharray="6 6"/>
    <line x1="1080" y1="0" x2="1080" y2="600" stroke-dasharray="6 6"/>
    <line x1="1320" y1="0" x2="1320" y2="600" stroke-dasharray="6 6"/>
  </g>
  <!-- Circuit Fiber Highways -->
  <path d="M 40,150 L 220,150 L 320,250 L 520,250 L 600,180 L 850,180 L 950,280 L 1200,280 L 1380,420" stroke="url(#topoLineGrad)" stroke-width="2" fill="none"/>
  <path d="M 100,450 L 280,450 L 380,320 L 660,320 L 740,420 L 1020,420 L 1120,300 L 1400,300" stroke="url(#topoLineGrad)" stroke-width="1.8" stroke-dasharray="5 5" fill="none"/>
  <path d="M 240,70 L 440,70 L 540,170 L 740,170 L 860,90 L 1080,90 L 1240,210" stroke="url(#topoLineGrad)" stroke-width="1.5" fill="none"/>
  <!-- Glowing Network Nodes -->
  <g>
    <circle cx="220" cy="150" r="14" fill="url(#nodeGlow)"/>
    <circle cx="220" cy="150" r="4" fill="#38BDF8"/>
    <circle cx="520" cy="250" r="18" fill="url(#goldNodeGlow)"/>
    <circle cx="520" cy="250" r="5" fill="#F29B38"/>
    <circle cx="850" cy="180" r="16" fill="url(#nodeGlow)"/>
    <circle cx="850" cy="180" r="4" fill="#38BDF8"/>
    <circle cx="950" cy="280" r="14" fill="url(#nodeGlow)"/>
    <circle cx="950" cy="280" r="3.5" fill="#818CF8"/>
    <circle cx="380" cy="320" r="14" fill="url(#nodeGlow)"/>
    <circle cx="380" cy="320" r="3.5" fill="#38BDF8"/>
    <circle cx="660" cy="320" r="16" fill="url(#goldNodeGlow)"/>
    <circle cx="660" cy="320" r="4.5" fill="#F29B38"/>
    <circle cx="1020" cy="420" r="16" fill="url(#nodeGlow)"/>
    <circle cx="1020" cy="420" r="4" fill="#38BDF8"/>
    <circle cx="540" cy="170" r="14" fill="url(#nodeGlow)"/>
    <circle cx="540" cy="170" r="3.5" fill="#10B981"/>
    <circle cx="1200" cy="280" r="16" fill="url(#goldNodeGlow)"/>
    <circle cx="1200" cy="280" r="4" fill="#F29B38"/>
  </g>
</svg>"""

SVG_ICONS = {
  'search': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
  'close': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
  'chevron_down': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
  'chevron_up': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>',
  'chevron_left': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>',
  'chevron_right': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>',
  'arrow_right': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
  'download': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
  'external': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
  'filter': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
  'play': '<svg viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
  'pause': '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>',
  'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
  'globe': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
  'sun': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>',
  'server': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>',
  'network': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><line x1="12" y1="12" x2="12" y2="8"/></svg>',
  'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
  'building': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="9" y1="6" x2="9.01" y2="6"/><line x1="15" y1="6" x2="15.01" y2="6"/><line x1="9" y1="10" x2="9.01" y2="10"/><line x1="15" y1="10" x2="15.01" y2="10"/><line x1="9" y1="14" x2="9.01" y2="14"/><line x1="15" y1="14" x2="15.01" y2="14"/><line x1="9" y1="18" x2="15" y2="18"/></svg>',
  'drone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><line x1="10" y1="10" x2="4" y2="4"/><line x1="14" y1="10" x2="20" y2="4"/><line x1="10" y1="14" x2="4" y2="20"/><line x1="14" y1="14" x2="20" y2="20"/><circle cx="4" cy="4" r="2"/><circle cx="20" cy="4" r="2"/><circle cx="4" cy="20" r="2"/><circle cx="20" cy="20" r="2"/></svg>',
  'satellite': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="2"/><path d="M4.93 19.07a10 10 0 0 1 0-14.14"/><path d="M7.76 16.24a6 6 0 0 1 0-8.48"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/><path d="M16.24 7.76a6 6 0 0 1 0 8.48"/></svg>',
  'award': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
  'users': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
  'calendar': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
  'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  'file_text': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
  'map_pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
  'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
  'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
  'briefcase': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
  'cpu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
  'trending_up': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
  'info': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
  'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>'
}
