import sys
input = sys.stdin.readline

from bisect import bisect_left
from operator import itemgetter
import math

N, Q = map(int, input().split())
P = []
Xs = []
for _ in range(N):
    X, R, H = map(int, input().split())
    P.append((X, R, H, math.pi*R**2*H/3))
    Xs.append(X)
Query = [list(map(int, input().split())) for _ in range(Q)]

P.sort(key=itemgetter(0))
Xs.sort()
V = [0]
for i in range(N):
    V.append(V[-1]+P[i][3])

for A, B in Query:
    ia = bisect_left(Xs, A)
    ib = bisect_left(Xs, B)
    ans = V[ib-1] - V[ia]
    ans += P[ia-1][3] * (max(0, P[ia-1][2]-A+P[ia-1][0])/P[ia-1][2])**3
    ans += P[ib-1][3] * (1-(max(P[ib-1][2], P[ib-1][2]-B+P[ib-1][0])/P[ib-1][2])**3)
    print(ans)