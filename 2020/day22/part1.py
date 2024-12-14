from collections import deque

import sys

data = sys.stdin.read().strip()

qs = []
for part in data.split('\n\n'):
    qs.append(deque(map(int, part.splitlines()[1:])))
while all(qs):
    for i in range(2):
        if qs[i][0] > qs[1 - i][0]:
            qs[i].append(qs[i].popleft())
            qs[i].append(qs[1 - i].popleft())
            break
w = qs[0] if qs[0] else qs[1]
print(sum(w.popleft() * i for i in range(len(w), 0, -1)))

