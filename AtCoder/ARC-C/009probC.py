mod = 1777777777

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

N, K = map(int, input().split())

dp = [0, 1]
for n in range(3, K+1):
    tmp = (n-1)*(dp[0]+dp[1]) % mod
    dp = [dp[1], tmp]

ans = dp[1]
for n in range(1, K+1):
    ans = ans * (N-n+1) * mod_inv(n) % mod

print(ans)