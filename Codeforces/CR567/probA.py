X, Y, Z = map(int, input().split())

a = (X+Y)//Z
n = X//Z + Y//Z
if a == n:
    b = 0
else:
    b = min(Z-X%Z, Z-Y%Z)
print(a,b)