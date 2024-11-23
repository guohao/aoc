import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    t+=len(line.split())==len(set(line.split()))
print(t)
