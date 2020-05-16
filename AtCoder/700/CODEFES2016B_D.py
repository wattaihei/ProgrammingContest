N = int(input())
A = [int(input()) for _ in range(N)]
"""
this is wrong answer!!
dp = [[[0, 0], [0, 0]] for _ in range(N)]
dp[0][0][0] = 2
dp[0][1][0] = 2
dp[0][0][1] = A[0]-1
dp[0][1][1] = A[0]-1
for i in range(1, N):
    for l in [0, 1]:
        remove = A[i] // dp[i-1][l][0]
        if A[i] % dp[i-1][l][0] == 0:
            if dp[i][1][1] < dp[i-1][l][1] + remove - 1:
                dp[i][1][1] = dp[i-1][l][1] + remove - 1
                dp[i][1][0] = dp[i-1][l][0] + 1
            if dp[i][0][1] < dp[i-1][l][1] + remove - 2:
                dp[i][0][1] = dp[i-1][l][1] + remove - 2
                dp[i][0][0] = dp[i-1][l][0]
        else:
            if dp[i][1][1] < dp[i-1][l][1] + remove:
                dp[i][1][1] = dp[i-1][l][1] + remove
                dp[i][1][0] = dp[i-1][l][0]
                dp[i][0][1] = dp[i][1][1]
                dp[i][0][0] = dp[i][1][0]
ans = max(dp[N-1][0][1], dp[N-1][1][1])
print(ans)
"""

p = 2
ans = A[0]-1
for i in range(1, N):
    if p == A[i]:
        p += 1
    else:
        if A[i] % p == 0:
            ans += A[i]//p-1
        else:
            ans += A[i]//p
print(ans)
