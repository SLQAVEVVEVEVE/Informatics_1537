x = 8**5+4**6+2**12-16
a = [0] * 2
while x > 0:
    a[x % 2] += 1
    x //= 2
print(a)