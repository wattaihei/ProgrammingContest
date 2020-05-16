import sys
input = sys.stdin.readline

INF = 10**16

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    P = set()
    L = 0
    for i in range(N-1):
        if A[i] == -1 and A[i+1] == -1:
            continue
        elif A[i] == -1 and A[i+1] != -1:
            P.add(A[i+1])
        elif A[i] != -1 and A[i+1] == -1:
            P.add(A[i])
        else:
            L = max(L, abs(A[i]-A[i+1]))
    if not P:
        print(L, 0)
    else:
        l = -1
        r = 10**14
        while r-l > 1:
            m = (r+l)//2
            p1 = -INF
            p2 = INF
            for n in P:
                p1 = max(n-m, p1)
                p2 = min(n+m, p2)
            if p1 <= p2:
                r = m
            else:
                l = m
        p1 = -INF
        p2 = INF
        for n in P:
            p1 = max(n-r, p1)
            p2 = min(n+r, p2)
        print(max(r, L), p1)