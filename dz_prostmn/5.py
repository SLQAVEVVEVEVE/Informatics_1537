# создадим список простых чисел до 365875
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for i in range(31, 365875):
    j = 0
    f = True
    while p[j] * p[j] <= i and f:
        if i % p[j] == 0:
            f = False
        j += 1
    if f:
        p.append(i)

ans = []
d = 100  # разница между делителями
# найдём простое число ближайщее к корню нижней границы диапазона
j = 0
while p[j] * p[j] < 309829:
    j += 1
j -= 1
for x in range(309829, 365875):
    i = j
    while p[i] * p[i] < x:
        if x % p[i] == 0 and x // p[i] in p:
            if x // p[i] - p[i] < d:
                d = x // p[i] - p[i]
                ans = [(p[i], x // p[i])]
            elif x // p[i] - p[i] == d:
                ans.append((p[i], x // p[i]))
        i += 1
for x in ans:
    print(x)