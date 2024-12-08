import sys
from functools import cache

import networkx as nx


def draw_room(r: str):
    g = nx.Graph()
    r = r[1:-1]

    @cache
    def expand(i, j, cmd):
        idx = 0
        while idx < len(cmd):
            c = cmd[idx]
            if c == '(':
                pc = 1
                end = idx + 1
                ps = idx + 1
                parts = []
                while pc:
                    if cmd[end] == '(':
                        pc += 1
                    elif cmd[end] == ')':
                        if pc == 1:
                            parts.append(cmd[ps:end])
                        pc -= 1
                    elif cmd[end] == '|':
                        if pc == 1:
                            parts.append(cmd[ps:end])
                            ps = end + 1
                    end += 1
                for part in parts:
                    expand(i, j, part + cmd[end:])
                return
            else:
                d = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}[c]
                ni, nj = i + d[0], j + d[1]
                g.add_edge((i, j), (ni, nj))
                i, j = ni, nj
                idx += 1

    expand(0, 0, r)
    return g


data = sys.stdin.read()
print(max(map(len, nx.single_source_shortest_path(draw_room(data.strip()), (0, 0)).values())) - 1)
