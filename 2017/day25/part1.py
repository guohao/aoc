import sys
from collections import deque

parts = sys.stdin.read().split('\n\n')
p0 = parts[0].splitlines()
state = p0[0][-2]
total = int(p0[1].split()[-2])

states = {}
for p in parts[1:]:
    lines = [x.split()[-1][:-1] for x in p.splitlines()]
    states[lines[0]] = lines[2:5] + lines[6:]
q = deque(['0'] * total)
for _ in range(total):
    s = states[state]
    v = q.popleft()
    if v == '0':
        q.appendleft(s[0])
        if s[1] == 'right':
            q.rotate(-1)
        else:
            q.rotate(1)
        state = s[2]
    else:
        q.appendleft(s[3])
        if s[4] == 'right':
            q.rotate(-1)
        else:
            q.rotate(1)
        state = s[5]

print(q.count('1'))
