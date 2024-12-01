import re
import sys
from collections import Counter

a, b = zip(*[list(map(int, re.findall(r'-?\d+', l))) for l in sys.stdin.readlines()])
b = Counter(b)
print(sum((x * b[x]) for x in a))
