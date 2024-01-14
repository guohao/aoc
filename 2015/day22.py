from collections import deque

from helper import *

spells = [
    # mana ,damage, heal, armor, ext_damage,return_mana,duration
    [53, 4, 0, 0, 0, 0, 0],
    [73, 2, 2, 0, 0, 0, 0],
    [113, 0, 0, 7, 0, 0, 6],
    [173, 0, 0, 0, 3, 0, 6],
    [229, 0, 0, 0, 0, 101, 5]
]

boss_damage = 9


def solve(lose_hp: int):
    init_state = {
        'hp': 50,
        'mana': 500,
        'boss_hp': 51,
        'cost_mana': 0,
        'armor': (0, 0),
        'damage': (0, 0),
        'return_mana': (0, 0)
    }
    dq = deque()
    for spell in spells:
        dq.append((init_state, spell))
    ans = math.inf
    while dq:
        state, effect = dq.popleft()
        if state['cost_mana'] >= ans:
            continue
        ns = state.copy()

        ns['hp'] -= lose_hp
        if ns['hp'] <= 0:
            continue

        # print(ns,effect)
        # my turn
        # apply effect
        if ns['armor'][1] > 0:
            ns['armor'] = (ns['armor'][0], ns['armor'][1] - 1)

        if ns['damage'][1] > 0:
            ns['boss_hp'] -= ns['damage'][0]
            ns['damage'] = (ns['damage'][0], ns['damage'][1] - 1)

        if ns['return_mana'][1] > 0:
            ns['mana'] += ns['return_mana'][0]
            ns['return_mana'] = (ns['return_mana'][0], ns['return_mana'][1] - 1)

        if ns['boss_hp'] <= 0:
            ans = min(ans, ns['cost_mana'])
            continue

        if ns['mana'] < effect[0]:
            continue
        ns['mana'] -= effect[0]
        ns['cost_mana'] += effect[0]

        if effect[3] > 0:
            if ns['armor'][1] > 0:
                continue
            else:
                ns['armor'] = (effect[3], effect[6])
        if effect[4] > 0:
            if ns['damage'][1] > 0:
                continue
            else:
                ns['damage'] = (effect[4], effect[6])
        if effect[5] > 0:
            if ns['return_mana'][1] > 0:
                continue
            else:
                ns['return_mana'] = (effect[5], effect[6])
        ns['hp'] += effect[2]
        ns['boss_hp'] -= effect[1]

        if ns['boss_hp'] <= 0:
            ans = min(ans, ns['cost_mana'])
            continue

        # boss turn
        armor = 0
        if ns['armor'][1] > 0:
            armor = ns['armor'][0]
            ns['armor'] = (ns['armor'][0], ns['armor'][1] - 1)

        if ns['damage'][1] > 0:
            ns['boss_hp'] -= ns['damage'][0]
            ns['damage'] = (ns['damage'][0], ns['damage'][1] - 1)

        if ns['return_mana'][1] > 0:
            ns['mana'] += ns['return_mana'][0]
            ns['return_mana'] = (ns['return_mana'][0], ns['return_mana'][1] - 1)

        if ns['boss_hp'] <= 0:
            ans = min(ans, ns['cost_mana'])
            continue
        ns['hp'] -= max(1, boss_damage - armor)
        if ns['hp'] <= 0:
            continue
        for spell in spells:
            dq.append((ns, spell))
    print(ans)


solve(0)
solve(1)
