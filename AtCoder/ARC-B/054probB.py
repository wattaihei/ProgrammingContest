import math

P = float(input())

a = 1.5
x = a *( math.log2(P)+math.log2(math.log(2)/a))
if x > 0:
    y = x + a/math.log(2)
else:
    y = P
print(y)