import sys
input = sys.stdin.readline
import heapq as hp
from bisect import bisect_right

INF = 10**14

N, M, R, T = map(int, input().split())
graph =  [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))
    graph[b-1].append((c, a-1))

D = [[INF]*N for _ in range(N)] # 頂点iへの最短距離がD[i]

def dijkstra(s):
    D[s][s] = 0 
    q = [] # しまっていく優先度付きキュー
    hp.heappush(q, (0, s))

    while q:
        nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
        if D[s][np] < nd: # 追加した後の残骸は見ない
            continue
        for d, p in graph[np]:
            if D[s][p] > D[s][np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
                D[s][p] = D[s][np] + d
                hp.heappush(q, (D[s][p], p))

for n in range(N):
    dijkstra(n)

ans = 0
for start in range(N):
    usa = []
    kam = []
    for p in range(N):
        usa.append(D[start][p]*T)
        kam.append(D[start][p]*R)
    usa.sort()
    for k in kam:
        if k == 0: continue
        ans += N - bisect_right(usa, k)
        if R < T:
            ans -= 1

print(ans)