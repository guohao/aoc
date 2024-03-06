def solve(data: str, offset: int) -> int:
    s = data[offset:] + data[:offset]
    ans = 0
    for i, c in enumerate(data):
        if c == s[i]:
            ans += int(c)
    return ans


def p1(data: str):
    return solve(data, 1)


def p2(data: str):
    return solve(data, len(data) // 2)
