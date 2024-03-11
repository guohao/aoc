import heapq
import re
import networkx as nx


def p1(data: str):
    G = nx.DiGraph()
    for line in data.splitlines():
        pre, after = re.findall(r' \w ', line)
        G.add_edge(pre.strip(), after.strip())
    return ''.join(list(nx.lexicographical_topological_sort(G)))



def p2(data: str):
    G = nx.DiGraph()
    for line in data.splitlines():
        pre, after = re.findall(r' \w ', line)
        G.add_edge(pre.strip(), after.strip())

    indegree_map = {v: d for v, d in G.in_degree() if d > 0}
    zero_indegree = [v for v, d in G.in_degree() if d == 0]
    heapq.heapify(zero_indegree)

    workers = []
    heapq.heapify(workers)

    t = 0
    while indegree_map:
        while not zero_indegree or len(workers) == 5:
            worker = heapq.heappop(workers)
            t = worker[0]
            node = worker[1]
            for _, child in G.edges(node):
                indegree_map[child] -= 1
                if indegree_map[child] == 0:
                    heapq.heappush(zero_indegree, child)
                    del indegree_map[child]
        node = heapq.heappop(zero_indegree)
        heapq.heappush(workers, (t + 60 + ord(node) - ord('A') + 1, node))

    worker = heapq.heappop(workers)
    return worker[0]
