import functools
from collections import defaultdict

from helper import *

data = raw_data(2023, 7)
lines = lines(data)
cards = []


def hands_to_int(hands: str) -> List[int]:
    _cards = 'AKQJT98765432'[::-1]
    return [_cards.index(c) for c in hands]


def hands_to_int_with_joker(hands: str) -> List[int]:
    _cards = 'AKQT98765432J'[::-1]
    return [_cards.index(c) for c in hands]


def type_of(hands: List[int], with_joker: bool) -> int:
    count = defaultdict(lambda: 0)
    for c in set(hands):
        count[c] = hands.count(c)
    if with_joker and 0 in count:
        del count[0]
        jc = hands.count(0)
    else:
        jc = 0
    count = sorted(count.values(), reverse=True)
    if not count:
        return 1
    a = count[0] + jc
    if a == 5:
        return 1
    if a == 4:
        return 2
    if a == 3:
        if count[1] == 2:
            return 3
        else:
            return 4
    if a == 2:
        if count[1] == 2:
            return 5
        else:
            return 6
    return 7


def my_cmp_with_joker(a: tuple[List[int], int], b: tuple[List[int], int]) -> int:
    return my_cmp(a, b, with_joker=True)


def my_cmp(a: tuple[List[int], int], b: tuple[List[int], int], with_joker=False) -> int:
    ha = a[0]
    hb = b[0]
    ta = type_of(ha, with_joker)
    tb = type_of(hb, with_joker)
    if ta == tb:
        if ha == hb:
            return 0
        return -1 if ha < hb else 1
    else:
        return tb - ta


for line in lines:
    hands, bid = line.split()
    cards.append((hands_to_int(hands), int(bid)))

cards.sort(key=functools.cmp_to_key(my_cmp))
print(sum(bid * i for i, (_, bid) in enumerate(cards, start=1)))

cards = []
for line in lines:
    hands, bid = line.split()
    cards.append((hands_to_int_with_joker(hands), int(bid)))

cards.sort(key=functools.cmp_to_key(my_cmp_with_joker))
print(sum(bid * i for i, (_, bid) in enumerate(cards, start=1)))
