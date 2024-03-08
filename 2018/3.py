import re
from collections import defaultdict


def p1(data: str):
    g = set()
    ol = set()
    for line in data.splitlines():
        id, fl, ft, w, h = list(map(int, re.findall(r'\d+', line)))
        for i in range(ft, ft + h):
            for j in range(fl, fl + w):
                p = (i, j)
                if p in g:
                    ol.add(p)
                g.add(p)
    return len(ol)


def p2(data: str):
    g = defaultdict(int)
    ol = set()
    for line in data.splitlines():
        id, fl, ft, w, h = list(map(int, re.findall(r'\d+', line)))
        for i in range(ft, ft + h):
            for j in range(fl, fl + w):
                p = (i, j)
                g[p] += 1
    for line in data.splitlines():
        id, fl, ft, w, h = list(map(int, re.findall(r'\d+', line)))
        o1 = True
        for i in range(ft, ft + h):
            for j in range(fl, fl + w):
                p = (i, j)
                if g[p] != 1:
                    o1 = False
        if o1:
            return id
