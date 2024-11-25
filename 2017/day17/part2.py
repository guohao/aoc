from collections import deque

skip = int(input())
q = deque()
for i in range(50000000):
    q.rotate(-skip)
    q.append(i)
q.rotate(-q.index(0)-1)
print(q.popleft())
