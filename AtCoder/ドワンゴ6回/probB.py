import sys
input = sys.stdin.readline

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


N = int(input())
A = list(map(int, input().split()))

NN = [1]
for n in range(1, N+1):
    NN.append(NN[-1]*n%mod)

div = 0
ans = 0
for i in range(N-1):
    div = (div + NN[N-1]*mod_inv(i+1) % mod) % mod
    ans = (ans + div*(A[i+1]-A[i])%mod) % mod

print(ans)