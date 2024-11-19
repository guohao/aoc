s = [ord(x) - ord('a') for x in input()]
while True:
    for i in reversed(range(len(s))):
        s[i] += 1
        if s[i] != 26:
            break
        else:
            s[i] = 0
    if len(set(s[i] for i in range(len(s) - 1) if s[i] == s[i + 1])) < 2:
        continue
    if any(chr(x + ord('a')) in 'iol' for x in s):
        continue
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] - 1 == s[i + 2] - 2:
            print(''.join(chr(x + ord('a')) for x in s))
            exit()
