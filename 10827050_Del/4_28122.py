for i in range(489421, 489440+1):
    a = []
    for d in range(1, int(i ** 0.5) + 1):
        if i % d == 0:
            a.append(d)
            a.append(i // d)
    if len(a) == 4:
        a.sort()
        print(a[0], a[1], a[2], a[3])