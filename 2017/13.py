import itertools


def p1(data: str):
    drs = [list(map(int, line.split(':'))) for line in data.splitlines()]
    return sum(d * r for d, r in drs if d % (r * 2 - 2) == 0)


def p2(data: str):
    drs = [list(map(int, line.split(':'))) for line in data.splitlines()]
    for x in itertools.count():
        if all((x + d) % (r * 2 - 2) for d, r in drs):
            return x
