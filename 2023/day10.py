import itertools

from common import io_utils

data = io_utils.get_data(2023, 10)
P = {
    'S': [(0, 1), (-1, 0), (1, 0), (0, -1)],
    '-': [(0, -1), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    'F': [(0, 1), (1, 0)],
    'L': [(0, 1), (-1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    '.': []}

lines = io_utils.raw_str_to_lines(data)
grid = {(i, j): lines[i][j] for i, j in itertools.product(range(len(lines)), range(len(lines[0])))}


def t(p):
    if p not in grid:
        return []
    return [(x[0] + p[0], x[1] + p[1]) for x in P[grid[p]]]


S = [p for p in grid.keys() if grid[p] == 'S'][0]
nv = [n for n in t(S) if S in t(n)]
diff = {(nv[0][0] - S[0], nv[0][1] - S[1]), (nv[1][0] - S[0], nv[1][1] - S[1])}
assert len(nv) == 2
grid[S] = [i[0] for i in P.items() if diff == set(i[1])][0]

pipes = []
nv = S
while nv:
    pipes.append(nv)
    nv = [n for n in t(nv) if n not in pipes]
    if len(nv) == 0:
        break
    nv = nv[0]
print(len(pipes) // 2)

ans = 0
for i in range(len(lines)):
    sin = False
    for j in range(len(lines[0])):
        if (i, j) in pipes and grid[(i, j)] in '|7F':
            sin = not sin
        ans += (i, j) not in pipes and sin
print(ans)
