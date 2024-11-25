import sys
import networkx as nx

g = nx.Graph()
lines = [line.strip() for line in sys.stdin.readlines()]
nodes = {}
n = len(lines)
for i in range(n):
    for j in range(n):
        nodes[i, j] = lines[i][j]

x, y = n // 2, n // 2
dx, dy = -1, 0

ans = 0
for _ in range(10000):
    u = x, y
    s = nodes.get(u, '.')
    if s == '#':
        dx, dy = dy, -dx
        nodes[u] = '.'
    else:
        dx, dy = -dy, dx
        nodes[u] = '#'
        ans += 1
    x, y = x + dx, y + dy

print(ans)
