import sys
input = sys.stdin.readline
from bisect import bisect_left

mod = 998244353

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]
A.sort(reverse=True)
B = A[::-1]

dp = [[1]]
for i, a in enumerate(A):
    ndp = [0]*(i+2)
    ndp[0] = dp[-1][0]*(a-1) % mod
    ndp[i+1] = 1
    for j in range(1, i+1):
        ndp[j] = (dp[-1][j]*(a-1) + dp[-1][j-1]) % mod
    dp.append(ndp)

C = [1]
for b in B:
    C.append(C[-1]*b%mod)

for l, r, p in Query:
    ans = 0
    for k in range(l, r+1):
        ma = N - bisect_left(B, k)
        if p < len(dp[ma]):
            ans ^= (dp[ma][p] * C[N-ma]) % mod
    print(ans%mod)