import sys
input = sys.stdin.readline

INF = (1<<60)

N = int(input())
graph = [[] for _ in range(N)]
Edges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    Edges.append((a-1, b-1))

def bfs(s, noback):
    q = [s]
    D = [-1]*N
    D[s] = 0
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if D[np] == -1 and np != noback:
                    D[np] = D[p] + 1
                    qq.append(np)
        q = qq
    
    Ds = [0]*(N+1)
    faraway = 0
    for i, d in enumerate(D):
        faraway = max(faraway, d)
        Ds[d] = max(Ds[d], len(graph[i])-1)
    return Ds, faraway

colorful = INF
nodes = INF

for n in range(N):
    M = [0]*(N+1)
    far = 0
    leaves = 0
    for s in graph[n]:
        leaves += 1
        Ds, faraway = bfs(s, n)
        far = max(far, faraway)
        for i, d in enumerate(Ds):
            M[i] = max(M[i], d)
    color = far + 2
    if color <= colorful:
        if color != colorful:
            nodes = INF
        colorful = color
        for f in range(far):
            leaves *= M[f]
        if leaves < nodes:
            nodes = leaves

for a, b in Edges:
    M = [0]*(N+1)
    leaves = 2
    D1, faraway1 = bfs(a, b)
    for i, d in enumerate(D1):
        M[i] = max(M[i], d)
    
    D2, faraway2 = bfs(b, a)
    for i, d in enumerate(D2):
        M[i] = max(M[i], d)
    
    far = max(faraway1, faraway2)
    color = far + 1
    if color <= colorful:
        if color != colorful:
            nodes = INF
        colorful = color
        for f in range(far):
            leaves *= M[f]
        if leaves < nodes:
            nodes = leaves

print(colorful, nodes)