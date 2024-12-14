import math
import sys

data = sys.stdin.read().strip()

data = list(map(int, data.strip()))
data += range(len(data) + 1, 1000000 + 1)
g = {}
for i in range(len(data) - 1):
    g[data[i]] = data[i + 1]
g[data[-1]] = data[0]
curr = data[0]


def next_nodes(node, cnt):
    for _ in range(cnt):
        node = g[node]
        yield node


for i in range(10000000):
    n1, n2, n3, n4 = next_nodes(curr, 4)
    g[curr] = g[n3]
    dst_cup = curr - 1
    while (dst_cup in [n1, n2, n3]) or (dst_cup <= 0):
        dst_cup -= 1
        if dst_cup <= 0:
            dst_cup = len(g)
    dst_follower = list(next_nodes(dst_cup, 1))[0]
    g[dst_cup] = n1
    g[n3] = dst_follower
    curr = n4
print(math.prod(next_nodes(1, 2)))
