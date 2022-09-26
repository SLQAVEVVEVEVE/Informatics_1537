i = 320401
a = [10, 12, 14, 16, 18]
count = 0
b=0
while count < 5:
    for x in a:
        if i % x == 0:
            b+=1
        if b==5:
            print(i, i//x)
            count+=1
            break
    b=0
    i+=1

