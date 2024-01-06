def next_letter(c: str) -> str:
    if c == 'z':
        return 'a'
    else:
        return chr(ord(c) + 1)


def gen_pass(s: str) -> str:
    s = list(s[::-1])
    for i in range(len(s)):
        s[i] = next_letter(s[i])
        if s[i] != 'a':
            break
    s.reverse()
    return ''.join(s)


def is_valid_pass(s: str) -> bool:
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    if sum(s.count(chr(c) * 2) for c in range(ord('a'), ord('z') + 1)) < 2:
        return False
    if not any(chr(c) + chr(c + 1) + chr(c + 2) in s for c in range(ord('a'), ord('y'))):
        return False
    return True


def gen_valid_pass(s: str) -> str:
    s = gen_pass(s)
    while not is_valid_pass(s):
        s = gen_pass(s)
    return s


print(gen_valid_pass("vzbxkghb"))
print(gen_valid_pass(gen_valid_pass("vzbxkghb")))
