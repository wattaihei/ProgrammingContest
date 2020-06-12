import sys
input = sys.stdin.readline
import math

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

N = int(input())
fac = prime(N)
ans = 0
for v in fac.values():
    tmp = 0
    for i in range(1, 10**9):
        if tmp + i <= v:
            tmp += i
            ans += 1
        else:
            break
print(ans)