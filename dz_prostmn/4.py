def pr(t):
    d = 2
    while d <= int(t ** 0.5):
        if t % i == 0:
            return False
        d += 1
    return True


mini = 10 ** 100
c = 0
sr = 0
for i in range(412567, 473265 + 1):
    a = []
    d = 2
    while d <= int(i ** 0.5):
        if i % d == 0 and pr(d):
            a.append(d)
        d += 1
    if len(a) == 2 and i == a[0] * a[1]:
        c += 1
        sr = sum(a) // len(a)
print(c, sr)
