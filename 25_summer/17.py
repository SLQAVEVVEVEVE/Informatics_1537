k = 0
from itertools import product

p = product('01234567', repeat=5)
for i in p:
    x = ''.join(i)
    if x[0] != '0' and x.count('6') == 1 and x.count('61') == 0 and x.count('63') == 0 and x.count('65') == 0 \
            and x.count('67') == 0 and x.count('16') == 0 and x.count('36') == 0 \
            and x.count('56') == 0 and x.count('76') == 0:
        k += 1
        print(x)
print(k)
