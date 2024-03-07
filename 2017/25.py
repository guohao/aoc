import re


def p1(data: str):
    parts = data.split('\n\n')
    steps = int(re.findall(r'\d+', parts[0].splitlines()[1])[0])
    states = {}
    for part in parts[1:]:
        lines = part.splitlines()
        state = lines[0][-2]
        ops = []
        for sop in (lines[2:5], lines[6:9]):
            w = sop[0][-2]
            d = sop[1].split()[-1][:-1]
            ns = sop[2][-2]
            ops.append((int(w), d, ns))
        states[state] = ops
    state = 'A'
    arr = [0] * steps * 2
    i = len(arr) // 2
    for _ in range(steps):
        ops = states[state][arr[i]]
        arr[i] = ops[0]
        if ops[1] == 'right':
            i += 1
        elif ops[1] == 'left':
            i -= 1
        state = ops[2]
    return arr.count(1)
