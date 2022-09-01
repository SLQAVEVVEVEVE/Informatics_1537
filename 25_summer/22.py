for x in range(0, 1000):
    y = 5 ** 2026 + 7 * 5 ** 1013 + 107 - x
    a = [0] * 6
    while y > 0:
        a[y % 6] += 1
        y //= 6
    if a[5] - a[0] == 28:
        print(x)
