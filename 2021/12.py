from collections import deque

import networkx as nx


def p1(data: str):
    g = nx.Graph()
    for line in data.splitlines():
        l, r = line.split('-')
        g.add_edge(l, r)
    ans = 0
    q = deque()
    q.append(('start',))
    while q:
        p = q.popleft()
        if p[-1] == 'end':
            ans += 1
            continue
        curr = p[-1]
        for x in g.neighbors(curr):
            if x.islower() and x in p:
                continue
            q.append(p + (x,))
    return ans


def p2(data: str):
    g = nx.Graph()
    for line in data.splitlines():
        l, r = line.split('-')
        g.add_edge(l, r)
    ans = 0
    q = deque()
    q.append(('start',))
    while q:
        p = q.popleft()
        if p[-1] == 'end':
            ans += 1
            continue
        curr = p[-1]
        for x in g.neighbors(curr):
            if x == 'start':
                continue
            if x.islower() and p.count(x) > 1:
                continue
            if x.islower() and p.count(x) == 1 and any(p.count(y) == 2 for y in p if y.islower()):
                continue
            q.append(p + (x,))
    return ans
