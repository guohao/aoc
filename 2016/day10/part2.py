import math
import re
import sys
from collections import defaultdict, deque

bots = defaultdict(list)
tos = defaultdict(list)
lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    if 'value' in line:
        v, b = re.findall(r'\d+', line)
        bots[f'bot {b}'].append(int(v))
    else:
        b, *t = re.findall(r'bot \d+|output \d+', line)
        tos[b] = t
q = deque(bot for bot, bag in bots.items() if len(bag) == 2)
while q:
    bot = q.pop()
    bag = bots[bot]
    bots[bot] = []
    bots[tos[bot][0]].append(min(bag))
    bots[tos[bot][1]].append(max(bag))
    for i in range(2):
        if len(bots[tos[bot][i]]) == 2:
            q.append(tos[bot][i])

print(math.prod(bots[f'output {i}'][0] for i in range(3)))
