import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    l,r = line.split('|')
    i,p = l.split(':')
    ps = set(map(int,p.split()))
    t += round(2**(len(set(map(int,r.split()))&ps)-1))

print(t)
