def p1(data: str):
    ans = 0
    ns = list(map(int, data.splitlines()))
    for i, n in enumerate(ns):
        if i == 0:
            continue
        if n > ns[i - 1]:
            ans += 1
    return ans


def p2(data: str):
    ans = 0
    ns = list(map(int, data.splitlines()))
    ps = [sum(ns[i - 2:i + 1]) for i in range(2, len(ns))]
    for i, s in enumerate(ps):
        if i == 0:
            continue
        if s > ps[i - 1]:
            ans += 1
    return ans
