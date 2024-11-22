from collections import deque

d = int(input())
q = deque(range(d, 0, -1))

q.rotate(len(q) // 2)
while len(q) != 1:
    q.pop()
    if not len(q) % 2:
        q.rotate(1)
print(q.pop())
