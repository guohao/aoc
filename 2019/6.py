import networkx as nx


def p1(data: str):
    G = nx.DiGraph()
    for line in data.splitlines():
        a, b = line.split(')')
        G.add_edge(a, b)

    return sum(len(nx.descendants(G, n)) for n in G.nodes())


def p2(data: str):
    G = nx.Graph()
    for line in data.splitlines():
        a, b = line.split(')')
        G.add_edge(a, b)

    return nx.shortest_path_length(G, 'YOU', 'SAN') - 2
