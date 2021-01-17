import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().rstrip().split())
mod = 10**9+7

dp = [[[0]*(K+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(i+1):
        for k in range(K+1):
            if j > 0 and k+2*(j-1) <= K:
                dp[i+1][j-1][k+2*(j-1)] += (j*j)*dp[i][j][k]
                dp[i+1][j-1][k+2*(j-1)] %= mod
            if k+2*j <= K:
                dp[i+1][j][k+2*j] += (2*j+1)*dp[i][j][k]
                dp[i+1][j][k+2*j] %= mod
            if k+2*(j+1) <= K:
                dp[i+1][j+1][k+2*(j+1)] += dp[i][j][k]
                dp[i+1][j+1][k+2*(j+1)] %= mod

print(dp[N][0][K])