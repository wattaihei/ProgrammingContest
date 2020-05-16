N, M, Q = map(int, input().split())
Left = [0 for _ in range(N)]
Right = [0 for _ in range(N)]
V = [[] for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    Left[l-1] += 1
    Right[r-1] += 1
    V[r-1].append(l-1)

PQ = [list(map(int, input().split())) for _ in range(Q)]



T = [[0 for _ in range(N)] for _ in range(N)]
a = M
nextl = 0
for l in range(N):
    b = a - nextl
    nextl = Left[l]
    nextr = 0
    for r in range(N-1, l-1, -1):
        T[l][r] = max(b - nextr, 0)
        nextr += Right[r]
        for li in V[r]:
            if li < l:
                nextr -= 1
    a = b


for p, q in PQ:
    print(T[p-1][q-1]) 