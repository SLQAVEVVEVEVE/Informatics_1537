from itertools import product
k=0
p = product('АКРУ', repeat=5)
for i in p:
    x = ''.join(i)
    k += 1
    if x[0] == 'р':
        print(x)
        break
    print(k, x)
print(k)