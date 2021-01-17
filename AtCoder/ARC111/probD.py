import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().rstrip().split())
Edges = []
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)
    Edges.append((a, b))

C = list(map(int, input().rstrip().split()))

CtoP = [[] for _ in range(N+1)]
for i, c in enumerate(C):
    CtoP[c].append(i)

Actual = C[:]
for c in range(1, N+1):
    for P in CtoP[c]:
        