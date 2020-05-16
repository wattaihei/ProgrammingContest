import sys
input = sys.stdin.readline
from fractions import gcd

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    P = list(map(lambda x: int(x)//100, input().split()))
    x, a = map(int, input().split())
    y, b = map(int, input().split())
    K = int(input())
    Query.append((N, P, x, a, y, b, K))

for N, P, x, a, y, b, K in Query:
    P.sort(reverse=True)
    ab = a*b//gcd(a, b)
    if y > x:
        x, y = y, x
        a, b = b, a
    l = 0
    r = N+1
    while r-l > 1:
        m = (r+l)//2
        both = m//ab
        xonly = m//a - both
        yonly = m//b - both
        k1 = min(both, N)
        k2 = min(both+xonly, N)
        k3 = min(both+xonly+yonly, N)
        S = sum(P[:k1])*(x+y) + sum(P[k1:k2])*x + sum(P[k2:k3])*y
        if S >= K:
            r = m
        else:
            l = m
    if r == N+1:
        print(-1)
    else:
        print(r)