import sys
input = sys.stdin.readline

INF = 10**18

N, K = map(int, input().split())
A = [0] + list(map(int, input().split())) + [0]

dp = [[INF]*(K+1) for _ in range(N+2)]
dp[0][0] = 0
for i in range(1, N+2):
    for k in range(K+1):
        tmp = INF
        for j in range(max(0, i-k-1), i):
            tmp = min(tmp, dp[j][k-(i-j-1)] + max(0, A[i]-A[j]))
        dp[i][k] = tmp

print(min(dp[-1]))