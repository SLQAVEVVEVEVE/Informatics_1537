a = []
for x1 in range(0, 10**2):
    for x2 in range(0, 10):
        s = '12' + str(x1) + '4' + str(x2) + '65'
        if int(s) > 10 ** 8:
            break
        if int(s) % 161 == 0:
            a.append([int(s), int(s) // 161])
        s='12'+'00'+'4'+str(x2)
for x2 in range(0, 10):
    s = '12'+'4' + str(x2) + '65'
    if int(s) % 161 == 0 and int(s) < 10 ** 8:
        a.append([int(s), int(s) // 161])
    s = '12' + '00' + '4' + str(x2)+'65'
    if int(s) % 161 == 0 and int(s) < 10 ** 8:
        a.append([int(s), int(s) // 161])
a.sort()
for i in range(len(a)):
    print(*a[i])
