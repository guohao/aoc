import networkx as nx


def p1(data: str):
    G = nx.DiGraph()
    for line in data.splitlines():
        cells = line.replace(',', '').split()
        parent = cells[0]
        children = cells[3:]
        for child in children:
            G.add_edge(parent, child)
    return (list(nx.topological_sort(G)))[0]


def p2(data: str):
    G = nx.DiGraph()
    for line in data.splitlines():
        cells = line.replace(',', '').split()
        parent = cells[0]
        weight = int(cells[1][1:-1])
        G.add_node(parent, weight=weight)
        children = cells[3:]
        for child in children:
            G.add_edge(parent, child)

    weights = nx.get_node_attributes(G, 'weight')

    def weight_of(node):
        return weights[node] + sum(weight_of(nb) for nb in G[node])

    def find_diff(node):
        for c in G[node]:
            ans = find_diff(c)
            if ans:
                return ans
        if len(G[node]) < 2:
            return None
        cw = {c: weight_of(c) for c in G[node]}
        if len(set(cw.values())) == 1:
            return None
        cc = sorted(((list(cw.values()).count(v)), c) for c, v in cw.items())
        target = [(v, c) for v, c in cc if v == 1][0]
        return weights[target[1]] + cw[cc[cc.index(target) + 1][1]] - cw[target[1]]

    root = (list(nx.topological_sort(G)))[0]
    return find_diff(root)
