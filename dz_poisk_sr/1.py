deliteli = (10, 12, 14, 16, 18)

count = 0
i = 320_401

while count < 5:
    right = True
    for num in deliteli:
        if i % num != 0:
            right = False
            break
    if right:
        print(i, i // deliteli[-1])
        count += 1
    i += 1
