import sys

t = 0
for l in sys.stdin.readlines():
    a, b = l.split()
    pa = 'ABC'.index(a)
    pb = 'XYZ'.index(b)
    t += pb * 3 + 1
    if pb == 1:
        t += pa
    elif pb == 2:
        t += (pa + 1) % 3
    else:
        t += (pa - 1) % 3

print(t)
