import sys
input = sys.stdin.readline

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N+1)] for _ in range(T+1)]
# 重さwまで品物nまででで最大になる価値

prev = [[0 for _ in range(N+1)] for _ in range(T+1)]

for n in range(N): # 品物nまでの世界で決めていく
    a, b = AB[n]
    for w in range(T):
        if a > w: # カバンに入りきらないなら入れられない
            dp[w][n+1] = dp[w][n]
            prev[w][n+1] = w
        else: #カバンに入れられる可能性があるなら
            if b+dp[w-a][n] >= dp[w][n]:
                dp[w][n+1] = dp[w-a][n] + b
                prev[w][n+1] = w - a
            else:
                dp[w][n+1] = dp[w][n]
                prev[w][n+1] = w

ans = dp[T-1][N]
used = [False]*N
c = T-1
for i in reversed(range(N)):
    if prev[c][i+1] == c - AB[i][0]:
        used[i] = True
    c = prev[c][i+1]

p = 0
for i in range(N):
    if not used[i] and AB[i][1] > p:
        p = AB[i][1]

print(ans+p)