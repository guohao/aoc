import io_utils

data = io_utils.get_data(2022, 10)
lines = data.strip().splitlines()
x = 1
s = []

for line in lines:
    s.append(x)
    c = line.split()[0]
    if c.startswith('add'):
        v = int(line.split()[1])
        s.append(x)
        x += v

t = [20, 60, 100, 140, 180, 220]
print(sum([x * s[x - 1] for x in t]))

o = ''
for i in range(0, len(s)):
    x = s[i]
    if x - 1 <= i % 40 <= x + 1:
        o += '#'
    else:
        o += '.'
for i in range(0, len(o), 40):
    print(o[i:i + 40])
