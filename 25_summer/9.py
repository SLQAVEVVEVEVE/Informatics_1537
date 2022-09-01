import math


def p(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    if a == 20:
        return 0
    return p(a - 1, b) + p(a - 2, b) + p(math.sqrt(a), b)


print(p(27, 18) * p(18, 6))
