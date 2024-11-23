import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    a = [''.join(sorted(x)) for x in line.split()]
    t += len(set(a)) == len(a)
print(t)
