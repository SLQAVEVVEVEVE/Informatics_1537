for num in range(125256, 125331):
    d = []
    for j in range(1, int(num**0.5) + 1):
        if num % j == 0:
            if j % 2 == 0:
                d.append(j)
            if num//j % 2 == 0 and num//j != j:
                d.append(num//j)
    if len(d) == 6:
        d.sort()
        print(d[0], d[1], d[2], d[3], d[4], d[5])