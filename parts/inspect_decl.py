with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos_decl = text.find('declInvestorInline')
print("declInvestorInline in HTML:")
print(text[pos_decl-100:pos_decl+200])

print("\n--- declInvestorInline in JS ---")
for line in text.split('\n'):
    if 'declInvestorInline' in line:
        print("  ", line.strip())

print("\n--- Review modal declaration snippet ---")
pos_rev_decl = text.find('Declaration Acceptances')
if pos_rev_decl == -1:
    pos_rev_decl = text.find('I/We,')
print(text[pos_rev_decl-50:pos_rev_decl+400])
