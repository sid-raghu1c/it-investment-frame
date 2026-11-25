with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function openReviewModal()')
print(text[pos:pos+4000])
