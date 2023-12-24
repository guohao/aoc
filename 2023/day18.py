from helper import *

D = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}


def p1():
    # Flood fill also works
    g = {}
    xs, ys = math.inf, math.inf
    xe, ye = -math.inf, -math.inf
    x = 0
    y = 0
    pre_d = ''
    first_d = ''
    for line in lines(data):
        d, m, _ = line.split()
        if first_d == '':
            first_d = d
        m = int(m)
        dx, dy = D[d]
        g[x, y] = (pre_d, d)
        for _ in range(m):
            x = x + dx
            y = y + dy
            g[x, y] = (d, d)
        pre_d = d
    g[x, y] = (pre_d, first_d)
    for node in g.keys():
        xs = min(xs, node[0])
        ys = min(ys, node[1])
        xe = max(xe, node[0])
        ye = max(ye, node[1])

    ans = len(g)
    for i in range(xs, xe + 1):
        non_edge_node = 0
        current_in = False
        for j in range(ys, ye + 1):
            if (i, j) in g:
                if g[i, j] in [('D', 'D'), ('L', 'U'), ('D', 'L'), ('R', "U"), ('D', 'R'), ('U', 'U')]:
                    current_in = not current_in
            else:
                if current_in:
                    non_edge_node += 1
        ans += non_edge_node
    print(ans)


def p2():
    ntd = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    points = []
    perimeter = 0
    x, y = 0, 0
    for line in lines(data):
        line = line.split('#')[1]
        m = int(line[:5], 16)
        dx, dy = D[ntd[int(line[-2])]]
        x = x + dx * m
        y = y + dy * m
        perimeter += m
        points.append((x, y))
    area = 0
    # Shoelace formula
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]
        area += (a[1] + b[1]) * (a[0] - b[0])
    area = abs(area) // 2
    # Pick's theorem
    area += perimeter // 2 + 1
    print(area)


data = raw_data(2023, 18)
p1()
p2()
