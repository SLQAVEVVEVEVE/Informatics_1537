def p(x):
    d = 2
    if x <= 1:
        return 0
    while d * d <= x:
        if x % d == 0:
            return 0
        d += 1
    return 1


def s(x):
    a = 0
    while x > 0:
        a += (x % 10)
        x //= 10
    return a


def Fact(x):
    a = 1
    while x > 1:
        a *= x
        x -= 1
    return a


def Fact1(x):
    b = 0
    for n in range(2, x + 1):
        if p(n) == 1:
            b += 1
    return b


x = 2022
count = 0
while count != 5:
    if (Fact1(x)) % 2 == 1 and (s(x)) % 22 == 0:
        print(x, Fact1(x))
        count += 1
    x -= 1