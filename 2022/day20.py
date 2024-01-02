from collections import deque

from helper import *

data = raw_data(2022, 20)


def p1():
    nums = list(map(int, lines(data)))
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


def p2():
    nums = [811589153 * int(x) for x in lines(data)]
    N = len(nums)
    move = deque(range(N))
    for _ in range(10):
        for i, di in enumerate(nums):
            src = move.index(i)
            move.rotate(-src)
            move.popleft()
            move.rotate(-di)
            move.appendleft(i)
    move.rotate(-move.index(nums.index(0)))
    ans = sum([nums[move[i % N]] for i in (1000, 2000, 3000)])
    print(ans)


p1()
p2()
