import itertools
import re


def rotate(s, n):
    return ''.join([s[(i - n + len(s)) % len(s)] for i in range(len(s))])


def swap(s, x, y):
    x, y = sorted([x, y])
    return s[:x] + s[y] + s[x + 1:y] + s[x] + s[y + 1:]


def solve(data: str, s):
    for line in data.splitlines():
        ps = s
        if 'swap pos' in line:
            x, y = list(map(int, re.findall(r'\d+', line)))
            s = swap(s, x, y)
        elif 'swap let' in line:
            a, b = re.findall(r'letter (\w)', line)
            ia = s.index(a)
            ib = s.index(b)
            s = swap(s, ia, ib)
        elif 'rotate' in line and 'step' in line:
            x = int(re.findall(r'\d+', line)[0])
            if 'left' in line:
                x = -x
            s = rotate(s, x)
        elif 'rotate' in line and 'based' in line:
            x = s.index(re.findall(r'letter (\w)', line)[0])
            if x >= 4:
                x = x + 2
            else:
                x = x + 1
            s = rotate(s, x)
        elif 'reverse' in line:
            x, y = list(map(int, re.findall(r'\d+', line)))
            s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
        elif 'move' in line:
            x, y = list(map(int, re.findall(r'\d+', line)))
            if x < y:
                s = s[:x] + s[x + 1:y + 1] + s[x] + s[y + 1:]
            else:
                s = s[:y] + s[x] + s[y:x] + s[x + 1:]
        assert len(s) == len(ps)
        assert list('abcdefgh') == sorted(s)
    return s


def p1(data: str):
    return solve(data, 'abcdefgh')


def p2(data: str):
    for sl in itertools.permutations(list('abcdefgh'), 8):
        ss = ''.join(sl)
        if solve(data, ss) == 'fbgdceah':
            return ss
