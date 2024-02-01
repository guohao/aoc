from helper import *


def gen_line(s: str) -> str:
    res = ''
    for i in range(len(s)):
        l = s[i - 1] if i - 1 >= 0 else '.'
        r = s[i + 1] if i + 1 < len(s) else '.'
        if l != r:
            res += '^'
        else:
            res += '.'
    return res


def p1():
    data = raw_data(2016, 18)
    # data = ".^^.^.^^^^"
    ans = 0
    for _ in range(40):
        ans += data.count('.')
        # print(data)
        data = gen_line(data)
    print(ans)


p1()
