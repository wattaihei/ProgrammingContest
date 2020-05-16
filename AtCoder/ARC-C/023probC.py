mod = 10**9+7

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m=mod):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    ret = 1
    for k in range(1, r+1):
        ret = ret * (n-k+1) * mod_inv(k) % mod
    return ret
        

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
pre = -1
c = 0
ans = 1
for a in A:
    if a == -1:
        c += 1
    else:
        if c > 0:
            d = a-pre
            ans = ans * cmb(d+c, c) % mod
        c = 0
        pre = a

print(ans)