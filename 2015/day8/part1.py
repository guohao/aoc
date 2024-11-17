r = 0
while True:
    line = input()
    if not line:
        break
    r += len(line) - len(eval(line))
print(r)
