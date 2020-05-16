import sys
input = sys.stdin.readline
INF = 10**14

N = int(input())
A = list(map(int, input().split()))

odds = (N+1)//2
evens = N//2
for a in A:
    if a == 0: continue
    if a % 2 == 0:
        evens -= 1
    else:
        odds -= 1

dp = [[[[INF, INF] for _ in range(odds+1)] for _ in range(evens+1)] for _ in range(N+1)]
dp[0][0][0][0] = 0
dp[0][0][0][1] = 0
for i, a in enumerate(A):
    for j in range(evens+1):
        for k in range(odds+1):
            if a == 0:
                if k != odds:
                    dp[i+1][j][k+1][1] = min(dp[i][j][k][0]+1, dp[i][j][k][1])
                if j != evens:
                    dp[i+1][j+1][k][0] = min(dp[i][j][k][1]+1, dp[i][j][k][0])
            elif a%2 == 0:
                dp[i+1][j][k][0] = min(dp[i][j][k][1]+1, dp[i][j][k][0])
            else:
                dp[i+1][j][k][1] = min(dp[i][j][k][0]+1, dp[i][j][k][1])


print(min(dp[N][evens][odds]))