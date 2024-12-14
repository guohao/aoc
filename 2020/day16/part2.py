import math
import re
import sys

data = sys.stdin.read().strip()

parts = data.split('\n\n')
holes = {}
flat_holes = []
for line in parts[0].splitlines():
    ns = list(map(int, re.findall(r'\d+', line)))
    name = line.split(':')[0]
    holes[name] = []
    for i in range(0, len(ns), 2):
        holes[name].append((ns[i], ns[i + 1]))
        flat_holes.append((ns[i], ns[i + 1]))


def match() -> bool:
    for n in map(int, line.split(',')):
        match_any = False
        for a, b in flat_holes:
            if a <= n <= b:
                match_any = True
                break
        if not match_any:
            return False
    return True


my_ticket = parts[1].splitlines()[1]
all_tickets = [my_ticket]
for line in parts[2].splitlines()[1:]:
    if match():
        all_tickets.append(line)
can_place = {}


def all_match_hole(hole):
    for t in all_tickets:
        if not any(a <= list(map(int, t.split(',')))[i] <= b for a, b in hole):
            return False
    return True


for name in holes:
    can_place[name] = []
    for i in range(len(holes)):
        if all_match_hole(holes[name]):
            can_place[name].append(i)
final_place = {}
while can_place:
    for hole in holes:
        if hole in can_place:
            if len(can_place[hole]) > 1:
                continue
            target = can_place[hole][0]
            final_place[hole] = target
            del can_place[hole]
            for other in can_place:
                if target in can_place[other]:
                    can_place[other].remove(target)

my_ticket = list(map(int, my_ticket.split(',')))
print(math.prod([int(my_ticket[v]) for k, v in final_place.items() if k.startswith("departure")]))
