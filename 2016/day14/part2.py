import itertools
import re
from collections import deque
from hashlib import md5


def digest_2017(k):
    s = md5(f'{salt}{k}'.encode()).hexdigest()
    for _ in range(2016):
        s = md5(f'{s}'.encode()).hexdigest()
    return s


salt = input()
c = 0
q = deque()
for i in range(1000):
    q.append(digest_2017(i))

for i in itertools.count():
    q.append(digest_2017(i + 1000))
    m = re.search(r'(\w)\1\1', q.popleft())
    if not m:
        continue
    if any(m.group(1) * 5 in x for x in q):
        c += 1
        if c == 64:
            print(i)
            exit()
