count = 0
n = 10000001
while count < 5:
    i = 2
    while n % i and i < 10000:
        i += 1
    if i + n//i < 10000:
        print(n, (i+n//i))
        count += 1
    n += 1