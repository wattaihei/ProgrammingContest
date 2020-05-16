import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
mod = 10**9+7

# dp[i][0] -> A
# dp[i][1] -> AB
# dp[i][2] -> ABC
dp = [0, 0, 0]
k = 1
for i in range(N):
    if S[i] == "A":
        dp[0] += k
    elif S[i] == "B":
        dp[1] += dp[0]
    elif S[i] == "C":
        dp[2] += dp[1]
    else:
        dp[2] = 3*dp[2] + dp[1]
        dp[1] = 3*dp[1] + dp[0]
        dp[0] = 3*dp[0] + k
        k = k*3%mod
    
    dp[0] %= mod
    dp[1] %= mod
    dp[2] %= mod

print(dp[2])