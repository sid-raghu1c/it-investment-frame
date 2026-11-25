with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
doc_configs = re.findall(r'doc_\w+', text)
print("Unique doc_ keys in script:", sorted(list(set(doc_configs))))

# Check where doc_configs or file upload initialization is defined
js_upload_init = re.search(r'const\s+DOC_CONFIGS\s*=\s*\{.*?\};|const\s+FILE_CONFIGS\s*=\s*\{.*?\};', text, re.DOTALL)
if js_upload_init:
    print("Found configs:")
    print(js_upload_init.group(0)[:600])
else:
    # search for upload-box
    print("Searching for upload-box in script:")
    for line in text.split('\n'):
        if 'upload-box-' in line and ('function' in line or 'const' in line or 'let' in line or 'var' in line):
            print(line.strip()[:100])
