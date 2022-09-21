with open('17-1.txt') as f:
    a = [int(x) for x in f]

m = 0
s = []
b = []
for i in range(len(a) - 1):
    if a[i] > a[i + 1] and a[i] > a[i - 1]:
        m+=1
        s.append(i + 1)

for j in range(len(s)-1):
    b.append(abs(s[j] - s[j+1]))

print(m, min(b))
#3316 2