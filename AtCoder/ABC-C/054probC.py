N, M = map(int, input().split())
# N-1辺表示をグラフ表示に
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def dfs(p, now, ans):
    now.append(p)
    if len(now) == N:
        ans += 1
        return ans
    allchecked = True
    for q in graph[p]:
        new = now[:]
        if not q in new:
            allchecked = False
            ans = dfs(q, new, ans)
    if allchecked:
        now.pop()
    return ans

print(dfs(0, [], 0))