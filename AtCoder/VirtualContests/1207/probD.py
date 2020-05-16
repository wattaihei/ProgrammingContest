import sys
input = sys.stdin.readline

N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
w1 = WV[0][0]

sortedV = []
for _, v in WV:
    sortedV.append(v)
sortedV.sort(reverse=True)

ans = 0
# n個とる
for n in range(1, N+1):
    if (w1+3)*n < W:
        s = 0
        for i in range(n):
            s += sortedV[i]
        ans = max(ans, s)
    elif W < w1*n:
        break
    else:
        limit_W = W - w1*n
        dp = [[0]*(limit_W+1) for _ in range(N+1)]
        for i in range(N):
            nw, nv = WV[i]
            for w in range(limit_W+1):
                if w-(nw-w1) < 0:
                    dp[i+1][w] = dp[i][w]
                else:
                    dp[i+1][w] = max(dp[i][w], dp[i][w-(nw-w1)]+nv)
        ans = max(ans, dp[N][limit_W])

print(ans)