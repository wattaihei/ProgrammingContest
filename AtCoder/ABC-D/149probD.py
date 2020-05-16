import sys
input = sys.stdin.readline


N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input().rstrip()

dp = [[0, 0, 0] for _ in range(N)]

for i in range(K):
    Q = T[i]
    if Q == "s":
        dp[i][0] = R
    elif Q == "p":
        dp[i][1] = S
    else:
        dp[i][2] = P

for i in range(K, N):
    Q = T[i]
    if Q == "s":
        dp[i][0] = max(dp[i-K][1], dp[i-K][2]) + R
        dp[i][1] = max(dp[i-K][0], dp[i-K][2])
        dp[i][2] = max(dp[i-K][0], dp[i-K][1])
    elif Q == "p":
        dp[i][0] = max(dp[i-K][1], dp[i-K][2])
        dp[i][1] = max(dp[i-K][0], dp[i-K][2]) + S
        dp[i][2] = max(dp[i-K][0], dp[i-K][1])
    else:
        dp[i][0] = max(dp[i-K][1], dp[i-K][2])
        dp[i][1] = max(dp[i-K][0], dp[i-K][2])
        dp[i][2] = max(dp[i-K][0], dp[i-K][1]) + P

ans = 0
for i in range(K):
    ans += max(dp[-1-i])
print(ans)