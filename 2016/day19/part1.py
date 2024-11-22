from collections import deque

d = int(input())
q = deque(range(1, d + 1))
while len(q)!=1:
    q.rotate(-1)
    q.popleft()
print(q.pop())
