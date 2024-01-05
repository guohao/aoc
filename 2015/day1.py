from helper import *

data = raw_data(2015, 1)

print(data.count('(') - data.count(')'))

floor = 0
for i, c in enumerate(data, start=1):
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i)
        break
