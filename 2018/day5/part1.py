import re
import string

d = input()
p = []
for i in range(26):
    aA = string.ascii_lowercase[i] + string.ascii_uppercase[i]
    p.append(aA)
    p.append(aA[::-1])

p = '|'.join(p)
while True:
    d, n = re.subn(p, '', d)
    if n == 0:
        print(len(d))
        break
