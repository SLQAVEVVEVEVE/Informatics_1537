k = 0
from itertools import product

p = product('ЛОПРСТ', repeat=9)
for i in p:
    x = ''.join(i)
    if x[0] != 'О' and x[0] != 'О' and x.count('Л') == 1 and x.count('О') == 3 and x.count('П') == 1 and x.count(
            'Р') == 1 and x.count('С') == 1 and x.count('Т') == 2:
        print(x, k)
        k += 1
