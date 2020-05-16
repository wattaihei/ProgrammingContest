# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 10**6 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N, K = map(int, input().split())
if K >= N-1:
    ans = cmb(2*N-1, N)
else:
    ans = 0
    a = K
    while a >= 0:
        ans += cmb(N, a) * cmb(N-1, a) % mod
        ans %= mod
        a -= 1

print(ans)