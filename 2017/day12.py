import networkx as nx
from helper import *

data = raw_data(2017, 12)


def solve():
    G = nx.Graph()

    for line in lines(data):
        l, r = line.split('<->')
        l = l.strip()
        for t in r.split(','):
            t = t.strip()
            G.add_edge(l, t)
            G.add_edge(t, l)
    print(len(nx.node_connected_component(G, '0')))
    print(len(list(nx.connected_components(G))))

solve()
