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
A = list(map(int, input().split()))

S = sum(A)
Buckets = prime(S).keys()

if not Buckets:
    print(-1)
else:
    ans = 10**15
    for bucket in Buckets:
        tmp = 0
        now_have = 0
        for a in A:
            now_have += a
            if now_have == bucket:
                now_have = 0
            tmp += min(now_have, bucket-now_have)
        ans = min(ans, tmp)
    print(ans)