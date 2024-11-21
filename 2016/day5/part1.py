import hashlib
import itertools

did = input()
ans = ''
for i in itertools.count():
    digest = hashlib.md5((did + str(i)).encode()).hexdigest()
    if digest[:5] == '0' * 5:
        ans += digest[5]
        if len(ans) == 8:
            print(ans)
            break
