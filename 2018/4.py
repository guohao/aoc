import re
from collections import defaultdict, Counter


def build_ga(data: str):
    gls = []
    lines = data.splitlines()
    lines.sort()
    lines.append('#')
    for i in range(len(lines)):
        if '#' not in lines[i]:
            continue
        for j in range(i + 1, len(lines)):
            if '#' in lines[j]:
                gls.append(lines[i:j])
                break
    ga = defaultdict(Counter)
    for g in gls:
        id = int(re.findall(r'#\d+', g[0])[0][1:])

        for j in range(1, len(g)):
            line = g[j]
            if 'asleep' not in line:
                continue
            st = int(line.split()[1][-3:-1])
            if j + 1 == len(g):
                et = 60
            else:
                et = int(g[j + 1].split()[1][-3:-1])
            for k in range(st, et):
                ga[id][k] += 1
    return ga


def p1(data: str):
    ga = build_ga(data)
    guard = sorted(ga.items(), key=lambda x: x[1].total())[-1]
    return guard[0] * guard[1].most_common(1)[0][0]


def p2(data: str):
    ga = build_ga(data)
    ga = {k: v.most_common(1)[0] for k, v in ga.items()}
    guard = sorted(ga.items(), key=lambda x: x[1][1])[-1]
    return guard[0] * guard[1][0]
