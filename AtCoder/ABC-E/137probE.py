import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1, c-P])

def dfs(p, dis, maxd):
    print(p, dis)
    for q, d in graph[p]:
        print(q, 'aaaa')
        if q == p:
            continue
        if q == N-1:
            if dis+d > maxd:
                maxd = dis+d
            return maxd
        maxd = dfs(q, dis+d, maxd)
    return maxd

ans = dfs(0, 0, 0)
for q, d in graph[N-1]:
    if N-1 == q:
        ans = -1

print(ans)