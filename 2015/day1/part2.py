floor = 0
for i, c in enumerate(input(), start=1):
    floor += (c == '(') - (c != '(')
    if floor == -1:
        print(i)
        break
