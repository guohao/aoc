from collections import deque

cmds = deque()
try:
    while True:
        line = input()
        line = line.upper()
        line = line.replace('AND', '&')
        line = line.replace('OR', '|')
        line = line.replace('NOT ', '~')
        line = line.replace('LSHIFT ', '<<')
        line = line.replace('RSHIFT ', '>>')
        line = '='.join(reversed(line.split(" -> ")))
        cmds.append(line)
except EOFError:
    pass

while cmds:
    line = cmds.popleft()
    try:
        exec(line)
    except Exception:
        cmds.append(line)

print(eval('A'))
