import sys
input = sys.stdin.buffer.readline

INF = 10**18

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[INF]*4 for _ in range(N+1)]
    dp[0][3] = 0
    for i, a in enumerate(A):
        dp[i+1][0] = min(dp[i+1][0], min(dp[i][2], dp[i][3])+a)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+a)
        dp[i+1][2] = min(dp[i+1][2], min(dp[i][0], dp[i][1]))
        dp[i+1][3] = min(dp[i+1][3], dp[i][2])
    print(min(dp[-1]))