import sys

t = 0
for line in sys.stdin.readlines():
    line = line.strip()
    t += len(line) - len(eval(line))
print(t)
