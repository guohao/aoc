from collections import deque, defaultdict
from intcode import IntCodeVM


def p1(data: str):
    vm = IntCodeVM(data)

    g = defaultdict(int)
    q = deque()
    q.append(((0, 0), (0, 1), 0))
    sq = vm.sq
    rq = vm.rq
    while q:
        (x, y), (dx, dy), c = q.popleft()
        rq.append(g[x, y])
        vm.run()
        if vm.halt:
            break
        g[x, y] = sq.popleft()
        if sq.popleft():
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        q.append(((x, y), (dx, dy), g[x, y]))
    return len(g)


def p2(data: str):
    vm = IntCodeVM(data)
    sq = vm.sq
    rq = vm.rq
    g = defaultdict(int)
    q = deque()
    q.append(((0, 0), (0, 1)))
    g[0, 0] = 1
    while q:
        (x, y), (dx, dy) = q.popleft()
        rq.append(g[x, y])
        vm.run()
        if vm.halt:
            break
        g[x, y] = sq.popleft()
        if sq.popleft():
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        q.append(((x, y), (dx, dy)))
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
