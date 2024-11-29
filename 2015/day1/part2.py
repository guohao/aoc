f = 0
for i, c in enumerate(input(), start=1):
    f += (c == '(') - (c != '(')
    if f == -1:
        print(i)
        break
