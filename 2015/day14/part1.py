import re

ans = 0
try:
    while True:
        s, d, r = map(int, re.findall(r'\d+', input()))
        ans = max(ans, (2503 // (d + r) * d + min(d, 2503 % (d + r))) * s)
except EOFError:
    print(ans)
