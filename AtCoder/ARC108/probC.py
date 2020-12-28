import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v ,c = map(int, input().rstrip().split())
    graph[u-1].append((v-1, c))
    graph[v-1].append((u-1, c))


q = [0]
D = [-1]*N
D[0] = 1
while q:
    qq = []
    for p in q:
        for np, nc in graph[p]:
            if D[np] == -1:
                D[np] = (D[p])%N + 1 if D[p] == nc else nc
                qq.append(np)
    q = qq

print(*D, sep="\n")