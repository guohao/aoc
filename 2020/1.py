import itertools
import math


def p1(data: str):
    ints = list(map(int, data.splitlines()))
    for pair in itertools.combinations(ints, 2):
        if sum(pair) == 2020:
            return math.prod(pair)


def p2(data: str):
    ints = list(map(int, data.splitlines()))
    for pair in itertools.combinations(ints, 3):
        if sum(pair) == 2020:
            return math.prod(pair)
