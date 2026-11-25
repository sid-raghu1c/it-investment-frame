import re

with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find tab navigation HTML
tab_nav_match = re.search(r'(<div[^>]*class="[^"]*tab[^"]*"[^>]*>.*?</div>\s*</div>)', text, re.DOTALL)
# Search for nav or tab container
nav_matches = re.findall(r'<nav[^>]*>.*?</nav>|<div[^>]*id="[^"]*tab[^"]*"[^>]*>', text, re.IGNORECASE | re.DOTALL)
print("Nav matches:", len(nav_matches))
for n in nav_matches:
    print(n[:200])

# Search for tab-bar or tabs in HTML
tab_bar = re.search(r'<div[^>]*class="[^"]*(?:tabs|tab-bar|tab-nav|form-tabs)[^"]*"[^>]*>.*?</div>', text, re.DOTALL)
if tab_bar:
    print("Found tab bar:")
    print(tab_bar.group(0)[:500])
else:
    print("Searching for card-sec-1 container:")
    sec1_pos = text.find('id="card-sec-1"')
    if sec1_pos != -1:
        print(text[sec1_pos-500:sec1_pos+200])

# Search for sectionsMeta in script
meta_match = re.search(r'sectionsMeta\s*:\s*\[.*?\]', text, re.DOTALL)
if meta_match:
    print("sectionsMeta:")
    print(meta_match.group(0))
