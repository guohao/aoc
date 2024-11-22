import itertools
import re
import string
import sys
from collections import deque

HEIGHT = 4
lines = [line.strip() for line in sys.stdin.readlines()]
q = deque([(0, 0, tuple(tuple(re.findall(r'\S+ microchip|\S+ generator', line)) for line in lines))])


def safe(floor_state: list[list[string]]) -> bool:
    for floor in floor_state:
        gc = sum('generator' in x for x in floor)
        if gc == 0:
            continue
        for x in floor:
            name, type = x.split()
            name = name.replace('-compatible', '')
            if 'microchip' == type and name + ' generator' not in floor:
                return False
    return True


seen = set()
while q:
    step, e, state = q.popleft()

    if state in seen:
        continue
    seen.add((state))
    if all(not a for a in state[:HEIGHT - 1]):
        print(step)
        break
    for ne in [e - 1, e + 1]:
        if ne not in range(HEIGHT):
            continue
        for c in itertools.chain(itertools.combinations(state[e], 1), itertools.combinations(state[e], 2)):
            n_state = [set(l) for l in state]
            n_state[e] = {x for x in state[e] if x not in c}
            n_state[ne] = set(c + state[ne])
            if safe(n_state):
                n_state = tuple(tuple(l) for l in n_state)
                q.append((step + 1, ne, n_state))
