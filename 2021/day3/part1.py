import sys
from collections import Counter

lines = [line.strip() for line in sys.stdin.readlines()]

seq = [Counter(l).most_common(1)[0][0] for l in zip(*lines)]

seq = ''.join(seq)
a = int(seq, 2)
b = ~a & ((1 << len(seq)) - 1)
print(a * b)
