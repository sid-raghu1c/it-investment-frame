with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos4 = text.find('id="card-sec-4"')
pos5 = text.find('id="card-sec-5"')
sec4 = text[pos4:pos5]

print("=== TAB 4 SUBPANELS & TITLES ===")
import re
titles = re.findall(r'<div class="sub-panel-title">.*?</div>', sec4, re.DOTALL)
for t in titles:
    print(re.sub(r'\s+', ' ', t.strip()))

print("\n=== TAB 4 UPLOAD BOXES ===")
uploads = re.findall(r'id="(?:upload-box-|file-)[^"]*"', sec4)
print(uploads)

print("\n=== OTHER SUBSIDY SECTION ===")
pos_other = sec4.find("Other Capital Subsidy Claimed")
print(sec4[pos_other-50:pos_other+1200])

print("\n=== ANY OTHER INFO SECTION ===")
pos_any = sec4.find("Any Other Information")
print(sec4[pos_any-50:pos_any+1000])
