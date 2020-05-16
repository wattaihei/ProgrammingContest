V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
init = []
INF = 1
for _ in range(E):
    a, b, d = map(int, input().split())
    INF = max(INF, d)
    if a == 1:
        init.append((d, b))
        continue
    if b == 1:
        init.append((d, a))
        continue
    graph[a].append((d, b)) 
    graph[b].append((d, a)) #無向グラフならこれ使う
    
INF = INF*(E+1)**2

dp = [[INF for _ in range(V+1)] for _ in range(V+1)]

for i, g in enumerate(graph):
    for d, j in g:
        dp[i][j] = d

for k in range(2, V+1):
    for i in range(2, V+1):
        for j in range(2, V+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

ans = INF
L = len(init)
#print(init)
for i in range(L-1):
    for j in range(i+1, L):
        di, ai = init[i]
        dj, aj = init[j]
        #print(di, dj, ai, aj)
        ans = min(ans, dp[ai][aj]+di+dj)

if ans == INF:
    print(-1)
else:
    print(ans)