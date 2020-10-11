N, M, S = map(int, input().split())
N = N**2
mod = 100000

dp = [0]*((S+1)*(N+1))
dp[0] = 1
for m in range(1, M+1):
    ndp = dp[:]
    for n in range(N):
        for s in range(S-m+1):
            ndp[(n+1)*(S+1)+s+m] = (ndp[(n+1)*(S+1)+s+m] + dp[n*(S+1)+s]) % mod
    dp = ndp

print(dp[-1])