import itertools
import re
import sys

lines = [l.strip() for l in sys.stdin.readlines()]
t = 0
for i in range(len(lines)):
    for m in re.finditer(r'\d+', lines[i]):
        for j, k in itertools.product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
            if (0 <= j < len(lines)
                    and 0 <= k < len(lines[0])
                    and lines[j][k] != '.' and not lines[j][k].isdigit()):
                t += int(m.group())
                break
print(t)
