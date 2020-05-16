import sys
input = sys.stdin.readline

INF = 10**17

N, M = map(int, input().split())
Edges = [list(map(int, input().split())) for _ in range(M)]


def bfs(graph, start):
    checked = [False]*N
    checked[start] = True
    q = [start]
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    qq.append(np)
                    checked[np] = True
        q = qq
    return checked

graph1 = [[] for _ in range(N)]
graph2 = [[] for _ in range(N)]
for a, b, e in Edges:
    graph1[a-1].append(b-1)
    graph2[b-1].append(a-1)

checked1 = bfs(graph1, 0)
checked2 = bfs(graph2, N-1)

n_Edges = []
for a, b, e in Edges:
    if checked1[a-1] and checked2[b-1]:
        n_Edges.append((a, b, e))

D = [INF]*N
D[0] = 0
ok = True
for i in range(N):
    update = False
    for a, b, c in n_Edges:
        if D[a-1] != INF and D[b-1] > D[a-1] - c:
            D[b-1] = D[a-1] - c
            update = True
    if i==N-1 and update:
        ok = False

if not ok:
    print('inf')
else:
    print(-D[N-1])