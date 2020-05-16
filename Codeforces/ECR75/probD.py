import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, S = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, S, LR))

for N, S, LR in Query:
    G = []
    for L, _ in LR:
        G.append(L)
    G.sort()
    l = G[N//2]
    r = S+1
    while r - l > 1:
        m = (l+r)//2
        A = []
        B = []
        C = []
        for L, R in LR:
            if L <= m <= R:
                C.append(L)
            elif R < m:
                A.append(L)
            else:
                B.append(L)
        C.sort()
        if len(A) < N//2+1 <= len(A)+len(C):
            if sum(A)+sum(B)+sum(C[:N//2-len(A)]) + m*(len(A)+len(C)-N//2) <= S:
                l = m
            else:
                r = m
        else:
            r = m
    print(l)