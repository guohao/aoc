def p1(data: str):
    n = int(data)
    recipes = '37'
    a, b = 0, 1
    while len(recipes) < 10 + n:
        for x in str(int(recipes[a]) + int(recipes[b])):
            recipes += x
        a = (int(recipes[a]) + a + 1) % len(recipes)
        b = (int(recipes[b]) + b + 1) % len(recipes)
    return recipes[n:n + 10]


def p2(data: str):
    data = data.strip()
    recipes = '37'
    a, b = 0, 1
    while True:
        for x in str(int(recipes[a]) + int(recipes[b])):
            recipes += x
            if recipes[-len(data):] == data:
                return recipes.index(data)
        a = (int(recipes[a]) + a + 1) % len(recipes)
        b = (int(recipes[b]) + b + 1) % len(recipes)
