import sys
input = sys.stdin.readline
from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
minusA = []
plusA = []
zeros = 0
for a in A:
    if a > 0:
        plusA.append(a)
    elif a < 0:
        minusA.append(-a)
    else:
        zeros += 1


l = -10**9-1
r = 10**9+1
while r-l > 1:
    m = (l+r)//2
    for a in A:
        if a < 0: 
            a *= -1
            
