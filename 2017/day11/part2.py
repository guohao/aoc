from collections import Counter

ds = ['s', 'se', 'ne', 'n', 'nw', 'sw']
pairs = {'s': 'n', 'se': 'nw', 'ne': 'sw'}


def distance(path: list[str]) -> int:
    seen = set()
    c = Counter(path)
    while True:
        s = sum(c.values())
        if s in seen:
            return s
        seen.add(s)
        for a, b in pairs.items():
            diff = min(c[a], c[b])
            c[a] -= diff
            c[b] -= diff
        for i in range(len(ds)):
            l, m, r = [ds[(i + j) % len(ds)] for j in range(-1, 2)]
            if c[l] > 0 and c[r] > 0:
                diff = min(c[l], c[r])
                c[m] += diff
                c[l] -= diff
                c[r] -= diff


d = input().split(',')
ans = 0
for i in range(len(d)):
    ans = max(ans, distance(d[:i]))
print(ans)
