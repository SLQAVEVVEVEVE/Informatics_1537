for n in range(4, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    s = s[0:len(s)-1]
    s += s[1] * 2
    r = int(s, 2)  # перевод в десятичную систему
    if r > 92:
        print(n)
        break