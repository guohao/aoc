import networkx as nx


def is_open(x, y):
    return (x * x + 3 * x + 2 * x * y + y + y * y + 1352).bit_count() % 2 == 0


G = nx.Graph()
for i in range(100):
    for j in range(100):
        if is_open(i, j):
            G.add_node((i, j))
for p in G.nodes():
    for q in G.nodes():
        if p == q:
            continue
        if abs(p[0] - q[0]) + abs(p[1] - q[1]) == 1:
            G.add_edge(p, q)
print(nx.shortest_path_length(G, (1, 1), (31, 39)))
print(len([k for k, v in nx.shortest_path_length(G, (1, 1)).items() if v <= 50]))
