import sys
input = sys.stdin.readline

mod = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))

inv2 = pow(2, mod-2, mod)
dp = [[0]*(S+1) for _ in range(N+1)]

dp[0][0] = pow(2, N, mod)
for i, a in enumerate(A):
    dp[i+1] = dp[i][:]
    for s in range(S-a+1):
        dp[i+1][s+a] = (dp[i+1][s+a] + dp[i][s] * inv2) % mod

print(dp[N][S])