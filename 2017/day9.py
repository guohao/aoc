from helper import *

data = raw_data(2017, 9)


def remove_cancel(line):
    while '!' in line:
        line = re.sub(r'!.', '', line)
    return line


def score_of(line):
    line = remove_cancel(line)
    ans1, ans2 = 0, 0
    d = 0
    i = 0
    while i < len(line):
        c = line[i]
        if c == '{':
            d += 1
        elif c == '}':
            ans1 += d
            d -= 1
        elif c == '<':
            i += 1
            while line[i] != '>':
                ans2 += 1
                i += 1
        elif c == ',':
            pass
        else:
            raise Exception(f'Unexpected character {c}')
        i += 1
    return ans1, ans2


def solve():
    ans1, ans2 = 0, 0
    for line in lines(data):
        a1, a2 = score_of(line)
        ans1 += a1
        ans2 += a2
    return ans1, ans2


print(solve())
