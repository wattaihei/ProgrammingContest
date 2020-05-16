from operator import itemgetter

N = int(input())
HW = [list(map(int, input().split())) for _ in range(N)]

L = 0
for h, w in HW:
    L = max([L, h, w])

# binary indexed tree
bit = [0 for _ in range(L+1)]

# 1からiまでのうちの最大値
# 立っているビットを下から処理
def query_max(i):
    s = 0
    while i > 0:
        s = max(bit[i], s)
        i -= i & -i
    return s

# i番目の要素をupdate
# 覆ってる区間すべてをみる
def update(i, x):
    M = 0
    while i <= L:
        bit[i] = max(bit[i], x)
        i += i & -i

HW.sort(reverse=True, key=itemgetter(1))
HW.sort(key=itemgetter(0))

dp = [0]*N

for i, (h, w) in enumerate(HW):
    dp[i] = query_max(w-1) + 1
    update(w, dp[i])

print(max(dp))