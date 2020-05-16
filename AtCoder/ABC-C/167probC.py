import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
As = []
C = []
for _ in range(N):
    c, *A = map(int, input().split())
    C.append(c)
    As.append(A)

INF = 10**18
ans = INF
for bit in range(1<<N):
    cost = 0
    Get = [0]*M
    for i in range(N):
        if bit&(1<<i):
            cost += C[i]
            for m in range(M):
                Get[m] += As[i][m]
    ok = True
    for m in range(M):
        if Get[m] < X:
            ok = False
            break
    if ok:
        ans = min(ans, cost)
if ans == INF:
    print(-1)
else:
    print(ans)