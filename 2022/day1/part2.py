import sys

parts = sys.stdin.read().split('\n\n')
ts =[]
for part in parts:
    ts.append(sum(map(int,part.splitlines())))
print(sum(sorted(ts)[-3:]))
