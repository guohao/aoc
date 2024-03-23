def solve(data: str, n):
    data = data.strip()
    s = data
    while len(s) < n:
        s = s + '0' + ''.join("1" if c == '0' else '0' for c in reversed(s))
    s = s[:n]
    cs = ''
    while len(cs) % 2 != 1:
        cs = ''
        for i in range(0, len(s) - 1, 2):
            p = s[i] + s[i + 1]
            if p in ['00', '11']:
                cs += '1'
            else:
                cs += '0'
        s = cs
    return cs


def p1(data: str):
    return solve(data, 272)


def p2(data: str):
    return solve(data, 35651584)
