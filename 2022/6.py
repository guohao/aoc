def solve(data: str, n: int):
    data = data.strip()
    for i in range(n, len(data)):
        if len(set(data[i - n:i])) == n:
            return i


def p1(data: str):
    return solve(data, 4)


def p2(data: str):
    return solve(data, 14)
