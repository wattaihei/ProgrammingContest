mod = 998244353

def cmb(n, r, mod=mod):
    if ( r<0 or r>n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 5*10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


N, M = map(int, input().split())

C = (pow(2, N-3, mod) ) if N >= 3 else 1

ans = 0
for k in range(N-1, M+1):
    if k == 2:
        p = 1
    else:
        p = cmb(k-2, N-3)
    ans = (ans + (k-1) * p * C) % mod
if N == 2:
    ans = 0
print(ans)