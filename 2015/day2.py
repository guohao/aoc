from helper import *

ans = 0
ans2 = 0
for line in lines(raw_data(2015, 2)):
    l, w, h = ints(line)
    ans += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    ans2 += min(l + w, w + h, h + l) * 2 + l * w * h
print(ans)
print(ans2)
