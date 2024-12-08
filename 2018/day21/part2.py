def calc(r5, r4):
    while True:
        r5 = (((r5 + (r4 & 255)) & 16777215) * 65899) & 16777215
        if r4 < 256:
            return r5
        r4 = r4 // 256


seen = []
r5 = 0
while True:
    r4 = r5 | 65536
    r5 = 13431073
    r5 = calc(r5, r4)
    if r5 in seen:
        print(seen[-1])
        break
    seen.append(r5)
