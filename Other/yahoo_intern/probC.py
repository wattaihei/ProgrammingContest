import sys
input = sys.stdin.readline

N, H, R = map(int, input().split())
HC = [list(map(int, input().split())) for _ in range(N)]

INF = 10**16

dp = [{0: INF} for _ in range(N+1)]
dp[0][0] = 0
for i, (h1, c) in enumerate(HC):
    if not h1 in dp[i+1]:
        dp[i+1] = h1
    for k in range(i):
        h2 = HC[k][0]
        for l, sec in dp[k].items():
            score = sec + c
            key = max(l, h1 - h2)
            if not key in dp[i] or dp[i+1][key] > score:
                dp[i+1][key] = score 

ans = INF
for i in range(N):
    h1 = HC[i][0]
    for key, sec in dp[i].items():
        if key > H - h1:
            key = H - h1
        ans = min(ans, key*R + sec)

print(ans)