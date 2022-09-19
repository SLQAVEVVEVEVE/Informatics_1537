import math

number = int(input())
count=0
a=[]
for i in range(2, int(number/2) + 1):  # обычно делитель не будет больше корня
    while number % i == 0:  # while, а не if
        a.append(i)
        count+=1
        number //= i  # убираем множитель из числа

if number != 1:  # но один делитель может быть больше корня
    a.append(number)

print(a)