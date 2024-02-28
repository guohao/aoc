from functools import reduce

from helper import *

data = raw_data(2017, 10)


def p1():
    ll = 256
    l = list(range(ll))
    i = 0
    s = 0
    for x in ints(data):
        l = l[i:] + l[:i]
        x = x % ll
        l = list(reversed(l[:x])) + l[x:]
        l = l[-i:] + l[:-i]
        i = (i + x + s) % ll
        s += 1
    return l[0] * l[1]


def p2():
    ll = 256
    l = list(range(ll))
    i = 0
    s = 0
    xs = ([ord(x) for x in data.strip()] + [17, 31, 73, 47, 23])
    for _ in range(64):
        for x in xs:
            l = l[i:] + l[:i]
            x = x % ll
            l = list(reversed(l[:x])) + l[x:]
            l = l[-i:] + l[:-i]
            i = (i + x + s) % ll
            s += 1
    v = 0
    for x in range(16):
        v = v * 16 * 16 + reduce(lambda a, b: a ^ b, l[x * 16:x * 16 + 16])
    return hex(v)[2:]


print(p1())
print(p2())
