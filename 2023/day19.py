from functools import reduce

from helper import *

data = raw_data(2023, 19)
rules = data.split('\n\n')[0]
rules = rules.strip()
R = {}
for rule in rules.splitlines():
    name = rule.split('{')[0]
    content = rule.split("{")[1][:-1]
    cmd = []
    for pair in content.split(','):
        if '<' in pair or '>' in pair:
            c, v = pair.split(':')
            if '<' in c:
                eo, ev = c.split('<')
                ev = int(ev)
                cmd.append(('<', eo, ev, v))
            elif '>' in c:
                eo, ev = c.split('>')
                ev = int(ev)
                cmd.append(('>', eo, ev, v))
        else:
            cmd.append(tuple([pair]))
    R[name] = cmd
R['R'] = None

ratings = data.split('\n\n')[1]
ans0 = 0


def dfs(flow_name, rating) -> int:
    if flow_name == 'R':
        return 0
    if flow_name == 'A':
        return sum(rating.values())
    for cmd in R[flow_name][:-1]:
        if cmd[0] == '<' and rating[cmd[1]] < cmd[2]:
            return dfs(cmd[3], rating)
        if cmd[0] == '>' and rating[cmd[1]] > cmd[2]:
            return dfs(cmd[3], rating)
    return dfs(R[flow_name][-1][0], rating)


for line in ratings.splitlines():
    x, m, a, s = [int(x) for x in re.findall(r'\d+', line)]
    rating = {'x': x, 'm': m, 'a': a, 's': s}
    ans0 += dfs('in', rating)

print(ans0)
PATHS = []


ans = 0
def dfs(name, paths):
    global ans
    if not name:
        return
    if name == 'R':
        return
    if name == 'A':
        D = {x: [i for i in range(1, 4001)] for x in 'xmas'}
        for step in paths:
            name, pick = step.split(":")
            picks = [revert_rule(r) for r in R[name][:int(pick)]]
            pick = R[name][int(pick)]
            if len(pick) > 1:
                picks.append(pick)
            for p in picks:
                if '<' == p[0]:
                    D[p[1]] = [x for x in D[p[1]] if x < p[2]]
                elif '>' == p[0]:
                    D[p[1]] = [x for x in D[p[1]] if x > p[2]]
        ans += reduce(lambda a, b: a * b, [len(v) for v in D.values()])
        return
    for i, c in enumerate(R[name]):
        np = paths.copy()
        np.append(name + ":" + str(i))
        dfs(c[-1], np)


def revert_rule(rule: tuple[str, str, int]) -> tuple[str, str, int]:
    if rule[0] == '<':
        return '>', rule[1], rule[2] - 1
    else:
        return '<', rule[1], rule[2] + 1


dfs('in', [])

print(ans)
