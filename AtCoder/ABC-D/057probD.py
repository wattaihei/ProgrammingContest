from bisect import bisect_left
from operator import mul
from functools import reduce

N, A, B = map(int, input().split())
V = list(map(int, input().split()))

V.sort(reverse=True)




def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

print(sum(V[:A])/len(V[:A]))

c = 0
for i in range(A-1, B):
    if V[i] == V[A-1]:
        c += 1
#print(V, V[A-1])

for i, v in enumerate(V):
    if v == V[A-1]:
        ia = i
        break
l = A - ia
maxl = V.count(V[A-1])
#print(A, ia, l, maxl, c)
if ia == 0:
    ans = 0
    for d in range(c):
        ans += cmb(maxl, l+d)
else:
    ans = cmb(maxl, l)
print(ans)