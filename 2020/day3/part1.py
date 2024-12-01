import sys

lines = [l.strip() for l in sys.stdin.readlines()]
X = len(lines[0])
ans = 0
x = 0
for y in range(len(lines)):
    if lines[y][x] == '#':
        ans += 1
    x = (x + 3) % X
print(ans)
