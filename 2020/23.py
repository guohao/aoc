import math
from collections import deque
from typing import List


def p1(data: str):
    q = deque(map(int, data.strip()))
    for _ in range(100):
        q.rotate(-1)
        n = q[-1]
        popped = [q.popleft() for _ in range(3)]
        min_v = min(q)
        n -= 1
        while n >= min_v and n not in q:
            n -= 1
        if n < min_v:
            n = max(q)
        idx = q.index(n)
        q.rotate(-(idx + 1))
        for x in reversed(popped):
            q.appendleft(x)
        q.rotate(idx + 1)
        i1 = q.index(1)
    q.rotate(-(q.index(1) + 1))
    q.pop()
    return ''.join(map(str, q))


def p2(data: str):
    data = list(map(int, data.strip()))
    data += range(len(data) + 1, 1000000 + 1)
    g = {}
    for i in range(len(data) - 1):
        g[data[i]] = data[i + 1]
    g[data[-1]] = data[0]
    curr = data[0]

    def next_nodes(node, cnt):
        for _ in range(cnt):
            node = g[node]
            yield node

    for i in range(10000000):
        n1, n2, n3, n4 = next_nodes(curr, 4)
        g[curr] = g[n3]
        dst_cup = curr - 1
        while (dst_cup in [n1, n2, n3]) or (dst_cup <= 0):
            dst_cup -= 1
            if dst_cup <= 0:
                dst_cup = len(g)
        dst_follower = list(next_nodes(dst_cup, 1))[0]
        g[dst_cup] = n1
        g[n3] = dst_follower
        curr = n4
    return math.prod(next_nodes(1, 2))
