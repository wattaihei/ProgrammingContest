import sys
input = sys.stdin.readline
from fractions import gcd

X, Y = map(int, input().split("/"))
g = gcd(X, Y)
x = X//g
y = Y//g

n_min = (2*x-y)//(y**2)
n_max = (2*x+y)//(y**2) + 1

ans = []
for n in range(n_min, n_max+1):
    if n <= 0: continue
    N = y*n
    M = N*(N+1)//2 - x*n
    if 0 < M <= N:
        ans.append((N, M))

if not ans:
    print("Impossible")
else:
    print("\n".join([str(a)+" "+str(b) for a, b in ans]))