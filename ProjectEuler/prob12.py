import math

def prime(n):
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

limit = 500

n = 1
while True:
    a = n*(n+1)//2
    factor = prime(a)
    K = 1
    for c in factor.values():
        K *= (c+1)
    if K > limit:
        break
    n += 1
print(a)
