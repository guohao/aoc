import helper

data = helper.raw_data(2022, 6)
data = helper.lines(data)[0]

for i in range(13, len(data)):
    if len(set(data[i - 13:i + 1])) == 14:
        print(i + 1)
        break
