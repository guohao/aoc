import sys
import re

ns = [list(map(int, re.findall(r'-?\d+', l))) for l in sys.stdin.readlines()]
print(sum(abs(a - b) for a, b in zip(*map(sorted, zip(*ns)))))
