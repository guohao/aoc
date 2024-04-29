import math
from sympy.ntheory.modular import crt


def p1(data: str):
    dt = int(data.splitlines()[0])
    ans = dt, -1
    for line in data.splitlines()[1].split(','):
        if line == 'x':
            continue
        x = int(line)
        r = math.ceil(dt / x) * x - dt
        if r < ans[0]:
            ans = r, x
    return math.prod(ans)


def p2(data: str):
    mods = []
    rems = []

    for i, bus in enumerate(data.splitlines()[1].split(',')):
        if bus == 'x':
            continue
        id = int(bus)
        mods.append(id)
        rems.append((id - i) % id)
    print(mods)
    return crt(mods, rems)[0]
