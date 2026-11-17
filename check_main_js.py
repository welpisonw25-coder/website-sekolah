with open('js/main.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Check loadDynamicSOP and loadDynamicKKG exist
print("loadDynamicSOP in main.js:", "function loadDynamicSOP()" in code)
print("loadDynamicKKG in main.js:", "function loadDynamicKKG()" in code)
print("Total characters in main.js:", len(code))
