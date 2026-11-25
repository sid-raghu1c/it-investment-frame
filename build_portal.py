# build_portal.py
# Compiler script for MPSeDC Modernized Homepage Single-File HTML Prototype

import json
import os
import sys

# Import modular components
from parts.css_styles import CSS_CONTENT as CSS_STYLES
from parts.svg_assets import (
  MPSEDC_LOGO_SVG,
  LION_CAPITAL_EMBLEM_SVG,
  MP_MAP_SVG,
  ISOMETRIC_DIGITAL_HUB_SVG,
  SVG_ICONS
)
from parts.data_json import (
  BILINGUAL_DICT,
  TENDERS_DATA,
  PROJECTS_DATA,
  POLICIES_DATA,
  IT_PARKS_DATA,
  UPDATES_DATA,
  OFFICERS_DATA
)
from parts.dom_markup import (
  TOP_UTILITY_BAR_MARKUP,
  MAIN_HEADER_MARKUP,
  HERO_SECTION_MARKUP,
  PERSONA_SECTION_MARKUP,
  QUICK_ACCESS_STRIP_MARKUP,
  STATS_SECTION_MARKUP,
  PROJECTS_SECTION_MARKUP,
  TENDERS_SECTION_MARKUP,
  IT_PARKS_SECTION_MARKUP,
  POLICIES_SECTION_MARKUP,
  NEWS_SECTION_MARKUP,
  FOOTER_MARKUP,
  MODALS_MARKUP
)
from parts.app_logic import APP_LOGIC_JS

def build_portal():
    print("=" * 60)
    print("Compiling MPSeDC Modernized Portal Single-File Prototype...")
    print("=" * 60)

    # Serialize JSON datasets for browser execution
    bilingual_json = json.dumps(BILINGUAL_DICT, ensure_ascii=False, indent=2)
    tenders_json = json.dumps(TENDERS_DATA, ensure_ascii=False, indent=2)
    projects_json = json.dumps(PROJECTS_DATA, ensure_ascii=False, indent=2)
    policies_json = json.dumps(POLICIES_DATA, ensure_ascii=False, indent=2)
    itparks_json = json.dumps(IT_PARKS_DATA, ensure_ascii=False, indent=2)
    updates_json = json.dumps(UPDATES_DATA, ensure_ascii=False, indent=2)
    officers_json = json.dumps(OFFICERS_DATA, ensure_ascii=False, indent=2)
    svg_icons_json = json.dumps(SVG_ICONS, ensure_ascii=False, indent=2)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>MPSeDC | Madhya Pradesh State Electronics Development Corporation Ltd.</title>
  <meta name="description" content="Official modern digital portal of MPSeDC, a Government of Madhya Pradesh Undertaking. State Data Center, MPSWAN, IT Parks and single-window investment promotion.">
  
  <!-- Typography: Google Fonts (Inter & Noto Sans Devanagari) with system fallback -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
{CSS_STYLES}
  </style>
</head>
<body>
{TOP_UTILITY_BAR_MARKUP}

{MAIN_HEADER_MARKUP}

<main id="main-content" tabindex="-1">
{HERO_SECTION_MARKUP}

{PERSONA_SECTION_MARKUP}

{QUICK_ACCESS_STRIP_MARKUP}

{STATS_SECTION_MARKUP}

{PROJECTS_SECTION_MARKUP}

{TENDERS_SECTION_MARKUP}

{IT_PARKS_SECTION_MARKUP}

{POLICIES_SECTION_MARKUP}

{NEWS_SECTION_MARKUP}
</main>

{FOOTER_MARKUP}

{MODALS_MARKUP}

  <!-- EMBEDDED DATASETS & JAVASCRIPT APPLICATION ENGINE -->
  <script>
    const BILINGUAL_DATA = {bilingual_json};
    const TENDERS_DATA = {tenders_json};
    const PROJECTS_DATA = {projects_json};
    const POLICIES_DATA = {policies_json};
    const IT_PARKS_DATA = {itparks_json};
    const UPDATES_DATA = {updates_json};
    const OFFICERS_DATA = {officers_json};
    const SVG_ICONS = {svg_icons_json};

{APP_LOGIC_JS}
  </script>
</body>
</html>
"""

    output_filename = "mpsedc_modernized_homepage.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_template)

    file_size_kb = os.path.getsize(output_filename) / 1024
    print(f"SUCCESS: Generated {output_filename}")
    print(f"File Size: {file_size_kb:.2f} KB ({os.path.getsize(output_filename):,} bytes)")

    # Integrity verification
    with open(output_filename, "r", encoding="utf-8") as f:
        content = f.read()

    checks = {
        "Has DOCTYPE": "<!DOCTYPE html>" in content,
        "Has Hindi Font": "Noto Sans Devanagari" in content,
        "Has Logo SVG": "logo-crest-svg" in content,
        "Has Map SVG": "mp-state-svg" in content,
        "Has Iso Hub SVG": "hero-isometric-svg" in content,
        "Has 12 Projects": 'PRJ-12' in content,
        "Has 6 IT Parks": '"sinhasa"' in content,
        "Has Corrigendum Accordion": "corrigendum-row" in content,
        "Has Mini Incentive Estimator": "Mini Incentive Estimator" in content,
        "Has Maker-Checker CMS Modal": "modal-cms-preview" in content,
        "Has Global Search Ctrl+K": "modal-global-search" in content,
        "Closing </html>": content.strip().endswith("</html>")
    }

    print("\nIntegrity Verification:")
    all_passed = True
    for name, passed in checks.items():
        status = "PASSED" if passed else "FAILED"
        print(f"  [{status}] {name}")
        if not passed:
            all_passed = False

    if all_passed:
        print("\nAll verification checks PASSED seamlessly!")
    else:
        print("\nWARNING: Some verification checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    build_portal()
