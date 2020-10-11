# 素因数分解、辞書で返すやつ
import math
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

import sys
input = sys.stdin.buffer.readline
N, H = map(int, input().split())
A = list(map(int, input().split()))

if 0 in A:
    D = {}
else:
    D = prime(H)
    for a in A:
        to_del = []
        for n in D.keys():
            r = 0
            while a % n == 0:
                a //= n
                r += 1
            if D[n] > r:
                D[n] -= r
            else:
                to_del.append(n)

        for d in to_del:
            del D[d]

print("YES" if not D else "NO")