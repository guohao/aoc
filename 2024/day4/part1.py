import sys
import itertools

ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
t = 0
for i, j in itertools.product(range(len(ls)), range(len(ls[0]))):
    for dx, dy in itertools.product(range(-1, 2), repeat=2):
        line = ''.join(g.get((i + k * dx, j + k * dy), '.') for k in range(4))
        if line == 'XMAS':
            t += 1
print(t)
