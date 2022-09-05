def product(num):
    res = 1
    for i in num:
        res *= i
    return res


p1 = 0
p2 = 0

for m in range(1, 1000):
    a = []
    b = []
    s = str(m)
    x = [int(a) for a in s]
    for i in x:
        if int(i) % 2 == 0 and int(i) != 0:
            a.append(i)
            p1 = product(a) * 2
        if int(i) % 2 != 0:
            b.append(i)
            p2 = product(b) * 1
    r = abs(p1 - p2)
    if r == 29:
        print(m)
