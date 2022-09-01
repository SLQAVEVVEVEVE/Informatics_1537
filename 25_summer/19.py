k = 0
from itertools import product

p = product('ГЕКЭ023', repeat=5)
for i in p:
    x = ''.join(i)
    k += 1
    if (x[0] == '0' or x[0] == '2' or x[0] == '3') and x.count('ГГ') == 0 and x.count('ЕЕ') == 0 and \
            x.count('КК') == 0 and x.count('ЭЭ') == 0 and x.count('00') == 0 and x.count('22') == 0 and x.count('33') == 0:
        print(x, k)
        break
