import sys

lines = [line.strip() for line in sys.stdin.readlines()]
a, h, d = 0, 0, 0
for line in lines:
    l, r = line.split()
    r = int(r)
    if 'fo' in l:
        h += r
        d += a * r
    elif 'down' in l:
        a += r
    else:
        a -= r
print(h * d)
