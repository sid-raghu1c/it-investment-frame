with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find functions related to file upload
upload_funcs = re.findall(r'function\s+(?:renderUploadBox|initUploadBoxes|handleFileSelect|handleFileUpload|validateUploadedFiles)[^{]*\{', text)
print("Upload functions:", upload_funcs)

# Look for where renderUploadBox is defined
pos = text.find('function renderUploadBox(')
if pos != -1:
    print("renderUploadBox code snippet:")
    print(text[pos:pos+1500])

# Look for MASTER_CONFIG.documents or checklist
chk_docs = re.search(r'checklistDocs\s*:\s*\[.*?\]', text, re.DOTALL)
if chk_docs:
    print("\nchecklistDocs found:")
    print(chk_docs.group(0)[:600])

# Search for allowed file types / accept
accept_matches = re.findall(r'accept\s*=\s*["\'][^"\']+["\']', text)
print("\nUnique accept attributes in HTML:")
print(set(accept_matches))
