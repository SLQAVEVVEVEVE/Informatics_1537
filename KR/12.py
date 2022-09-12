for A in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        k *= (((x % A == 0) <= ((x % 54 == 0) or (x % 130 == 0))) and (A > 110))
        if k == 0: break
    if k == 1:
        print(A)
