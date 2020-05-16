N, M = map(int, input().split())

graph = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)

checked = [False for _ in range(N)]
def dfs(p, checked, a):
    if checked[p]:
        return 0
    a.append(p)
    checked[p] = True
    for n in graph[p]:
        if checked[n]:
            continue
        a = dfs(n, checked, a)
    return a

ans = 0
for i in range(N):
    a = dfs(i, checked, [])
    if a:
        k = 0
        for ai in a:
            k += len(graph[ai])
        if k == 2*(len(a)-1):
            ans += 1
print(ans)