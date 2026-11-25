with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

for pid in ['panel-4C', 'panel-4Di', 'panel-4Dii']:
    p_pos = text.find(f'id="{pid}"')
    # find where next panel starts or auth section
    end_pos = text.find('id="panel-', p_pos + 10)
    if end_pos == -1 or end_pos > p_pos + 5000:
        end_pos = text.find('id="authSection"', p_pos + 10)
        if end_pos == -1:
            end_pos = text.find('Authorized Person', p_pos + 10)
    print(f"=== {pid} ===")
    print(text[p_pos:end_pos])
