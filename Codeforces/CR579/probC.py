from fractions import gcd
import math

N = int(input())
A = list(map(int, input().split()))

G = A[0]
for a in A:
    G = gcd(a, G)

def prime2(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor

B = prime2(G)

ans = 1
for k, v in B.items():
    ans *= (v+1)
print(ans)