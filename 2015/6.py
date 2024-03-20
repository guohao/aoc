import re


def p1(data: str):
    n = 1000
    ls = [[0] * n for _ in range(n)]
    for line in data.splitlines():
        x0, y0, x1, y1 = list(map(int, re.findall(r'\d+', line)))
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                if 'toggle' in line:
                    ls[i][j] = 1 - ls[i][j]
                else:
                    ls[i][j] = 'turn on' in line
    return sum(sum(line) for line in ls)


def p2(data: str):
    n = 1000
    ls = [[0] * n for _ in range(n)]
    for line in data.splitlines():
        x0, y0, x1, y1 = list(map(int, re.findall(r'\d+', line)))
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                if 'toggle' in line:
                    ls[i][j] += 2
                elif 'turn on' in line:
                    ls[i][j] += 1
                else:
                    ls[i][j] = max(0, ls[i][j] - 1)
    return sum(sum(line) for line in ls)
