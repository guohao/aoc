import sys

data = sys.stdin.read().strip()

ans = 0
for part in data.split('\n\n'):
    s = set()
    for line in part.splitlines():
        for x in line:
            s.add(x)
    ans += len(s)
print(ans)

