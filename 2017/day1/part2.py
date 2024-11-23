import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for a in lines:
    r = len(a) // 2
    b = a[-r:] + a[:-r]
    t += sum(int(a[i]) for i in range(len(a)) if a[i] == b[i])
print(t)
