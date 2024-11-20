import re

rs = []
while True:
    line = input()
    if not line:
        break
    l, r = line.split('=>')
    rs.append((l.strip(), r.strip()))

mm = input()[::-1]

reversed_rules = {v[::-1]: k[::-1] for k, v in rs}
reversed_pattern = '|'.join(reversed_rules.keys())

count = 0
while mm != 'e':
    mm = re.sub(reversed_pattern, lambda match: reversed_rules[match.group()], mm, count=1)
    count += 1

print(count)
