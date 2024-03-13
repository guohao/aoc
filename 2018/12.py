import re


def solve(data: str, turns: int):
    pa, pb = data.split('\n\n')
    seq = ''.join(re.findall('[.#]', pa))
    rules = {}
    for line in pb.splitlines():
        pl, pr = line.split(' => ')
        rules[pl] = pr
    lo = 0
    t = 0
    seen = set()
    for t in range(turns):
        # for t in range(turns):
        k = (t - lo, seq)
        if k in seen:
            lo = turns - (t - lo)
            break
        else:
            seen.add(k)
        lo -= 4
        seq = '.' * 4 + seq + '.' * 4
        seq = ''.join(rules[seq[i - 2:i + 3]] for i in range(2, len(seq) - 2))
        seq = seq.rstrip('.')
        lo += len(seq) - len(seq.strip('.')) + 2
        seq = seq.strip('.')
    return sum(b for a, b in zip(seq, range(lo, len(seq) + abs(lo))) if a == '#')


def p1(data: str):
    return solve(data, 20)


def p2(data: str):
    return solve(data, 50000000000)
