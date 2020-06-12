import sys
input = sys.stdin.readline
import math

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
        if num > n:
            break
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor

A = prime(N)
a1 = 1
a2 = 1
for num, k in A.items():
    if k % 2 == 1:
        a2 *= num
    a1 *= num**(k//2)
print(a1, a2)