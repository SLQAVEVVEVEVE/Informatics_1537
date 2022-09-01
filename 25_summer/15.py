for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        k *= ((A % 25 == 0) * ((x % 24 == 0) * (x % 75 == 0) <= (x % A == 0)))
    if k == 1:
        print(A)
