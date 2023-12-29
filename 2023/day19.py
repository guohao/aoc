from functools import reduce

from helper import *

data = raw_data(2023, 19)
rules, mps = data.split('\n\n')
workflows = {}
for rule in rules.splitlines():
    name = re.search(r'(.*){', rule).group(1)
    flows = re.search(r'{(.*)}', rule).group(1)
    workflows[name] = flows.split(',')

ans = 0
for mp in mps.splitlines():
    ns = nums(mp)
    ratings = {'x': ns[0], 'm': ns[1], 'a': ns[2], 's': ns[3]}

    flow = 'in'
    while flow != 'A' and flow != 'R':
        for rule in workflows[flow]:
            if '<' in rule or '>' in rule:
                left, target = rule.split(':')
                if '<' in left:
                    mp, count = left.split('<')
                else:
                    mp, count = left.split('>')
                count = int(count)
                if '<' in left:
                    if ratings[mp] < count:
                        flow = target
                        break
                else:
                    if ratings[mp] > count:
                        flow = target
                        break
            else:
                flow = rule
    if flow == 'A':
        ans += sum(ns)
print(ans)

candidates = {x: [i for i in range(1, 4001)] for x in 'xmas'}


def bfs(flow: str, candidates: dict[str, List[int]]) -> int:
    if flow == 'A':
        return reduce(lambda x, y: x * y, map(len, candidates.values()))
    if flow == 'R':
        return 0
    if any(not v for v in candidates.values()):
        return 0

    ret = 0
    for rule in workflows[flow]:
        if '<' in rule or '>' in rule:
            left, target = rule.split(':')
            if '<' in left:
                mp, count = left.split('<')
            else:
                mp, count = left.split('>')
            count = int(count)
            if '<' in left:
                nt = list(filter(lambda x: x < count, candidates[mp]))
            else:
                nt = list(filter(lambda x: x > count, candidates[mp]))
            if nt:
                nc = candidates.copy()
                nc[mp] = nt
                ret += bfs(target, nc)
            if '<' in left:
                candidates[mp] = list(filter(lambda x: x >= count, candidates[mp]))
            else:
                candidates[mp] = list(filter(lambda x: x <= count, candidates[mp]))
        else:
            ret += bfs(rule, candidates)
    return ret


print(bfs('in', candidates))
