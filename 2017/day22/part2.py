import sys
import networkx as nx

g = nx.Graph()
lines = [line.strip() for line in sys.stdin.readlines()]
nodes = {}
n = len(lines)
for i in range(n):
    for j in range(n):
        nodes[i, j] ='infected' if  lines[i][j] =='#' else 'clean'

x, y = n // 2, n // 2
dx, dy = -1, 0

ans = 0
for _ in range(10000000):
    u = x, y
    s = nodes.get(u, 'clean')
    if s == 'clean':
        dx, dy = -dy, dx
        nodes[u] = 'weakened'
    elif s=='weakened':
        nodes[u] = 'infected'
        ans += 1
    elif s=='infected':
        dx, dy = dy, -dx
        nodes[u] = 'flagged'
    else:
        dx, dy = -dx, -dy
        nodes[u] = 'clean'
    x, y = x + dx, y + dy

print(ans)
