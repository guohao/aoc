import sys
from collections import Counter

hands = []
cards = 'AKQJT98765432'[::-1]
for line in sys.stdin.readlines():
    hand, bid = line.split()
    points = list(map(cards.index, hand))
    c = Counter(points)
    mc = sorted(c.values())[::-1]
    hands.append(((mc, points), int(bid)))
hands.sort()
print(sum(rnk * bid for rnk, (_, bid) in enumerate(hands, start=1)))
