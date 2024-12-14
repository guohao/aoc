import networkx as nx


import sys
data = sys.stdin.read().strip()

    G = nx.DiGraph()
    for line in data.splitlines():
        a, b = line.split(')')
        G.add_edge(a, b)

    return sum(len(nx.descendants(G, n)) for n in G.nodes())


import sys
data = sys.stdin.read().strip()

    G = nx.Graph()
    for line in data.splitlines():
        a, b = line.split(')')
        G.add_edge(a, b)

    return nx.shortest_path_length(G, 'YOU', 'SAN') - 2
