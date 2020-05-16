import sys
input = sys.stdin.readline

import math

Q = int(input())
X = [int(input()) for _ in range(Q)]

def prime(n):
    factor = {}
    for num in [2, 3, 5]:
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


for N in X:
    factor = prime(N)
    ans = 0
    for num, c in factor.items():
        if num == 2:
            ans += c
        elif num == 3:
            ans += 2*c
        elif num == 5:
            ans += 3*c
        else:
            ans = -1
            break
    print(ans)