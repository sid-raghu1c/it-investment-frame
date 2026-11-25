with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="card-sec-3"')
pos_end = text.find('id="card-sec-4"')
sec3 = text[pos:pos_end]

# find table in sec3
import re
table_match = re.search(r'<table[^>]*>.*?</table>', sec3, re.DOTALL)
if table_match:
    print("Table in sec3:")
    print(table_match.group(0)[:2000])

# check headings in sec3
h_matches = re.findall(r'<div class="sub-panel-title">.*?</div>', sec3, re.DOTALL)
print("\nSub-panel titles in sec3:")
for h in h_matches:
    print("  ", re.sub(r'\s+', ' ', h.strip()))
