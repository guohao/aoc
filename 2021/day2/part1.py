import sys

lines = [line.strip() for line in sys.stdin.readlines()]
h, d = 0, 0
for line in lines:
    a, b = line.split()
    b = int(b)
    if 'fo' in a:
        h += b
    elif 'down' in a:
        d += b
    else:
        d-=b
print(h * d)
