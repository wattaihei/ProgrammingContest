import sys
input = sys.stdin.readline

mod = 10**9+7
N = int(input())
A = list(map(int, input().split()))

NN = 4*10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

P = [0, 1]
for k in range(2, N+1):
    P.append(inverse[k]+P[-1])

ans = 0
for i, a in enumerate(A):
    ans += (P[i+1]+P[N-i]-1) * g1[N] * a % mod
    ans %= mod

print(ans)