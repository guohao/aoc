import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]
rs = defaultdict(int)
for line in lines:
    line = line.replace('dec', '-=')
    line = line.replace('inc', '+=')
    cells = line.split()
    cells[0] = f'rs["{cells[0]}"]'
    cells[-3] = f'rs["{cells[-3]}"]'
    line = ' '.join(cells) + ' else 0'
    exec(line)
print(max(rs.values()))
