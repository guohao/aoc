from helper import *

data = raw_data(2016, 11)


def solve(append: bool):
    ni = 1
    nd = {}
    fs = []
    for line in lines(data):
        line = line.replace("-compatible", "")
        cl = set()
        for cell in re.findall(r'\S+ microchip|\S+ generator', line):
            if cell.split()[0] not in nd:
                nd[cell.split()[0]] = ni
                ni += 1
            cl.add(nd[cell.split()[0]] * (-1 if cell.endswith("microchip") else 1))
        fs.append(frozenset(cl))
    if append:
        fs[0] = fs[0] | {-6, 6, -7, 7}

    states = set()
    states.add((tuple(fs), -1, 0, frozenset()))
    seen = set()
    for i in itertools.count():
        ns = set()
        if len(states) == 0:
            break
        for fs, src, current, carry in states:
            state = (
                tuple([(len([y for y in x if -y in x]), len(x) - len([y for y in x if -y in x])) for x in fs]), current)
            if state in seen:
                continue
            seen.add(state)
            hold = carry | frozenset(fs[current])

            if current == 3 and sum(len(x) for x in fs[:3]) == 0:
                print(i)
                return
            fs = [set(x) for x in fs]
            fs[current] = frozenset(hold)
            next_visit = []
            if current + 1 < len(fs):
                next_visit.append(current + 1)
            if current - 1 >= 0:
                next_visit.append(current - 1)

            for tv in next_visit:
                for j in (1, 2):
                    for comb in itertools.combinations(hold, j):
                        if j == src and comb == carry:
                            continue
                        nfs = [frozenset(x) for x in fs]
                        for x in comb:
                            nfs[current] = nfs[current] - {x}
                        if any(-x not in nfs[current] for x in nfs[current] if x < 0):
                            if any(x > 0 for x in nfs[current]):
                                continue
                        nh = fs[tv] | frozenset(comb)
                        if any(-x not in nh for x in nh if x < 0):
                            if any(x > 0 for x in nh):
                                continue
                        ns.add((tuple(nfs), current, tv, frozenset(comb)))
            states = ns


solve(False)
solve(True)
