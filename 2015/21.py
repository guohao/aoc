import itertools
import math
import re


def solve(data: str, player_win=True):
    bhp, bd, ba = [list(map(int, re.findall(r'\d+', line)))[0] for line in data.splitlines()]

    def p_win(php, pd, pa):
        for t in itertools.count():
            if bhp - t * max(1, pd - ba) <= 0:
                return True
            if php - t * (max(1, bd - pa)) <= 0:
                return False

    ans = math.inf
    if not player_win:
        ans = 0

    for a in [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]:
        for b in [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]:
            rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
            for c in [((0, 0, 0),)] + list(itertools.combinations(rings, 1)) + list(itertools.combinations(rings, 2)):
                cost = a[0] + b[0]
                damage = a[1]
                armor = b[1]
                for i in range(len(c)):
                    cost += c[i][0]
                    damage += c[i][1]
                    armor += c[i][2]
                if player_win:
                    if p_win(100, damage, armor):
                        ans = min(ans, cost)
                else:
                    if not p_win(100, damage, armor):
                        ans = max(ans, cost)

    return ans


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, False)
