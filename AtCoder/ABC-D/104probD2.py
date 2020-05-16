S = list(input())
N = len(S)
mod = int(1E9+7)

dp = [[0, 0, 0, 0] for _ in range(N+1)]

dp[N][3] = 1
for i in range(N-1, -1, -1):
    m = 3 if S[i] == '?' else 1
    dp[i][3] = m*dp[i+1][3]
    if S[i] == '?':
        dp[i][0] = m*dp[i+1][0] + dp[i+1][1]
        dp[i][1] = m*dp[i+1][1] + dp[i+1][2]
        dp[i][2] = m*dp[i+1][2] + dp[i+1][3]
    if S[i] == 'A':
        dp[i][0] = m*dp[i+1][0] + dp[i+1][1]
        dp[i][1] = m*dp[i+1][1]
        dp[i][2] = m*dp[i+1][2]
    if S[i] == 'B':
        dp[i][0] = m*dp[i+1][0]
        dp[i][1] = m*dp[i+1][1] + dp[i+1][2]
        dp[i][2] = m*dp[i+1][2]
    if S[i] == 'C':
        dp[i][0] = m*dp[i+1][0]
        dp[i][1] = m*dp[i+1][1]
        dp[i][2] = m*dp[i+1][2] + dp[i+1][3]
    dp[i][0] %= mod
    dp[i][1] %= mod
    dp[i][2] %= mod
    dp[i][3] %= mod
    
print(dp[0][0])