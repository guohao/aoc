import math
import re
from functools import cache


def solve(data: str, lost_my_hp=0):
    BHP, BD = list(map(int, re.findall(r'\d+', data)))

    spells = [
        # cost_mana,damage,heal,(damage,armor,return_mana,timer)
        (53, 4, 0, (0, 0, 0, 0)),
        (73, 2, 2, (0, 0, 0, 0)),
        (113, 0, 0, (0, 7, 0, 6)),
        (173, 0, 0, (3, 0, 0, 6)),
        (229, 0, 0, (0, 0, 101, 5))
    ]

    @cache
    def dfs(bhp, ps, my_turn):
        my_hp, mana, effects = ps
        armor = 0

        if bhp <= 0:
            return 0

        if my_turn:
            my_hp -= lost_my_hp
            if my_hp <= 0:
                return math.inf

        n_effects = {}
        for si, timer in effects:
            effect = spells[si][-1]
            bhp -= effect[0]
            armor += effect[1]
            mana += effect[2]
            timer -= 1
            if timer:
                n_effects[si] = (si, timer)
        effects = tuple(n_effects.values())
        if bhp <= 0:
            return 0

        ans = math.inf
        if my_turn:
            castable = [(i, s) for i, s in enumerate(spells) if i not in n_effects and s[0] <= mana]
            for i, (cost, damage, heal, effect) in castable:
                if effect[-1] > 0:
                    nps = my_hp + heal, mana - cost, (*effects, (i, effect[-1]))
                else:
                    nps = my_hp + heal, mana - cost, effects
                ans = min(ans, cost + dfs(bhp - damage, nps, not my_turn))
        else:
            my_hp -= max(1, BD - armor)
            ans = min(ans, dfs(bhp, (my_hp, mana, effects), not my_turn))
        return ans

    return dfs(BHP, (50, 500, ()), True)


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, 1)
