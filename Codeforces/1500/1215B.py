N = int(input())
A = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]
for i in range(N):
    if i == 0:
        if A[i] > 0:
            dp[0][0] = 1
        else:
            dp[0][1] = 1
    else:
        if A[i] > 0:
            dp[i][0] = dp[i-1][0] + 1
            dp[i][1] = dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + 1
a, b = 0, 0
for i in range(N):
    a += dp[i][0]
    b += dp[i][1]
print(b, a)