from collections import deque

import networkx
import networkx as nx

from intcode import IntCodeVM


def p1(data: str):
    q = deque([[]])
    seen = set()
    D = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    while q:
        path = q.popleft()
        vm = IntCodeVM(data)
        x, y = 0, 0
        for move in path:
            vm.rq.append(move)
            vm.run()
            s = vm.sq.popleft()
            if s == 2:
                return len(path)
            elif s == 1:
                d = D[move]
                x, y = x + d[0], y + d[1]
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i in range(1, 5):
            q.append(path + [i])


def p2(data: str):
    q = deque([[]])
    seen = set()
    D = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    oxygen = 0, 0
    while q:
        path = q.popleft()
        vm = IntCodeVM(data)
        x, y = 0, 0
        for move in path:
            vm.rq.append(move)
            vm.run()
            s = vm.sq.popleft()
            if s == 0:
                continue
            d = D[move]
            x, y = x + d[0], y + d[1]
            if s == 2:
                oxygen = x, y
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for i in range(1, 5):
            q.append(path + [i])
    G = networkx.Graph()
    for x, y in seen:
        for d in D.values():
            nb = (x + d[0], y + d[1])
            if nb in seen:
                G.add_edge(nb, (x, y))
    return max(nx.shortest_path_length(G, oxygen).values())
