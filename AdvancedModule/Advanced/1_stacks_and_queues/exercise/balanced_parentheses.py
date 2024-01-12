parentheses = input()

open_bracket_stack = []

for index in range(len(parentheses)):
    current_parenthese = parentheses[index]
    if current_parenthese in '{[(':
        open_bracket_stack.append(current_parenthese)
    else:
        if not open_bracket_stack:
            print('NO')
            break
        last_open_bracket = open_bracket_stack.pop()
        current_combination = last_open_bracket + current_parenthese
        if current_combination not in '(){}[]':
            print('NO')
            break
else:
    print('YES')
    