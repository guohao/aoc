import hashlib
import itertools

d = input()
for i in itertools.count():
    md5 = hashlib.md5(f'{d}{i}'.encode()).hexdigest()
    if md5[:6] == '0' * 6:
        print(i)
        break
