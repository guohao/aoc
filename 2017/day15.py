def p1(data: str):
    a = 591
    b = 393
    fa = 16807
    fb = 48271
    ans = 0
    for _ in range(40000000):
        a = (a * fa) % 2147483647
        b = (b * fb) % 2147483647
        if a & 0xffff == b & 0xffff:
            ans += 1
    return ans


def gen(a, fa, m):
    while True:
        a = (a * fa) % 2147483647
        if a % m == 0:
            yield a & 0xffff


def p2(data: str):
    a = 591
    b = 393
    fa = 16807
    fb = 48271
    ans = 0
    ga = iter(gen(a, fa, 4))
    gb = iter(gen(b, fb, 8))
    for _ in range(5000000):
        if next(ga) == next(gb):
            ans += 1
    return ans
