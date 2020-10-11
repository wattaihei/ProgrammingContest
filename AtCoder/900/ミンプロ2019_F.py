mod = 998244353
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


import sys
input = sys.stdin.readline

S = list(input().rstrip())

L = len(S)
dp = [[0]*(L+1) for _ in range(L+1)]
dp[0][0] = 1
rmax = [0, 0]
rmin = [0, 0]
rsum = 0
for i, s in enumerate(S):
    p = int(s)
    rsum += p
    if p == 0:
        rmin[1] += 2
    elif p == 1:
        rmax[1] += 1
        rmin[1] += 1
    else:
        rmax[1] += 2
    if rmax[1] > 0:
        rmax[0] += 1
        rmax[1] -= 1
    if rmin[1] > 0:
        rmin[0] += 1
        rmin[1] -= 1
    for j in range(i+1):
        if rmax[0] >= j+1:
            dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % mod
        if rmin[0] >= (i+1) - j:
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod


ans = 0
for j in range(L+1):
    ans = (ans + dp[L][j] * cmb(L, rsum-j)) % mod
print(ans)