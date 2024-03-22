def solve(data: str, ignore=True):
    data = data.strip().replace(' ', '')
    ans = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            end = data.index(')', i + 1)
            a, b = list(map(int, data[i + 1:end].split('x')))
            if ignore:
                ans += b * a
            else:
                ans += b * solve(data[end + 1:end + 1 + a], False)
            i = end + a + 1
        else:
            i += 1
            ans += 1
    return ans


def p1(data: str):
    return solve(data, True)


def p2(data: str):
    return solve(data, False)
