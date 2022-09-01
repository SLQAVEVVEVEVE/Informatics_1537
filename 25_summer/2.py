import math

maxi = 0
for i in range(0, 300000000+1):
    num = 0
    if round(math.sqrt(i)) == math.sqrt(i):
        maxi = 1
        for j in range(2, round(math.sqrt(i) - 1)):
            if i % j == 0:
                if maxi == 1: maxi = i // j
                num += 2
        if num == 2: print(i, maxi)
