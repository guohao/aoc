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


import sys

data = sys.stdin.read().strip()

ans = 0
for line in data.splitlines():
    ans = max(ans, seat(line))
print(ans)
