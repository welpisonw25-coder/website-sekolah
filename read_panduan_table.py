with open('panduan-serah-terima.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(370, 450):
    print(f"{i+1}: {lines[i]}", end="")
