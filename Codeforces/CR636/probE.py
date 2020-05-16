import sys
input = sys.stdin.readline

INF = 10**16

Q = int(input())
Query = []
for _ in range(Q):
    N, M, a, b, c = map(int, input().split())
    P = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    Query.append((N, M, a-1, b-1, c-1, P, graph))

def bfs(s, N, graph):
    q = [s]
    D = [-1]*N
    D[s] = 0
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = D[p] + 1
                    qq.append(np)
        q = qq
    return D   


for N, M, a, b, c, P, graph in Query:
    Da = bfs(a, N, graph)
    Db = bfs(b, N, graph)
    Dc = bfs(c, N, graph)
    P.sort()
    W = [0]
    for p in P:
        W.append(W[-1]+p)
    
    ans = INF
    for n in range(N):
        da = Da[n]
        db = Db[n]
        dc = Dc[n]
        if da+db+dc > M: continue
        score = W[db] + W[da+db+dc]
        if score < ans:
            ans = score
    print(ans)