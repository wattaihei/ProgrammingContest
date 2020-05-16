import sys
input = sys.stdin.readline

INF = 10**17

N = int(input())
A = list(map(int, input().split()))

dp = [[-INF]*3 for _ in range(N)]

for i, a in enumerate(A):
    if i == 0:
        dp[i][2] = a
    elif i == 1:
        dp[i][0] = max(a, dp[i-1][1])
    elif i == 2:
        dp[i][1] = a
        dp[i][2] = dp[0][2] + a
    elif (i+1)%2 == 0:
        dp[i][0] = max(dp[i-3][2], dp[i-2][0]) + a
    else:
        dp[i][1] = max([dp[i-4][2], dp[i-3][0], dp[i-2][1]]) + a
        dp[i][2] = dp[i-2][2] + a

if N%2 == 0:
    ans = dp[N-1][0]
    if N > 1:
        ans = max(ans, dp[N-2][2])
else:
    ans = dp[N-1][1]
    if N > 1:
        ans = max(ans, dp[N-2][0])
    if N > 2:
        ans = max(ans, dp[N-3][2])
    # tmp = 0
    # for i in reversed(range(N)):
    #     if i%2 == 0 and i >= 2:
    #         tmp += A[i]
    #         ans = max(ans, dp[i-2][1]+tmp)

print(ans)