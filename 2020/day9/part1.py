import itertools
from collections import deque

import sys

data = sys.stdin.read().strip()

seq = deque()
for n in map(int, data.splitlines()):
    if len(seq) < 25:
        seq.append(n)
    else:
        if not any(a + b == n for a, b in itertools.combinations(seq, 2)):
            print(n)
            break
        seq.append(n)
        seq.popleft()

