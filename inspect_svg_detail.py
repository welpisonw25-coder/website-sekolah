with open('js/main.js', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('window.openBaganModal = function () {')
pos_disp = c.find("modal.style.display = 'flex'", pos)
print(c[pos_disp-100:pos_disp+200])
