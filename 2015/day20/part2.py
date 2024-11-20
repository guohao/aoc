import itertools
import math

goal = int(input())


def sum_of_factors(k: int) -> int:
    s = 0
    for i in range(1, int(math.sqrt(k)) + 1):
        if k % i == 0:
            if k // i <= 50:
                s += i * 11
            if i <= 50:
                s += k // i * 11
    return s


for j in itertools.count(1):
    if sum_of_factors(j) >= goal:
        print(j)
        break
