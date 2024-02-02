from helper import *

data = raw_data(2016, 21)
lines = lines(data)


def p1(s):
    for line in lines:
        if line.startswith('swap position'):
            x, y = ints(line)
            x, y = min(x, y), max(x, y)
            s = s[:x] + s[y] + s[x + 1:y] + s[x] + s[y + 1:]
        elif line.startswith('swap letter'):
            a, b = line.split()[-1], line.split()[-4]
            s = s.replace(a, '1').replace(b, a).replace('1', b)
        elif line.startswith('rotate left'):
            d = ints(line)[0] % len(s)
            s = s[d:] + s[:d]
        elif line.startswith('rotate right'):
            d = ints(line)[0] % len(s)
            s = s[-d:] + s[:-d]
        elif line.startswith('rotate based'):
            lt = line.split()[-1]
            i = s.index(lt)
            if i >= 4:
                i += 1
            i += s.count(lt)
            i = i % len(s)
            s = s[-i:] + s[:-i]
        elif line.startswith('reverse'):
            x, y = ints(line)
            x, y = min(x, y), max(x, y)
            s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
        elif line.startswith('move'):
            x, y = ints(line)
            lt = s[x]
            s = s[:x] + s[x + 1:]
            s = s[:y] + lt + s[y:]
        else:
            raise ValueError
    return s


def p2(password):
    for s in itertools.permutations('abcdefgh'):
        s = ''.join(s)
        if password == p1(s):
            print(s)
            break


print(p1('abcdefgh'))
p2('fbgdceah')
