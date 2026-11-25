with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for pid in ['panel-4A', 'panel-4B', 'panel-4C', 'panel-4Di', 'panel-4Dii']:
    p_pos = text.find(f'id="{pid}"')
    if p_pos != -1:
        # find closing div or next panel
        snippet = text[p_pos:p_pos+2000]
        # find title and upload boxes inside this snippet
        title_m = re.search(r'<div class="sub-panel-title">.*?</div>', snippet, re.DOTALL)
        title = title_m.group(0) if title_m else "No title"
        uploads = re.findall(r'id="(?:upload-box-|file-)[^"]*"', snippet)
        print(f"\n=== {pid} ===")
        print("Title:", re.sub(r'\s+', ' ', title))
        print("Upload IDs found:", uploads)
        # find gstin fields
        gst_fields = re.findall(r'<input[^>]*id="[^"]*gst[^"]*"[^>]*>', snippet, re.I)
        print("GST inputs found:", gst_fields)
