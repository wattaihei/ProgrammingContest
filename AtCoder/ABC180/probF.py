import sys
input = sys.stdin.buffer.readline

mod = 10**9+7

def perm(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    return g1[n] * g2[n-r] % mod

NN = 10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


N, M, L = map(int, input().split())

inv2 = pow(2, mod-2, mod)

dp = [[0]*(N*2+1) for _ in range(N*2+1)]
dp[0][0] = 1

for l in reversed(range(1, L+1)):
    invl = pow(l, mod-2, mod)
    for k in reversed(range(N)):
        for m in reversed(range(M+1)):
            if l == 1:
                dp[m][k+1] = (dp[m][k+1] + dp[m][k] * (N-k)) % mod
            elif l == 2:
                dp[m+l][k+l] = (dp[m+l][k+l] + dp[m][k] * perm(N-k, l) * inv2) % mod
                dp[m+l-1][k+l] = (dp[m+l-1][k+l] + dp[m][k] * perm(N-k, l) * inv2) % mod
            else:
                dp[m+l][k+l] = (dp[m+l][k+l] + dp[m][k] * perm(N-k, l) * inv2 * invl) % mod
                dp[m+l-1][k+l] = (dp[m+l-1][k+l] + dp[m][k] * perm(N-k, l) * inv2) % mod

    if l == L:
        dp[0][0] = 0

print(dp[M][N])