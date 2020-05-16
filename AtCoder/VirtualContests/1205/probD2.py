import sys
input = sys.stdin.readline
INF = 10**16

N, M = map(int, input().split())
dp = [[INF for _ in range(N)] for _ in range(N)]
P = []
for _ in range(M):
    a, b, d = map(int, input().split())
    if a == 1:
        P.append((b-1, d))
    elif b == 1:
        P.append((a-1, d))
    else:
        dp[a-1][b-1] = d
        dp[b-1][a-1] = d

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

ans = INF
L = len(P)
for i in range(L-1):
    for j in range(i+1, L):
        ans = min(ans, dp[P[i][0]][P[j][0]] + P[i][1] + P[j][1])

if ans == INF:
    print(-1)
else:
    print(ans)