from functools import reduce


def p1(data):
    ll = 256
    l = list(range(ll))
    i = 0
    s = 0
    for x in list(map(int, data.split(','))):
        l = l[i:] + l[:i]
        x = x % ll
        l = list(reversed(l[:x])) + l[x:]
        l = l[-i:] + l[:-i]
        i = (i + x + s) % ll
        s += 1
    return l[0] * l[1]


def p2(data: str):
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
