import hashlib
import itertools

did = input()
ans = ['x'] * 8
for i in itertools.count():
    digest = hashlib.md5((did + str(i)).encode()).hexdigest()
    if digest[:5] == '0' * 5:
        p = int(digest[5], 16)
        if p < 8 and ans[p] == 'x':
            ans[p] = digest[6]
            if 'x' not in ans:
                print(''.join(ans))
                break
