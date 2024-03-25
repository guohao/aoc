from functools import reduce

import networkx as nx


def knot_hashes(s: str):
    ll = 256
    l = list(range(ll))
    i = 0
    skip = 0
    xs = ([ord(x) for x in s] + [17, 31, 73, 47, 23])
    for _ in range(64):
        for x in xs:
            l = l[i:] + l[:i]
            x = x % ll
            l = list(reversed(l[:x])) + l[x:]
            l = l[-i:] + l[:-i]
            i = (i + x + skip) % ll
            skip += 1

    ans = ''
    for x in range(16):
        ans += hex(reduce(lambda a, b: a ^ b, l[x * 16:x * 16 + 16]))[2:].zfill(2)
    return ans


def p1(data: str):
    ans = 0
    for i in range(128):
        s = data.strip() + '-' + str(i)
        hashed = knot_hashes(s)
        ans += int(hashed, 16).bit_count()
    return ans


def p2(data: str):
    G = nx.Graph()

    for i in range(128):
        s = data.strip() + '-' + str(i)
        hashed = knot_hashes(s)
        v = bin(int(hashed, 16))[2:].zfill(128)
        for j in range(128):
            if v[j] == '1':
                G.add_node((i, j))
    for node in G.nodes():
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nd = (node[0] + dx, node[1] + dy)
            if G.has_node(nd):
                G.add_edge(node, nd)
    return len(list(nx.connected_components(G)))
