from fractions import gcd
import math

N = int(input())
ans = 10**16
for n in range(1, int(math.sqrt(N))+2):
    if N%n == 0:
        b = N//n
        if gcd(b, n) == 1 and max(b, n) < ans:
            ans = max(b, n)
            a1 = b
            a2 = n
print(a2, a1)