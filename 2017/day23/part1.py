import sys
import re
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]
r = defaultdict(int)
i = 0


def vo(n: str):
    if re.fullmatch(r'-?\d+', n):
        return int(n)
    return r[n]


ans = 0
while 0 <= i < len(lines):
    c, *a = lines[i].split()
    if 'set' == c:
        r[a[0]] = vo(a[1])
    elif 'sub' == c:
        r[a[0]] -= vo(a[1])
    elif 'mul' == c:
        ans += 1
        r[a[0]] *= vo(a[1])
    elif 'jnz' == c:
        if vo(a[0]) != 0:
            i += vo(a[1])
            continue
    i += 1
print(ans)
