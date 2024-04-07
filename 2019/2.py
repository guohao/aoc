import itertools


def solve(ns, n, v):
    ns[1] = n
    ns[2] = v
    i = 0
    while i < len(ns):
        opc = ns[i]
        if opc == 1:
            ns[ns[i + 3]] = ns[ns[i + 1]] + ns[ns[i + 2]]
        elif opc == 2:
            ns[ns[i + 3]] = ns[ns[i + 1]] * ns[ns[i + 2]]
        else:
            break
        i += 4
    return ns[0]


def p1is(ns: list[int]):
    return solve(ns, 12, 2)


def p2is(ns: list[int]):
    for n in range(100):
        for v in range(100):
            if 19690720 == solve(ns.copy(), n, v):
                return 100 * n + v
