from helper import *

data = raw_data(2015, 5)


def is_nice(s: str):
    if sum(s.count(x) for x in 'aeiou') < 3:
        return False
    if not re.search(r'(\w)\1', s):
        return False
    if any(x in s for x in ['ab', 'cd', 'pq', 'xy']):
        return False
    return True


def is_nice_2(s: str):
    if not re.search(r'(\w{2}).*\1', s):
        return False
    if not re.search(r'(\w)\w\1', s):
        return False
    return True


print(sum(is_nice(s) for s in lines(data)))
print(sum(is_nice_2(s) for s in lines(data)))
