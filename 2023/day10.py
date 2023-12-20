import nographs as nog
from helper import *

data = raw_data(2023, 10)
P = {
    'S': [(0, 1), (-1, 0), (1, 0), (0, -1)],
    '-': [(0, -1), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    'F': [(0, 1), (1, 0)],
    'L': [(0, 1), (-1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    '.': []}

lines = lines(data)
grid = nog.Array(lines).mutable_copy()
S = grid.findall('S')[0]
nv = [x for x in S.neighbors(S.moves()) if any(S == (d[0] + x[0], d[1] + x[1]) for d in P[grid[x]])]
diff = {(nv[0][0] - S[0], nv[0][1] - S[1]), (nv[1][0] - S[0], nv[1][1] - S[1])}
grid[S] = [i[0] for i in P.items() if diff == set(i[1])][0]

pipes = set()
nv = S
while nv:
    if nv in pipes:
        break
    pipes.add(nv)
    for d in P[grid[nv]]:
        nnv = (nv[0] + d[0], nv[1] + d[1])
        if nnv not in pipes:
            nv = nnv
            break
print(len(pipes) // 2)

ans = 0
for i in range(len(lines)):
    cin = False
    for j in range(len(lines[0])):
        if (i, j) in pipes and grid[(i, j)] in '|7F':
            cin = not cin
        ans += (i, j) not in pipes and cin
print(ans)
