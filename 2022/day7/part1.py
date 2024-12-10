import sys
from collections import defaultdict


data = sys.stdin.read().strip()
d = defaultdict(int)
p = []
for line in data.splitlines():
    match line.split():
        case ['$', 'cd', nd]:
            if nd == '..':
                del p[-1]
            else:
                p.append(nd)
        case [size, _] if size.isdigit():
            size = int(size)
            for i in range(len(p)):
                k = '/'.join(p[:i + 1])
                d[k] += size

print(sum(x for x in d.values() if x <= 100000))
