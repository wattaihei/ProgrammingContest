from operator import itemgetter
from bisect import bisect_left

N = int(input())
HW = [list(map(int, input().split())) for _ in range(N)]

INF = 10**9

A = {}
pre = -1
for h, w in HW:
    if not h in A.keys():
        A[h] = [w]
    else:
        A[h].append(w)

B = sorted(list(A.items()), key=itemgetter(0))

m = 0
ans = 0
for _, L in B:
    nm = INF
    for l in L:
        if m < l:
            nm = min(nm, l)
    if nm != INF:
        ans += 1
        m = nm

print(ans)