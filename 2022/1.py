import networkx as nx


def p1(data: str):
    ans = 0
    for part in data.split('\n\n'):
        ans = max(ans, sum(list(map(int, part.split()))))
    return ans


def p2(data: str):
    cs = []
    for part in data.split('\n\n'):
        cs.append(sum(list(map(int, part.split()))))
    return sum(sorted(cs, reverse=True)[:3])

nx.clustering()