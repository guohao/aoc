def next_pos(r, c):
    if r == 1:
        return c + 1, 1
    return r - 1, c + 1


def p1():
    r = 1
    c = 1
    code = 20151125
    while True:
        r, c = next_pos(r, c)
        code = (code * 252533) % 33554393
        if r == 3010 and c == 3019:
            print(code)
            return


p1()
