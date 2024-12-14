import sys

data = sys.stdin.read().strip()

ans = 0
for part in data.split('\n\n'):
    d = {}
    for line in part.splitlines():
        for cell in line.split():
            k, v = cell.split(':')
            d[k] = v
    if 'cid' in d:
        del d['cid']
    if len(d) == 7:
        ans += 1
print(ans)
