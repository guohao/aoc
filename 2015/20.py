import math


def sum_of_factors(x, pt=False):
    i = 1
    s = set()
    while i <= math.sqrt(x):
        if x % i == 0:
            if not pt or i * 50 >= x:
                s.add(i)
            if not pt or x // i * 50 >= x:
                s.add(x // i)
        i += 1
    return sum(s) * 10


def solve(data: str, pt=False):
    n = int(data)
    for d in range(1, n):
        if sum_of_factors(d, pt) >= n:
            return d


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, True)
