import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

dp = [[0]*5 for _ in range(N+1)]

for i, a in enumerate(A):
    b = a%2 if a > 0 else 2
    dp[i+1][0] = dp[i][0] + a
    dp[i+1][1] = min(dp[i][1], dp[i][0]) + b
    dp[i+1][2] = min([dp[i][2], dp[i][1], dp[i][0]]) + (a+1)%2
    dp[i+1][3] = min([dp[i][3], dp[i][2], dp[i][1], dp[i][0]]) + b
    dp[i+1][4] = min(dp[i]) + a

ans = min([dp[N][4], dp[N][3], dp[N][2]])
print(ans)