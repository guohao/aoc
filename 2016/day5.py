from helper import *
import hashlib


def s_md5(s: str):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


def p1():
    s = "abbhdwsy"
    ans = ''
    for i in itertools.count():
        if len(ans) == 8:
            break
        h = s_md5(s + str(i))
        if h.startswith('0' * 5):
            ans += h[5]
    print(ans)


def p2():
    s = "abbhdwsy"
    ans = []
    for i in itertools.count():
        if len(ans) == 8:
            break
        h = s_md5(s + str(i))
        if h.startswith('0' * 5):
            p = int(h[5], 16)
            if 0 <= p <= 7 and p not in [x[0] for x in ans]:
                ans.append((p, h[6]))
    ans.sort(key=lambda x: x[0])
    print(''.join(x[1] for x in ans))


p1()
p2()
