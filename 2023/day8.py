import re

from common import io_utils

data = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
data = io_utils.get_data(2023, 8)
lines = io_utils.raw_str_to_lines(data)
cmds = re.findall(r'\w', lines[0])
ans = 0
pos = {}
for line in lines[1:]:
    a, b, c = re.findall(r'\w+', line)
    pos[a] = (b, c)

ps = [x for x in pos.keys() if x.endswith('A')]

c = 0
fz = {}
cy = {}

while len(ps) != len(cy):
    for cmd in cmds:
        c += 1
        if 0 == len(ps):
            print(c)
            break
        idx = 0
        if cmd == 'R':
            idx = 1
        for i, p in enumerate(ps.copy()):
            if i in cy.keys():
                continue
            ps[i] = pos[p][idx]
            if ps[i].endswith("Z"):
                if i not in fz.keys():
                    fz[i] = c
                else:
                    cy[i] = c - fz[i]
        # print(ps)
    ps = list(set(ps))

for i in range(len(fz)):
    first_z = fz[i]
    cycle = cy[i]
j = fz[0]
while True:
    j += cy[0]
    cnt = 0
    for i in range(len(fz)):
        first_z = fz[i]
        cycle = cy[i]
        if (j - first_z) % cycle == 0:
            cnt += 1
    if cnt == len(fz):
        print(j)
        break

# print(c)
