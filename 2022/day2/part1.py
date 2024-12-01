import sys

t = 0
for l in sys.stdin.readlines():
    a, b = l.split()
    pa = 'ABC'.index(a)
    pb = 'XYZ'.index(b)
    if pa == pb:
        t += 3
    elif (pb - 1) % 3 == pa:
        t += 6
    t += pb + 1

print(t)
