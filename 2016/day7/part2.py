import regex
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    ins = set()
    outs = set()
    for m in regex.finditer(r'(\w)(\w)\1', line, overlapped=True):
        if m.group(1) == m.group(2):
            continue
        if line[:m.start()].count('[') - line[:m.start()].count(']'):
            ins.add(m.group(1) + m.group(2))
        else:
            outs.add(m.group(2) + m.group(1))
    m = ins & outs
    t += len(m) > 0
print(t)
