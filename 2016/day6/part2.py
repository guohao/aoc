import sys
from collections import Counter

lines = [line.strip() for line in sys.stdin.readlines()]

print(''.join(Counter(s).most_common()[-1][0] for s in zip(*lines)))
