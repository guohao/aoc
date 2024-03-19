import itertools
import math


def p1is(data):
    ms = [a * b for a, b in itertools.combinations(data, 2)]
    return 2 * sum(ms) + min(ms)


def p2is(data):
    return 2 * sum(sorted(data)[:2]) + math.prod(data)
