with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for pid in ['panel-4A', 'panel-4B', 'panel-4C', 'panel-4Di', 'panel-4Dii']:
    p_pos = text.find(f'id="{pid}"')
    if p_pos != -1:
        # find end of this panel (either next panel or Authorized person section)
        next_pid_pos = len(text)
        for other in ['panel-4A', 'panel-4B', 'panel-4C', 'panel-4Di', 'panel-4Dii', 'id="authSection"', '<!-- Authorized Person']:
            pos2 = text.find(other, p_pos + 10)
            if pos2 != -1 and pos2 < next_pid_pos:
                next_pid_pos = pos2
        print(f"\n==================== {pid} ====================")
        print(text[p_pos:next_pid_pos].strip())
