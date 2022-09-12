from itertools import product
k=0
p = product('аежйл', repeat=5)
for i in p:
    x = ''.join(i)
    if x.count('й')<=1 and x[0]!='й' and x[4]!='й' and x.count('йе')==0 and x.count('ей')==0:
        k += 1
    print(k, x)
#1456