import sys

lines = sys.stdin.readlines()
t = 0
for line in lines:
    a, b, c = map(int, line.split('x'))
    t += min(a + b, b + c, a + c) * 2 + a * b * c
print(t)
