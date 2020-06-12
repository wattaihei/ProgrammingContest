import sys
input = sys.stdin.readline

mod = 998244353

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [1]
for i, a in enumerate(A):
    ndp = [0]*(i+2)
    ndp[0] = dp[0]*(a-1) % mod
    ndp[i+1] = 1
    for j in range(1, i+1):
        ndp[j] = (dp[j]*(a-1) + dp[j-1]) % mod
    dp = ndp

for b in B:
    print(dp[b])