def format_svg_name(full_name, center_x, is_small_box=False):
    if not full_name: return ''
    name = full_name.strip()
    threshold = 16 if is_small_box else 19
    if len(name) > threshold and ' ' in name:
        spaces = [i for i, ch in enumerate(name) if ch == ' ']
        mid = len(name) / 2.0
        best_idx = min(spaces, key=lambda idx: abs(idx - mid))
        s1 = name[:best_idx]
        s2 = name[best_idx+1:]
        return f'<tspan x="{center_x}" y="27">{s1}</tspan><tspan x="{center_x}" y="43">{s2}</tspan>'
    else:
        y = 33 if is_small_box else 32
        return f'<tspan x="{center_x}" y="{y}">{name}</tspan>'

test_names = [
    ("Adi Puspito, S.Pd", 130, False),
    ("Yuli Syetia Sari, S.Pd", 125, False),
    ("Elias Tabuni, S.Pd", 125, False),
    ("Rita Paulina Wabiser, S.Pd", 125, False),
    ("Warno, S.Pd.SD", 125, False),
    ("Rini Handayani, S.Pd", 125, False),
    ("Cicik Mursidah, S.Pd", 125, False),
    ("Ferdinand, S.Pd", 107.5, True),
    ("Zainal Habiib Al Arif, S.Pd", 107.5, True),
    ("Esther Tina Maria Panjaitan, S.Pd", 107.5, True),
    ("Flavianus Rainaldus, S.Ag", 107.5, True),
    ("Maria Magdalena Wenda, S.Pd", 125, False),
    ("Budi Santoso", 125, False)
]

for name, cx, small in test_names:
    print(f"{name:35} -> {format_svg_name(name, cx, small)}")
