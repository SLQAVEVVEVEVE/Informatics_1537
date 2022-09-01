def p(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return p(a - 8, b) + p(a // 2, b)


print(p(102, 43) * p(43, 5))
