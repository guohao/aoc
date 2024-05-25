from collections import Counter


def solve(data: str, with_joker: bool):
    hands = []
    if with_joker:
        cards = 'AKQT98765432J'[::-1]
    else:
        cards = 'AKQJT98765432'[::-1]
    for line in data.splitlines():
        hand, bid = line.split()
        points = list(map(cards.index, hand))
        c = Counter(points)
        if with_joker and 0 < hand.count('J') < 5:
            jc = c.pop(cards.index('J'))
            c[c.most_common()[0][0]] += jc
        mc = sorted(c.values())[::-1]
        hands.append(((mc, points), int(bid)))
    hands.sort()
    return sum(rnk * bid for rnk, (_, bid) in enumerate(hands, start=1))


def p1(data: str):
    return solve(data, False)


def p2(data: str):
    return solve(data, True)
