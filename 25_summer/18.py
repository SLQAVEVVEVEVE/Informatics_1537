k = 0
from itertools import product

p = product('012345678', repeat=5)
for i in p:
    x = ''.join(i)
    if x[0] != '0' and x[0] != '1' and x[0] != '3' and x[0] != '5' and x[0] != '7' and x[4] != '1' and x[4] != '8' and x.count('3') <= 1:
        k += 1
        print(x)
print(k)
