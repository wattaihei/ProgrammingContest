N, M = map(int, input().split())
mod = 10**9+7
L = max(N, M) + 1

dp = [[1, 1] for _ in range(L+1)]
dp[1][0] = 1
dp[1][1] = 1

for l in range(2, L+1):
    dp[l][0] = (dp[l-1][1] + dp[l-2][1]) % mod
    dp[l][1] = (dp[l-1][0] + dp[l-2][0]) % mod

ans = dp[N][0] + dp[N][1] + dp[M][0] + dp[M][1] - 2
if ans < 0: ans += mod
ans %= mod
print(ans)