import re
from functools import cache

import sys

data = sys.stdin.read().strip()

parts = data.split('\n\n')
rules = {}
for line in parts[0].splitlines():
    l, r = line.split(':')
    rules[l.strip()] = r.strip()


@cache
def extract_rule(rule):
    if re.match(r'"\w+"', rule):
        return rule[1:-1]
    ps = []
    if '|' not in rule:
        for child in rule.split():
            ps.append(extract_rule(rules[child]))
        return ''.join(ps)
    else:
        for child in rule.split('|'):
            if len(child) == 0:
                continue
            ps.append(extract_rule(child))
        return '(' + '|'.join(f'{item}' for item in ps) + ')'


pattern = extract_rule(rules['0'])
ans = 0
for text in parts[1].splitlines():
    if re.fullmatch(pattern, text):
        ans += 1
print(ans)

