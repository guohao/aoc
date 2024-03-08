import itertools


def p1(data: str):
    return sum(map(int, data.splitlines()))


def p2(data: str):
    f = 0
    seen = set()
    for fc in itertools.cycle(map(int, data.splitlines())):
        if f in seen:
            return f
        seen.add(f)
        f += fc
