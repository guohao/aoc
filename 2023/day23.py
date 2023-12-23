import nographs as nog
from helper import *

data = raw_data(2023, 23)
lines = lines(data)
g = nog.Array(lines, 2)
N = len(lines)
dots = g.findall(".")
START, GOAL = dots[0], dots[-1]

narrow = True


def next_edges(state, _):
    p, v = state
    if p in v or p == GOAL:
        return
    nv = v | {p}
    if narrow:
        if g[p] == '>':
            yield p + (0, 1), nv
        elif g[p] == 'v':
            yield p + (1, 0), nv
        elif g[p] == '^':
            yield p + (-1, 0), nv
        elif g[p] == '<':
            yield p + (1, 0), nv
        else:
            for ne in p.neighbors(nog.Position.moves(2), g.limits()):
                if g[ne] != '#' and ne not in v:
                    yield ne, nv
    else:
        for ne in p.neighbors(nog.Position.moves(2), g.limits()):
            if g[ne] != '#' and ne not in v:
                yield ne, nv


def bfs():
    traversal = nog.TraversalBreadthFirst(next_edges, is_tree=True)
    ret = 0
    for current in traversal.start_from((START, frozenset())):
        if current[0] == GOAL:
            ret = max(ret, len(current[1]))
    print(ret)


bfs()
narrow = False
bfs()
