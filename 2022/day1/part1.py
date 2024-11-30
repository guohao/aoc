import sys

parts = sys.stdin.read().split('\n\n')
t =0
for part in parts:
    t=max(t,sum(map(int,part.splitlines())))
print(t)
