r = 0
while True:
    line = input()
    if not line:
        break
    r += line.count('\\') + line.count('"') + 2
print(r)
