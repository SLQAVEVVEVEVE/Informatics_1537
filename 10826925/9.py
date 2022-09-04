x = 36**7+6**19-18
a = [0] * 6
while x > 0:
    a[x % 6] += 1
    x //= 6
print(a)