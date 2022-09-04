for a in range(100, 0, -1):
    k = 1
    for x in range(1, 1000):
        k*=((a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 18 != 0))))
        if k==0: break
    if k == 1:
        print(a)
        break