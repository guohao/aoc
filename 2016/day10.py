from collections import defaultdict

from helper import *

data = raw_data(2016, 10)
lines = lines(data)
ops = {}
bot = defaultdict(list)
output = defaultdict(list)
for line in lines:
    if line.startswith("value"):
        src, target = ints(line)
        bot[target].append(src)
    else:
        src, low_to, high_to = ints(line)
        low_type, high_type = re.findall(r' (bot|output)', line)
        ops[src] = ((low_type, low_to), (high_type, high_to))

while bot:
    for src in bot.copy():
        if len(bot[src]) == 2:
            low, high = sorted(bot.pop(src))
            print(src, low, high)
            if low == 17 and high == 61:
                print(src)
            eval(ops[src][0][0])[ops[src][0][1]].append(low)
            eval(ops[src][1][0])[ops[src][1][1]].append(high)

print(math.prod(output[i][0] for i in range(3)))
