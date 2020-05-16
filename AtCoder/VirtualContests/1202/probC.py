from fractions import gcd

A, B = map(int, input().split())
C = gcd(A, B)
print(B-C)