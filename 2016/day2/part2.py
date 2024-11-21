ans = ''
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
g = {}
k = 1
i = j = 2
while i >= -2:
    g[i, j] = hex(k)[2:].upper()
    k += 1
    if abs(i) + abs(j) == 4:
        i -= 1
        j = abs(i)
    else:
        j += 1

x = y = 0
for line in lines:
    for c in line:
        px, py = x, y
        if c == 'R':
            y += 1
        elif c == 'L':
            y -= 1
        elif c == 'U':
            x += 1
        else:
            x -= 1
        if (x, y) not in g:
            x, y = px, py
    ans += g[x, y]

print(ans)
