import sys
input = sys.stdin.readline

mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
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

N, M, K = map(int, input().split())

ans = 0
for a in range(1, min(N,M)+1):
    if N+M-2*a >= K:
        ans = (ans + cmb(N, a) * cmb(M-1, a-1)) % mod
    #print(ans)

ans = ans * g1[N-1] * g1[M] % mod
print(ans)
