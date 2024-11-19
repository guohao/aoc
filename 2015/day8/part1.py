r = 0
try:
    while True:
        line = input()
        r += len(line) - len(eval(line))
except EOFError:
    print(r)
