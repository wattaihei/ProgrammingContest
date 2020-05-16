N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = 'IMPOSSIBLE'
qs = [0]
for _ in range(2):
    qqs = []
    for q in qs:
        for n in graph[q]:
            if n == N-1:
                ans = 'POSSIBLE'
                break
            qqs.append(n)
    qs = qqs

print(ans)