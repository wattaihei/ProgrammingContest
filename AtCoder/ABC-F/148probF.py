import sys
input = sys.stdin.readline

N, u, v = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

u -= 1
v -= 1

def bfs1():
    q = [v]
    d = 0
    D = [-1]*N
    D[v] = 0
    while q:
        qq = []
        d += 1
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = d
                    qq.append(np)
        q = qq
    return D

D = bfs1()
dis = D[u]
canuse = [True]*N
for i in range(N):
    if D[i] <= dis//2:
        canuse[i] = False

def bfs2():
    q = [u]
    d = 0
    D = [-1]*N
    D[u] = 0
    while q:
        qq = []
        d += 1
        for p in q:
            for np in graph[p]:
                if D[np] == -1 and canuse[np]:
                    D[np] = d
                    qq.append(np)
        q = qq
    return D


D2 = bfs2()
ans = 0
for i in range(N):
    if len(graph[i]) == 1 and D2[i] != -1:
        ans = max(D[i]-1, ans)
print(ans)