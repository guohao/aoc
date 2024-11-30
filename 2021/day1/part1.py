import sys

lines = [int(line.strip()) for line in sys.stdin.readlines()]
t = 0
for i in range(1, len(lines)):
    t += lines[i] > lines[i - 1]
print(t)
