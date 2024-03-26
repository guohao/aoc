import re
from functools import cache


def p1(data: str):
    a, b = list(map(int, re.findall(r'\d+', data)))
    ans = 0
    T = 40000000

    def low_16(s):
        return bin(s)[2:][-16:].zfill(16)

    @cache
    def gen(ca, cb):
        ca = (ca * 16807) % 2147483647
        cb = (cb * 48271) % 2147483647
        return ca, cb, low_16(ca) == low_16(cb)

    for _ in range(T):
        a, b, m = gen(a, b)
        if m:
            ans += 1
    return ans


def p2(data: str):
    a, b = list(map(int, re.findall(r'\d+', data)))
    ans = 0
    T = 5000000

    def low_16(s):
        return bin(s)[2:][-16:].zfill(16)

    @cache
    def gen(ca, cb):
        ca = (ca * 16807) % 2147483647
        while ca % 4 != 0:
            ca = (ca * 16807) % 2147483647
        cb = (cb * 48271) % 2147483647
        while cb % 8 != 0:
            cb = (cb * 48271) % 2147483647
        return ca, cb, low_16(ca) == low_16(cb)

    for _ in range(T):
        a, b, m = gen(a, b)
        if m:
            ans += 1
    return ans
