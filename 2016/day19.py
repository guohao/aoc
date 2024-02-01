from collections import deque


def p1(n):
    q = deque()
    for i in range(n):
        q.append(i + 1)

    while len(q) > 1:
        q.rotate(-1)
        q.popleft()
    print(q.popleft())


def p2(n):
    q = deque()
    for i in range(n):
        q.append(i + 1)

    tr = 0
    for _ in range(n - 1):
        while tr != len(q) // 2:
            q.rotate(-1)
            tr += 1
        q.popleft()
        tr -= 1
    print(q.popleft())


p1(3012210)
p2(3012210)
