N = int(input())

dp = [0 for _ in range(N)]

dp[0] = 1

for i in range(1, N):
    dp[i] = dp[i-1] + 4*i

print(dp[-1])
