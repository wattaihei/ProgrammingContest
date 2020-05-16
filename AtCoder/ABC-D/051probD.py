from copy import deepcopy

N, M = map(int, input().split())

INF = 10000000
D = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    D[a-1][b-1] = c
    D[b-1][a-1] = c

F = deepcopy(D)
for k in range(N):
    for i in range(N):
        for j in range(N):
            F[i][j] = min(F[i][j], F[i][k]+F[k][j])
a = 0
for i in range(N):
    for j in range(N):
        if D[i][j] == F[i][j]:
            a += 1
a //= 2
print(M-a)
