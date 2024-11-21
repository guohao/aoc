import string

import sys

t = 0
for line in sys.stdin.readlines():
    if 3 > sum(line.count(x) for x in 'aeiou'):
        continue
    if not any(x * 2 in line for x in string.ascii_lowercase):
        continue
    if any(x in line for x in ['ab', 'cd', 'pq', 'xy']):
        continue
    t += 1
print(t)
