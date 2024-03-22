import hashlib
import itertools


def p1(data: str):
    data = data.strip()
    s = ''
    for n in itertools.count(0):
        md5 = hashlib.md5((data + str(n)).encode()).hexdigest()
        if md5.startswith('0' * 5):
            s += md5[5]
            if len(s) == 8:
                return s


def p2(data: str):
    data = data.strip()
    s = ['_'] * 8
    for n in itertools.count(0):
        md5 = hashlib.md5((data + str(n)).encode()).hexdigest()
        if md5.startswith('0' * 5):
            if md5[5].isdigit():
                p = int(md5[5])
                if 0 <= p <= 7 and s[p] == '_':
                    s[p] = md5[6]
            if '_' not in s:
                return ''.join(s)
