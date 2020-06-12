import sys
input = sys.stdin.readline
INF = 10**18

N = int(input())
S = list(input().rstrip())
C = list(map(int, input().split()))
D = list(map(int, input().split()))

dp = [[INF]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
for i, (s, c, d) in enumerate(zip(S, C, D)):
    for j in range(N):
        if s == "(":
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
            if j > 0:
                dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j]+c)
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+d)
        else:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+c)
            if j > 0:
                dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+d)

print(dp[N][0])