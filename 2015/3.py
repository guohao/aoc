def solve(data, n):
    x, y = [0] * n, [0] * n
    ans = {(0, 0)}
    t = 0
    for c in data:
        match c:
            case '<':
                x[t] -= 1
            case '>':
                x[t] += 1
            case 'v':
                y[t] += 1
            case '^':
                y[t] -= 1
        ans.add((x[t], y[t]))
        t = (t + 1) % n
    return len(ans)


def p1(data):
    return solve(data, 1)


def p2(data):
    return solve(data, 2)
