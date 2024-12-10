import sys

x = 1
s = []
for cmd in sys.stdin.readlines():
    cmd = cmd.strip()
    s.append(x)
    if cmd != 'noop':
        s.append(x)
        x += int(cmd.split()[1])
print(sum(i * s[i - 1] for i in range(20, 260, 40)))
