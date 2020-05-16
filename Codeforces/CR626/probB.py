import sys
input = sys.stdin.readline
import math
from bisect import bisect_left

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

pA = [0]
for a in A:
    if a:
        pA.append(pA[-1]+1)
    else:
        pA.append(0)

pB = [0]
for b in B:
    if b:
        pB.append(pB[-1]+1)
    else:
        pB.append(0)

pA.sort()
pB.sort()


ans = 0
for n in range(1, int(math.sqrt(K))+3):
    if K%n == 0 and K//n >= n:
        ans += (N+1 - bisect_left(pA, n)) * (M+1 - bisect_left(pB, K//n))
        if K//n != n:
            ans += (N+1 - bisect_left(pA, K//n)) * (M+1 - bisect_left(pB, n))
print(ans)