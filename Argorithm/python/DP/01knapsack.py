# AOJ Course より

N, W = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(W+1)]
# 重さwまで品物nまででで最大になる価値

for n in range(N): # 品物nまでの世界で決めていく
    for w in range(W+1):
        vn, wn = K[n]
        if wn > w: # カバンに入りきらないなら入れられない
            dp[w][n] = dp[w][n-1]
        else: #カバンに入れられる可能性があるなら
            dp[w][n] = max(dp[w][n-1], vn+dp[w-wn][n-1]) #　入れた場合と入れなかった場合で価値の高い方を選ぶ

print(dp[W][N-1])