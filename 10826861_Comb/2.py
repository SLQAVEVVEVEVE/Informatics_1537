from itertools import product
k=0
p = product('бинорx', repeat=4)
for i in p:
    x = ''.join(i)
    if x.count('х')==1:
        k+=1

print(k)