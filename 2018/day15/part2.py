import math
import sys
from itertools import count, product

import networkx as nx


def fight(ep: int) -> int:
    g = nx.Graph()
    gs = {}
    es = {}

    def add_empty(_y, _x):
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nb = _y + dy, _x + dx
            g.add_node((_y, _x))
            if nb in g:
                g.add_edge(nb, (_y, _x))

    for y, line in enumerate(lines):
        units = {'G': gs, 'E': es}
        for x, c in enumerate(line):
            if c == '#':
                continue
            elif c in 'GE':
                units[c][y, x] = 200
            elif c == '.':
                add_empty(y, x)

    for turn in count():
        for y, x in sorted(gs | es):
            if (y, x) not in gs | es:
                continue
            mates, enemies = (gs, es) if (y, x) in gs else (es, gs)
            if not enemies:
                print(turn * sum((gs | es).values()))
                return True
            neighbors = [(dy + y, dx + x) for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]]
            if all(nb not in enemies for nb in neighbors):
                sources = [nb for nb in neighbors if nb in g]
                targets = []
                for ey, ex in enemies:
                    for nb in [(dy + ey, dx + ex) for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]]:
                        if nb in g:
                            targets.append(nb)
                min_len = math.inf
                target = -1, -1
                for u, v in product(sources, targets):
                    if nx.has_path(g, u, v):
                        pl = nx.shortest_path_length(g, u, v)
                        if pl < min_len:
                            min_len = pl
                            target = u
                        elif pl == min_len:
                            target = min(u, target)
                if target != (-1, -1):
                    if (y, x) not in mates:
                        print(mates)
                        print(y, x)
                    mates[target] = mates[y, x]
                    del mates[y, x]
                    g.remove_node(target)
                    add_empty(y, x)
                    y, x = target
            neighbors = [(dy + y, dx + x) for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]]
            min_hp = math.inf
            attack_target = -1, -1
            for nb in sorted(neighbors):
                if nb in enemies:
                    if enemies[nb] < min_hp:
                        min_hp = enemies[nb]
                        attack_target = nb
                    elif enemies[nb] == min_hp:
                        attack_target = min(nb, attack_target)
            if attack_target != (-1, -1):
                if enemies == gs:
                    enemies[attack_target] -= ep
                else:
                    enemies[attack_target] -= 3
                if enemies[attack_target] <= 0:
                    if es == enemies:
                        return -1
                    del enemies[attack_target]
                    add_empty(*attack_target)


lines = sys.stdin.readlines()
for p in count(4):
    outcome = fight(p)
    if outcome != -1:
        print(outcome)
        break
