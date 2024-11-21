import sys
from collections import deque

cmds = deque()
lines = sys.stdin.readlines()
for line in lines:
    line = line.upper().strip()
    line = line.replace('AND', '&')
    line = line.replace('OR', '|')
    line = line.replace('NOT ', '~')
    line = line.replace('LSHIFT ', '<<')
    line = line.replace('RSHIFT ', '>>')
    line = '='.join(reversed(line.split(" -> ")))
    cmds.append(line)

while cmds:
    line = cmds.popleft()
    try:
        exec(line)
    except Exception as e:
        cmds.append(line)

print(eval('A'))
