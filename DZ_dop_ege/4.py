for x in range(1, 1000):
    s = [0] * 4
    m = 0
    a = 64 ** 11 - 4 ** 10 + 96 - x
    while a > 0:
        s[a % 4] += 1
        a //= 4

    m = s[1] + s[2] * 2 + s[3] * 3
    if m == 71:
        print(x)
#16
