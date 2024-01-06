from helper import *

data = raw_data(2015, 6)
N = 1000


def p1():
    g = [[0] * N for _ in range(N)]
    for line in lines(data):
        x0, y0, x1, y1 = nums(line)
        if line.startswith('turn on '):
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    g[x][y] = 1
        elif line.startswith('turn off'):
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    g[x][y] = 0
        else:
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    g[x][y] ^= 1
    print(sum(sum(g[i]) for i in range(N)))


def p2():
    g = [[0] * N for _ in range(N)]
    for line in lines(data):
        x0, y0, x1, y1 = nums(line)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if line.startswith('turn on '):
                    g[x][y] += 1
                elif line.startswith('turn off'):
                    g[x][y] = max(0, g[x][y] - 1)
                else:
                    g[x][y] += 2
    print(sum(sum(g[i]) for i in range(N)))


p1()
p2()
