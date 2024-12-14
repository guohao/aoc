from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

vm = IntCodeVM(data)
vm.run()
G = {}
lines = ''.join(chr(x) for x in vm.sq)
for i, line in enumerate(lines.splitlines()):
    for j, c in enumerate(line):
        G[i, j] = c

ans = 0
for x, y in G:
    if G[x, y] == '.':
        continue
    if all((x + dx, y + dy) in G and G[x + dx, y + dy] == '#' for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        ans += x * y
print(ans)
