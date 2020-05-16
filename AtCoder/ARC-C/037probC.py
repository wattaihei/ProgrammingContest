import sys
input = sys.stdin.readline

from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

l = 0
r = 10**18+1

while r-l>1:
    m = (l+r)//2
    count = 0
    for a in A:
        b = m//a
        count += bisect_right(B, b)
    if count < K:
        l = m
    else:
        r = m
print(r)