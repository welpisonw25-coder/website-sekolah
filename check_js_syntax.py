def check_js_brackets(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    
    stack = []
    in_string = None
    in_single_comment = False
    in_multi_comment = False
    escaped = False
    line = 1
    col = 0
    
    i = 0
    n = len(code)
    while i < n:
        ch = code[i]
        col += 1
        if ch == '\n':
            line += 1
            col = 0
            if in_single_comment:
                in_single_comment = False
            i += 1
            continue
            
        if in_single_comment:
            i += 1
            continue
            
        if in_multi_comment:
            if ch == '*' and i + 1 < n and code[i+1] == '/':
                in_multi_comment = False
                i += 2
                continue
            i += 1
            continue
            
        if in_string:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == in_string:
                in_string = None
            i += 1
            continue
            
        # Not in string or comment
        if ch == '/' and i + 1 < n and code[i+1] == '/':
            in_single_comment = True
            i += 2
            continue
        if ch == '/' and i + 1 < n and code[i+1] == '*':
            in_multi_comment = True
            i += 2
            continue
            
        if ch in ('"', "'", '`'):
            in_string = ch
            escaped = False
            i += 1
            continue
            
        if ch in ('(', '[', '{'):
            stack.append((ch, line, col))
        elif ch in (')', ']', '}'):
            if not stack:
                print(f"Error in {filepath}: Unexpected closing {ch} at line {line}, col {col}")
                return False
            top, t_line, t_col = stack.pop()
            matches = {')': '(', ']': '[', '}': '{'}
            if matches[ch] != top:
                print(f"Error in {filepath}: Mismatched {top} (line {t_line}) with {ch} at line {line}, col {col}")
                return False
        i += 1

    if stack:
        print(f"Error in {filepath}: Unclosed brackets: {len(stack)}")
        for item in stack[-5:]:
            print(f"  Unclosed {item[0]} from line {item[1]}, col {item[2]}")
        return False
    
    print(f"{filepath}: ALL BRACKETS PERFECTLY BALANCED!")
    return True

check_js_brackets('js/main.js')
check_js_brackets('js/admin.js')
