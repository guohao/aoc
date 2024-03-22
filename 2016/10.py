import math
import re
from collections import defaultdict


def solve(data: str, puzzle_one=True):
    r = defaultdict(list)
    gives = {}
    for line in data.splitlines():
        if 'value' in line:
            v, b = re.findall(r'\d+', line)
            r['bot ' + str(b)].append(int(v))
        elif 'gives' in line:
            vs = re.findall(r'\d+', line)
            ns = re.findall(r'bot |output ', line)
            give_to = [ns[i] + vs[i] for i in range(3)]
            gives[give_to[0]] = give_to[1:]

    def one_turn():
        for bot in r:
            if len(r[bot]) == 2:
                give_to = gives[bot]
                chips = sorted(r[bot])
                if chips == [17, 61]:
                    if puzzle_one:
                        return False, bot
                r[give_to[0]].append(chips[0])
                r[give_to[1]].append(chips[1])
                r[bot] = []
                return True, None
        return False, math.prod(math.prod(r['output ' + str(i)]) for i in range(3))

    while True:
        go_on, ans = one_turn()
        if not go_on:
            return ans


def p1(data: str):
    return solve(data, True).split()[1]


def p2(data: str):
    return solve(data, False)
