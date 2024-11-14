import itertools
import hashlib

key = input()
for i in itertools.count():
    md5 = hashlib.md5()
    md5.update(key.encode())
    md5.update(str(i).encode())
    v = md5.hexdigest()
    if v[:5] == '0' * 5:
        print(i)
        break
