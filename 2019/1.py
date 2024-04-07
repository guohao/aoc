def p1is(n: list[int]):
    return n[0] // 3 - 2

def p2is(n: list[int]):
    n = n[0]
    ans = 0
    while n > 2:
      n = n // 3 - 2
      ans += n
    if n < 0:
        n = 0
    ans +=n
    return ans
