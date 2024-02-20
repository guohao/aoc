from helper import *

data = raw_data(2017, 2)


def p1():
    ans = 0
    for line in lines(data):
        nums = sorted(map(int, line.split()))
        ans += nums[-1] - nums[0]
    return ans


def p2():
    ans = 0
    for line in lines(data):
        nums = sorted(map(int, line.split()))
        for a in nums:
            found = False
            for b in nums:
                if a == b:
                    continue
                if b / a == b // a:
                    ans += b // a
                    found = True
            if found:
                break
    return ans


print(p1())
print(p2())
