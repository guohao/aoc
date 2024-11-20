import itertools
import math

goal = int(input()) // 10


def sum_of_factors(k: int) -> int:
    s = 0
    for i in range(1, int(math.sqrt(k)) + 1):
        if k % i == 0:
            s += i
            s += k // i
    return s


for j in itertools.count(1):
    if sum_of_factors(j) >= goal:
        print(j)
        break
