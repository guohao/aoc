import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
nodes = {}
for line in lines[2:]:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    nodes[nums[0], nums[1]] = (nums[-1], nums[-2])

for a in nodes:
    for b in nodes:
        if a == b:
            continue
        if nodes[b][0]:
            t += nodes[a][1] >= nodes[b][0]

print(t)
