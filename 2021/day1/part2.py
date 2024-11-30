import sys

lines = [int(line.strip()) for line in sys.stdin.readlines()]
t = 0
for i in range(4, len(lines) + 1):
    t += sum(lines[i - 3:i]) > sum(lines[i - 4:i - 1])
print(t)
