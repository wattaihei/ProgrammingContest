
mod = 998244353 #出力の制限
# コンビネーション
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

N, A, B, K = map(int, input().split())

ans = 0
for n in range(N+1):
    m = (K-n*A)//B
    if (K-n*A)%B == 0 and 0 <= m <= N:
        ans += cmb(N, m)*cmb(N, n) % mod
        ans %= mod
print(ans)