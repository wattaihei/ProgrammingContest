from fractions import gcd

A, B = map(int, input().split())
g = gcd(A, B)
print(A*B//g)