from fractions import math

N = int(input())

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

Factor = {}
for n in range(2, N+1):
    ns = prime(n)
    for k, v in ns.items():
        if not k in Factor.keys():
            Factor[k] = v
        else:
            Factor[k] += v

c74 = 0
c24 = 0
c14 = 0
c4 = 0
c2 = 0
for num, co in Factor.items():
    if co >= 74:
        c74 += 1
    if co >= 24:
        c24 += 1
    if co >= 14:
        c14 += 1
    if co >= 4:
        c4 += 1
    if co >= 2:
        c2 += 1

ans = c74 + c24*(c2-1) + c14*(c4-1) + c4*(c4-1)*(c2-2)//2
print(ans)

