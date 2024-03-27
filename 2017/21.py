def rotate_and_flip(s: str):
    gs = [[x[::-1] for x in s.split('/')], s.split('/')]
    ans = []
    for _ in range(4):
        ans += gs
        ngs = []
        for g in gs:
            ngs.append([''.join(x) for x in list(zip(*g))[::-1]])
        gs = ngs
    return ['/'.join(x) for x in ans]


rotate_and_flip('.#./..#/###')


def solve(data: str, n):
    mappings = {}
    for line in data.splitlines():
        l, r = map(str.strip, line.split('=>'))
        for m in rotate_and_flip(l):
            mappings[m] = r
    state = ".#./..#/###".split('/')
    for _ in range(n):
        sl = 2 if len(state) % 2 == 0 else 3
        ns = ['' for _ in range(len(state) // sl * (sl + 1))]
        for i in range(len(state) // sl):
            for j in range(len(state) // sl):
                part = '/'.join(state[i * sl + k][j * sl:j * sl + sl] for k in range(sl))
                mapped = mappings[part].split('/')
                for k in range(sl + 1):
                    ns[i * (sl + 1) + k] += mapped[k]
        state = ns
    return sum(l.count('#') for l in state)


def p1(data: str):
    return solve(data, 5)


def p2(data: str):
    return solve(data, 18)
