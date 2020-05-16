import sys
input = sys.stdin.readline


N = int(input())
A = [int(input()) for _ in range(N)]

mod = 10**9+7

dp = [0]*(N+1)
last_ind = [-1]*(2*10**5+1)

for i, a in enumerate(A):
    ind = last_ind[a]
    if ind == -1 or ind == i-1:
        dp[i+1] = dp[i]
    else:
        dp[i+1] = (dp[i] + dp[ind+1] + 1) % mod
    last_ind[a] = i

print((dp[N]+1)%mod)