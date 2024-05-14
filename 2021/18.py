import itertools
import math
from collections import deque
from functools import reduce


def t(s: str):
    q = deque()
    d = 0
    for c in s:
        if c == '[':
            d += 1
        elif c == ']':
            d -= 1
        elif c == ',':
            continue
        else:
            q.append((d, int(c)))
    return q


def merge(a, b):
    rq = deque()
    for d, v in a + b:
        rq.append((d + 1, v))
    lq = deque()
    while True:
        while any(x == 5 for x, _ in rq):
            d, a = rq.popleft()
            if d == 5:
                bd, b = rq.popleft()
                assert bd == 5
                if rq:
                    nd, c = rq.popleft()
                    rq.appendleft((nd, b + c))
                rq.appendleft((d - 1, 0))
                if lq:
                    nd, c = lq.pop()
                    rq.appendleft((nd, c + a))
            else:
                lq.append((d, a))
        while lq:
            rq.appendleft(lq.pop())
        if any(v >= 10 for _, v in lq + rq):
            while True:
                d, a = rq.popleft()
                if a >= 10:
                    rq.appendleft((d + 1, math.ceil(a / 2)))
                    rq.appendleft((d + 1, math.floor(a / 2)))
                    break
                else:
                    lq.append((d, a))
        else:
            break
    return rq


def magnitude(q: deque):
    hq = deque()
    while q:
        d, a = q.popleft()
        if hq and hq[-1][0] == d:
            _, b = hq.pop()
            q.appendleft((d - 1, 3 * b + 2 * a))
        else:
            hq.append((d, a))
    return hq[0][1]


def p1(data: str):
    return magnitude(reduce(merge, map(t, data.splitlines())))


def p2(data: str):
    sns = list(map(t, data.splitlines()))
    return max(magnitude(merge(*p)) for p in itertools.permutations(sns, 2))
