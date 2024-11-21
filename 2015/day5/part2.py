import re
import sys

t = 0
for line in sys.stdin.readlines():
    if not re.search(r'(\w{2}).*\1', line):
        continue
    if not re.search(r'(\w)\w\1', line):
        continue
    t += 1
print(t)
