import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

D = [-1]*N
def bfs(s):
    isBi = True
    q = [s]
    D[s] = 0
    d = 0
    while q:
        qq = []
        d ^= 1
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = d
                    qq.append(np)
                elif D[np] != d:
                    isBi = False
        q = qq
    return isBi

a = 0
b = 0
c = 0
for n in range(N):
    if D[n] == -1:
        if len(graph[n]) == 0:
            c += 1
        elif bfs(n):
            a += 1
        else:
            b += 1

ans = 2*a**2 + 2*a*b + b**2 + 2*N*c - c**2
print(ans)