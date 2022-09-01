def p(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return p(a - 2, b) + p(a // 2, b)


print(p(28, 10) * p(10, 1))
