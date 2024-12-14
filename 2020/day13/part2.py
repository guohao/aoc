import sys
from sympy.ntheory.modular import crt

data = sys.stdin.read().strip()

mods = []
rems = []

for i, bus in enumerate(data.splitlines()[1].split(',')):
    if bus == 'x':
        continue
    id = int(bus)
    mods.append(id)
    rems.append((id - i) % id)
print(crt(mods, rems)[0])
