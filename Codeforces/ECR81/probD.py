import sys
input = sys.stdin.readline
import math
from fractions import gcd

# 素因数分解、辞書で返すやつ
# mathをimportする
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

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, m in Query:
    g = gcd(a, m)
    m //= g
    primes = prime(m)
    p = m
    for n in primes.keys():
        p = p//n*(n-1)
    print(p)