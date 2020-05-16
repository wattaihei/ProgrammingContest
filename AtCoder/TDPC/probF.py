N, K = map(int, input().split())
mod = 10**9+7

dp = [[0, 0] for _ in range(N+1)]
dp[0][1] = 1
dp[0][0] = 1
dp[1][1] = 1

for n in range(2, N+1):
    dp[n][0] = (dp[n-1][0] + dp[n-1][1]) % mod
    if n-K < 0:
        dp[n][1] = (dp[n-1][0] + dp[n-1][1]) % mod
    else:
        dp[n][1] = (dp[n-1][0] + dp[n-1][1] - dp[n-K][0]) % mod

print(dp[N][1]%mod)
