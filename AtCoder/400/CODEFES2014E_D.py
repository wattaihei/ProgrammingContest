import sys
input = sys.stdin.readline
import heapq as hp

from operator import itemgetter

N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
A = [int(input()) for _ in range(M)]

XY.sort(key=itemgetter(1))
XY.sort(key=itemgetter(0))

A.sort()
ind = 0
ans = 0
q = []
for a in A:
    while ind < N:
        x, y = XY[ind]
        if x <= a:
            hp.heappush(q, y)
            ind += 1
        else:
            break
    while q:
        p = hp.heappop(q)
        if a <= p:
            ans += 1
            break

print(ans)