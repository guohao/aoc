from functools import reduce, cache

from helper import *

data = raw_data(2015, 24)
weights = [int(x) for x in lines(data)]


def solve2():
    target = sum(weights) // 4
    for la in range(1, len(weights) - 3):
        for a in itertools.combinations(weights, la):
            if sum(a) != target:
                continue
            remain = [x for x in list(set(weights) - set(list(a))) if x < target]
            if len(remain) + la < len(weights):
                continue
            for lb in range(1, len(remain) - 1):
                if sum(remain[:lb]) > sum(a):
                    continue
                for b in itertools.combinations(remain, lb):
                    if sum(b) != target:
                        continue
                    remain2 = [x for x in list(set(remain) - set(list(b))) if x < target]
                    if len(remain2) + la < len(remain):
                        continue

                    for lc in range(1, len(remain2) - 1):
                        if sum(remain[:lc]) > target:
                            continue
                        for c in itertools.combinations(remain2, lc):
                            if sum(c) != target:
                                continue
                            d = list(set(remain2) - set(list(c)))
                            if sum(d) != target:
                                continue
                            print(math.prod(a))
                            return


def solve():
    target = sum(weights) // 3
    for la in range(1, len(weights) - 2):
        for a in itertools.combinations(weights, la):
            if sum(a) != target:
                continue
            remain = [x for x in list(set(weights) - set(list(a))) if x < sum(a)]
            if len(remain) + la < len(weights):
                continue
            for lb in range(1, len(remain) - 1):
                if sum(remain[:lb]) > sum(a):
                    continue
                for b in itertools.combinations(remain, lb):
                    if sum(b) != target:
                        continue
                    c = list(set(remain) - set(list(b)))
                    if sum(c) != target:
                        continue
                    print(math.prod(a))
                    return


@cache
def search(visited: frozenset[int], current: frozenset[int], target: int, remain: int) -> bool:
    ava = [x for x in weights if x not in visited]
    if remain == 1:
        return sum(ava) == target
    if sum(current) == target:
        return search(frozenset(ava) | current, frozenset(), target, remain - 1)
    if sum(current) > target:
        return False

    for i in range(len(ava) - 1):
        if search(visited | {ava[i]}, current | {ava[i]}, target, remain):
            return True
    return False


def search0(groups):
    target = sum(weights) // groups
    for l in range(len(weights) - groups + 1):
        for a in itertools.combinations(weights, l):
            if sum(a) != target:
                continue
            if search(frozenset(a), frozenset(), target, groups - 1):
                return math.prod(a)


def search1(groups):
    candidates = []
    target = sum(weights) // groups

    for l in range(len(weights) - groups + 1):
        if sum(weights[:l]) > target:
            continue
        for a in itertools.combinations(weights, l):
            if sum(a) != target:
                continue
            candidates.append(a)
    candidates.sort(key=lambda x: len(x))
    for i in range(len(candidates)):
        a = candidates[i]
        visited = set(a)
        remain = [t for t in candidates if all(x not in visited for x in t)]
        for others in itertools.combinations(remain, groups - 1):
            if all(x == y or len(set(x) & set(y)) == 0 for x in others for y in others):
                print(math.prod(a))
                return


solve()
solve2()
print(search0(3))
search1(3)
search1(4)
