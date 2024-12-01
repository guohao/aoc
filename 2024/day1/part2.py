import re
import sys
from collections import Counter

ns = [list(map(int, re.findall(r'-?\d+', l))) for l in sys.stdin.readlines()]

a = [n[0] for n in ns]
b = [n[1] for n in ns]
b = Counter(b)
print(sum((a[i] * b[a[i]]) for i in range(len(a))))
