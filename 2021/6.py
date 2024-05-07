from collections import defaultdict


def solve(data: str, days: int):
    seq = list(map(int, data.strip().split(',')))
    lfs = defaultdict(int)
    for t in seq:
        lfs[t] += 1

    def gen_next_day(d):
        nlfs = defaultdict(int)
        for t, c in d.items():
            if t > 0:
                nlfs[t - 1] += c
            else:
                nlfs[6] += c
                nlfs[8] += c
        return nlfs

    for _ in range(days):
        lfs = gen_next_day(lfs)
    return sum(lfs.values())


def p1(data: str):
    return solve(data, 80)


def p2(data: str):
    return solve(data, 256)
