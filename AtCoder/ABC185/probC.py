import sys
input = sys.stdin.readline

L = int(input())
P = 12

dp = [[0]*(L+1) for _ in range(P+1)]
dp[0][0] = 1
for i in range(P):
    for s in range(L):
        for l in range(1, L+1):
            if s+l <= L:
                dp[i+1][s+l] += dp[i][s]

print(dp[P][L])