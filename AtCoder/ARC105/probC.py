import sys
input = sys.stdin.buffer.readline
from operator import itemgetter
from itertools import permutations
from bisect import bisect_right, bisect_left

INF = 10**18

N, M = map(int, input().split())
W = list(map(int, input().split()))
LV = [list(map(int, input().split())) for _ in range(M)]
LV.sort(key=itemgetter(1))

Ps = []

def counts(remains, scores):
    if not remains:
        Ps.append(scores)
        return
    l = len(remains)
    for bit in range(1, 1<<l):
        new_remains = []
        s = 0
        for i, r in enumerate(remains):
            if (1<<i)&bit:
                s += r
            else:
                new_remains.append(r)
        counts(new_remains, scores+[s])

counts(W, [])

L, V = zip(*LV)
B = [0]
for l in L:
    B.append(max(B[-1], l))

print(Ps)

if min(V) < max(W):
    ans = -1
else:
    ans = INF
    for A in Ps:
        tmpWeight = A[0]
        if bisect_left(V, tmpWeight) != 0: continue
        cost = 0
        for a in A[1:]:
            ind = bisect_left(V, a+tmpWeight)
            if bisect_left(V, a) != 0 or ind == 0:
                cost = INF
                break
            cost += B[ind]
            tmpWeight = a
        if cost < ans:
            ans = cost
print(ans)