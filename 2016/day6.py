from collections import defaultdict

from helper import *

data = raw_data(2016, 6)
lines = lines(data)


def solve():
    cs = [defaultdict(lambda: 0) for _ in range(len(lines[0]))]
    for line in lines:
        for i, c in enumerate(line):
            cs[i][c] += 1
    ans = ''
    for ds in cs:
        ans += [k for k, v in ds.items() if v == max(ds.values())][0]
    print(ans)

    ans = ''
    for ds in cs:
        ans += [k for k, v in ds.items() if v == min(ds.values())][0]
    print(ans)


solve()
