import hashlib
import re
from collections import deque

data = "jlmsuwbz"


def solve(extra_hash: int):
    found = 0
    dq = deque(maxlen=1001)
    for i in range(100000):
        if found == 64:
            print(i - 1001)
            break
        hashed = hashlib.md5((data + str(i)).encode()).hexdigest()
        for _ in range(extra_hash):
            hashed = hashlib.md5(hashed.encode()).hexdigest()
        dq.append(hashed)
        if len(dq) < 1001:
            continue
        a = dq.popleft()
        m = re.search(r'(\w)\1\1', a)
        if not m:
            continue
        c = m.group(1)
        if any(c * 5 in b for b in dq):
            found += 1


solve(0)
solve(2016)
