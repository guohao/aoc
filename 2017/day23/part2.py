import math

b = 93 * 100 + 100000
c = b + 17000


def is_prime(n: int) -> bool:
    for j in range(2, int(math.sqrt(n))):
        if n % j == 0:
            return False
    return True


ans = 0
for i in range(b, c + 1, 17):
    if not is_prime(i):
        ans += 1
print(ans)
