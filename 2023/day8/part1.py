import itertools
import re
import sys

parts = sys.stdin.read().split('\n\n')
ins = itertools.cycle(parts[0])
d = {}
for line in parts[1].splitlines():
    f, l, r = re.findall(r'\w{3}', line)
    d[f] = {'L': l, 'R': r}
node = 'AAA'
for t in itertools.count():
    if node == 'ZZZ':
        print(t)
        break
    node = d[node][next(ins)]