def p(a):
    k = 0
    for i in range(2, a // 2):
        if a % i == 0:
            return 0
    return 1


for i in (2 ** 17, 2 ** 18, 2 ** 19, 2 ** 20):
    for minus in range(1, 6):
        if (i - minus) <= 1048571 and p(i - minus):
            print(i - minus, i)
    for plus in range(1, 6):
        if (i + plus) <= 1048571 and p(i + plus):
            print(i + plus, i)


#131071 131072
#262139 262144
#262147 262144
#524287 524288
#1048571 1048576