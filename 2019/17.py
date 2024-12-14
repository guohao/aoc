import re
from collections import deque

from intcode import IntCodeVM


import sys
data = sys.stdin.read().strip()

    vm = IntCodeVM(data)
    vm.run()
    G = {}
    lines = ''.join(chr(x) for x in vm.sq)
    for i, line in enumerate(lines.splitlines()):
        for j, c in enumerate(line):
            G[i, j] = c

    ans = 0
    for x, y in G:
        if G[x, y] == '.':
            continue
        if all((x + dx, y + dy) in G and G[x + dx, y + dy] == '#' for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
            ans += x * y
    print(ans)


import sys
data = sys.stdin.read().strip()

    vm = IntCodeVM(data, deque(), deque())
    vm.run()
    G = {}
    lines = ''.join(chr(x) for x in vm.sq)
    for i, line in enumerate(lines.splitlines()):
        for j, c in enumerate(line):
            G[i, j] = c

    start = [(x, y) for x, y in G if G[x, y] == '^'][0]
    q = deque([(start, (-1, 0))])
    path = []
    while q:
        (x, y), (dx, dy) = q.popleft()
        LR = [('L', (-dy, dx)), ('R', (dy, -dx))]
        for d, (ndx, ndy) in LR:
            nb = (x + ndx, y + ndy)
            c = 0
            while nb in G and G[nb] == '#':
                c += 1
                nb = (nb[0] + ndx, nb[1] + ndy)
            if c > 0:
                dx, dy = ndx, ndy
                x, y = c * dx + x, c * dy + y
                path.append(d + str(c))
                q.append(((x, y), (dx, dy)))
                break
    spath = ''.join(path)
    for i in range(1, 6):
        a = path[:i]
        for j in range(1, 6):
            b = path[i:i + j]
            cs = i + j
            while cs < len(path):
                if path[cs:cs + i] == a:
                    cs += i
                elif path[cs:cs + j] == b:
                    cs += j
                else:
                    break
            for k in range(1, 6):
                c = path[cs:cs + k]
                mr = spath
                for s, r in [(a, 'A'), (b, 'B'), (c, 'C')]:
                    mr = mr.replace(''.join(s), r)
                if not re.sub(r'[ABC]', '', mr):
                    vm2 = IntCodeVM('2' + data[1:], deque(), deque())
                    for fun in [mr, a, b, c, 'n']:
                        seq = []
                        for x in fun:
                            seq.append(x[0])
                            if len(x) > 1:
                                seq.append(x[1:])
                        for c in ','.join(list(seq)) + '\n':
                            vm2.rq.append(ord(c))
                    vm2.run()
                    return vm2.sq.pop()
