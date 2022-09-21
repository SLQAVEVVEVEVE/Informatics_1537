with open('17-3.txt') as f:
    a = [int(x) for x in f]


def t(x):
    s = ''
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    if s.count('36') > 0:
        return 1
    else:
        return 0


def newsys(num, base):
    new_num = ''

    while num > 0:
        new_num = str(num % base) + new_num
        num //= base

    return new_num


mx_107num = -1
for num in a:
    if num % 107 == 0:
        mx_107num = max(mx_107num, num)

count = 0
mn_sum = 100_000
for i in range(len(a) - 1):
    if a[i] > mx_107num or a[i + 1] > mx_107num:
        if t(a[i]) or t(a[i+1]):
            count += 1
            mn_sum = min(mn_sum, a[i] + a[i + 1])

print(count, mn_sum)
#14 11350