def p1(data: str):
    x, y = 0, 0
    for line in data.splitlines():
        n = int(line.split()[1])
        if 'forward' in line:
            y += n
        elif 'up' in line:
            x -= n
        else:
            x += n
    return abs(x * y)


def p2(data: str):
    x, y = 0, 0
    aim = 0
    for line in data.splitlines():
        n = int(line.split()[1])
        if 'forward' in line:
            y += n
            x += aim * n
        elif 'up' in line:
            aim -= n
        else:
            aim += n
    return abs(x * y)
