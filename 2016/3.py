def p1ss(line: str):
    vs = sorted(map(int, line.split()))
    return sum(vs[:2]) > vs[2]


def p2(data: str):
    lines = []
    for line in data.splitlines():
        lines.append(list(map(int, line.split())))
    ans = 0
    for i in range(0, len(lines), 3):
        for vs in zip(*lines[i:i + 3]):
            vs = sorted(vs)
            if sum(vs[:2]) > vs[2]:
                ans += 1
    return ans
