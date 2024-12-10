import sys
from collections import deque

lines = [l.strip() for l in sys.stdin.readlines()]
nums = list(map(int, lines))
N = len(nums)
move = deque(range(N))
for i, di in enumerate(nums):
    src = move.index(i)
    move.rotate(-src)
    move.popleft()
    move.rotate(-di)
    move.appendleft(i)
move.rotate(-move.index(nums.index(0)))
ans = sum([nums[move[i % N]] for i in (1000, 2000, 3000)])
print(ans)
