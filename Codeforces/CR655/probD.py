import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
dp = [[0, 0] for _ in range(N+1)]
for i, a in enumerate(A):
    if i%2 == 0:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1] + a
    else:
        dp[i+1][0] = dp[i][0] + a
        dp[i+1][1] = dp[i][1]

for i in range(N):
    if i%2 == 0:
        tmp = dp[i][0] + (dp[N][1] - dp[i][1])
    else:
        tmp = dp[i][1] + (dp[N][0] - dp[i][0])
    ans = max(ans, tmp)

print(ans)