import sys

data = sys.stdin.read().strip()

ops = data.splitlines()
i = 0
acc = 0
seen = set()
while i < len(ops):
    if i in seen:
        break
    seen.add(i)
    op = ops[i]
    if 'acc' in op:
        acc += int(op.split()[1])
    elif 'jmp' in op:
        i += int(op.split()[1])
        continue
    i += 1
print(acc)
