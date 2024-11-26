import sys

lines = sys.stdin.readlines()
for a in lines:
    for b in lines:
        if a == b or len(a)!=len(b):
            continue
        if sum(a[i] != b[i] for i in range(len(a))) == 1:
            print(''.join(a[i] for i in range(len(a)) if a[i] == b[i]))
            exit()
