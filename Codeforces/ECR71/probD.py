from operator import itemgetter
from collections import Counter

mod = 998244353

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

a = 1
PP = [1]
for n in range(1, N+1):
    a = (a*n)%mod
    PP.append(a)

X = []
Y = []
for x, y in P:
    X.append(x)
    Y.append(y)

cx = PP[N]
for c in list(Counter(X).values()):
    cx //= PP[c]

cy = PP[N]
for c in list(Counter(Y).values()):
    cy //= PP[c]

P.sort(key=itemgetter(1))
P.sort(key=itemgetter(0))

cxy = 1
c = 1
px, py = -1, -1
for x, y in P:
    if px == x and py == y:
        c += 1
    else:
        cxy *= c
        c = 1
    px, py = x, y

cxy *= c
print(cx, cy, cxy)
ans = (PP[N] - cx - cy + cxy) % mod
print(ans)