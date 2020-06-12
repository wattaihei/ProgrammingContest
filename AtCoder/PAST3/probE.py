import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

Color = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]

for query in Query:
    if query[0] == 1:
        x = query[1]-1
        print(Color[x])
        for np in graph[x]:
            Color[np] = Color[x]
    else:
        x, y = query[1]-1, query[2]
        print(Color[x])
        Color[x] = y