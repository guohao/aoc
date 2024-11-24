from collections import deque
import re

nums = list(map(int, re.findall(r'-?\d+', input())))
q = deque(range(256))
skip_size = 0
cur_pos = 0
for lens in nums:
    q1 = deque()
    for _ in range(lens):
        q1.append(q.popleft())
    while q1:
        q.append(q1.pop())
    q.rotate(-skip_size)
    cur_pos += lens + skip_size
    skip_size += 1

q.rotate(cur_pos)
print(q.popleft() * q.popleft())
