# コンビネーション
mod = 998244353
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 10**4 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
a = 0
b = 0
for i in range(N):
    if A[i-1] == A[i]:
        a += 1
    else:
        b += 1

ans = 0
for n in range(1, b+1):
    for m in range(min(n, b-n+1)):
        ans += pow(K-2, b-n-m, mod) * cmb(b, n) % mod * cmb(b-n, m) % mod
    ans %= mod

ans = ans * pow(K, a, mod) % mod
print(ans)