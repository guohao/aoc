from helper import *

data = raw_data(2023, 14)
lines = lines(data)


def move(g, d: tuple[int, int]):
    while True:
        change = False
        for p in g.keys():
            v = g[p]
            neighbor = (p[0] + d[0], p[1] + d[1])
            if v == 'O' and neighbor in g and g[neighbor] == '.':
                g[p], g[neighbor] = g[neighbor], g[p]
                change = True
        if not change:
            break


def load_of(g):
    return sum(len(lines) - p[0] for p, v in g.items() if v == 'O')


def p1():
    g = {(i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}
    move(g, (-1, 0))
    print(load_of(g))


def move_cycle(g):
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for _move in moves:
        move(g, _move)


def p2():
    g = {(i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}
    n = 1000000000
    memo = {}
    cycle = 0
    while cycle < n:
        state = tuple(g.values())
        if state in memo:
            step = cycle - memo[state]
            n -= (n - cycle) // step * step
        memo[state] = cycle
        move_cycle(g)
        cycle += 1
    print(load_of(g))


p1()
p2()
