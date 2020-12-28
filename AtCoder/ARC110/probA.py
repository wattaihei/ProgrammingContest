import sys
input = sys.stdin.readline
import math

N = int(input())

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

dic = {}
for a in range(N, 1, -1):
    fac = prime(a)
    for k, c in fac.items():
        if k in dic:
            dic[k] = max(dic[k], c)
        else:
            dic[k] = c

ans = 1
for k, c in dic.items():
    ans *= k**c
print(ans+1)