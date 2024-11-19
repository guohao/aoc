r = 0
try:
    while True:
        line = input()
        r += line.count('\\') + line.count('"') + 2
except EOFError:
    print(r)
