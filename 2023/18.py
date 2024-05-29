from util import *


def p1(data: str):
    vs = [(0, 0)]
    for line in data.splitlines():
        d, n, _ = line.split()
        n = int(n)
        d = dsd()[d]
        vs.append((vs[-1][0] + d[0] * n, vs[-1][1] + d[1] * n))
    return total_points(vs)


def p2(data: str):
    vs = [(0, 0)]
    for line in data.splitlines():
        h = re.findall(r'\w{2,}', line.split()[-1])[0]
        n = int(h[:-1], 16)
        d = {'0': (0, 1), '2': (0, -1), '1': (1, 0), '3': (-1, 0)}[h[-1]]
        vs.append((vs[-1][0] + d[0] * n, vs[-1][1] + d[1] * n))
    return total_points(vs)
