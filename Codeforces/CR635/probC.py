import sys
input = sys.stdin.readline
mod = 998244353

S = list(input().rstrip())
T = list(input().rstrip())

Ls = len(S)
Lt = len(T)
T = T[::-1]

dp = [0]*(Lt+1)
dp[0] = 1
ans = 0
for i, s in enumerate(S):
    dp[0] = dp[0]*2 % mod
    for j in reversed(range(Lt)):
        t = T[j]
        if t == s:
            dp[j+1] = (dp[j+1]+dp[j]) % mod

print(dp[-1])