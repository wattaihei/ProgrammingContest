import sys
input = sys.stdin.readline
import heapq as hp

N = int(input())
TAB = [list(map(int, input().split())) for _ in range(N)]

l = -3*10**9
r = 3*10**9

while r-l > 1:
    m = (l+r)//2

    P = [[] for _ in range(N+1)]
    ok = True
    for T, A, B in TAB:
        if (A-m) < 0:
            ok = False
            break
        L = T - (A-m)//B
        R = T + (A-m)//B
        if L < 1:
            L = 1
        P[L].append(R)

    q = []
    for n in range(1, N+1):
        for right in P[n]:
            hp.heappush(q, right)
        if not q:
            ok = False
            break
        a = hp.heappop(q)
        if a < n:
            ok = False
            break
    if ok:
        l = m
    else:
        r = m

print(l)