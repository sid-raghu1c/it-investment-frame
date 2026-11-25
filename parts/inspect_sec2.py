with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

sec2_start = text.find('id="card-sec-2"')
sec3_start = text.find('id="card-sec-3"')
sec2_content = text[sec2_start:sec3_start]

print("Length of sec2:", len(sec2_content))

import re
# find all subpanels, radio options, upload boxes, and inputs
radio_entity = re.findall(r'<input[^>]*name="entityType"[^>]*value="([^"]+)"[^>]*>.*?<label[^>]*>(.*?)</label>', sec2_content, re.DOTALL)
print("Entity types radio options:")
for val, lbl in radio_entity:
    print(f"  value: '{val}', label: '{lbl.strip()}'")

# Find conditional sections or sub-panels
subpanels = re.findall(r'<div[^>]*class="[^"]*sub-panel[^"]*"[^>]*id="([^"]+)"', sec2_content)
print("Sub-panel IDs in sec2:", subpanels)

# Find conditional containers in JS
js_entity_switch = re.findall(r'entityType\s*===\s*["\']([^"\']+)["\']', text)
print("Entity type values in JS:", set(js_entity_switch))

# Search for gstin or gst in sec2
gst_matches = re.findall(r'[^\n]*gst[^\n]*', sec2_content, re.IGNORECASE)
print(f"GST matches in sec2 ({len(gst_matches)}):")
for g in gst_matches[:10]:
    print("  ", g.strip())
