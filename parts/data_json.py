# parts/data_json.py
# Structured Mock JSON Datasets & Bilingual Dictionaries for MPSeDC Modernized Portal
# Embedded in <script> tags and processed dynamically via vanilla JS

import json

BILINGUAL_DICT = {
  "en": {
    "site_title": "MPSeDC | Madhya Pradesh State Electronics Development Corporation Ltd.",
    "state_gov_tag": "Government of Madhya Pradesh | Dept. of Science & Technology",
    "skip_to_content": "Skip to Main Content",
    "screen_reader": "Screen Reader Access",
    "font_size": "Font Size",
    "contrast": "High Contrast",
    "lang_toggle": "हिन्दी",
    "cms_admin": "CMS Admin Preview",
    "org_name": "MPSeDC",
    "org_subtitle": "Madhya Pradesh State Electronics Development Corporation Ltd.",
    "org_undertaking": "A Government of Madhya Pradesh Undertaking",
    "search_placeholder": "Search Tenders, Policies, Projects, Circulars (Ctrl+K)...",
    "nav_home": "Home",
    "nav_about": "About Us",
    "nav_services": "Services & Solutions",
    "nav_projects": "Projects & Infrastructure",
    "nav_policies": "Policies & Rules",
    "nav_tenders": "Tenders & RFPs",
    "nav_media": "Media & Updates",
    "nav_contact": "Contact Us",
    "hero_title": "Powering Madhya Pradesh Through Digital Innovation",
    "hero_desc": "Driving digital transformation through state-of-the-art IT infrastructure, single-window investment promotion, resilient cyber-defense, and citizen-centric governance solutions.",
    "cta_explore_services": "Explore Services",
    "cta_explore_infra": "Explore IT Infrastructure",
    "cta_investment": "Investment Opportunities",
    "persona_vendors_title": "Vendors & OEMs",
    "persona_vendors_desc": "Discover procurement opportunities, active e-tenders, hardware/software RFPs, and corrigendums.",
    "persona_vendors_cta": "Explore Live Tenders",
    "persona_investors_title": "Investors & Startups",
    "persona_investors_desc": "Discover plug-and-play IT parks, attractive capital subsidies, and policies for IT, GCC & AVGC.",
    "persona_investors_cta": "Explore Investment",
    "persona_govt_title": "Government Departments",
    "persona_govt_desc": "Leverage Tier-IV State Data Center hosting, secure MPSWAN connectivity, and e-Office suites.",
    "persona_govt_cta": "Explore G2G Services",
    "persona_citizens_title": "Citizens & Job Seekers",
    "persona_citizens_desc": "Access GET recruitment notices, summer internship rosters, recruitment exam results, and RTI.",
    "persona_citizens_cta": "Explore Updates",
    "quick_tenders": "Active Tenders",
    "quick_portal": "IT Investment Portal",
    "quick_itparks": "IT Parks & Plots",
    "quick_policies": "Policies & Rules",
    "quick_circulars": "Circulars & Orders",
    "quick_recruitment": "Recruitment & Results",
    "quick_rti": "RTI Disclosures",
    "quick_geoportal": "MP Geoportal",
    "stats_section_title": "MPSeDC at a Glance",
    "stats_section_subtitle": "Decades of driving Madhya Pradesh's technological pre-eminence and digital sovereignty.",
    "projects_section_title": "Projects & Technology Verticals",
    "projects_section_subtitle": "Pioneering state-wide digital backbones, geospatial intelligence, and institutional frameworks.",
    "tenders_section_title": "Interactive Tender & RFP Hub",
    "tenders_section_subtitle": "Transparent, electronic public procurement adhering to MP PWD & Store Purchase Rules.",
    "itparks_section_title": "IT Parks & Infrastructure Explorer",
    "itparks_section_subtitle": "Ready-to-occupy Grade-A workspaces, electronics clusters, and developed industrial plots across MP.",
    "policies_section_title": "Policies & Government Initiatives",
    "policies_section_subtitle": "Progressive, investor-friendly frameworks offering capital rebates, employment assistance & power subsidies.",
    "news_section_title": "Latest News, Recruitment & Circulars",
    "news_section_subtitle": "Timely notifications, employment rosters, corrigendum bulletins, and official state orders.",
    "footer_about_title": "About MPSeDC",
    "footer_quick_title": "Quick Links",
    "footer_govt_title": "Important Government Links",
    "footer_legal_title": "Legal & Compliance",
    "footer_address": "State IT Centre, 47-A, Arera Hills, Bhopal, Madhya Pradesh – 462011",
    "footer_copyright": "© 2026 Madhya Pradesh State Electronics Development Corporation Ltd. All Rights Reserved.",
    "footer_disclaimer": "[Demonstration Prototype] Developed for technical review and modernization benchmarking."
  },
  "hi": {
    "site_title": "एमपीएसईडीसी | मध्य प्रदेश राज्य इलेक्ट्रॉनिक्स विकास निगम लिमिटेड",
    "state_gov_tag": "मध्य प्रदेश शासन | विज्ञान एवं प्रौद्योगिकी विभाग",
    "skip_to_content": "मुख्य सामग्री पर जाएं",
    "screen_reader": "स्क्रीन रीडर एक्सेस",
    "font_size": "फ़ॉन्ट आकार",
    "contrast": "उच्च कंट्रास्ट",
    "lang_toggle": "English",
    "cms_admin": "सीएमएस एडमिन पूर्वावलोकन",
    "org_name": "एमपीएसईडीसी",
    "org_subtitle": "मध्य प्रदेश राज्य इलेक्ट्रॉनिक्स विकास निगम लिमिटेड",
    "org_undertaking": "मध्य प्रदेश शासन का उपक्रम",
    "search_placeholder": "निविदाएं, नीतियां, परियोजनाएं, परिपत्र खोजें (Ctrl+K)...",
    "nav_home": "मुख्य पृष्ठ",
    "nav_about": "हमारे बारे में",
    "nav_services": "सेवाएं एवं समाधान",
    "nav_projects": "परियोजनाएं एवं अवसंरचना",
    "nav_policies": "नीतियां एवं नियम",
    "nav_tenders": "निविदाएं एवं आरएफपी",
    "nav_media": "मीडिया एवं सूचनाएं",
    "nav_contact": "संपर्क करें",
    "hero_title": "डिजिटल नवाचार के माध्यम से मध्य प्रदेश का सशक्तिकरण",
    "hero_desc": "अत्याधुनिक आईटी अवसंरचना, एकल-खिड़की निवेश संवर्धन, मजबूत साइबर सुरक्षा एवं नागरिक-केंद्रित ई-गवर्नेंस समाधानों के साथ प्रदेश का डिजिटल कायाकल्प।",
    "cta_explore_services": "सेवाएं देखें",
    "cta_explore_infra": "आईटी अवसंरचना",
    "cta_investment": "निवेश के अवसर",
    "persona_vendors_title": "विक्रेता एवं ओईएम",
    "persona_vendors_desc": "खरीद अवसर, सक्रिय ई-निविदाएं, हार्डवेयर/सॉफ्टवेयर आरएफपी और शुद्धिपत्र प्राप्त करें।",
    "persona_vendors_cta": "सक्रिय निविदाएं देखें",
    "persona_investors_title": "निवेशक एवं स्टार्टअप",
    "persona_investors_desc": "प्लग-एंड-प्ले आईटी पार्क, आकर्षक पूंजीगत सब्सिडी तथा आईटी, जीसीसी व एवीजीसी नीतियां देखें।",
    "persona_investors_cta": "निवेश अन्वेषण करें",
    "persona_govt_title": "शासकीय विभाग",
    "persona_govt_desc": "टियर-IV स्टेट डेटा सेंटर होस्टिंग, सुरक्षित एमपीडबल्यूएएन कनेक्टिविटी और ई-ऑफिस सुइट प्राप्त करें।",
    "persona_govt_cta": "जी2जी सेवाएं देखें",
    "persona_citizens_title": "नागरिक एवं परीक्षार्थी",
    "persona_citizens_desc": "जीईटी भर्ती सूचनाएं, ग्रीष्मकालीन इंटर्नशिप रोस्टर, भर्ती परीक्षा परिणाम और आरटीआई प्राप्त करें।",
    "persona_citizens_cta": "अद्यतन सूचनाएं देखें",
    "quick_tenders": "सक्रिय निविदाएं",
    "quick_portal": "आईटी निवेश पोर्टल",
    "quick_itparks": "आईटी पार्क एवं भूखंड",
    "quick_policies": "नीतियां एवं नियम",
    "quick_circulars": "परिपत्र एवं आदेश",
    "quick_recruitment": "भर्ती एवं परिणाम",
    "quick_rti": "आरटीआई प्रकटीकरण",
    "quick_geoportal": "मध्य प्रदेश जियोपोर्टल",
    "stats_section_title": "एमपीएसईडीसी एक नज़र में",
    "stats_section_subtitle": "मध्य प्रदेश के तकनीकी नेतृत्व और डिजिटल संप्रभुता के चार दशकों की गौरवशाली यात्रा।",
    "projects_section_title": "परियोजनाएं एवं प्रौद्योगिकी कार्यक्षेत्र",
    "projects_section_subtitle": "राज्यव्यापी डिजिटल बैकबोन, भू-स्थानिक बुद्धिमत्ता और संस्थागत तंत्र का निर्माण।",
    "tenders_section_title": "इंटरैक्टिव निविदा एवं आरएफपी हब",
    "tenders_section_subtitle": "मप्र लोक निर्माण एवं भंडार क्रय नियमों के अनुरूप पारदर्शी, इलेक्ट्रॉनिक सार्वजनिक खरीद।",
    "itparks_section_title": "आईटी पार्क एवं अवसंरचना अन्वेषक",
    "itparks_section_subtitle": "मध्य प्रदेश भर में तैयार ग्रेड-ए कार्यस्थल, इलेक्ट्रॉनिक्स क्लस्टर और विकसित औद्योगिक भूखंड।",
    "policies_section_title": "नीतियां एवं शासकीय पहल",
    "policies_section_subtitle": "पूंजीगत छूट, रोजगार प्रोत्साहन और विद्युत सब्सिडी प्रदान करने वाले प्रगतिशील निवेश ढांचे।",
    "news_section_title": "नवीनतम समाचार, भर्ती एवं परिपत्र",
    "news_section_subtitle": "समयबद्ध सूचनाएं, रोजगार रोस्टर, शुद्धिपत्र बुलेटिन और आधिकारिक शासकीय आदेश।",
    "footer_about_title": "एमपीएसईडीसी के बारे में",
    "footer_quick_title": "त्वरित लिंक",
    "footer_govt_title": "महत्वपूर्ण शासकीय लिंक",
    "footer_legal_title": "विधिक एवं अनुपालन",
    "footer_address": "स्टेट आईटी सेंटर, 47-ए, अरेरा हिल्स, भोपाल, मध्य प्रदेश – 462011",
    "footer_copyright": "© 2026 मध्य प्रदेश राज्य इलेक्ट्रॉनिक्स विकास निगम लिमिटेड। सर्वाधिकार सुरक्षित।",
    "footer_disclaimer": "[प्रदर्शन प्रोटोटाइप] तकनीकी समीक्षा और आधुनिकीकरण मानक परीक्षण हेतु निर्मित।"
  }
}

TENDERS_DATA = [
  {
    "id": "TND-2026-001",
    "tender_no": "MPSEDC/SDC/2026/RFP-04",
    "title": "Selection of System Integrator for Augmentation of Tier-IV State Data Center Cloud Compute & Storage",
    "title_hi": "टियर-IV स्टेट डेटा सेंटर क्लाउड कंप्यूट और स्टोरेज के संवर्धन हेतु सिस्टम इंटीग्रेटर का चयन",
    "category": "Infrastructure",
    "published_date": "2026-02-12 11:00 IST",
    "submission_deadline": "2026-03-15 15:00 IST",
    "original_deadline": "2026-02-28 15:00 IST",
    "status": "Extended",
    "emd_val": "₹ 25,00,000",
    "doc_fee": "₹ 11,800",
    "description": "Comprehensive augmentation of hyper-converged infrastructure (HCI), NVMe flash storage tiers, and unified SDN security perimeter at SDC Bhopal.",
    "documents": [
      {"name": "RFP_SDC_Cloud_Augmentation_Vol_I.pdf", "size": "4.2 MB", "type": "RFP Document"},
      {"name": "Technical_Specifications_HCI_Storage.pdf", "size": "2.8 MB", "type": "Annexure A"},
      {"name": "Price_Bid_BOQ_Template.xls", "size": "450 KB", "type": "Commercial BOQ"}
    ],
    "corrigendums": [
      {
        "corrigendum_no": "Corrigendum No. 1",
        "date": "2026-02-22 17:30 IST",
        "memo_no": "MPSEDC/SDC/2026/CORR-01",
        "remarks": "Clarification on SLA terms and extension of Pre-Bid query submission deadline.",
        "revised_deadline": "2026-03-05 15:00 IST",
        "file_size": "850 KB"
      },
      {
        "corrigendum_no": "Corrigendum No. 2",
        "date": "2026-02-27 18:00 IST",
        "memo_no": "MPSEDC/SDC/2026/CORR-02",
        "remarks": "Revision of OEM turnover eligibility criteria and final extension of bid submission deadline.",
        "revised_deadline": "2026-03-15 15:00 IST",
        "file_size": "1.1 MB"
      }
    ]
  },
  {
    "id": "TND-2026-002",
    "tender_no": "MPSEDC/MPSWAN/2026/RFP-02",
    "title": "Empanelment of Telecom Service Providers for Redundant 10Gbps MPLS WAN Links across 55 District HQs",
    "title_hi": "55 जिला मुख्यालयों में रिडंडेंट 10Gbps एमपीएलएस वैन लिंक्स हेतु टेलीकॉम सेवा प्रदाताओं का पैनल चयन",
    "category": "Hardware",
    "published_date": "2026-02-18 10:30 IST",
    "submission_deadline": "2026-03-20 16:00 IST",
    "original_deadline": None,
    "status": "Live",
    "emd_val": "₹ 15,00,000",
    "doc_fee": "₹ 5,900",
    "description": "Establishment of high-availability dual-homed optical fiber bandwidth connectivity connecting Secretariat, Collectorates, and Tehsils.",
    "documents": [
      {"name": "RFP_MPSWAN_Telecom_2026.pdf", "size": "3.8 MB", "type": "RFP Document"},
      {"name": "District_PoP_Locations_SLA.pdf", "size": "1.5 MB", "type": "Annexure"}
    ],
    "corrigendums": []
  },
  {
    "id": "TND-2026-003",
    "tender_no": "MPSEDC/APP/2026/RFP-09",
    "title": "Development, Deployment & Maintenance of AI-Powered Citizen Grievance Analytics Engine for CM Helpline",
    "title_hi": "सीएम हेल्पलाइन हेतु एआई-संचालित नागरिक शिकायत एनालिटिक्स इंजन का विकास, परिनियोजन एवं रखरखाव",
    "category": "Software",
    "published_date": "2026-02-10 14:00 IST",
    "submission_deadline": "2026-03-12 15:00 IST",
    "original_deadline": None,
    "status": "Live",
    "emd_val": "₹ 10,00,000",
    "doc_fee": "₹ 5,900",
    "description": "Natural Language Processing (NLP) and predictive sentiment analysis stack trained on bilingual Devanagari Hindi and vernacular audio recordings.",
    "documents": [
      {"name": "RFP_AI_Grievance_Engine.pdf", "size": "5.1 MB", "type": "RFP Document"},
      {"name": "API_Integration_Architecture.pdf", "size": "3.1 MB", "type": "Annexure"}
    ],
    "corrigendums": [
      {
        "corrigendum_no": "Corrigendum No. 1",
        "date": "2026-02-25 16:00 IST",
        "memo_no": "MPSEDC/APP/2026/CORR-01",
        "remarks": "Incorporation of Indic LLM benchmarking guidelines as discussed in Pre-Bid meeting.",
        "revised_deadline": "2026-03-12 15:00 IST",
        "file_size": "620 KB"
      }
    ]
  },
  {
    "id": "TND-2026-004",
    "tender_no": "MPSEDC/MAN/2026/RFP-01",
    "title": "Hiring of Specialized Project Management & Technical Resources (PMU) for State e-Governance Missions",
    "title_hi": "राज्य ई-गवर्नेंस मिशनों हेतु विशिष्ट परियोजना प्रबंधन एवं तकनीकी संसाधन (पीएमयू) का चयन",
    "category": "Manpower",
    "published_date": "2026-01-20 11:00 IST",
    "submission_deadline": "2026-02-15 17:00 IST",
    "original_deadline": None,
    "status": "Closed",
    "emd_val": "₹ 8,00,000",
    "doc_fee": "₹ 2,950",
    "description": "Engagement of Enterprise Architects, Full-Stack Devs, Cloud Security Specialists, and Data Scientists for MPSeDC project divisions.",
    "documents": [
      {"name": "RFP_PMU_Manpower_Empanelment.pdf", "size": "2.4 MB", "type": "RFP Document"}
    ],
    "corrigendums": []
  },
  {
    "id": "TND-2026-005",
    "tender_no": "MPSEDC/DRONE/2026/RFP-03",
    "title": "Selection of Drone Flight Operators & GIS Data Processing Agencies for High-Resolution Orthophoto Mapping",
    "title_hi": "उच्च-रिज़ॉल्यूशन ऑर्थोफ़ोटो मैपिंग हेतु ड्रोन उड़ान संचालकों एवं जीआईएस डेटा प्रोसेसिंग एजेंसियों का चयन",
    "category": "Consultancy",
    "published_date": "2026-02-05 10:00 IST",
    "submission_deadline": "2026-03-08 15:00 IST",
    "original_deadline": None,
    "status": "Live",
    "emd_val": "₹ 12,50,000",
    "doc_fee": "₹ 5,900",
    "description": "Large-scale cadastral drone surveying, DSM/DTM extraction, and integration with MP Bhulekh and MPSSDI geoportal repositories.",
    "documents": [
      {"name": "RFP_Drone_GIS_Mapping_Phase4.pdf", "size": "4.9 MB", "type": "RFP Document"}
    ],
    "corrigendums": []
  },
  {
    "id": "TND-2026-006",
    "tender_no": "MPSEDC/SEC/2025/RFP-11",
    "title": "Establishment & Operation of 24x7 Security Operations Center (SOC) & MP-CERT Incident Management Division",
    "title_hi": "24x7 सुरक्षा संचालन केंद्र (एसओसी) एवं एमपी-सर्ट घटना प्रबंधन प्रभाग की स्थापना व संचालन",
    "category": "Infrastructure",
    "published_date": "2025-11-15 10:00 IST",
    "submission_deadline": "2025-12-20 15:00 IST",
    "original_deadline": None,
    "status": "Archived",
    "emd_val": "₹ 30,00,000",
    "doc_fee": "₹ 11,800",
    "description": "Managed Detection and Response (MDR), SIEM/SOAR platform license deployment, and CERT-In empanelled auditing for MP state digital assets.",
    "documents": [
      {"name": "RFP_SOC_MP_CERT_Archive.pdf", "size": "6.2 MB", "type": "Archived RFP"}
    ],
    "corrigendums": []
  },
  {
    "id": "TND-2026-007",
    "tender_no": "MPSEDC/ETDC/2026/RFP-01",
    "title": "Supply, Installation & NABL Calibration of High-Precision Radio Frequency (RF) & EMI/EMC Test Benches",
    "title_hi": "ईटीडीसी प्रयोगशाला हेतु उच्च-सटीक रेडियो फ्रीक्वेंसी एवं ईएमआई/ईएमसी परीक्षण बेंचों की आपूर्ति व एनएबीएल अंशांकन",
    "category": "Hardware",
    "published_date": "2026-01-10 11:30 IST",
    "submission_deadline": "2026-02-10 16:00 IST",
    "original_deadline": None,
    "status": "Cancelled",
    "emd_val": "₹ 5,00,000",
    "doc_fee": "₹ 2,950",
    "description": "Procurement of Rohde & Schwarz / Keysight EMI receivers, anechoic test enclosures, and compliance antennas for ETDC Bhopal.",
    "documents": [
      {"name": "Cancellation_Notice_ETDC_RF.pdf", "size": "420 KB", "type": "Cancellation Order"}
    ],
    "corrigendums": []
  }
]

PROJECTS_DATA = [
  {
    "id": "PRJ-01",
    "name": "State Data Center (SDC)",
    "name_hi": "स्टेट डेटा सेंटर (एसडीसी)",
    "category": "Core Infrastructure",
    "short_desc": "Uptime Tier-IV certified central digital vault delivering sovereign cloud hosting and disaster recovery.",
    "full_desc": "The Madhya Pradesh State Data Center (SDC) provides a shared, secure, high-availability IT infrastructure for hosting government department databases, web services, and cloud compute nodes with 99.9% uptime SLA.",
    "icon_key": "server",
    "nodal_officer": "General Manager (SDC & Cloud)",
    "impact_metrics": "50+ State Depts | 1,200+ Hosted VMs | 4 Petabytes NVMe Storage",
    "live_url": "https://mpsedc.mp.gov.in/"
  },
  {
    "id": "PRJ-02",
    "name": "MPSWAN Telecom Network",
    "name_hi": "एमपीडबल्यूएएन दूरसंचार नेटवर्क",
    "category": "Core Infrastructure",
    "short_desc": "High-speed broadband optical network interconnecting 55 districts, 350+ blocks, and 1,000+ state offices.",
    "full_desc": "Madhya Pradesh State Wide Area Network serves as the core communication arterial system of the state, provisioning voice, data, and video conferencing across all administrative tiers with automated failover.",
    "icon_key": "network",
    "nodal_officer": "Chief General Manager (Telecom)",
    "impact_metrics": "55 District PoPs | 10 Gbps Backbone | 350+ Blocks Connected",
    "live_url": "https://mpsedc.mp.gov.in/"
  },
  {
    "id": "PRJ-03",
    "name": "MPSSDI / GIS Platform",
    "name_hi": "एमपी एसएसडीआई / जीआईएस प्लेटफॉर्म",
    "category": "GIS & Emerging Tech",
    "short_desc": "Enterprise Spatial Data Infrastructure enabling multi-department geospatial mapping and analytics.",
    "full_desc": "Madhya Pradesh State Spatial Data Infrastructure standardizes geographic layers including cadastral maps, forest boundaries, water bodies, and road networks for spatial governance and urban planning.",
    "icon_key": "satellite",
    "nodal_officer": "Head of GIS & Spatial Technologies",
    "impact_metrics": "180+ Geospatial Layers | 55 Districts Mapped | 1:500 Cadastral Precision",
    "live_url": "https://geoportal.mp.gov.in/"
  },
  {
    "id": "PRJ-04",
    "name": "IT Parks & Plug-and-Play Hubs",
    "name_hi": "आईटी पार्क एवं प्लग-एंड-प्ले हब",
    "category": "Core Infrastructure",
    "short_desc": "Grade-A technology campuses with 24x7 power redundancy, optical loops, and co-working incubation.",
    "full_desc": "World-class operational IT Parks at Bhopal, Indore (Crystal & Pardeshipura), Jabalpur, and Gwalior offering plug-and-play incubator suites and land parcels to multinational IT/ITeS and GCC firms.",
    "icon_key": "building",
    "nodal_officer": "Chief Investment Officer (IT Parks)",
    "impact_metrics": "6 Operational Clusters | 1.8M Sq. Ft. Built-up | 45,000+ IT Jobs",
    "live_url": "https://invest.mp.gov.in/"
  },
  {
    "id": "PRJ-05",
    "name": "Centre of Excellence (CoE)",
    "name_hi": "सेंटर ऑफ एक्सीलेंस (सीओई)",
    "category": "GIS & Emerging Tech",
    "short_desc": "Advanced R&D hubs focused on AI/ML, Blockchain, Drone Autonomy, and Semiconductor Verification.",
    "full_desc": "Established in partnership with premier academia and industry leaders to foster incubation, deep-tech research, intellectual property registration, and specialized engineering training for MP youth.",
    "icon_key": "cpu",
    "nodal_officer": "Director (Technology & Innovation)",
    "impact_metrics": "4 Emerging Tech Labs | 35 Startups Mentored | 12 Research Patents",
    "live_url": "https://mpsedc.mp.gov.in/"
  },
  {
    "id": "PRJ-06",
    "name": "IT Investment Promotion",
    "name_hi": "आईटी निवेश संवर्धन",
    "category": "Citizen & Investment Portals",
    "short_desc": "Single-window institutional facilitation for IT, ITeS, ESDM, GCC, and AVGC enterprise investors.",
    "full_desc": "End-to-end investor relationship management from initial land allocation queries and incentive evaluation to post-allotment clearances and subsidy disbursement under MP IT Policy 2023.",
    "icon_key": "briefcase",
    "nodal_officer": "Executive Director (Investments)",
    "impact_metrics": "₹ 4,800+ Cr Committed | 120+ MNCs Onboarded | 30-Day SLA Approval",
    "live_url": "https://invest.mp.gov.in/"
  },
  {
    "id": "PRJ-07",
    "name": "Electronics Manufacturing Cluster (EMC)",
    "name_hi": "इलेक्ट्रॉनिक्स मैन्युफैक्चरिंग क्लस्टर (ईएमसी)",
    "category": "Core Infrastructure",
    "short_desc": "EMC 2.0 specialized hardware fabrication and testing ecosystem at Malanpur, Bhind.",
    "full_desc": "State-sponsored manufacturing cluster with effluent treatment, high-capacity industrial power feeders, testing laboratories, and duty-free import facilitation for ESDM and PCB assemblers.",
    "icon_key": "cpu",
    "nodal_officer": "Project Director (EMC Malanpur)",
    "impact_metrics": "150 Acres Industrial Land | 28 Fabrication Plots | ₹ 1,200 Cr Investment",
    "live_url": "https://mpsedc.mp.gov.in/"
  },
  {
    "id": "PRJ-08",
    "name": "ETDC Testing Laboratories",
    "name_hi": "ईटीडीसी परीक्षण प्रयोगशालाएं",
    "category": "Core Infrastructure",
    "short_desc": "NABL accredited electronics testing and development center offering BIS certification testing.",
    "full_desc": "Electronics Test and Development Centre (ETDC) Bhopal provides environmental, EMI/EMC, safety, and calibration services to electronics manufacturers, telecom vendors, and defense contractors.",
    "icon_key": "shield",
    "nodal_officer": "Scientist-in-Charge (ETDC)",
    "impact_metrics": "NABL Accredited | 450+ Annual Tests | BIS & CE Recognized",
    "live_url": "https://mpsedc.mp.gov.in/"
  },
  {
    "id": "PRJ-09",
    "name": "MP Online Citizen Gateway",
    "name_hi": "एमपी ऑनलाइन नागरिक सेवा पोर्टल",
    "category": "Citizen & Investment Portals",
    "short_desc": "Joint venture pioneer portal delivering 1,000+ citizen services through 50,000+ rural Kiosks.",
    "full_desc": "The flagship G2C/B2C service delivery vehicle of MP, handling admissions, bill payments, examinations, welfare disbursements, and commercial tax filings with seamless payment gateway orchestration.",
    "icon_key": "globe",
    "nodal_officer": "COO (MP Online Ltd.)",
    "impact_metrics": "50,000+ Kiosks | 120M+ Annual Transactions | 99.8% Payment Success",
    "live_url": "https://mponline.gov.in/"
  },
  {
    "id": "PRJ-10",
    "name": "MP State Agency for Public Services (MPSAPS)",
    "name_hi": "मध्य प्रदेश लोक सेवा अभिकरण (एमपीएसएपीएस)",
    "category": "Citizen & Investment Portals",
    "short_desc": "Public Services Guarantee Act automation ensuring time-bound statutory delivery to citizens.",
    "full_desc": "Pioneered legislative citizen service delivery with strict timeframes, automated escalation to appellate authorities, and digital caste, domicile, and income certificate generation.",
    "icon_key": "award",
    "nodal_officer": "Executive Officer (MPSAPS)",
    "impact_metrics": "560+ Guaranteed Services | 98.4% Timely Delivery | 45M Certificates Issued",
    "live_url": "https://mpedistrict.gov.in/"
  },
  {
    "id": "PRJ-11",
    "name": "MP Drone Initiative",
    "name_hi": "मध्य प्रदेश ड्रोन पहल",
    "category": "GIS & Emerging Tech",
    "short_desc": "State-wide unmanned aerial vehicle integration for agriculture, mining, disaster relief & mapping.",
    "full_desc": "Promoting drone technology adoption through pilot training academies, crop damage assessment flights, mining boundary surveillance, and the SVAMITVA village property card surveying mission.",
    "icon_key": "drone",
    "nodal_officer": "Mission Director (Drone Technologies)",
    "impact_metrics": "12,000+ Villages Surveyed | 6 Certified Training Schools | 500+ Pilots Trained",
    "live_url": "https://drone.mp.gov.in/"
  },
  {
    "id": "PRJ-12",
    "name": "MP Geoportal 2.0",
    "name_hi": "मध्य प्रदेश जियोपोर्टल 2.0",
    "category": "GIS & Emerging Tech",
    "short_desc": "Unified public mapping portal integrating 3D terrain, revenue land parcels, and administrative bounds.",
    "full_desc": "A cutting-edge WebGIS clearinghouse providing open and restricted spatial datasets to town planners, academic researchers, infrastructure developers, and disaster managers.",
    "icon_key": "satellite",
    "nodal_officer": "Chief GIS Architect",
    "impact_metrics": "1:1000 Web Maps | Real-time Satellite Feeds | Open OGC Compliant",
    "live_url": "https://geoportal.mp.gov.in/"
  }
]

POLICIES_DATA = [
  {
    "id": "POL-01",
    "title": "Madhya Pradesh IT, ITeS & ESDM Investment Promotion Policy 2023",
    "title_hi": "मध्य प्रदेश आईटी, आईटीईएस एवं ईएसडीएम निवेश संवर्धन नीति 2023",
    "year": "2023",
    "category": "IT & Electronics",
    "highlights": [
      "Capital Investment Subsidy up to 30% on eligible fixed assets (max ₹ 30 Cr)",
      "100% reimbursement of stamp duty & registration fees on lease deeds",
      "Power tariff concession at ₹ 1.50 per unit rebate for 5 years",
      "Employment Generation Assistance up to ₹ 10,000 per employee/year for 5 years"
    ],
    "summary": "Designed to establish Madhya Pradesh as India's pre-eminent hub for software engineering, cloud computing, electronics systems design, and IT infrastructure development with streamlined ease of doing business.",
    "download_size": "3.4 MB",
    "has_estimator": True
  },
  {
    "id": "POL-02",
    "title": "Madhya Pradesh Global Capability Centers (GCC) Policy 2024",
    "title_hi": "मध्य प्रदेश ग्लोबल कैपेबिलिटी सेंटर (जीसीसी) नीति 2024",
    "year": "2024",
    "category": "GCC & Finance",
    "highlights": [
      "Special lease rental subsidy up to 50% for 3 years in Tier-1 & Tier-2 cities",
      "Talent attraction grant of ₹ 25,000 per lateral hire relocating to MP",
      "Dedicated fast-track green corridor for international GCC executive visas",
      "Innovation & Co-working workspace subsidy in designated IT Parks"
    ],
    "summary": "Specialized policy incentivizing Fortune 500 corporations and global multinationals to anchor their engineering centers, analytics hubs, and core financial back-offices in Indore and Bhopal.",
    "download_size": "2.8 MB",
    "has_estimator": False
  },
  {
    "id": "POL-03",
    "title": "Madhya Pradesh AVGC-XR Promotion Policy 2025",
    "title_hi": "मध्य प्रदेश एवीजीसी-एक्सआर संवर्धन नीति 2025",
    "year": "2025",
    "category": "Media & Creative Tech",
    "highlights": [
      "Rendering farm infrastructure compute subsidy up to 40%",
      "Special intellectual property (IP) creation grant up to ₹ 20 Lakh per title",
      "Quality certification fee reimbursement up to 75%",
      "Game development incubation grants with equity-free capital"
    ],
    "summary": "Targeted framework catalyzing animation studios, gaming engines, VFX visual post-production houses, and virtual reality engineering hubs with state-of-the-art compute subsidies.",
    "download_size": "2.1 MB",
    "has_estimator": False
  },
  {
    "id": "POL-04",
    "title": "Madhya Pradesh SpaceTech & Geospatial Policy 2025",
    "title_hi": "मध्य प्रदेश स्पेसटेक एवं भू-स्थानिक नीति 2025",
    "year": "2025",
    "category": "Aerospace & Satellites",
    "highlights": [
      "Ground station establishment capital subsidy up to 35%",
      "Small satellite component manufacturing testing facility grants",
      "Free access to high-resolution MP Geoportal satellite archives",
      "Payload integration testing assistance at ETDC labs"
    ],
    "summary": "A future-forward initiative promoting satellite subsystem fabrication, Earth observation analytics, and downstream geospatial software startups in central India.",
    "download_size": "1.9 MB",
    "has_estimator": False
  },
  {
    "id": "POL-05",
    "title": "Madhya Pradesh Drone Promotion & Utilization Policy",
    "title_hi": "मध्य प्रदेश ड्रोन संवर्धन एवं उपयोगिता नीति",
    "year": "2024",
    "category": "Autonomous Tech",
    "highlights": [
      "25% capital subsidy for setting up Remote Pilot Training Organizations (RPTO)",
      "Drone assembly testing sandbox at EMC Malanpur",
      "Departmental priority procurement for MP-manufactured drones"
    ],
    "summary": "Comprehensive regulatory and incentive blueprint promoting domestic drone manufacturing, pilot skilling, and integration across agriculture and disaster management.",
    "download_size": "2.5 MB",
    "has_estimator": False
  },
  {
    "id": "POL-06",
    "title": "State Cyber Security & Data Governance Guidelines",
    "title_hi": "राज्य साइबर सुरक्षा एवं डेटा गवर्नेंस दिशा-निर्देश",
    "year": "2024",
    "category": "Governance & Security",
    "highlights": [
      "Mandatory biannual CERT-In third-party vulnerability assessments",
      "Strict data sovereignty protocols for all G2C and G2G data repositories",
      "Implementation of Zero Trust Architecture (ZTA) across all departmental networks"
    ],
    "summary": "Standardized mandatory technical protocols safeguarding state cyber-infrastructure against advanced persistent threats, data breaches, and service interruptions.",
    "download_size": "1.7 MB",
    "has_estimator": False
  }
]

IT_PARKS_DATA = {
  "bhopal": {
    "name": "Bhopal IT Park (Badwai & Arera Hills)",
    "name_hi": "भोपाल आईटी पार्क (बड़वई एवं अरेरा हिल्स)",
    "district": "Bhopal",
    "total_area": "200 Acres",
    "built_up": "450,000 Sq. Ft.",
    "available_space": "85,000 Sq. Ft. Plug-and-Play",
    "power_redundancy": "33KV Dual Independent Feeders + 100% DG Backup",
    "fiber_connectivity": "Triple Redundant Carrier Rings (Airtel, BSNL, Jio)",
    "key_tenants": ["Netlink Software", "Wipro Technologies", "Vakrangee", "MP Online Corp"],
    "pin_top": "52%",
    "pin_left": "46%",
    "description": "Strategically positioned adjacent to Raja Bhoj International Airport and Arera Hills administrative center, Bhopal IT Park features lush campus grounds, high-speed fiber backbones, and customizable incubation suites."
  },
  "indore": {
    "name": "Indore IT Park (Crystal IT Park & Pardeshipura)",
    "name_hi": "इंदौर आईटी पार्क (क्रिस्टल आईटी पार्क एवं परदेशीपुरा)",
    "district": "Indore",
    "total_area": "150 Acres",
    "built_up": "750,000 Sq. Ft.",
    "available_space": "120,000 Sq. Ft. Grade-A Space",
    "power_redundancy": "Dual 33KV Express Feeders with N+1 DG Generator Array",
    "fiber_connectivity": "Four Fiber Providers with Optical Local Loops",
    "key_tenants": ["Tata Consultancy Services", "Infosys Limited", "Cognizant", "Teleperformance"],
    "pin_top": "60%",
    "pin_left": "33%",
    "description": "The commercial IT jewel of Madhya Pradesh, hosting multinational software campuses, specialized SEZ units, Tier-III data backbones, and premier tech talent pools from IIT Indore and IIM Indore."
  },
  "jabalpur": {
    "name": "Jabalpur IT Park (Tilhari / Bargi Hills)",
    "name_hi": "जबलपुर आईटी पार्क (तिलहरी / बरगी हिल्स)",
    "district": "Jabalpur",
    "total_area": "65 Acres",
    "built_up": "250,000 Sq. Ft.",
    "available_space": "42,000 Sq. Ft. Modular Suites",
    "power_redundancy": "33/11 KV Dedicated Substation with 24x7 DG",
    "fiber_connectivity": "High-Reliability BSNL & Jio Optical Fiber Rings",
    "key_tenants": ["Paytm (One97)", "Tech Mahindra BPO", "Sysmantech", "IIITDM Incubator"],
    "pin_top": "54%",
    "pin_left": "68%",
    "description": "Nestled near the picturesque Bargi Hills with direct connectivity to IIITDM Jabalpur and engineering colleges, catering specifically to BPO, customer experience, and software export units."
  },
  "gwalior": {
    "name": "Gwalior IT Park (Rairu)",
    "name_hi": "ग्वालियर आईटी पार्क (रायरू)",
    "district": "Gwalior",
    "total_area": "40 Acres",
    "built_up": "180,000 Sq. Ft.",
    "available_space": "35,000 Sq. Ft. Plug-and-Play",
    "power_redundancy": "Dual Feeders from MPPKVVCL + Automated DG Switchover",
    "fiber_connectivity": "Underground Optical Ring Network",
    "key_tenants": ["Softvision Networks", "IIITM Tech Hub", "OmniNet Solutions"],
    "pin_top": "22%",
    "pin_left": "48%",
    "description": "Located on the Delhi-Mumbai industrial corridor node at Rairu, Gwalior IT Park provides cost-effective Grade-A workspaces, proximity to ABV-IIITM Gwalior, and rapid highway logistics."
  },
  "malanpur": {
    "name": "Malanpur Electronics Manufacturing Cluster (EMC)",
    "name_hi": "मालनपुर इलेक्ट्रॉनिक्स मैन्युफैक्चरिंग क्लस्टर (ईएमसी)",
    "district": "Bhind (Gwalior Sub-region)",
    "total_area": "150 Acres Industrial Land",
    "built_up": "Industrial Sheds & Open Plots",
    "available_space": "18 Industrial Plots Ready for Allotment",
    "power_redundancy": "132KV Dedicated Industrial Grid Substation",
    "fiber_connectivity": "Dual Industrial Fiber Feeds",
    "key_tenants": ["Surya Roshni", "Tejas Telecom OEM", "OptoElectronics India", "Cadence PCB"],
    "pin_top": "18%",
    "pin_left": "54%",
    "description": "Central India's flagship EMC 2.0 cluster offering specialized effluent treatment plants (ETP), heavy industrial power feeders, zero-duty component import, and testing sandbox access."
  },
  "sinhasa": {
    "name": "Sinhasa IT Park (Indore Cluster II)",
    "name_hi": "सिंहासा आईटी पार्क (इंदौर क्लस्टर II)",
    "district": "Indore",
    "total_area": "112 Acres",
    "built_up": "320,000 Sq. Ft. + Land Parcels",
    "available_space": "65,000 Sq. Ft. + 14 Open Plots",
    "power_redundancy": "33KV Substation + 100% Redundant Power Supply",
    "fiber_connectivity": "Redundant Dark Fiber Mesh",
    "key_tenants": ["Diaspark", "Impetus Technologies", "Yash Technologies Hub"],
    "pin_top": "66%",
    "pin_left": "29%",
    "description": "An expansion phase of the booming Indore IT ecosystem, offering large contiguous land plots for enterprise corporate headquarters, clean-tech R&D centers, and high-density engineering offices."
  }
}

UPDATES_DATA = [
  {
    "id": "UPD-01",
    "title": "Recruitment Notification: Selection of Graduate Engineer Trainees (GET - IT/CSE) Batch 2026",
    "title_hi": "भर्ती अधिसूचना: ग्रेजुएट इंजीनियर ट्रेनी (जीईटी - आईटी/सीएसई) बैच 2026 का चयन",
    "category": "recruitment",
    "date": "2026-02-15 11:00 IST",
    "memo_no": "MPSEDC/HR/2026/REC-01",
    "is_archived": False,
    "file_size": "1.2 MB",
    "description": "Applications invited from B.E./B.Tech/MCA graduates with valid GATE scores for 35 positions of Graduate Engineer Trainee in Cloud Infrastructure and Cyber Security."
  },
  {
    "id": "UPD-02",
    "title": "Final Assessment Results: Empanelment of Senior Full-Stack Developers under Project Management Unit",
    "title_hi": "अंतिम मूल्यांकन परिणाम: परियोजना प्रबंधन इकाई के तहत वरिष्ठ फुल-स्टैक डेवलपर्स का पैनल चयन",
    "category": "results",
    "date": "2026-02-10 16:30 IST",
    "memo_no": "MPSEDC/HR/2026/RES-04",
    "is_archived": False,
    "file_size": "850 KB",
    "description": "List of shortlisted candidates based on technical interviews held on 28th and 29th January 2026 for SDC modernization division."
  },
  {
    "id": "UPD-03",
    "title": "Summer Internship Program 2026: Notice for Engineering & MCA Students of Madhya Pradesh",
    "title_hi": "ग्रीष्मकालीन इंटर्नशिप कार्यक्रम 2026: मध्य प्रदेश के इंजीनियरिंग एवं एमसीए विद्यार्थियों हेतु सूचना",
    "category": "internship",
    "date": "2026-02-05 10:00 IST",
    "memo_no": "MPSEDC/TRG/2026/INT-01",
    "is_archived": False,
    "file_size": "650 KB",
    "description": "8-week structured internship in State Data Center operations, AI/ML model deployment, and GIS mapping for pre-final year students."
  },
  {
    "id": "UPD-04",
    "title": "Government Order: Revised Operational Guidelines for Capital Subsidy Disbursement under MP IT Policy 2023",
    "title_hi": "शासकीय आदेश: मप्र आईटी नीति 2023 के तहत पूंजीगत सब्सिडी संवितरण हेतु संशोधित दिशा-निर्देश",
    "category": "notifications",
    "date": "2026-01-28 14:00 IST",
    "memo_no": "DST/MPSEDC/2026/NOTIF-12",
    "is_archived": False,
    "file_size": "2.4 MB",
    "description": "Competent authority approved timelines, checklist of CA certificates, and online escrow disbursement mechanisms for eligible IT/ITeS units."
  },
  {
    "id": "UPD-05",
    "title": "Announcement: MP State Cyber Security Hackathon & Capture The Flag (CTF) Challenge 2026",
    "title_hi": "घोषणा: मध्य प्रदेश राज्य साइबर सुरक्षा हैकाथॉन एवं कैप्चर द फ्लैग (सीटीएफ) चैलेंज 2026",
    "category": "events",
    "date": "2026-01-15 12:00 IST",
    "memo_no": "MPSEDC/CERT/2026/EVENT-02",
    "is_archived": False,
    "file_size": "1.8 MB",
    "description": "State-wide ethical hacking competition with cash prizes up to ₹ 10 Lakh and direct internship opportunities with MP-CERT division."
  },
  {
    "id": "UPD-06",
    "title": "Notice: Corrigendum to Tender No. MPSEDC/SDC/2026/RFP-04 for Cloud Infrastructure Augmentation",
    "title_hi": "सूचना: क्लाउड अवसंरचना संवर्धन हेतु निविदा क्रमांक MPSEDC/SDC/2026/RFP-04 का शुद्धिपत्र",
    "category": "notifications",
    "date": "2026-02-27 18:00 IST",
    "memo_no": "MPSEDC/SDC/2026/CORR-02",
    "is_archived": False,
    "file_size": "1.1 MB",
    "description": "Extension of bid submission deadline up to 15th March 2026, 15:00 IST and clarification of hypervisor licensing specifications."
  },
  {
    "id": "UPD-07",
    "title": "Archive Notice: Selection of Cloud Service Provider for Disaster Recovery Site at Hyderabad (2024)",
    "title_hi": "अभिलेख सूचना: हैदराबाद में आपदा पुनर्प्राप्ति स्थल हेतु क्लाउड सेवा प्रदाता का चयन (2024)",
    "category": "notifications",
    "date": "2024-11-20 15:00 IST",
    "memo_no": "MPSEDC/DR/2024/ARC-08",
    "is_archived": True,
    "file_size": "3.1 MB",
    "description": "Historical procurement document for the secondary disaster recovery replication center connecting SDC Bhopal."
  },
  {
    "id": "UPD-08",
    "title": "Archive Results: Written Examination Scores for Assistant Programmer Recruitment 2024",
    "title_hi": "अभिलेख परिणाम: सहायक प्रोग्रामर भर्ती 2024 हेतु लिखित परीक्षा प्राप्तांक",
    "category": "results",
    "date": "2024-09-15 11:30 IST",
    "memo_no": "MPSEDC/HR/2024/RES-09",
    "is_archived": True,
    "file_size": "1.4 MB",
    "description": "Archived scorecard and category-wise merit list for the 2024 Assistant Programmer technical recruitment drive."
  }
]

OFFICERS_DATA = [
  {"name": "Managing Director", "dept": "Executive Directorate", "phone": "+91-755-2518300", "email": "md@mpsedc.com"},
  {"name": "Chief General Manager (SDC & Tech)", "dept": "State Data Center Division", "phone": "+91-755-2518312", "email": "cgm.sdc@mpsedc.com"},
  {"name": "Chief Investment Officer", "dept": "IT Parks & Investment Promotion", "phone": "+91-755-2518325", "email": "invest@mpsedc.com"},
  {"name": "General Manager (MPSWAN)", "dept": "State Wide Area Network", "phone": "+91-755-2518330", "email": "mpswan@mpsedc.com"},
  {"name": "Head of MP-CERT & Cyber Security", "dept": "Cyber Security Operations", "phone": "+91-755-2518340", "email": "cert@mpsedc.com"},
  {"name": "Company Secretary & Nodal RTI", "dept": "Legal & Public Grievance", "phone": "+91-755-2518350", "email": "cs@mpsedc.com"}
]
