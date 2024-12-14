import re
import sys
from functools import cache

data = sys.stdin.read().strip()

parts = data.split('\n\n')
rules = {}
parts[0] = parts[0] + "\n8: 42 | 42 8\n11: 42 31 | 42 11 31\n"
for line in parts[0].splitlines():
    l, r = line.split(':')
    rules[l.strip()] = r.strip()


@cache
def extract_rule(rule):
    if rule == "42 | 42 8":
        return '(' + extract_rule('42') + '+)'
    if rule == '42 31 | 42 11 31':
        forth_two = extract_rule('42')
        thirty_one = extract_rule('31')
        p11 = []
        for i in range(1, 5):
            times = '{' + str(i) + '}'
            p11.append(f'({forth_two}{times}{thirty_one}{times})')
        return '(' + '|'.join(p11) + ')'
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
