mod = 10**9+7

import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()
s = 0
p = 0
for a in A:
    s += a
    p += s

print(p)
C = Counter(A)
q = 1
for v in C.values():
    for n in range(1, v+1):
        q = q * n % mod

print(q)