from collections import deque, defaultdict


def ic(ns, pc, rb, fi):
    def vo(mode: str, key: int):
        if mode == '0':
            return ns[key]
        elif mode == '1':
            return key
        elif mode == '2':
            return ns[key + rb]
        else:
            raise ValueError(f'{mode} {key}')

    def wo(mode: str, key: int):
        if mode == '0':
            return key
        else:
            return rb + key

    i = pc
    ans = deque()
    while i < len(ns):
        op = ns[i] % 100
        if op == 99:
            return -1, rb, 0, 0
        modes = str(ns[i] // 100).zfill(3)[::-1]
        if op == 1:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = a + b
            i += 4
        elif op == 2:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = a * b
            i += 4
        elif op == 3:
            c = wo(modes[0], ns[i + 1])
            ns[c] = fi
            i += 2
        elif op == 4:
            ans.append(vo(modes[0], ns[i + 1]))
            i += 2
            if len(ans) == 2:
                return i, rb, ans.popleft(), ans.popleft()
        elif op == 5:
            if vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 6:
            if not vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 7:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = int(a < b)
            i += 4
        elif op == 8:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = int(a == b)
            i += 4
        elif op == 9:
            rb += vo(modes[0], ns[i + 1])
            i += 2
        else:
            assert False


def p1(data: str):
    ns: list[int] = list(map(int, data.strip().split(','))) + [0 for _ in range(1000)]
    pc = 0
    rb = 0

    g = defaultdict(int)
    q = deque()
    q.append(((0, 0), (0, 1), 0))
    while q:
        (x, y), (dx, dy), c = q.popleft()
        pc, rb, cc, r = ic(ns, pc, rb, c)
        if pc == -1:
            break
        g[x, y] = cc
        if r:
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        q.append(((x, y), (dx, dy), g[x, y]))
    return len(g)


def p2(data: str):
    ns: list[int] = list(map(int, data.strip().split(','))) + [0 for _ in range(1000)]
    pc = 0
    rb = 0

    g = defaultdict(int)
    q = deque()
    q.append(((0, 0), (0, 1), 1))
    while q:
        (x, y), (dx, dy), c = q.popleft()
        pc, rb, cc, r = ic(ns, pc, rb, c)
        if pc == -1:
            break
        g[x, y] = cc
        if r:
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        q.append(((x, y), (dx, dy), g[x, y]))
    min_x, max_x = min(x for x, _ in g.keys()), max(x for x, _ in g.keys())
    min_y, max_y = min(y for _, y in g.keys()), max(y for _, y in g.keys())
    for j in range(max_y, min_y - 1, -1):
        line = ''
        for i in range(min_x, max_x + 1):
            if g[i, j] == 1:
                line += '#'
            else:
                line += '.'
        print(line)
    return 0
