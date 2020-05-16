import sys
input = sys.stdin.readline

mod = 10**9+7

P, K = map(int, input().split())

dp = [1, 0]

for _ in range(K):
    dp1 = dp[:]
    dp[0] = ((P+1)*dp1[0] + 2*dp1[1]) % mod
    dp[1] = (dp1[0] + 2*dp1[1])*(P-1) % mod

print(dp[0])