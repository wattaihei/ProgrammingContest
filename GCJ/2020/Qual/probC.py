import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, AB))


for qnum, (N, AB) in enumerate(Query):
    Qu = []
    for i, (a, b) in enumerate(AB):
        Qu.append((a, b, i))
    Qu.sort()

    ans = [-1]*N
    pc = 0
    pj = 0
    for a, b, u in Qu:
        if pc < pj:
            if a < pc:
                ans = []
                break
            elif a < pj:
                ans[u] = "C"
                pc = b
            else:
                ans[u] = "J"
                pj = b
        else:
            if a < pj:
                ans = []
                break
            elif a < pc:
                ans[u] = "J"
                pj = b
            else:
                ans[u] = "C"
                pc = b
    com = "IMPOSSIBLE" if not ans else "".join(ans)
    print("Case #{}:".format(qnum+1), com)