import re
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    ms = [m for m in re.finditer(r'(\w)(\w)\2\1', line) if m.group(1) != m.group(2)]
    if not ms:
        continue
    if any(line[:m.start()].count('[') - line[:m.start()].count(']') for m in ms):
        continue
    t += 1
print(t)
