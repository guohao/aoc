def p1(data: str):
    x = 1
    s = []
    for cmd in data.splitlines():
        s.append(x)
        if cmd != 'noop':
            s.append(x)
            x += int(cmd.split()[1])
    return sum(i * s[i - 1] for i in range(20, 260, 40))


def p2(data: str):
    x = 1
    s = []
    for cmd in data.splitlines():
        s.append(x)
        if cmd != 'noop':
            s.append(x)
            x += int(cmd.split()[1])
    for r in range(6):
        line = ''
        for c in range(40):
            if c in range(s[r * 40 + c] - 1, s[r * 40 + c] + 2):
                line += '#'
            else:
                line += '.'
        print(line)
