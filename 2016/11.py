from itertools import *
import re


def solve(data: str, extra=None):
    if extra is None:
        extra = []
    init_state = ()
    for line in data.splitlines():
        floor = ()
        for a, b in re.findall(r'([\w-]+ microchip)|([\w-]+ generator)', line):
            floor += (a if a else b,)
        init_state += (floor,)
    init_state = (init_state[0] + tuple(extra), *init_state[1:])

    def fired(chips):
        chips = set(chips)
        gs = [c for c in chips if c.endswith("generator")]
        if len(gs) == 0:
            return False
        for c in chips:
            if c.endswith("generator"):
                continue
            if c.split('-')[0] + " generator" not in chips:
                return True
        return False

    states = {(init_state, 0)}

    seen = set()
    for t in count():
        next_moves = set()
        seen = seen.union(states)
        for state, fl in states:
            if fl == 3 and sum(len(f) for f in state[:3]) == 0:
                return t
            for carry in chain(combinations(state[fl], 1),
                               combinations(state[fl], 2)):
                moved = sorted(set(state[fl]) - set(carry))
                if fired(moved):
                    continue
                for i in [-1, 1]:
                    nfl = fl + i
                    if nfl < 0 or nfl > 3:
                        continue
                    floor = state[nfl] + carry
                    if fired(floor):
                        continue
                    new_state = list(state)
                    new_state[fl] = tuple(moved)
                    new_state[nfl] = tuple(sorted(floor))
                    next_moves.add((tuple(new_state), nfl))
        states = next_moves - seen


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, [
        'elerium generator',
        'elerium-compatible microchip',
        'dilithium generator',
        'dilithium-compatible microchip'
    ])
