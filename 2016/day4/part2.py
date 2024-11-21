import re
import sys
from collections import Counter

lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    name, sid, _ = re.findall(r'(\w.*)-(\d+)\[(\w+)]', line)[0]
    decode = ''.join(chr(ord('a') + (ord(c) - ord('a') + int(sid)) % 26) for c in name.replace("-", ''))
    if 'NorthPoleobjects'.lower() in decode:
        print(sid)
        break
