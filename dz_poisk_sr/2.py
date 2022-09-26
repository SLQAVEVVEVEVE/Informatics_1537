a = []
s = '126789'
if int(s) % 39 == 0 and int(s) < 10 ** 8:
    a.append([int(s), int(s) // 39])
for x in range(0, 10 ** 10):
    s = '12' + str(x) + '6789'
    if int(s) > 10 ** 8:
        break
    if int(s) % 39 == 0:
        a.append([int(s), int(s) // 39])

a.sort()
for i in range(len(a)):
    print(*a[i])
