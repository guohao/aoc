from helper import *

data = raw_data(2016, 2)


def solve(r, c, g):
    ans = ''
    for line in lines(data):
        for move in line:
            match move:
                case 'D':
                    if (r + 1, c) in g:
                        r += 1
                case 'L':
                    if (r, c - 1) in g:
                        c -= 1
                case 'R':
                    if (r, c + 1) in g:
                        c += 1
                case 'U':
                    if (r - 1, c) in g:
                        r -= 1
        ans += g[r, c]
    return ans


def p1():
    g = {}
    for i in range(3):
        for j in range(3):
            g[i, j] = str(i * 3 + j + 1)
    print(solve(0, 0, g))


def p2():
    real_map = """
        1
      2 3 4
    5 6 7 8 9
      A B C
        D
    """
    g = {}
    for i, line in enumerate(lines(real_map)):
        chs = re.findall(r'\w', line)
        padding = (5 - len(chs)) // 2
        for j in range(len(chs)):
            g[i, j + padding] = chs[j]
    r, c = [k for k, v in g.items() if v == '5'][0]
    print(solve(r, c, g))


p1()
p2()
