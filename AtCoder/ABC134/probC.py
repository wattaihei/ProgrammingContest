import sys
input = sys.stdin.buffer.readline

INF = 10**18

N = int(input())
A = [int(input()) for _ in range(N)]


dp = [-INF]*(N+1)
for i, a in enumerate(A):
    dp[i+1] = max(dp[i], a)

dp2 = [-INF]*(N+1)
for i in reversed(range(N)):
    a = A[i]
    dp2[i] = max(dp2[i+1], a)


for i in range(N):
    print(max(dp[i], dp2[i+1]))