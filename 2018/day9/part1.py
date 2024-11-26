import re
from collections import deque

pc, last_points = list(map(int, re.findall(r'-?\d+', input())))
ps = [0] * pc

q = deque()
for i in range(last_points + 1):
    if i == 0 or i % 23:
        q.rotate(-1)
        q.append(i)
    else:
        q.rotate(7)
        ps[i % pc] += q.pop() + i
        q.rotate(-1)
print(max(ps))
