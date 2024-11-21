x = y = 0
ans = ''
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    for c in line:
        if c == 'R':
            y += 1
        elif c == 'L':
            y -= 1
        elif c == 'U':
            x -= 1
        else:
            x += 1
        x = max(-1, min(1, x))
        y = max(-1, min(1, y))
    g = {}
    k = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            g[i, j] = k
            k += 1
    ans += str(g[x, y])

print(ans)
