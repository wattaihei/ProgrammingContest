# 蟻本p64より
# O(NlogN)で最長増加部分列のながさを出す


from bisect import bisect_left # 二部探索

N = int(input()) # 主列のながさ
A = list(map(int, input().split()))

INF = max(A) + 1 # どれよりも大きい数を用意(dpを単調増加にするため)
dp = [INF for _ in range(N)] # dp[i]=長さi+1であるような増加部分列における最終要素の最小値

for a in A:
    k = bisect_left(dp, a) # すでに入っているものに対してできる限り長くなるような位置を探す
    dp[k] = a # 更新

ans = N
for i, d in enumerate(dp):
    if d == INF:
        ans = i
        break
print(ans)