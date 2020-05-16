import sys
input = sys.stdin.readline

N, P = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()

dp1 = [[[0, 0] for _ in range(P+1)] for _ in range(N+1)]

for n in range(N):
    a, b = AB[n]
    for p in range(1, P+1):
        dp1[n+1][p][:] = dp1[n][p][:]
        if p >= a:
            dp1[n+1][p][0] = max(dp1[n+1][p][0], dp1[n][p-a][0]+b)
            dp1[n+1][p][1] = max(dp1[n+1][p][1], dp1[n][p-a][1]+b)
        dp1[n+1][p][1] = max(dp1[n+1][p][1], dp1[n][p][0]+b)

# dp2 = [[0]*(P+1) for _ in range(N+1)]

# for n in reversed(range(N)):
#     a, b = AB[n]
#     for p in range(1, P+1):
#         dp2[n][p] = max(dp2[n+1][p], dp2[n][p-1])
#         if p >= a:
#             dp2[n][p] = max(dp2[n][p], dp2[n+1][p-a]+b)

ans = dp1[N][P][1]
print(ans)