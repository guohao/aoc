def p1(data: str):
    seq = [0]
    step = int(data)
    i = 0
    for k in range(1, 2018):
        i = (i + step) % len(seq) + 1
        seq = seq[:i] + [k] + seq[i:]
    return seq[(i + 1) % len(seq)]


def p2(data: str):
    step = int(data)
    i = 0
    iz = 0
    ans = -1
    for k in range(1, 50000000 + 1):
        i = (i + step) % k + 1
        if i == iz + 1:
            ans = k
        elif i <= iz:
            iz += 1
    return ans
