import itertools
from collections import deque


def ic(data: str, ps: int, fi: int):
    ns: list[int] = list(map(int, data.strip().split(',')))
    i = 0

    def vo(mode: str, key: int):
        if mode == '0':
            return ns[key]
        else:
            return key

    ins = deque()
    ins.append(ps)
    ins.append(fi)

    ans = 0
    while i < len(ns):
        op = ns[i] % 100
        modes = str(ns[i] // 100).zfill(2)[::-1]
        if op == 1:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) + vo(modes[1], ns[i + 2])
            i += 4
        elif op == 2:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) * vo(modes[1], ns[i + 2])
            i += 4
        elif op == 3:
            ns[ns[i + 1]] = ins.popleft()
            i += 2
        elif op == 4:
            ans = vo(modes[0], ns[i + 1])
            i += 2
        elif op == 5:
            if vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 6:
            if not vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 7:
            ns[ns[i + 3]] = int(vo(modes[0], ns[i + 1]) < vo(modes[1], ns[i + 2]))
            i += 4
        elif op == 8:
            ns[ns[i + 3]] = int(vo(modes[0], ns[i + 1]) == vo(modes[1], ns[i + 2]))
            i += 4
        else:
            break
    return ans


def p1(data: str):
    ans = 0
    for amps in itertools.permutations(list(range(5)), 5):
        cur_input = 0
        for amp in amps:
            cur_input = ic(data, amp, cur_input)
        ans = max(ans, cur_input)
    return ans


def run_once(i, rq, sq, ns):
    def vo(mode: str, key: int):
        if mode == '0':
            return ns[key]
        else:
            return key

    while i < len(ns):
        op = ns[i] % 100
        modes = str(ns[i] // 100).zfill(2)[::-1]
        if op == 1:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) + vo(modes[1], ns[i + 2])
            i += 4
        elif op == 2:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) * vo(modes[1], ns[i + 2])
            i += 4
        elif op == 3:
            if not rq:
                return i, rq, sq, ns
            ns[ns[i + 1]] = rq.popleft()
            i += 2
        elif op == 4:
            sq.append(vo(modes[0], ns[i + 1]))
            i += 2
        elif op == 5:
            if vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 6:
            if not vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 7:
            ns[ns[i + 3]] = int(vo(modes[0], ns[i + 1]) < vo(modes[1], ns[i + 2]))
            i += 4
        elif op == 8:
            ns[ns[i + 3]] = int(vo(modes[0], ns[i + 1]) == vo(modes[1], ns[i + 2]))
            i += 4
        else:
            return None


def run_amps(amps: tuple, data: str):
    ns = list(map(int, data.strip().split(',')))
    qs = [deque([amps[i]]) for i in range(5)]
    qs[0].append(0)
    running = deque()
    for i in range(5):
        state = (0, qs[i], qs[(i + 1) % 5], ns.copy())
        running.append(state)
    while running:
        state = run_once(*running.popleft())
        if state:
            running.append(state)
    return qs[0][-1]


def p2(data: str):
    ans = 0
    for amps in itertools.permutations(list(range(5, 10)), 5):
        ans = max(ans, run_amps(amps, data))
    return ans

