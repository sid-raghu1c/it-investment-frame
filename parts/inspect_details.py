import re

with open(r'd:\my_live_wireframes\it-investment-frame\mp_tourism_capital_subsidy_application_form.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Tab 1 inspection
print("--- TAB 1 CHECKS ---")
for query in ["Location Where the Unit is Established", "Vikas Khand", "Vidhan Sabha"]:
    pos = text.find(query)
    print(f"'{query}' found at {pos}:")
    if pos != -1:
        print(text[pos-20:pos+120])

# Tab 2 inspection
print("\n--- TAB 2 CHECKS ---")
for query in ["Ownership of the Unit / Entity Details", "Investor Name", "Authorized Person Name", "Upload Authorization Document"]:
    pos = text.find(query)
    print(f"'{query}' found at {pos}:")
    if pos != -1:
        print(text[pos-20:pos+120])

# Check entity sub panels in Tab 2
print("\n--- TAB 2 ENTITY PANELS ---")
panels = ["companyFields", "partnershipFields", "proprietorshipFields", "individualFields", "otherEntityFields"]
for p in panels:
    pos = text.find(f'id="{p}"')
    print(f"Panel '{p}' at {pos}")
    if pos != -1:
        print(text[pos:pos+300])
        print("...")

