import itertools
import math
import re
import sys
from collections import defaultdict

lines = [l.strip() for l in sys.stdin.readlines()]
gears = defaultdict(list)
for i in range(len(lines)):
    for m in re.finditer(r'\d+', lines[i]):
        for j, k in itertools.product(range(i - 1, i + 2), range(m.start() - 1, m.end() + 1)):
            if (0 <= j < len(lines)
                    and 0 <= k < len(lines[0])
                    and lines[j][k] == '*'):
                gears[j, k].append(int(m.group()))

print(sum(math.prod(v) for k, v in gears.items() if len(v) == 2))
