from collections import deque


def p1ss(line: str):
    operands = deque()
    operators = deque()
    for c in line.replace('(', '( ').replace(')', ' )').split():
        if c.isdigit():
            operands.append(c)
        elif c == '(':
            operators.append(c)
        elif c == ')':
            while operators and operators[-1] != '(':
                operands.append(eval(f'{operands.pop()} {operators.pop()} {operands.pop()}'))
            operators.pop()
        else:
            while operators and operators[-1] != '(':
                operands.append(eval(f'{operands.pop()} {operators.pop()} {operands.pop()}'))
            operators.append(c)
    while operators:
        operands.append(eval(f'{operands.pop()} {operators.pop()} {operands.pop()}'))
    return operands.pop()


def p2ss(line: str):
    operands = deque()
    operators = deque()
    precedence = {'+': 1, '*': 0}
    for c in line.replace('(', '( ').replace(')', ' )').split():
        if c.isdigit():
            operands.append(c)
        elif c == '(':
            operators.append(c)
        elif c == ')':
            while operators and operators[-1] != '(':
                operands.append(eval(f'{operands.pop()} {operators.pop()} {operands.pop()}'))
            operators.pop()
        else:
            while operators and operators[-1] != '(' and precedence[c] <= precedence[operators[-1]]:
                operands.append(eval(f'{operands.pop()} {operators.pop()} {operands.pop()}'))
            operators.append(c)
    while operators:
        operands.append(eval(f'{operands.pop()} {operators.pop()} {operands.pop()}'))
    return operands.pop()
