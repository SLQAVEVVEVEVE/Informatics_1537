x = 49**6+7**18-21
a = [0] * 7
while x > 0:
    a[x % 7] += 1
    x //= 7
print(a)