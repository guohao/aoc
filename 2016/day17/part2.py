import math
from hashlib import md5

d = input()
ans = -math.inf

DS = {0: ('U', (-1, 0)),
      1: ('D', (1, 0)),
      2: ('L', (0, -1)),
      3: ('R', (0, 1))}


def dfs(path: str, x, y):
    if x <= 0 or x > 4:
        return
    if y <= 0 or y > 4:
        return
    global ans
    if x == y == 4:
        ans = max(ans, len(path))
        return
    for i, c in enumerate(md5(f'{d}{path}'.encode()).hexdigest()[:4]):
        if int(c, 16) > int('a', 16):
            ds = DS[i]
            dfs(path + ds[0], x + ds[1][0], y + ds[1][1])


dfs('', 1, 1)

print(ans)
