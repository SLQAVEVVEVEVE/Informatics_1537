def p(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return 0
        d += 1
    return 1


def prost_divisors(numb):
    global is_simple
    a = []
    for i in range(numb - 1, 1, -1):
        if numb % i == 0 and p(i):
            a.append(i)
    return a

i=960001
count=0
for l in prost_divisors(i):
    a=prost_divisors(i)
    for j in a:
        while count < 5:
            for x in a:
                if i % x == 0:

            i += 1




