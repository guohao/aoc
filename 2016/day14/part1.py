import itertools
import re
from hashlib import md5


def digest(k):
    return md5(f'{salt}{k}'.encode()).hexdigest()


salt = input()
c = 0
for i in itertools.count():
    m = re.search(r'(\w)\1\1', digest(i))
    if not m:
        continue
    for j in range(i + 1, i + 1001):
        if m.group(1) * 5 in digest(j):
            c += 1
            if c == 64:
                print(i)
                exit()
            break
