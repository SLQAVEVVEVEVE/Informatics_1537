for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            k *= ((x + y <= 22) or (y <= x - 6) or (y >= A))
            if k == 0:
                break
    if k == 1:
        print(A)
