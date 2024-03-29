def p1(data: str):
    seen = {(0, 0)}
    hx, hy, tx, ty = 0, 0, 0, 0
    directions = {'U': (-1, 0), 'R': (0, 1), 'L': (0, -1), 'D': (1, 0)}
    for line in data.splitlines():
        d, s = line.split()
        s = int(s)
        dx, dy = directions[d]
        for _ in range(s):
            hx = hx + dx
            hy = hy + dy
            if abs(hx - tx) == 2:
                tx += (hx - tx) // 2
                ty = hy
            elif abs(hy - ty) == 2:
                ty += (hy - ty) // 2
                tx = hx
            seen.add((tx, ty))
    return len(seen)


def p2(data: str):
    seen = {(0, 0)}
    rs = [(0, 0)] * 10
    directions = {'U': (-1, 0), 'R': (0, 1), 'L': (0, -1), 'D': (1, 0)}

    def cmp(a, b):
        return (a > b) - (a < b)

    for line in data.splitlines():
        d, s = line.split()
        dx, dy = directions[d]
        for k in range(int(s)):
            rs[0] = rs[0][0] + dx, rs[0][1] + dy
            for i in range(1, len(rs)):
                xc = cmp(rs[i - 1][0], rs[i][0])
                yc = cmp(rs[i - 1][1], rs[i][1])
                diff = abs(rs[i - 1][0] - rs[i][0]) + abs(rs[i - 1][1] - rs[i][1])
                if (diff == 2 and xc * yc == 0) or diff > 2:
                    rs[i] = (rs[i][0] + xc, rs[i][1] + yc)
                seen.add(rs[-1])
    return len(seen)
