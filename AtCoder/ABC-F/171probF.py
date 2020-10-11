import sys
input = sys.stdin.readline


# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 2*10**6+5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

K = int(input())
S = input().rstrip()
L = len(S)

ans = 0
t25 = 1
t26 = pow(26, K, mod)
inv26 = pow(26, mod-2, mod)
for k in range(K+1):
    ans = (ans + t25 * t26 * cmb(k+L-1, k)) % mod
    t25 = t25 * 25 % mod
    t26 = t26 * inv26 % mod
print(ans)