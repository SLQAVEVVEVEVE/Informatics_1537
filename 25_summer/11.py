for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        k *= (((x % 6 == 0) <= (x % 14 != 0)) or (x + A >= 70) and (A % 20 == 0))
    if k == 1:
        print(A)
