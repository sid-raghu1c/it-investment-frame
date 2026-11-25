with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('const UPLOAD_SPECS =')
if pos != -1:
    print(text[pos:pos+3500])
else:
    print("UPLOAD_SPECS not found")
