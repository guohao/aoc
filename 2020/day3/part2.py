import math
import sys

lines = [l.strip() for l in sys.stdin.readlines()]
X = len(lines[0])
Y = len(lines)


def tree_num(x):
    r, d = x
    ans = 0
    x = y = 0
    while y < Y:
        if lines[y][x] == '#':
            ans += 1
        x = (x + r) % X
        y += d
    print(ans)


tries = [(1, 1), [3, 1], [5, 1], [7, 1], [1, 2]]
print(math.prod(map(tree_num, tries)))
