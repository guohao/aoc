from collections import deque

from util import *


def p1(data: str):
    parts = d2p(data)
    maps = []
    for part in parts[1:]:
        maps.append(list(map(ints, part.splitlines()[1:])))
    curr = ints(parts[0])
    for m in maps:
        mapped = []
        for i, src in enumerate(curr, start=1):
            for dm, sm, l in m:
                if sm <= src < sm + l:
                    mapped.append(dm + src - sm)
                    break
            if len(mapped) != i:
                mapped.append(src)
        curr = mapped
    return min(curr)


def p2(data: str):
    parts = d2p(data)
    maps = []
    for part in parts[1:]:
        maps.append(list(map(ints, part.splitlines()[1:])))
    curr = ints(parts[0])
    curr = list(zip(curr[::2], curr[1::2]))
    for m in maps:
        mapped = []
        q = deque(curr)

        def handle(ss, sl):
            for dm, sm, dl in m:
                a = sm
                b = sm + dl
                c = ss
                d = ss + sl
                if (d - a) * (c - b) < 0:
                    mapped.append((dm + max(c - a, 0), min(b, d) - max(c, a)))
                    if c < a:
                        q.append((c, a - c))
                    if b < d:
                        q.append((b, d - b))
                    return
            mapped.append((ss, sl))

        while q:
            handle(*q.popleft())
        curr = mapped
    return min(k for k, _ in curr)
