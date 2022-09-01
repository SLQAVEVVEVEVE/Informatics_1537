for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            k *= (2 * y + x != 70) or (x < y) or (A < x)
            if k == 0:
                break
    if k == 1:
        print(A)
