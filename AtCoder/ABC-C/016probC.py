N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
checked = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    checked[i][i] = True
FriFri = [0]*N
for s in range(N):
    Fri = graph[s]
    #print(s, Fri)
    for f1 in Fri:
        for f2 in Fri:
            if (not f1 in graph[f2]) and (not checked[f1][f2]):
                checked[f1][f2] = True
                FriFri[f1] += 1
for f in FriFri:
    print(f)