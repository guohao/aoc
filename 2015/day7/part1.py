from collections import deque

cmds = deque()
while True:
    line = input()
    if not line:
        break
    line = line.upper()
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
    except Exception:
        cmds.append(line)

print(eval('A'))
