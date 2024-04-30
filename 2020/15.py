def p1(data: str):
    seq = list(map(int, data.split(',')))
    seen = {}
    for t in range(2019):
        if t == len(seq) - 1:
            if seq[t] in seen:
                seq.append(t - seen[seq[t]])
            else:
                seq.append(0)
        seen[seq[t]] = t
    return seq[-1]


def p2(data: str):
    seq = list(map(int, data.split(',')))
    seen = {}
    for t in range(30000000 - 1):
        if t == len(seq) - 1:
            if seq[t] in seen:
                seq.append(t - seen[seq[t]])
            else:
                seq.append(0)
        seen[seq[t]] = t
    return seq[-1]
