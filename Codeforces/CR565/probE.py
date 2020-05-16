import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    Query.append((N, M, graph))


for N, M, graph in Query:
    q = [0]
    checked = [False]*N
    checked[0] = True
    dis = [[1], []]
    d = 0
    while q:
        qq = []
        d += 1
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
                    dis[d%2].append(np+1)
        q = qq
    if len(dis[0]) > len(dis[1]):
        print(len(dis[1]))
        for a in dis[1]:
            print(a, end=' ')
        print()
    else:
        print(len(dis[0]))
        for a in dis[0]:
            print(a, end=' ')
        print()