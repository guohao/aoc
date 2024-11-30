import sys

from regex import regex

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    ws = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    d2i = lambda x: ws.index(x) if x in ws else int(x)
    nums = list(map(d2i, regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)))
    t += nums[0] * 10 + nums[-1]
print(t)
