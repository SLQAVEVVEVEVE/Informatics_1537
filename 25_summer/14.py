for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        k *= (((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80))
    if k == 1:
        print(A)
