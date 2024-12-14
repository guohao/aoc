import sys

data = sys.stdin.read().strip()


def seat(s: str):
    def bs(ub, repl, ic):
        lo = 0
        hi = ub
        for fb in repl:
            mid = (lo + hi) // 2
            if fb == ic:
                hi = mid
            else:
                lo = mid
        return lo

    r = bs(128, s[:7], 'F')
    c = bs(8, s[7:], 'L')
    return r * 8 + c


ids = set()
for line in data.splitlines():
    ids.add(seat(line))
for si in ids:
    if si + 1 not in ids and si + 2 in ids:
        print(si + 1)
        break
