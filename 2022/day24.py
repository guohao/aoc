from helper import *

data = raw_data(2022, 24)
DIRECTIONS = {"<": (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
lines = lines(data)
X = len(lines)
Y = len(lines[0])
g = {(i, j): c for i, line in enumerate(data.strip().splitlines()) for j, c in enumerate(line)}
init_blizzards = {((i, j), DIRECTIONS[g[i, j]]) for i, j in g if g[i, j] not in '.#'}
start = (0, lines[0].index('.'))
goal = (X - 1, lines[-1].index('.'))


def solve(goals):
    gi = 0
    states = {start}
    blizzards = init_blizzards
    for t in range(2000):
        blizzards_snapshot = set()
        cur = set()
        for p, d in blizzards:
            np = (p[0] + d[0], p[1] + d[1])
            while np not in g or g[np] == '#':
                np = ((np[0] + d[0]) % X, (np[1] + d[1]) % Y)
            cur.add((np, d))
            blizzards_snapshot.add(np)
        blizzards = cur
        new_states = set()
        for p in states:
            if p not in blizzards_snapshot:
                new_states.add(p)
            if p == goals[gi]:
                new_states = {goals[gi]}
                gi += 1
                if gi < len(goals):
                    break
                print(t)
                return
            for d in DIRECTIONS.values():
                np = (p[0] + d[0], p[1] + d[1])
                if np in g and g[np] != '#':
                    if np in blizzards_snapshot:
                        continue
                    new_states.add(np)
        states = new_states


solve([goal])
solve([goal, start, goal])
