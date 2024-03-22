def move(g, start, data):
    x, y = start
    ans = ''
    for line in data.splitlines():
        for c in line:
            dx, dy = x, y
            match c:
                case 'U':
                    dx -= 1
                case 'R':
                    dy += 1
                case 'L':
                    dy -= 1
                case 'D':
                    dx += 1
            if (dx, dy) in g:
                x, y = dx, dy
        ans += g[x, y]
    return ans


def p1(data: str):
    g = {(i, j): str((i - 1) * 3 + j) for i in range(1, 4) for j in range(1, 4)}
    x, y = 2, 2
    return move(g, (x, y), data)


def p2(data: str):
    g = {}
    lens = [1, 3, 5, 3, 1]
    n = 1
    for i in range(len(lens)):
        offset = (5 - lens[i]) // 2
        for j in range(offset, offset + lens[i]):
            g[i, j] = hex(n)[-1].upper()
            n += 1
    x, y = 2, 0
    return move(g, (x, y), data)
