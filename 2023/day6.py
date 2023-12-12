import re

import io_utils

data = io_utils.get_data(2023, 6)
data = io_utils.raw_str_to_lines(data)


def ways(total_time: int, current_record: int) -> int:
    return len([x for x in range(1, total_time) if x * (total_time - x) > current_record])


ans1 = 1
times = [int(x) for x in re.findall(r'\d+', data[0])]
records = [int(x) for x in re.findall(r'\d+', data[1])]

for i, time in enumerate(times):
    ans1 *= ways(time, records[i])

print(ans1)
time = int(''.join(re.findall(r'\d+', data[0])))
record = int(''.join(re.findall(r'\d+', data[1])))
ways = ways(time, record)
print(ways)
