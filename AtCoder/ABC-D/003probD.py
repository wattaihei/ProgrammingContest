import sys
input = sys.stdin.readline

# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 1000 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

limit = D+L
dp = [[0]*Y for _ in range(X)]

for r in range(X):
    for c in range(Y):
        dp[r][c] = cmb((r+1)*(c+1), limit)
        for rk in range(r+1):
            for ck in range(c+1):
                if rk == 0 and ck == 0: continue
                dp[r][c] -= dp[r-rk][c-ck] * (rk+1) * (ck+1)
                dp[r][c] %= mod

ans = (R-X+1)*(C-Y+1)*cmb(limit, D)*dp[X-1][Y-1] % mod
print(ans)