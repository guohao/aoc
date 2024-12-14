import sys
from collections import Counter

data = sys.stdin.read().strip()

parts = data.split('\n\n')
s = parts[0]
ms = {}
for line in parts[1].splitlines():
    l, r = line.split(' -> ')
    ms[l] = r
for _ in range(10):
    ns = ''
    for i in range(len(s)):
        pair = s[i - 1:i + 1]
        if pair in ms:
            ns += ms[pair]
        ns += s[i]
    s = ns
c = sorted(Counter(s).values())
print(c[-1] - c[0])
