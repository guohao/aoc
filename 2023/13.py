from util import *


def p1(data: str):
    def mirror(part: str):
        def mirror_row(lines):
            n = len(lines)
            for i in range(1, n):
                sl = min(n - i, i)
                a = lines[i - sl:i][::-1]
                b = lines[i:i + sl]
                if a == b:
                    return i
            return 0

        rows = part.splitlines()
        cols = list(zip(*rows))
        return 100 * mirror_row(rows) + mirror_row(cols)

    return sum(map(mirror, d2p(data)))


def p2(data: str):
    def diff1(part: str):
        def mirror_row(lines):
            n = len(lines)
            for i in range(1, n):
                sl = min(n - i, i)
                a = lines[i - sl:i][::-1]
                b = lines[i:i + sl]
                dc = 0
                for j in range(sl):
                    for k in range(len(a[0])):
                        if a[j][k] != b[j][k]:
                            dc += 1
                if dc == 1:
                    return i
            return 0

        rows = part.splitlines()
        cols = list(zip(*rows))
        return 100 * mirror_row(rows) + mirror_row(cols)

    return sum(map(diff1, d2p(data)))
