import itertools
import re
from collections import deque


def solve(pc, tc):
    q = deque({0})
    pi = itertools.cycle(range(pc))
    players = [0] * pc
    for turn in range(1, tc + 1):
        cp = next(pi)
        if turn % 23 == 0:
            players[cp] += turn
            q.rotate(7)
            players[cp] += q.pop()
            q.rotate(-1)
        else:
            q.rotate(-1)
            q.append(turn)
    return max(players)


def p1(data: str):
    pc, tc = re.findall(r'\d+', data)
    pc, tc = int(pc), int(tc)
    return solve(pc, tc)


def p2(data: str):
    pc, tc = re.findall(r'\d+', data)
    pc, tc = int(pc), int(tc)
    return solve(pc, tc * 100)
