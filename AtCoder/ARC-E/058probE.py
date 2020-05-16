N, X, Y, Z = map(int, input().split())
mod = 10**9+7

def power_func(a,n,p):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %p
        if bi[i]=="1":
            res=(res*a) %p
    return res

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

C = [0]*(N+1)
for lx in range(1, X+1):
    for ly in range(1, Y+1):
        for lz in range(1, Z+1):
            L = lx + ly + lz
            if L > N:
                continue
            s = cmb(X-1, lx-1)
            s = s * cmb(Y-1, ly-1) % mod
            s = s * cmb(Z-1, lz-1) % mod
            C[L] += s
            C[L] %= mod
