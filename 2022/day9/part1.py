import sys


def solve(data: str, n):
    seen = {(0, 0)}
    rs = [(0, 0)] * n
    directions = {'U': (-1, 0), 'R': (0, 1), 'L': (0, -1), 'D': (1, 0)}

    for line in data.splitlines():
        d, s = line.split()
        dx, dy = directions[d]
        for k in range(int(s)):
            rs[0] = rs[0][0] + dx, rs[0][1] + dy
            for i in range(1, len(rs)):
                ax, ay = rs[i - 1]
                bx, by = rs[i]
                if ax == bx and abs(ay - by) == 2:
                    by = by + (ay - by) // 2
                elif ay == by and abs(ax - bx) == 2:
                    bx = bx + (ax - bx) // 2
                elif abs(ay - by) + abs(ax - bx) > 2:
                    by = by + ((ay > by) - (ay < by))
                    bx = bx + ((ax > bx) - (ax < bx))
                rs[i] = bx, by
            seen.add(rs[-1])
    return len(seen)


print(solve(sys.stdin.read().strip(), 2))
