with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('infraStandardBody')
while pos != -1:
    print("Found at pos", pos)
    print(text[pos-100:pos+500])
    print("="*40)
    pos = text.find('infraStandardBody', pos + 20)

pos_rows = text.find('infraStandardRows:')
if pos_rows != -1:
    print("infraStandardRows:")
    print(text[pos_rows:pos_rows+1500])
