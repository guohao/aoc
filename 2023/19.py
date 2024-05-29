from util import *


def p1(data: str):
    parts = d2p(data)
    rules = parts[0].splitlines()

    def calc(name, x, m, a, s):
        if name == 'A':
            return x + m + a + s
        elif name == 'R':
            return 0
        rule = [x for x in rules if x.split('{')[0] == name][0]
        content = rule[len(name) + 1:-1]
        for item in content.split(','):
            cells = item.split(':')
            if len(cells) == 1 or eval(cells[0]):
                return calc(cells[-1], x, m, a, s)

    ans = 0
    for line in parts[1].splitlines():
        d = list(map(int, re.findall(r'\d+', line)))
        ans += calc('in', *d)
    return ans


def p2(data: str):
    parts = d2p(data)
    rules = parts[0].splitlines()

    def calc(name, d):
        if name == 'R':
            return 0
        if name == 'A':
            return math.prod(map(len, d.values()))
        rule = [x for x in rules if x.split('{')[0] == name][0]
        content = rule[len(name) + 1:-1]
        ans = 0
        for item in content.split(','):
            cells = item.split(':')
            target = cells[-1]
            if len(cells) == 1:
                ans += calc(target, d)
                break
            else:
                k = cells[0][0]
                expr = cells[0].replace(k, 'v')
                md = d.copy()
                md[k] = [v for v in d[k] if eval(expr)]
                ans += calc(target, md)
                d[k] = [v for v in d[k] if not eval(expr)]
        return ans

    return calc('in', {x: list(range(1, 4001)) for x in 'xmas'})
