import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
X -= 1; Y -= 1

graph = [[] for _ in range(N)]
for i in range(N-1):
    graph[i].append(i+1)
    graph[i+1].append(i)

graph[X].append(Y)
graph[Y].append(X)

def bfs(a):
    D = [-1]*N
    D[a] = 0
    q = [a]
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = D[p] + 1
                    qq.append(np)
        q = qq
    return D

ans = [0]*(N-1)
for n in range(N):
    D = bfs(n)
    for m in range(N):
        if m == n: continue
        ans[D[m]-1] += 1

for a in ans:
    print(a//2)