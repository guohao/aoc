import sys

t = 0
lines = sys.stdin.readlines()
for line in lines:
    a, b, c = map(int, line.split('x'))
    t += min(a * b, b * c, a * c) + 2 * (a * b + b * c + a * c)
print(t)
