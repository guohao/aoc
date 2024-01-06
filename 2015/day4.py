import hashlib

from helper import *


def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

def sovle(data: str) -> int:
    for i in range(100000000):
        if md5(data + str(i)).startswith('00000'):
            return i

def sovle2(data: str) -> int:
    for i in range(100000000):
        if md5(data + str(i)).startswith('000000'):
            return i

print(sovle('ckczppom'))
print(sovle2('ckczppom'))
