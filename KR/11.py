for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            k *= ((3 * x + 5 * y < A) or (x >= y) or (y > 8))
            if k==0: break
    if k==1:
        print(A)
