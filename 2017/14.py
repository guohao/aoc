from collections import deque
from functools import reduce

import networkx as nx


def knot_hash(data: str):
    sz = 0
    q = deque(range(256))
    i = 0
    seq = [ord(c) for c in data.strip()] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for c in seq:
            q2 = deque()
            for _ in range(c):
                q2.append(q.popleft())
            while q2:
                q.append(q2.pop())
            q.rotate(-sz)
            i += c + sz
            sz += 1
    q.rotate(i)

    ans = ''
    q = list(q)
    for k in range(0, 256, 16):
        ans += hex(reduce(lambda a, b: a ^ b, q[k:k + 16]))[2:].zfill(2)
    return ans


def p1(data: str):
    data = data.strip()
    ans = 0
    for i in range(128):
        s = data + '-' + str(i)
        hashed = knot_hash(s)
        for c in hashed:
            ans += int(c, 16).bit_count()
    return ans


def p2(data: str):
    G = nx.Graph()
    data = data.strip()
    for x in range(128):
        s = data + '-' + str(x)
        hashed = knot_hash(s)
        for y, b in enumerate(bin(int(hashed, 16))[2:].zfill(128)):
            if b == '0':
                continue
            G.add_node((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nb = x + dx, y + dy
                if G.has_node(nb):
                    G.add_edge(nb, (x, y))
    return len(list(nx.connected_components(G)))
