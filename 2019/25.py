import random
from collections import deque

from intcode import IntCodeVM


def p1(data: str):
    q = deque()
    q.append([])
    while q:
        cmds, carried = q.popleft()
        vm = IntCodeVM(data, deque(), deque())
        vm.run()
        out = ''.join(chr(x) for x in vm.sq)
        if 'north' in out:
            q.append('north')
        if 'south' in out:
            ava_cmds.append('south')
        if 'east' in out:
            ava_cmds.append('east')
        if 'west' in out:
            ava_cmds.append('west')
        if carried:
            for item in carried:
                ava_cmds.append('drop ' + item)
        vm.sq.clear()
        print(out)
        if 'Command?' in out:
            # d = random.Random().choice(['north', 'east', 'west', 'south'])
            d = input()
            for x in d + '\n':
                vm.rq.append(ord(x))
