import sys

lines = [line.strip() for line in sys.stdin.readlines()]
p = {}
for line in lines:
    if '->' in line:
        cells = line.replace(',', '').split()
        for c in cells[3:]:  p[c] = cells[0]

cur = list(p.keys())[0]
while cur in p:
    cur = p[cur]
print(cur)
