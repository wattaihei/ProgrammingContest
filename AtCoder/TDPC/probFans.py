N, K = map(int, input().split())
MOD = 10**9 + 7

dp = [[0, 0] for _ in range(N + 1)]  # dp[stop][isStop] 右端がendの場合の数
dp[0][1] = 1
dp[0][0] = 1
dp[1][0] = 0
dp[1][1] = 1

for end in range(2, N + 1) :
    dp[end][0] = (dp[end - 1][0] + dp[end - 1][1]) % MOD
    if end - K >= 0 :
        dp[end][1] = (dp[end][0] - dp[end - K][0]) % MOD
    else :
        dp[end][1] = dp[end][0]

ans = dp[N][1] % MOD
print(ans)


