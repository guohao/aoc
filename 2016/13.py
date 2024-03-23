import networkx as nx


def solve(data: str, part2=False):
    n = int(data)
    X, Y = 31, 39
    g = nx.Graph()
    for x in range(0, X + 50):
        for y in range(0, Y + 50):
            k = x * x + 3 * x + 2 * x * y + y + y * y + n
            if k.bit_count() % 2 == 0:
                g.add_node((x, y))
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if i == j:
                        continue
                    x1, y1 = x + i, y + j
                    if g.has_node((x1, y1)):
                        g.add_edge((x1, y1), (x, y))
    if part2:
        ans = set()
        for path in nx.single_source_shortest_path(g, (1, 1), 50).values():
            ans = ans.union(set(path))
        return len(ans)
    else:
        return nx.shortest_path_length(g, (1, 1), (X, Y))


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, True)
