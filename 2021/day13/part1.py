import re
import sys

data = sys.stdin.read().strip()

parts = data.split('\n\n')
g = set()
for line in parts[0].splitlines():
    g.add(tuple(map(int, line.split(','))))
fold = parts[1].splitlines()[0]
ng = set()
fl = int(re.findall(r'\d+', fold)[0])
if 'x=' in fold:
    for x, y in g:
        if x < fl:
            ng.add((x, y))
        elif x > fl:
            ng.add((fl - (x - fl), y))
else:
    for x, y in g:
        if y < fl:
            ng.add((x, y))
        elif y > fl:
            ng.add((x, fl - (y - fl)))
g = ng
print(len(g))
