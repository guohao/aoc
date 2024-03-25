import networkx as nx


def solve(data: str):
    G = nx.Graph()

    for line in data.splitlines():
        l, r = line.split('<->')
        l = l.strip()
        for t in r.split(','):
            t = t.strip()
            G.add_edge(l, t)
            G.add_edge(t, l)
    return len(nx.node_connected_component(G, '0')), len(list(nx.connected_components(G)))


def p1(data: str):
    return solve(data)[0]


def p2(data: str):
    return solve(data)[1]
