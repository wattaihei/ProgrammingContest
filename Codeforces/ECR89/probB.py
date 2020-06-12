import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    n, x, m = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(m)]
    Query.append((n, x, m, LR))

for N, X, M, LR in Query:
    P = [[X, X]]
    for l, r in LR:
        willapp = False
        PP = []
        for pl, pr in P:
            if pl <= r and l <= pr:
                willapp = True
                l = min(l, pl)
                r = max(r, pr)
            else:
                PP.append((pl, pr))
        if willapp:
            PP.append((l, r))
        P = PP
    
    ans = 0
    for l, r in P:
        ans += r - l + 1
    print(ans)

    