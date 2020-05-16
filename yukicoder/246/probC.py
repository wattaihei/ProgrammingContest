import sys
input = sys.stdin.readline

from math import log2
P, Q = map(int, input().split())

l = 1
r = 10**18
for _ in range(10**4):
    m = (r+l)/2
    # print(m)
    if m**2 < P + Q*(m)*log2(m):
        l = m
    else:
        r = m
print(l)