import math
import sys

parts = sys.stdin.read().split('\n\n')
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
    print(ans)


print(calc('in', {x: list(range(1, 4001)) for x in 'xmas'}))
