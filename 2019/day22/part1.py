import sys

data = sys.stdin.read().strip()

cards = list(range(10007))
for line in data.splitlines():
    if 'new stack' in line:
        cards.reverse()
    elif 'cut' in line:
        n = int(line.split()[-1])
        cards = cards[n:] + cards[:n]
    else:
        n = int(line.split()[-1])
        n_cards = [0 for _ in range(len(cards))]
        i = 0
        for c in cards:
            n_cards[i] = c
            i = (i + n) % len(n_cards)
        cards = n_cards
print(cards.index(2019))
