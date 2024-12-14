import sys

data = sys.stdin.read().strip()

x, y = 0, 0
d = -1, 10
for line in data.splitlines():
    c = line[0]
    if c in "NSEW":
        dc = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}[c]
        m = int(line[1:])
        d = d[0] + m * dc[0], d[1] + m * dc[1]
    elif c == 'F':
        m = int(line[1:])
        x, y = x + m * d[0], y + m * d[1]
    elif c == 'L':
        m = int(line[1:])
        if m == 90:
            d = -d[1], d[0]
        elif m == 180:
            d = -d[0], -d[1]
        elif m == 270:
            d = d[1], -d[0]
    elif c == 'R':
        m = int(line[1:])
        if m == 90:
            d = d[1], -d[0]
        elif m == 180:
            d = -d[0], -d[1]
        elif m == 270:
            d = -d[1], d[0]
print(abs(x) + abs(y))
