import re

import sys

data = sys.stdin.read().strip()


def valid():
    if len(d) != 7:
        return False
    if not 1920 <= int(d['byr']) <= 2002:
        return False
    if not 2010 <= int(d['iyr']) <= 2020:
        return False
    if not 2020 <= int(d['eyr']) <= 2030:
        return False
    if 'cm' not in d['hgt'] and 'in' not in d['hgt']:
        return False
    if 'cm' in d['hgt']:
        if not 150 <= int(d['hgt'][:-2]) <= 193:
            return False
    if 'in' in d['hgt']:
        if not 59 <= int(d['hgt'][:-2]) <= 76:
            return False
    if not re.fullmatch(r'#[0-9a-f]{6}', d['hcl']):
        return False
    if d['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.fullmatch(r'\d{9}', d['pid']):
        return False
    return True


ans = 0
for part in data.split('\n\n'):
    d = {}
    for line in part.splitlines():
        for cell in line.split():
            k, v = cell.split(':')
            d[k] = v
    if 'cid' in d:
        del d['cid']
    if valid():
        ans += 1
print(ans)
