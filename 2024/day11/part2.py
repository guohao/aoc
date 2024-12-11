import re
import sys
from functools import cache

nums = list(map(int, re.findall(r'-?\d+', sys.stdin.read())))

@cache
def gen(n):
    if n == 0:
        return 1,
    elif len(str(n)) % 2 == 0:
        s = str(n)
        l, r = int(s[:len(s) // 2]), int(s[len(s) // 2:])
        return l, r
    else:
        return n * 2024,


@cache
def geni(n, i):
    if i == 0:
        return 1
    a = 0
    for k in gen(n):
        a += geni(k, i - 1)
    return a


print(sum(geni(x, 75) for x in nums))
