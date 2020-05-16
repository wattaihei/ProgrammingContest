N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = []
for n in range(N):
    a = 0
    fri = [False for _ in range(N)]
    for m in graph[n]:
        for j in graph[m]:
            fri[j] = True
            if j == n or j in graph[n]:
                fri[j] = False
    for j in range(N):
        if fri[j]:
            a += 1
    ans.append(a)

for a in ans:
    print(a)