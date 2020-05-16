N, A = map(int, input().split())
X = list(map(int, input().split()))
L = max(X)
L = max(L, A)

dp = [[[0 for _ in range((N+1)*(L+1))] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for j in range(1, N+1):
    for k in range(N+1):
        for s in range((N+1)*(L+1)):
            if s < X[j-1]:
                dp[j][k][s] = dp[j-1][k][s]
            if k >= 1 and s >= X[j-1]:
                dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-X[j-1]]
ans = 0
for k in range(1, N+1):
    ans += dp[N][k][k*A]
print(ans)