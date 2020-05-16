H, W, A, B = map(int, input().split())

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = int(10**9+7) #出力の制限
NN = 10**6 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


ans = 0
for i in range(W-B):
    a = cmb(H-A+B-1+i, B+i, mod)* cmb(W-B+A-2-i, A-1, mod)
    ans += a
    ans %= mod
print(ans)