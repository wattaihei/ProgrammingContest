import sys
input = sys.stdin.readline

N, c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0,c] for _ in range(N+1)]
ans = [0]
for i, (a, b) in enumerate(zip(A, B)):
    dp[i+1][0] = min(dp[i][0]+a, dp[i][1]+a)
    dp[i+1][1] = min(dp[i][0]+b+c, dp[i][1]+b)
    ans.append(min(dp[i+1]))

print(*ans)