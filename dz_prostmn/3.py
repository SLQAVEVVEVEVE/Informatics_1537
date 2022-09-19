def p(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return 0
        d += 1
    return 1


def np(number):
    a = []
    for i in range(2, int(number / 2) + 1):
        while number % i == 0:
            a.append(i)
            number //= i
    if number != 1:
        a.append(number)
    return a


for x in range(6, 6000):
    print(np(x), x)
