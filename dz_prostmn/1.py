a = [36, 12540, 1920000]
for i in a:
    count = 0
    for d in range(1, i+1):
        if i % d == 0:
            count += 1
    print(count)
