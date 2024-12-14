import itertools
import re
from collections import deque

import copy
from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

q = deque()
vm = IntCodeVM(data, deque(), deque())

q.append((vm, 0, 0, None, frozenset()))
seen = set()
failed = set()
while q:
    vm, x, y, cmd, carried = q.popleft()
    key = (x, y, cmd, carried)
    if key in seen:
        continue
    seen.add(key)

    out = vm.execute_ascii(cmd)
    if vm.halt:
        continue
    check_items = False
    parts = out.split('\n\n')
    doors = []
    items = []
    for part in parts:
        if 'Doors' in part:
            for door in part.splitlines()[1:]:
                door = door.split()[1]
                doors.append(door)
        elif 'Items' in part:
            for item in part.splitlines()[1:]:
                item = item[2:]
                if item != 'infinite loop':
                    items.append(item)
        elif 'Command?' in part:
            pass
        else:
            if 'a pressure-sensitive floor' in part:
                check_items = True
    for door in doors:
        dx, dy = {'east': (0, 1), 'west': (0, -1), 'north': (-1, 0), 'south': (1, 0)}[door]
        nx, ny = x + dx, y + dy
        all_items = items + list(carried)

        if len(all_items) == 0:
            q.append((copy.copy(vm), nx, ny, door, carried))
            continue

        for i in range(len(all_items), 0, -1):
            if check_items:
                n_vm = copy.copy(vm)
                for c_items in itertools.combinations(all_items, i):
                    kk = (x, y) + (cmd,) + tuple(c_items)
                    if kk in failed:
                        continue
                    for item in c_items:
                        if item not in carried:
                            n_vm.execute_ascii('take ' + item)
                    for item in carried:
                        if item not in c_items:
                            n_vm.execute_ascii('drop ' + item)
                    cr = n_vm.execute_ascii(door)
                    if 'ejected' in cr:
                        if kk not in failed:
                            failed.add(kk)
                        continue
                    print(re.findall(r'\d+', cr)[0])
                    exit()
            else:
                for c_items in itertools.combinations(all_items, i):
                    n_vm = copy.copy(vm)
                    for item in c_items:
                        if item not in carried:
                            n_vm.execute_ascii('take ' + item)
                    for item in carried:
                        if item not in c_items:
                            n_vm.execute_ascii('drop ' + item)
                    q.append((copy.copy(n_vm), nx, ny, door, frozenset(c_items)))
