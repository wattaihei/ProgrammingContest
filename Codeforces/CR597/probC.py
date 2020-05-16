mod = 10**9+7

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

S = input().rstrip()
N = len(S)

pre = '-1'
ans = 1
A = []
c = 0
for s in S:
    if s == 'm' or s == 'w':
        ans = 0
        break
    if s == 'n':
        if pre == 'n':
            c += 1
        else:
            if c > 1:
                A.append(c)
            c = 1
    elif s == 'u':
        if pre == 'u':
            c += 1
        else:
            if c > 1:
                A.append(c)
            c = 1
    else:
        if c > 1:
            A.append(c)
        c = 0
    pre = s
A.append(c)

if ans == 0:
    print(0)
else:
    for a in A:
        tmp = 1
        n, m = a-1, 1
        while n >= m:
            tmp += cmb(n, m)
            tmp %= mod
            n -= 1
            m += 1
        ans = ans * tmp % mod
    print(ans)