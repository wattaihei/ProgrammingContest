from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r < 0: return 0
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for a in A:
    ia = bisect_left(A, a//2)
    #print(ia, a, A[ia])
    a1 = cmb(a, A[ia-1])
    if ia >= N:
        a2 = 0
    else:
        a2 = cmb(a, A[ia])
    #print(a, a1, a2)
    if a1 > ans:
        ans = a1
        p1, p2 = a, A[ia-1]
    if a2 > ans:
        ans = a2
        p1, p2 = a, A[ia]
print(p1, p2)
    