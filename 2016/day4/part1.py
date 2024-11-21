import re
import sys
from collections import Counter

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    name, id, cs = re.findall(r'(\w.*)-(\d+)\[(\w+)]', line)[0]
    if cs == ''.join(x[0] for x in Counter(sorted(name.replace('-', ''))).most_common(5)):
        t += int(id)

print(t)
