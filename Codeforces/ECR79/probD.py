
mod = 998244353


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

def mod_inv(a,m=mod):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

import sys
input = sys.stdin.readline

M = 10**6
N = int(input())
invN = mod_inv(N)
NUM = [0]*(M+1)
P = [0]*(M+1)
for _ in range(N):
    X, *A = map(int, input().split())
    invX = mod_inv(X)
    for a in A:
        NUM[a] += 1
        P[a] = (P[a] + invN*invX%mod) %mod
ans = 0
for n in range(1, M+1):
    ans = (ans + NUM[n]*invN%mod *P[n] %mod)%mod

print(ans)
