import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


q = [0]
par = [-1]*N
par[0] = 0
while q:
    qq = []
    for p in q:
        for np in graph[p]:
            if par[np] == -1:
                par[np] = p+1
                qq.append(np)
    q = qq

print("Yes")
print(*par[1:], sep="\n")