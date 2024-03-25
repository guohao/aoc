import re


def p1(data: str):
    nodes = []
    for line in data.splitlines()[2:]:
        line = line.replace('T', '')
        x, y, s, u, _, _ = list(map(int, re.findall(r'\d+', line)))
        nodes.append(((x, y), s, u))
    ans = 0
    for a in nodes:
        for b in nodes:
            if a == b:
                continue
            if 0 < a[2] <= b[1] - b[2]:
                ans += 1
    return ans


def p2(data: str):
    nodes = []
    ans = 0
    for line in data.splitlines()[2:]:
        line = line.replace('T', '')
        x, y, s, u, _, _ = list(map(int, re.findall(r'\d+', line)))
        nodes.append(((x, y), s, u))
        if u == 0:
            ans += x + y
    max_x = max(n[0][0] for n in nodes)
    return ans + max_x + 5 * (max_x - 1)
