from helper import *

data = raw_data(2015, 8)

ans = 0
ans1 = 0
for line in lines(data):
    ans += len(line) - len(eval(line))
    lst = list(line)
    ans1 += lst.count('\\') + lst.count('"') + 2
print(ans)
print(ans1)
