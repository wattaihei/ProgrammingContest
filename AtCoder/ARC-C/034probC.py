import math

def prime(n, factor):
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

A, B = map(int, input().split())
mod = 10**9+7

factor = {}
for n in range(B+1, A+1):
    factor = prime(n, factor)
#print(factor)
ans = 1
for v in factor.values():
    ans = ans * (v+1) % mod
print(ans)