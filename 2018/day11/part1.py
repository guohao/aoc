from functools import cache

gsn = int(input())


@cache
def power_level(x, y):
    rack_id = x + 10
    return int(f'{(rack_id * y + gsn) * rack_id:03}'[-3]) - 5


n = 300
g = {}
for i in range(n):
    for j in range(n):
        s = 0
        for k in range(3):
            for l in range(3):
                s += power_level(i + k, j + l)
        g[i, j] = s
print(max(g, key=lambda v: g[v]))
