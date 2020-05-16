import sys
input = sys.stdin.readline
from fractions import gcd

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for r, b, k in Query:
    g = gcd(r, b)
    L = [r//g, b//g]
    m = min(L)
    l = max(L)
    if m*(k-1) + 2 > l:
        print("OBEY")
    else:
        print("REBEL")