from collections import Counter

import sys

data = sys.stdin.read().strip()

ns = data.strip()
layers = len(ns) // (25 * 6)
ans = 0
zc = len(ns)
for i in range(0, layers * 150, 150):
    c = Counter(ns[i:i + 150])
    if c['0'] < zc:
        zc = c['0']
        ans = c['1'] * c['2']
print(ans)

