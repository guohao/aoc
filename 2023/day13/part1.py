import sys


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


print(sum(map(mirror, sys.stdin.read().split('\n\n'))))
