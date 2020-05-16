X = int(input())

a = X//11*2
b = X%11
if b == 0:
    a += 0
elif b <= 6:
    a += 1
else:
    a += 2
print(a)