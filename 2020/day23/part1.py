import math
from collections import deque
from typing import List

import sys

data = sys.stdin.read().strip()

q = deque(map(int, data.strip()))
for _ in range(100):
    q.rotate(-1)
    n = q[-1]
    popped = [q.popleft() for _ in range(3)]
    min_v = min(q)
    n -= 1
    while n >= min_v and n not in q:
        n -= 1
    if n < min_v:
        n = max(q)
    idx = q.index(n)
    q.rotate(-(idx + 1))
    for x in reversed(popped):
        q.appendleft(x)
    q.rotate(idx + 1)
    i1 = q.index(1)
q.rotate(-(q.index(1) + 1))
q.pop()
print(''.join(map(str, q)))
