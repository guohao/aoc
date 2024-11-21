import re
import sys

rs = []
parts = sys.stdin.read().split('\n\n')
for line in parts[0].splitlines():
    l, r = line.split('=>')
    rs.append((l.strip(), r.strip()))

mm = parts[1].strip()
alls = set()
for k, v in rs:
    for m in re.finditer(k, mm):
        alls.add(mm[:m.start()] + v + mm[m.end():])
print(len(alls))
