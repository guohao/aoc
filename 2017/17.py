from collections import deque


def p1(data: str):
    n = int(data)
    q = deque()
    for i in range(2018):
        q.rotate(n + 1)
        q.append(i)
    return q[-2]


def p2(data: str):
    n = int(data)
    q = deque()
    for i in range(50000000):
        q.rotate(n + 1)
        q.append(i)
    while q.pop():
        pass
    return q.pop()
