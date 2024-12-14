import re
import sys

data = sys.stdin.read().strip()

mem = {}
ma = 0
mo = 0
for line in data.splitlines():
    if 'mask' in line:
        mask = line.split('= ')[1]
        ma = int(mask.replace('X', '1'), 2)
        mo = int(mask.replace('X', '0'), 2)
    else:
        l, r = line.split(' = ')
        l = int(re.findall(r'\d+', l)[0])
        r = int(re.findall(r'\d+', r)[0])
        mem[l] = r & ma | mo
print(sum(mem.values()))
