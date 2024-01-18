from helper import *

data = raw_data(2016, 8)
lines = lines(data)
C = 50
R = 6
g = [[0] * C for _ in range(R)]
for line in lines:
    a, b = ints(line)
    if line.startswith("rect"):
        for i in range(b):
            for j in range(a):
                g[i][j] = 1
    elif line.startswith('rotate row'):
        tmp = g[a].copy()
        for j in range(C):
            g[a][(j + b) % C] = tmp[j]
    else:
        tmp = [g[i][a] for i in range(R)]
        for i in range(R):
            g[(i + b) % R][a] = tmp[i]

ans = 0
for i in range(R):
    for j in range(C):
        if g[i][j] == 1:
            ans += 1
print(ans)

for i in range(R):
    line = ''
    for j in range(C):
        if g[i][j] == 1:
            line += '#'
        else:
            line += '  '
    print(line)
