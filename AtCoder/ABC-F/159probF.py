import sys
input = sys.stdin.readline

mod = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1
for i, a in enumerate(A):
    dp[i+1][0] = i+2
    for s in range(1, S+1):
        if s-a >= 0:
            dp[i+1][s] = (dp[i][s] + dp[i][s-a]) % mod
        else:
            dp[i+1][s] = dp[i][s]

ans = 0
for r in range(N+1):
    ans = (ans + dp[r][S]) % mod

print(ans)
