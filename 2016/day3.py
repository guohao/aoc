from helper import *


def is_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


def p1():
    ans = 0
    for line in lines(raw_data(2016, 3)):
        a, b, c = ints(line)
        if is_triangle(a, b, c):
            ans += 1
    print(ans)


def p2():
    all = lines(raw_data(2016, 3))
    vs = [[] for _ in range(len(all))]
    for line in all:
        for j, v in enumerate(ints(line)):
            vs[j].append(v)
    ans = 0
    for v in vs:
        for i in range(0, len(v), 3):
            if is_triangle(v[i], v[i + 1], v[i + 2]):
                ans += 1
    print(ans)

p1()
p2()