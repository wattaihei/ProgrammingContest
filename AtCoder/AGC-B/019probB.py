from collections import Counter
import sys
sys.setrecursionlimit(5000000)

S = list(input())
L = len(S)
A = Counter(S)

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

if L == 1:
    print(1)
else:
    ans = cmb(L, 2) + 1
    for v in A.values():
        if v == 1: continue
        ans -= cmb(v, 2)
    print(ans)