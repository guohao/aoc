import sys

lines = [l.strip() for l in sys.stdin.readlines()]

numbers = {}
ops = {}

for line in lines:
    name, op = line.split(':')
    if op.strip().isnumeric():
        numbers[name] = int(op)
    else:
        a, op, b = op.split()
        ops[name] = (a, op, b)

while 'root' in ops:
    for name, op in ops.copy().items():
        a, op, b = op
        if a in numbers and b in numbers:
            if op == '+':
                numbers[name] = numbers[a] + numbers[b]
            elif op == '-':
                numbers[name] = numbers[a] - numbers[b]
            elif op == '*':
                numbers[name] = numbers[a] * numbers[b]
            elif op == '/':
                numbers[name] = numbers[a] // numbers[b]
            del ops[name]
print(numbers['root'])
