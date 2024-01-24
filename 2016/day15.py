from helper import *
from z3 import *

data = raw_data(2016, 15)


def solve(p2: bool):
    discs = []
    for line in lines(data):
        _, pc, _, ps = ints(line)
        discs.append((pc, ps))
    solver = z3.Solver()
    t = Int("t")
    solver.add(t >= 0)
    for i, (pc, ps) in enumerate(discs, start=1):
        solver.add((t + i + ps) % pc == 0)
    if p2:
        solver.add((t + len(discs) + 1) % 11 == 0)
    solver.check()
    print(solver.model().eval(t))


solve(False)
solve(True)
