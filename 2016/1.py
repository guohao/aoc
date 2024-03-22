def p1(data: str):
    x = 0
    y = 0
    d = (1, 0)
    for step in data.strip().split(', '):
        if step[0] == 'R':
            d = (-d[1], d[0])
        else:
            d = (d[1], -d[0])
        n = int(step[1:])
        x += d[0] * n
        y += d[1] * n
    return abs(x) + abs(y)


def p2(data: str):
    x = 0
    y = 0
    d = (1, 0)
    seen = set()
    for step in data.strip().split(', '):
        if step[0] == 'R':
            d = (-d[1], d[0])
        else:
            d = (d[1], -d[0])
        for i in range(int(step[1:])):
            x += d[0]
            y += d[1]
            if (x, y) in seen:
                return abs(x) + abs(y)
            seen.add((x, y))
