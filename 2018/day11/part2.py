from collections import defaultdict

gsn = int(input())
N = 301
best = 0
ans = 0, 0, 0

sat = defaultdict(int)
for x in range(1, N):
    for y in range(1, N):
        cid = x + 10
        p = int(f'{(cid * y + gsn) * cid:03}'[-3]) - 5
        sat[x, y] = sat[x - 1, y] - sat[x - 1, y - 1] + sat[x, y - 1] + p

for k in range(1, N):
    for x in range(k, N):
        for y in range(k, N):
            total = sat[x, y] - sat[x, y - k] - sat[x - k, y] + sat[x - k, y - k]
            if total > best:
                best = total
                ans = x - k + 1, y - k + 1, k
print(ans)
