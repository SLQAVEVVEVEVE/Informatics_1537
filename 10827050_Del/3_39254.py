count = 0
i = 500000001
while count < 5:
    dell = 1
    countDel = 0
    for j in range(2, (i//2) + 1):
        if i % j == 0:
            countDel += 1
            dell *= j
            if dell > i:
                break
            elif countDel == 5:
                print(dell, i)
                count += 1
                break
    i += 1