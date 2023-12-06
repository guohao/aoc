import re

from common import io_utils

data = io_utils.get_data(2023, 6)
data = io_utils.raw_str_to_lines(data)

time = int(''.join(re.findall(r'\d+', data[0])))
record = int(''.join(re.findall(r'\d+', data[1])))

ways = len([x for x in range(1, time) if x * (time - x) > record])

print(ways)