import sys
input = sys.stdin.readline
from operator import itemgetter

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=itemgetter(0))

dp = [[0 for _ in range(N+1)] for _ in range(T+1)]
# 重さwまで品物nまででで最大になる価値
C = []

for n in range(N): # 品物nまでの世界で決めていく
    a, b = AB[n]
    for w in range(T):
        if a > w: # カバンに入りきらないなら入れられない
            dp[w][n+1] = dp[w][n]
        else: #カバンに入れられる可能性があるなら
            if b+dp[w-a][n] >= dp[w][n]:
                dp[w][n+1] = dp[w-a][n] + b
            else:
                dp[w][n+1] = dp[w][n]
    C.append(dp[T-1][n]+b)

ans = max(C)
print(ans)