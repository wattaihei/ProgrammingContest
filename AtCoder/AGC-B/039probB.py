import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
graph = [[int(a) for a in list(input().rstrip())] for _ in range(N)]
INF = 10**9

dis = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if dis[i][j] == 0:
            dis[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

state = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            state[i].append(j)

D = [INF for _ in range(N)]
checked = [False for _ in range(N)]
D[0] = 0
checked[0] = True
ok = True

def dfs(p, d, ok):
    for np in state[p]:
        if checked[np]:
            c = d + 1 - D[np]
            if c > 1 and c % 2 == 1:
                ok = False
        else:
            checked[np] = True
            D[np] = d+1
            ok = dfs(np, d+1, ok)
    return ok

ok = dfs(0, 0, ok)

if not ok:
    print(-1)
else:
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, dis[i][j]+1)
    print(ans)