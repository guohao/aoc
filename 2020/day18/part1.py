import sys
from collections import deque


t = 0
for line in sys.stdin.readlines():
    line= line.strip()
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
    t += operands.pop()
print(t)


