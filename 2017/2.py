def p1(data):
    ans = 0
    for line in data.splitlines():
        nums = list(map(int, line.split()))
        ans += max(nums) - min(nums)
    return ans


def find_divisible(nums):
    for a in nums:
        for b in nums:
            if a == b:
                continue
            if a % b == 0:
                return a // b


def p2(data):
    ans = 0
    for line in data.splitlines():
        nums = sorted(map(int, line.split()))
        ans += find_divisible(nums)
    return ans
