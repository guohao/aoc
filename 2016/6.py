from collections import Counter


def p1(data: str):
    ans = ''
    for line in zip(*data.splitlines()):
        ans += Counter(line).most_common(1)[0][0]
    return ans

def p2(data:str):
    ans = ''
    for line in zip(*data.splitlines()):
        ans += Counter(line).most_common()[-1][0]
    return ans
