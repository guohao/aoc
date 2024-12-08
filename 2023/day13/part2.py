import sys


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


print(sum(map(diff1, sys.stdin.read().split('\n\n'))))
