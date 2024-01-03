from helper import *
from z3 import *

data = raw_data(2022, 21)

numbers = {}
ops = {}

for line in lines(data):
    name, op = line.split(':')
    if name == 'humn':
        numbers[name] = 'x'
        continue

    if op.strip().isnumeric():
        numbers[name] = op
    else:
        a, op, b = op.split()
        if name == 'root':
            ops[name] = (a, '==', b)
        else:
            ops[name] = (a, op, b)

while 'root' in ops:
    for name, op in ops.copy().items():
        a, op, b = op
        if a in numbers and b in numbers:
            if a.isnumeric() and b.isnumeric():
                if op == '+':
                    numbers[name] = numbers[a] + numbers[b]
                elif op == '-':
                    numbers[name] = numbers[a] - numbers[b]
                elif op == '*':
                    numbers[name] = numbers[a] * numbers[b]
                elif op == '/':
                    numbers[name] = numbers[a] // numbers[b]
            else:
                numbers[name] = f'(({numbers[a]})' + op + f'({numbers[b]}))'
            del ops[name]

x = Int('x')
solve(eval(numbers['root']))
