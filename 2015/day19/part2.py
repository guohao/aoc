import re
import sys

rs = []
parts = sys.stdin.read().split('\n\n')
for line in parts[0].splitlines():
    l, r = line.split('=>')
    rs.append((r.strip()[::-1], l.strip()[::-1]))

reversed_pattern = '|'.join(v for v, _ in rs)
reversed_rules = dict(rs)
mm = parts[1].strip()[::-1]

count = 0
while mm != 'e':
    mm = re.sub(reversed_pattern, lambda match: reversed_rules[match.group()], mm, count=1)
    count += 1

print(count)
