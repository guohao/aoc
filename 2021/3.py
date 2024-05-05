import math
from collections import Counter


def p1(data: str):
    common = ['', '']
    for x in zip(*data.splitlines()):
        c = Counter(x).most_common()
        common[0] += c[0][0]
        common[1] += c[-1][0]
    return math.prod(int(x, 2) for x in common)


def p2(data: str):
    ns = data.splitlines()
    mcs = ns.copy()
    mc = 0
    for i in range(len(ns[0])):
        if len(mcs) == 1:
            mc = mcs[0]
            break
        a = list(zip(*mcs))
        c = Counter(a[i])
        if c['1'] == c['0']:
            bmc = '1'
        else:
            bmc = c.most_common()[0][0]
        mcs = [x for x in mcs if x[i] == bmc]
    lcs = ns.copy()
    lc = 0
    for i in range(len(ns[0])):
        if len(lcs) == 1:
            lc = lcs[0]
            break
        c = Counter(list(zip(*lcs))[i])
        if c['1'] == c['0']:
            blc = '0'
        else:
            blc = c.most_common()[-1][0]
        lcs = [x for x in lcs if x[i] == blc]
    return int(lc, 2) * int(mc, 2)
