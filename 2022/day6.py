import io_utils

data = io_utils.get_data(2022, 6)
data = io_utils.raw_str_to_lines(data)[0]

for i in range(13, len(data)):
    if len(set(data[i-13:i+1])) == 14:
        print(i+1)
        break