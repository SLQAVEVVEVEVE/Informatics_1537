a = []
for n in range(1, 100):
    s = bin(n)[2:] # перевод в двоичную систему
    s = str(s)
    if n % 2 == 0:
        s = "1" + s + "0"
    else:
        s = "11" + s + "11"
    r = int(s, 2) # перевод в десятичную систему
    if r > 52:
        a.append(r)
print(min(a))