from collections import deque

skip = int(input())
q = deque()
for i in range(2018):
    q.rotate(-skip)
    q.append(i)
print(q.popleft())
