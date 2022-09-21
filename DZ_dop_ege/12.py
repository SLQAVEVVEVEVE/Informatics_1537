with open("17-2.txt") as f:
    a = [int(x) for x in f]


def newsys(num, base):
    new_num = ''

    while num > 0:
        new_num = str(num % base) + new_num
        num //= base

    return new_num


m = 0
maxi = -1
b = []
for i in range(len(a) - 1):
    k = str(bin(a[i]))
    l = newsys(a[i], 5)
    if k[-4:] == '1001' and l[-2:] == '11':
        m += a[i]
        if a[i] > maxi:
            maxi = a[i]

print(maxi, m)
#6681 23686