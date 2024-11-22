import itertools
import networkx as nx

fn = int(input())
g = nx.Graph()


def is_open(x, y):
    if x < 0 or y < 0:
        return False
    return not (x * x + 3 * x + 2 * x * y + y + y * y + fn).bit_count() % 2


for i, j in itertools.product(range(100), repeat=2):
    if is_open(i, j):
        for k, l in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if k == l == 0:
                continue
            if is_open(i + k, l + j):
                g.add_edge((i + k, l + j), (i, j))

print(len(nx.single_source_shortest_path_length(g, (1, 1), cutoff=50)))
