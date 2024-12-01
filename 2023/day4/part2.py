import sys

lines = [line.strip() for line in sys.stdin.readlines()]
pows = [1] * len(lines)
for i, line in enumerate(lines):
    l, r = line.split('|')
    _, p = l.split(':')
    n = len(set(map(int, r.split())) & set(map(int, p.split())))
    for j in range(i + 1, i + 1 + n):
        pows[j] += pows[i]

print(sum(pows))
