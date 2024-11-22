import itertools
import re
import string
import sys
from collections import deque

HEIGHT = 4
init_state = []
for line in sys.stdin.readlines():
    line = line.replace('-compatible', '')
    line = line.replace('microchip', 'M')
    line = line.replace('generator', 'G')
    items = []
    for item in re.findall(r'\S+ M|\S+ G', line):
        name, type = item.split()
        items.append(name[0].upper() + ' ' + type)
    init_state.append(items)
init_state[0] += ['E M', 'E G', 'D G', 'D M']
q = deque([(0, 0, tuple(tuple(l) for l in init_state))])



def safe(floor_state: list[list[string]]) -> bool:
    for floor in floor_state:
        gc = sum('G' in x for x in floor)
        if gc == 0:
            continue
        for x in floor:
            name, type = x.split()
            if 'M' == type and name + ' G' not in floor:
                return False
    return True


seen = set()
while q:
    step, e, state = q.popleft()
    if (e, state) in seen:
        continue
    seen.add((e, state))
    if all(not a for a in state[:HEIGHT - 1]):
        print(step)
        break
    candidate =state[e]
    visit = []
    if e - 1 in range(HEIGHT) and state[e - 1]:
        visit.append((e - 1, itertools.combinations(candidate, 1)))
    visit.append((e + 1, itertools.combinations(candidate, 2)))
    for ne, select in visit:
        if ne not in range(HEIGHT):
            continue
        for c in select:
            n_state = list(state)
            n_state[e] = {x for x in state[e] if x not in c}
            n_state[ne] = set(c + state[ne])
            if safe([n_state[e], n_state[ne]]):
                n_state = tuple(tuple(sorted(l)) for l in n_state)
                q.append((step + 1, ne, n_state))
