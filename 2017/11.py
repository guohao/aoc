import util


def p1(data: str):
    return max(map(abs, list(myutil.hex_walk(data.strip().split(',')))[-1]))


def p2(data: str):
    ans = 0
    for move in myutil.hex_walk(data.strip().split(',')):
        ans = max(ans, max(map(abs, move)))
    return ans
