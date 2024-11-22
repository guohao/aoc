import itertools
import re
import string
import sys
from collections import deque

HEIGHT = 4
lines = [line.strip() for line in sys.stdin.readlines()]
name_map = {}
init_state = []
for line in lines:
    fs = []
    for x in re.findall(r'\S+ microchip|\S+ generator', line):
        name, type = x.split()
        name = name.replace('-compatible', '')
        if name not in name_map:
            name_map[name] = len(name_map) + 1
        fs.append(name_map[name] * (-1 if type == 'microchip' else 1))
    init_state.append(fs)

init_state[0] += [len(name_map) + 1, -len(name_map) - 1, len(name_map) + 2, -len(name_map) - 2]
q = deque([(0, 0, tuple(tuple(l) for l in init_state))])


def safe(floor_state: list[list[string]]) -> bool:
    for floor in floor_state:
        gc = sum(x > 0 for x in floor)
        if gc == 0:
            continue
        for x in floor:
            if x < 0 and -x not in floor:
                return False
    return True


seen = set()
while q:
    step, e, state = q.popleft()
    if state in seen:
        continue
    seen.add(state)
    if all(not a for a in state[:HEIGHT - 1]):
        print(step)
        break
    select_1 = itertools.combinations(state[e], 1)
    select_2 = itertools.combinations(state[e], 2)
    visit = [(e - 1, select_1), (e + 1, itertools.chain(select_1, select_2))]
    for ne, select in visit:
        if ne not in range(HEIGHT):
            continue
        for c in select:
            n_state = [set(l) for l in state]
            n_state[e] = {x for x in state[e] if x not in c}
            n_state[ne] = set(c + state[ne])
            if safe([n_state[e], n_state[ne]]):
                n_state = tuple(tuple(l) for l in n_state)
                q.append((step + 1, ne, n_state))
