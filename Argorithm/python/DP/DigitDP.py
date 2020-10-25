# ABC029-D
# N以下1の現れる回数

N = input()
L = len(N)

dp = [[[0, 0] for _ in range(L+1)] for _ in range(L+1)]
# dp[l][k][isless] = 上からl桁目まで読んだ時、1がk個あって、
# isless = 0　なら上からl桁の数が全て一致している
# isless = 1　なら一致せず、どこかの桁が小さい

dp[0][0][0] = 1
# 一番上の桁の上に0があるとみなす

for l in range(L):
    a = int(N[l])
    for isless in [0, 1]:
        for k in range(L):
            for num in range(10):
                # 次の桁が実際のものより小さいならisless = 1で確定
                if num < a:
                    if num == 1:
                        dp[l+1][k+1][1] += dp[l][k][isless]
                    else:
                        dp[l+1][k][1] += dp[l][k][isless] 
                # 次の桁が一致したならそれまでの状態を引き継ぐ
                # 超えてたらislessになっているもののみ通す
                elif num == a or isless:
                    if num == 1:
                        dp[l+1][k+1][isless] += dp[l][k][isless]
                    else:
                        dp[l+1][k][isless] += dp[l][k][isless]
#print(dp)
ans = 0
for k in range(L+1):
    ans += k*(dp[L][k][1] + dp[L][k][0])
print(ans)