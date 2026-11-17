with open('deploy_online.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(12, 45):
    print(f"{i+1}: {lines[i]}", end="")
