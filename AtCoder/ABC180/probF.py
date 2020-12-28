import sys
input = sys.stdin.buffer.readline

mod = 10**9+7

N, M, L = map(int, input().split())

dp = [[[0]*(N+1) for _ in range(M+2)] for _ in range(L+2)]
dp[1][0][0] = 1
dp[2][1][2] = 1
dp[2][2][0] = 1 
for l in range(2, L):
    for m in range(M+1):
        for k in range(N+1):
            if 0 <= k-1 and m+1 <= M:
                dp[l+1][m+1][k-1] = (dp[l+1][m+1][k-1] + dp[l][m][k] * k) % mod
            if 0 <= k-2 and m+2 <= M:
                dp[l+1][m+2][k-2] = (dp[l+1][m+2][k-2] + dp[l][m][k] * k*(k-1)//2) % mod

