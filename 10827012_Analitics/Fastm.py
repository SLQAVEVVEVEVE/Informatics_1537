for i in range(300000000, 0, -1):
    x = i
    a = 1
    b = 0
    while x > 0:
        d = x % 9
        a *= d
        if a > 10 or d == 0: # доп проверка, чтобы ускорить алгоритм
            break
        if d < 5:
            b += d
            if b > 9: # доп проверка, чтобы ускорить алгоритм
                break
        x //= 9
    if a == 10 and b == 9:
        print(i)
        break