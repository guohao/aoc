from collections import Counter, defaultdict

import networkx as nx


def p1(data: str):
    G = nx.DiGraph()
    for a in map(int, data.splitlines()):
        G.add_node(a)
    G.add_node(0)
    G.add_node(3 + max(G.nodes))
    for n in G.nodes:
        for i in range(1, 4):
            if n - i in G:
                G.add_edge(n - i, n)
    path = nx.dag_longest_path(G, 0, max(G.nodes))
    c = Counter([path[i] - path[i - 1] for i in range(1, len(path))])
    return c[1] * c[3]


def p2(data: str):
    G = nx.DiGraph()
    for a in map(int, data.splitlines()):
        G.add_node(a)
    G.add_node(0)
    G.add_node(3 + max(G.nodes))
    for n in G.nodes:
        for i in range(1, 4):
            if n - i in G:
                G.add_edge(n - i, n)
    dp = defaultdict(int)
    dp[0] = 1
    for i in sorted(G.nodes)[1:]:
        for succ in G.predecessors(i):
            dp[i] += dp[succ]
    return dp[max(dp.keys())]
