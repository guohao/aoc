from collections import deque


def p1(data: str):
    n = int(data)
    q = deque(range(1, n + 1))
    ro = 0
    while len(q) != 1:
        q.rotate(-1)
        q.popleft()
    return q.pop()


def p2(data: str):
    n = int(data)
    q = deque(range(1, n + 1))
    q.rotate(len(q) // 2)
    for i in range(n - 1):
        q.popleft()
        if i % 2 == 1:
            q.rotate(-1)
    return q.popleft()
