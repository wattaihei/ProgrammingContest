
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 10**6 + 7 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


def solve1(N):
    if N == 2:
        return 1
    ans = 0
    for k in range(1, N):
        # (N-1)-(k-1)-1
        # (N-2)-(k-1)
        # score = cmb(k, N-1-k)*2*(N-1-k) + cmb(k, N-2-k)*(N-2-k)
        score = cmb(k-2, N-k-1)*2*(N-k-1) + cmb(k-2, N-2-k)*(N-2-k)
        score += cmb(k-2, N-k-1)*2 + cmb(k-2, N-k-2)*2
        score = k* score * g1[k-1] * g1[N-1-k] % mod
        ans = (ans + score) % mod
        # ans = (ans + k * cmb(k-1, N-1-k) * g1[k-1] * g1[N-1-k] * min(k, N-k+1)) % mod
    return ans

def solve2(N):
    from itertools import permutations
    ans = 0
    for P in permutations(range(N-1)):
        bit = 0
        score = 0
        for i, p in enumerate(P):
            bit |= (1<<p) | (1<<(p+1))
            if bit == (1<<N)-1:
                score = i+1
                break
        ans += score
    return ans

N = int(input())
print(solve1(N))
# print(solve2(N))