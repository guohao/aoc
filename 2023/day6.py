import re

from common import io_utils

data = io_utils.get_data(2023, 6)
data = io_utils.raw_str_to_lines(data)

times = re.findall(r'\d+', data[0])
records = re.findall(r'\d+', data[1])
ans1 = 1
for i in range(len(times)):
    t = int(times[i])
    record = int(records[i])
    ans1 *= len([x for x in range(1, t) if x * (t - x) > record])
print(ans1)

t = int(re.findall(r'\d+', data[0].replace(' ', ''))[0])
d = int(re.findall(r'\d+', data[1].replace(' ', ''))[0])
for i in range(1, t):
    if i * (t - i) > d:
        ans = (t - i * 2) + 1
        print(ans)
        break
