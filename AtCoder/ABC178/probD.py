# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( n<0 or r<0 or r>n ):
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

N = int(input())

ans = 0
for n in range(1, N//3+1):
    ans = (ans + cmb(N-2*n-1, n-1)) % mod

print(ans)