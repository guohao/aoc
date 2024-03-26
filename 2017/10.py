from collections import deque
from functools import reduce


def p1(data: str):
    sz = 0
    q = deque(range(256))
    i = 0
    for c in data.split(','):
        cl = int(c)
        q2 = deque()
        for _ in range(cl):
            q2.append(q.popleft())
        while q2:
            q.append(q2.pop())
        q.rotate(-sz)
        i += cl + sz
        sz += 1
    q.rotate(i)
    return q.popleft() * q.popleft()


def p2(data: str):
    sz = 0
    q = deque(range(256))
    i = 0
    seq = [ord(c) for c in data.strip()] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for c in seq:
            q2 = deque()
            for _ in range(c):
                q2.append(q.popleft())
            while q2:
                q.append(q2.pop())
            q.rotate(-sz)
            i += c + sz
            sz += 1
    q.rotate(i)

    ans = ''
    q = list(q)
    for k in range(0, 256, 16):
        ans += hex(reduce(lambda a, b: a ^ b, q[k:k + 16]))[2:].zfill(2)
    return ans
