import sys

t = 0
for line in sys.stdin.readlines():
    line = line.strip()
    t += line.count('\\') + line.count('"') + 2

print(t)
