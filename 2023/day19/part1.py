import re
import sys

parts = sys.stdin.read().split('\n\n')
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
print(ans)
