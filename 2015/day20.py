def sum_of_factors(n):
    factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i == i:
                factors.append(i)
            else:
                factors.extend([i, n // i])
    return sum(factors)


def p1():
    for i in range(1, 1000000):
        if sum_of_factors(i) >= 3600000 - i:
            print(i)
            break


def sum_of_factors_2(n):
    factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i == i:
                if i >= n // 50:
                    factors.append(i)
            else:
                if n // i >= n // 50:
                    factors.extend([i, n // i])
    return sum(factors)


def p2():
    for i in range(1, 100000000):
        if 11 * (sum_of_factors_2(i) + i) >= 36000000:
            print(i)
            break


p1()
p2()
