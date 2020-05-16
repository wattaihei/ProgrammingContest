import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(s):
    D = [-1]*N
    D[s] = 0
    q = [s]
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = D[p] + 1
                    qq.append(np)
        q = qq
    return D


D1 = bfs(0)
D2 = bfs(N-1)
distance = D1[N-1]

P = []
for a in A:
    d1 = D1[a]
    d2 = D2[a]
    P.append((d1, d2))

P.sort()
ans = 0
for i in range(K-1):
    b1, b2 = P[i]
    c1, c2 = P[i+1]
    ans = max(ans, min(c1+b2+1, c2+b1+1))
ans = min(ans, distance)

print(ans)