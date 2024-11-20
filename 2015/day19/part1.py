import re

rs = []
while True:
    line = input()
    if not line:
        break
    l, r = line.split('=>')
    rs.append((l.strip(), r.strip()))

mm = input()
alls = set()
for k, v in rs:
    for m in re.finditer(k, mm):
        alls.add(mm[:m.start()] + v + mm[m.end():])
print(len(alls))
