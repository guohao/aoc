import re
import sys

data = sys.stdin.read().strip()

parts = data.split('\n\n')
g = set()
for line in parts[0].splitlines():
    g.add(tuple(map(int, line.split(','))))
for fold in parts[1].splitlines():
    ng = set()
    fl = int(re.findall(r'\d+', fold)[0])
    if 'x=' in fold:
        for x, y in g:
            if x < fl:
                ng.add((x, y))
            elif x > fl:
                ng.add((2 * fl - x, y))
    else:
        for x, y in g:
            if y < fl:
                ng.add((x, y))
            elif y > fl:
                ng.add((x, 2 * fl - y))
    g = ng
min_x, max_x = min(x for x, y in g), max(x for x, y in g)
min_y, max_y = min(y for x, y in g), max(y for x, y in g)
for y in range(min_y, max_y + 1):
    line = ''
    for x in range(min_x, max_x + 1):
        if (x, y) in g:
            line += '#'
        else:
            line += '.'
    print(line)
