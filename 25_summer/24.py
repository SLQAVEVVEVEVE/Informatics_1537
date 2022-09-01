x = (7 ** 48 - 7 ** 4 + 123) * 5 * 8 / 6
a = []
count = 0
while x > 0:
    a.append(x % 7)
    if (x % 7) == 4:
        count += 1
    x //= 7
print( count)
